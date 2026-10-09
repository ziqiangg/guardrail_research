from inv_common import *
HE=["Item","Kind (quota/system limit/pricing/other)","Value","Applies to","When exceeded","Source URL"]
R=[]
R.append(row([
"API queries [Documented] (QUO)","Quota",
"1,200 queries per minute (QPM) per project; a value from 0 to 1,200 QPM can be applied, and more needs a request to Cloud Customer Care [Documented] (QUO; INT)",
"Every call to the Model Armor API in the project, including calls made by integrated services [Documented] (INT)",
"The task fails; HTTP 429 RESOURCE_EXHAUSTED is the typical error. Retry 500, 502, 503 and 504 with truncated exponential backoff and jitter, and optionally 429 [Documented] (QUO; INT; RTY)"]))
R.append(row([
"Requests to ExternalProcessor [Documented] (QUO)","Quota",
"600 QPM per project [Documented] (QUO)",
"Relevant when Model Armor is integrated with other Google Cloud services (Service Extensions callouts) [Documented] (QUO)",
"Generic quota behaviour: 'the system blocks access to the resource, and the task that you're trying to perform fails' [Documented] (QUO)"]))
R.append(row([
"Token limit for prompt injection and jailbreak, responsible AI and CSAM [Documented] (QUO)","System limit",
"65,536 tokens (about 262,144 characters); a token is about 4 characters [Documented] (QUO). Earlier release notes gave 2,000 (2025-05-28), 10,000 for prompt injection (2025-07-28) and 65,536 (2026-08-25) [Documented] (RN)",
"Direct text in prompts and responses and text extracted from supported files; not the Gemini Enterprise integration [Documented] (QUO)",
"If a match is found the filter returns MATCH_FOUND; if none is found and the limit is exceeded it returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.' [Documented] (QUO)"]))
R.append(row([
"Sensitive Data Protection token limit [Documented] (QUO)","System limit",
"130,000 tokens [Documented] (QUO)",
"Sensitive Data Protection filter, basic and advanced [Documented] (QUO)",
"EXECUTION_SKIPPED with the token-limit message when no match was found within the limit [Documented] (QUO)"]))
R.append(row([
"Real-time streaming versus buffered streaming [Documented] (QUO; SAN)","System limit",
"Unlimited tokens in real-time mode; buffered mode follows the token limits; individual chunks must not exceed the token limits [Documented] (QUO; SAN)",
"StreamSanitizeUserPrompt and StreamSanitizeModelResponse; text only; no SDP de-identification [Documented] (SAN)",
"Buffered mode: same as the token limits above [Documented] (QUO)"]))
R.append(row([
"File and image size [Documented] (QUO)","System limit",
"4 MB for all supported files and images [Documented] (QUO); introduced by release note 2025-09-27 [Documented] (RN)",
"Documents and images [Documented] (QUO; OV)",
"Model Armor skips scanning the file or image [Documented] (QUO; OV)"]))
R.append(row([
"Minimum file size [Documented] (QUO)","System limit",
"69 bytes [Documented] (QUO)",
"Files submitted for scanning [Documented] (QUO)",
"The request is rejected with InvalidDocumentInputException, because such files are highly likely to be invalid [Documented] (QUO; OV)"]))
R.append(row([
"URLs scanned by malicious URL detection [Documented] (QUO)","System limit",
"First 256 URLs in a prompt or response [Documented] (QUO; OV)",
"Malicious URL filter; token limits do not apply [Documented] (QUO)",
"URLs after the first 256 are not scanned [Documented] (OV)"]))
R.append(row([
"Prompt injection and jailbreak minimum word count [Documented] (OV)","System limit",
"Three words [Documented] (OV; QUO)",
"Prompt injection and jailbreak detection [Documented] (OV)",
"Fewer than three words returns NO_MATCH_FOUND, because such inputs lack enough information to constitute an attack [Documented] (OV; QUO)"]))
R.append(row([
"Images per request [Documented] (OV)","System limit",
"One image per request with SanitizeUserPrompt and SanitizeModelResponse [Documented] (OV)",
"Image screening (Preview) [Documented] (OV)",
"Behaviour for a second image [Not disclosed] (checked OV and SAN). A regional endpoint without image support returns invocation_result FAILURE [Documented] (OV)"]))
R.append(row([
"Exclusion-rule limits [Documented] (QUO)","System limit",
"10 rule sets per filter configuration; 10 rules per rule set; 10 dictionaries per template request; 128 KB word list per dictionary; 1,000-character regular expression; 130,000 tokens (0.5 MB) of input text evaluated [Documented] (QUO). Preview feature [Documented] (QUO; EXC)",
"Template-specific exclusion rules [Documented] (QUO)",
"If the input is over 130,000 tokens and a filter matches outside the evaluated part, the filter returns EXECUTION_SKIPPED with a message that exclusion rules could not be confirmed on full text [Documented] (QUO)"]))
R.append(row([
"Template ID length and characters [Documented] (TPL)","System limit",
"Letters, digits, underscores or hyphens; at most 63 characters; no spaces; must not start with a hyphen [Documented] (TPL console steps)",
"Template creation [Documented] (TPL)",
"[Not disclosed] (error behaviour not stated; checked TPL and RT)"]))
R.append(row([
"Standalone price [Documented] (PRC)","Pricing",
"No cost up to 2 million tokens per month; beyond that billed at $0.10 per million tokens [Documented] (PRC)",
"Model Armor purchased without Security Command Center Premium or Enterprise [Documented] (PRC). Skipped data is not charged [Documented] (OV)",
"Billed per million tokens above the allowance [Documented] (PRC)"]))
R.append(row([
"Security Command Center tier allowances [Documented] (PRC)","Pricing",
"Enterprise subscription 3 billion tokens per month and Premium subscription 3 billion; Premium activated at organisation level 2 million and at project level 2 million; $0.10 per additional million tokens in each case [Documented] (PRC)",
"Model Armor used under Security Command Center [Documented] (PRC)",
"Billed per million tokens above the allowance [Documented] (PRC)"]))
R.append(row([
"Sensitive Data Protection charge inside Model Armor [Documented] (PRC)","Pricing",
"No additional charge: 'When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it.' [Documented] (PRC)",
"Basic and advanced SDP filters invoked by Model Armor [Documented] (PRC)",
"Not applicable. Cloud Logging costs are separate [Documented] (LOG)"]))
R.append(row([
"Token definition used for billing and limits [Documented] (PRC)","Other",
"Pricing page: 'four characters (using UTF-8 code points) per token excluding white space', the same definition as Gemini Enterprise Agent Platform [Documented] (PRC). OV and QUO say 'about 4 characters' per token [Documented] (OV; QUO)",
"All prompts and responses screened by Model Armor [Documented] (PRC)",
"Not applicable"]))
BLOCK_E=table(HE,R)
if __name__=="__main__":
    print(len(R))
