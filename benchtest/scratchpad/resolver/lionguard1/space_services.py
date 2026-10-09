"""
Business logic for moderation and guardrail services
"""

import json
import os
import uuid
import asyncio
from datetime import datetime
from typing import Dict, List, Tuple, Optional

import openai
import gspread
from google.oauth2 import service_account

# Import from parent directory
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from utils import MODEL_CONFIGS, predict_with_model

# --- Categories ---
CATEGORIES = {
    "binary": ["binary"],
    "hateful": ["hateful_l1", "hateful_l2"],
    "insults": ["insults"],
    "sexual": ["sexual_l1", "sexual_l2"],
    "physical_violence": ["physical_violence"],
    "self_harm": ["self_harm_l1", "self_harm_l2"],
    "all_other_misconduct": ["all_other_misconduct_l1", "all_other_misconduct_l2"],
}

# --- OpenAI Setup ---
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
async_client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Google Sheets Config ---
GOOGLE_SHEET_URL = os.environ.get("GOOGLE_SHEET_URL")
GOOGLE_CREDENTIALS = os.environ.get("GCP_SERVICE_ACCOUNT")
RESULTS_SHEET_NAME = "results"
VOTES_SHEET_NAME = "votes"
CHATBOT_SHEET_NAME = "chatbot"


def get_gspread_client():
    """Get authenticated Google Sheets client"""
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(GOOGLE_CREDENTIALS),
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    return gspread.authorize(credentials)


def save_results_data(row: Dict):
    """Save moderation results to Google Sheets"""
    try:
        gc = get_gspread_client()
        sheet = gc.open_by_url(GOOGLE_SHEET_URL)
        ws = sheet.worksheet(RESULTS_SHEET_NAME)
        ws.append_row(list(row.values()))
    except Exception as e:
        print(f"Error saving results data: {e}")


def save_vote_data(text_id: str, agree: bool):
    """Save user feedback vote to Google Sheets"""
    try:
        gc = get_gspread_client()
        sheet = gc.open_by_url(GOOGLE_SHEET_URL)
        ws = sheet.worksheet(VOTES_SHEET_NAME)
        vote_row = {
            "datetime": datetime.now().isoformat(),
            "text_id": text_id,
            "agree": agree
        }
        ws.append_row(list(vote_row.values()))
    except Exception as e:
        print(f"Error saving vote data: {e}")


def log_chatbot_data(row: Dict):
    """Log chatbot interaction to Google Sheets"""
    try:
        gc = get_gspread_client()
        sheet = gc.open_by_url(GOOGLE_SHEET_URL)
        ws = sheet.worksheet(CHATBOT_SHEET_NAME)
        ws.append_row([
            row["datetime"], row["text_id"], row["text"], row["binary_score"],
            row["hateful_l1_score"], row["hateful_l2_score"], row["insults_score"],
            row["sexual_l1_score"], row["sexual_l2_score"], row["physical_violence_score"],
            row["self_harm_l1_score"], row["self_harm_l2_score"], row["aom_l1_score"],
            row["aom_l2_score"], row["openai_score"]
        ])
    except Exception as e:
        print(f"Error saving chatbot data: {e}")


# --- Moderation Logic ---

def analyze_text(text: str, model_key: str = None) -> Dict:
    """
    Analyze text for moderation risks
    Returns dict with binary score, categories, text_id, and model info
    """
    if not text.strip():
        return {
            "binary_score": 0.0,
            "binary_verdict": "pass",
            "binary_percentage": 0,
            "categories": [],
            "text_id": "",
            "model_used": model_key or "lionguard-2.1"
        }
    
    try:
        text_id = str(uuid.uuid4())
        results, selected_model_key = predict_with_model([text], model_key)
        binary_score = results.get('binary', [0.0])[0]
        
        # Determine verdict
        if binary_score < 0.4:
            verdict = "pass"
        elif 0.4 <= binary_score < 0.7:
            verdict = "warn"
        else:
            verdict = "fail"
        
        # Process categories
        main_categories = ['hateful', 'insults', 'sexual', 'physical_violence', 'self_harm', 'all_other_misconduct']
        category_emojis = {
            'hateful': '🤬',
            'insults': '💢',
            'sexual': '🔞',
            'physical_violence': '⚔️',
            'self_harm': '☹️',
            'all_other_misconduct': '🙅‍♀️'
        }
        
        categories_list = []
        max_scores = {}
        
        for category in main_categories:
            subcategories = CATEGORIES[category]
            level_scores = [results.get(subcategory_key, [0.0])[0] for subcategory_key in subcategories]
            max_score = max(level_scores) if level_scores else 0.0
            max_scores[category] = max_score
            
            category_name = category.replace('_', ' ').title()
            categories_list.append({
                "name": category_name,
                "emoji": category_emojis.get(category, '📝'),
                "max_score": max_score
            })
        
        # Save to Google Sheets if enabled
        if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:
            results_row = {
                "datetime": datetime.now().isoformat(),
                "text_id": text_id,
                "text": text,
                "binary_score": binary_score,
                "model": selected_model_key,
            }
            for category in main_categories:
                results_row[f"{category}_max"] = max_scores[category]
            save_results_data(results_row)
        
        return {
            "binary_score": binary_score,
            "binary_verdict": verdict,
            "binary_percentage": int(binary_score * 100),
            "categories": categories_list,
            "text_id": text_id,
            "model_used": selected_model_key
        }
    
    except Exception as e:
        print(f"Error analyzing text: {e}")
        raise


def submit_feedback(text_id: str, agree: bool) -> Dict:
    """Submit user feedback"""
    if not text_id:
        return {"success": False, "message": "No text ID provided"}
    
    if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:
        save_vote_data(text_id, agree)
        message = "🎉 Thank you!" if agree else "📝 Thanks for the feedback!"
        return {"success": True, "message": message}
    
    return {"success": False, "message": "Voting not available"}


# --- Guardrail Comparison Logic (Async) ---

async def get_openai_response_async(message: str, system_prompt: str = "You are a helpful assistant.") -> str:
    """Get OpenAI chat response asynchronously"""
    try:
        response = await async_client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=500,
            temperature=0,
            seed=42,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}. Please check your OpenAI API key."


async def openai_moderation_async(message: str) -> bool:
    """Check if message is flagged by OpenAI moderation"""
    try:
        response = await async_client.moderations.create(input=message)
        return response.results[0].flagged
    except Exception as e:
        print(f"Error in OpenAI moderation: {e}")
        return False


def lionguard_2_sync(message: str, model_key: str, threshold: float = 0.5) -> Tuple[bool, float]:
    """Check if message is flagged by Lionguard"""
    try:
        results, _ = predict_with_model([message], model_key)
        binary_prob = results.get('binary', [0.0])[0]
        return binary_prob > threshold, binary_prob
    except Exception as e:
        print(f"Error in LionGuard inference for {model_key}: {e}")
        return False, 0.0


async def process_no_moderation(message: str, history: List[Dict]) -> List[Dict]:
    """Process message without moderation"""
    no_mod_response = await get_openai_response_async(message)
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": no_mod_response})
    return history


async def process_openai_moderation(message: str, history: List[Dict]) -> List[Dict]:
    """Process message with OpenAI moderation"""
    openai_flagged = await openai_moderation_async(message)
    history.append({"role": "user", "content": message})
    if openai_flagged:
        openai_response = "🚫 This message has been flagged by OpenAI moderation"
        history.append({"role": "assistant", "content": openai_response})
    else:
        openai_response = await get_openai_response_async(message)
        history.append({"role": "assistant", "content": openai_response})
    return history


async def process_lionguard(message: str, history: List[Dict], model_key: str) -> Tuple[List[Dict], float]:
    """Process message with Lionguard model"""
    loop = asyncio.get_event_loop()
    lg_flagged, lg_score = await loop.run_in_executor(None, lionguard_2_sync, message, model_key, 0.5)
    
    history.append({"role": "user", "content": message})
    if lg_flagged:
        lg_response = f"🚫 This message has been flagged by {MODEL_CONFIGS[model_key]['label']}"
        history.append({"role": "assistant", "content": lg_response})
    else:
        lg_response = await get_openai_response_async(message)
        history.append({"role": "assistant", "content": lg_response})
    return history, lg_score


def _log_chatbot_sync(message: str, lg_score: float, model_key: str):
    """Sync helper for logging chatbot data"""
    try:
        results, selected_model_key = predict_with_model([message], model_key)
        now = datetime.now().isoformat()
        text_id = str(uuid.uuid4())
        row = {
            "datetime": now,
            "text_id": text_id,
            "text": message,
            "binary_score": results.get("binary", [None])[0],
            "hateful_l1_score": results.get(CATEGORIES['hateful'][0], [None])[0],
            "hateful_l2_score": results.get(CATEGORIES['hateful'][1], [None])[0],
            "insults_score": results.get(CATEGORIES['insults'][0], [None])[0],
            "sexual_l1_score": results.get(CATEGORIES['sexual'][0], [None])[0],
            "sexual_l2_score": results.get(CATEGORIES['sexual'][1], [None])[0],
            "physical_violence_score": results.get(CATEGORIES['physical_violence'][0], [None])[0],
            "self_harm_l1_score": results.get(CATEGORIES['self_harm'][0], [None])[0],
            "self_harm_l2_score": results.get(CATEGORIES['self_harm'][1], [None])[0],
            "aom_l1_score": results.get(CATEGORIES['all_other_misconduct'][0], [None])[0],
            "aom_l2_score": results.get(CATEGORIES['all_other_misconduct'][1], [None])[0],
            "openai_score": None,
        }
        try:
            openai_result = client.moderations.create(input=message)
            row["openai_score"] = float(openai_result.results[0].category_scores.get("hate", 0.0))
        except Exception:
            row["openai_score"] = None
        
        log_chatbot_data(row)
    except Exception as e:
        print(f"Error in sync logging: {e}")


async def process_chat_message(
    message: str,
    model_key: str,
    history_no_mod: List[Dict],
    history_openai: List[Dict],
    history_lg: List[Dict]
) -> Tuple[List[Dict], List[Dict], List[Dict], Optional[float]]:
    """
    Process message concurrently across all three guardrails
    Returns updated histories and LionGuard score
    """
    if not message.strip():
        return history_no_mod, history_openai, history_lg, None
    
    # Run all three processes concurrently
    results = await asyncio.gather(
        process_no_moderation(message, history_no_mod),
        process_openai_moderation(message, history_openai),
        process_lionguard(message, history_lg, model_key),
        return_exceptions=True
    )
    
    # Unpack results
    history_no_mod = results[0] if not isinstance(results[0], Exception) else history_no_mod
    history_openai = results[1] if not isinstance(results[1], Exception) else history_openai
    history_lg_result = results[2] if not isinstance(results[2], Exception) else (history_lg, 0.0)
    history_lg = history_lg_result[0]
    lg_score = history_lg_result[1] if isinstance(history_lg_result, tuple) else 0.0
    
    # Log to Google Sheets in background
    if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:
        try:
            loop = asyncio.get_event_loop()
            loop.run_in_executor(None, _log_chatbot_sync, message, lg_score, model_key)
        except Exception as e:
            print(f"Chatbot logging failed: {e}")
    
    return history_no_mod, history_openai, history_lg, lg_score

