// LionGuard 2 Frontend JavaScript

// State management
const state = {
    selectedModel: 'lionguard-2.1',
    selectedModelGC: 'lionguard-2.1',
    currentTextId: '',
    chatHistories: {
        no_moderation: [],
        openai_moderation: [],
        lionguard: []
    }
};

// Utility functions
function showLoading(button) {
    button.disabled = true;
    button.classList.add('loading');
    const originalText = button.textContent;
    button.textContent = 'Loading...';
    return originalText;
}

function hideLoading(button, originalText) {
    button.disabled = false;
    button.classList.remove('loading');
    button.textContent = originalText;
}

function getScoreLevel(score) {
    if (score < 0.4) {
        return { className: 'good', icon: '<i class="bx bx-check-circle"></i>', title: 'Low risk' };
    }
    if (score < 0.7) {
        return { className: 'warn', icon: '<i class="bx bx-error"></i>', title: 'Needs review' };
    }
    return { className: 'bad', icon: '<i class="bx bx-error-circle"></i>', title: 'High risk' };
}

function formatScore(score) {
    const percentage = Math.round(score * 100);
    const { className, icon, title } = getScoreLevel(score);
    
    return `<span class="score-chip ${className}" title="${title}">${icon} ${percentage}%</span>`;
}

function renderCategoryMeter(score) {
    const filledSegments = Math.min(10, Math.round(score * 10));
    const { className } = getScoreLevel(score);
    
    const segments = Array.from({ length: 10 }, (_, index) => {
        const isFilled = index < filledSegments;
        const filledClass = isFilled ? `filled ${className}` : '';
        return `<span class="category-meter-segment ${filledClass}"></span>`;
    }).join('');
    
    return `<div class="category-meter" aria-label="${Math.round(score * 100)}%">${segments}</div>`;
}

// Tab switching
function initTabs() {
    const tabs = document.querySelectorAll('.tab[data-tab]');
    const tabContents = document.querySelectorAll('.tab-content');
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const demoTabs = ['detector', 'chat'];

    const updateDropdownState = (targetTab) => {
        if (!dropdownToggle) return;
        if (demoTabs.includes(targetTab)) {
            dropdownToggle.classList.add('active');
        } else {
            dropdownToggle.classList.remove('active');
        }
    };
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetTab = tab.dataset.tab;
            
            // Update tabs
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            // Update content
            tabContents.forEach(content => {
                content.classList.remove('active');
                if (content.id === `${targetTab}-content`) {
                    content.classList.add('active');
                }
            });

            updateDropdownState(targetTab);
            
            // Smooth scroll to top when switching tabs
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

    const initialActiveTab = document.querySelector('.tab[data-tab].active');
    if (initialActiveTab) {
        updateDropdownState(initialActiveTab.dataset.tab);
    }
}

function initNavDropdown() {
    const dropdown = document.querySelector('.nav-dropdown');
    if (!dropdown) return;
    
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const dropdownTabs = dropdown.querySelectorAll('.dropdown-item[data-tab]');
    
    const closeDropdown = () => {
        dropdown.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
    };
    
    const toggleDropdown = (event) => {
        event.stopPropagation();
        const isOpen = dropdown.classList.toggle('open');
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    };
    
    toggle.addEventListener('click', toggleDropdown);
    
    dropdownTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            closeDropdown();
        });
    });
    
    document.addEventListener('click', (event) => {
        if (!dropdown.contains(event.target)) {
            closeDropdown();
        }
    });
}

// Model selection for Classifier
function initModelSelector() {
    const select = document.getElementById('model-select');
    if (!select) return;
    select.value = state.selectedModel;
    select.addEventListener('change', () => {
        state.selectedModel = select.value;
    });
}

// Model selection for Guardrail Comparison
function initModelSelectorGC() {
    const select = document.getElementById('model-select-gc');
    if (!select) return;
    select.value = state.selectedModelGC;
    select.addEventListener('change', () => {
        state.selectedModelGC = select.value;
    });
}

// Classifier: Analyze text
async function analyzeText() {
    const textInput = document.getElementById('text-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const binaryResult = document.getElementById('binary-result');
    const categoryResults = document.getElementById('category-results');
    const feedbackSection = document.getElementById('feedback-section');
    const feedbackMessage = document.getElementById('feedback-message');
    
    const text = textInput.value.trim();
    
    if (!text) {
        alert('Please enter some text to analyze');
        return;
    }
    
    const originalText = showLoading(analyzeBtn);
    feedbackMessage.textContent = '';
    feedbackMessage.className = 'feedback-message';
    
    try {
        const response = await fetch('/moderate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: text,
                model: state.selectedModel
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to analyze text');
        }
        
        const data = await response.json();
        
        // Display binary result
        const verdictClass = data.binary_verdict;
        const verdictText = verdictClass.charAt(0).toUpperCase() + verdictClass.slice(1);
        const verdictIcons = {
            'pass': '<i class="bx bx-check-shield"></i>',
            'warn': '<i class="bx bx-shield-minus"></i>',
            'fail': '<i class="bx bx-shield-x"></i>'
        };
        
        binaryResult.innerHTML = `
            <div class="binary-card ${verdictClass}">
                <div class="binary-icon">${verdictIcons[verdictClass]}</div>
                <div class="binary-body">
                    <div class="binary-label">Overall</div>
                    <div class="binary-score-line">
                        <h2>${verdictText}</h2>
                        <span class="binary-percentage">${data.binary_percentage}/100</span>
                    </div>
                </div>
            </div>
        `;
        
        // Display category results
        const categoryHTML = data.categories.map(cat => `
            <div class="category-card">
                <div class="category-label">${cat.emoji} ${cat.name}</div>
                ${renderCategoryMeter(cat.max_score)}
                <div class="category-score">${formatScore(cat.max_score)}</div>
            </div>
        `).join('');
        
        categoryResults.innerHTML = `
            <div class="category-grid">
                ${categoryHTML}
            </div>
        `;
        
        // Show feedback section
        state.currentTextId = data.text_id;
        feedbackSection.style.display = 'block';
        
    } catch (error) {
        console.error('Error:', error);
        binaryResult.innerHTML = `
            <div style="color: #E63946; padding: 20px; text-align: center;">
                ❌ Error analyzing text: ${error.message}
            </div>
        `;
    } finally {
        hideLoading(analyzeBtn, originalText);
    }
}

// Classifier: Submit feedback
async function submitFeedback(agree) {
    const feedbackMessage = document.getElementById('feedback-message');
    
    if (!state.currentTextId) {
        feedbackMessage.textContent = 'No analysis to provide feedback on';
        feedbackMessage.className = 'feedback-message info';
        return;
    }
    
    try {
        const response = await fetch('/send_feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text_id: state.currentTextId,
                agree: agree
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to submit feedback');
        }
        
        const data = await response.json();
        
        feedbackMessage.textContent = data.message;
        feedbackMessage.className = 'feedback-message success';
        
    } catch (error) {
        console.error('Error:', error);
        feedbackMessage.textContent = 'Error submitting feedback';
        feedbackMessage.className = 'feedback-message info';
    }
}

// Guardrail Comparison: Render chat messages
function renderChatMessages(containerId, messages) {
    const container = document.getElementById(containerId);
    container.innerHTML = messages.map(msg => `
        <div class="chat-message ${msg.role}">
            ${msg.content}
        </div>
    `).join('');
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

// Guardrail Comparison: Send message
async function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');
    
    const message = messageInput.value.trim();
    
    if (!message) {
        alert('Please enter a message');
        return;
    }
    
    const originalText = showLoading(sendBtn);
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                model: state.selectedModelGC,
                histories: state.chatHistories
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to send message');
        }
        
        const data = await response.json();
        
        // Update state
        state.chatHistories = data.histories;
        
        // Render all chat panels
        renderChatMessages('chat-no-mod', data.histories.no_moderation);
        renderChatMessages('chat-openai', data.histories.openai_moderation);
        renderChatMessages('chat-lionguard', data.histories.lionguard);
        
        // Clear input
        messageInput.value = '';
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending message: ' + error.message);
    } finally {
        hideLoading(sendBtn, originalText);
    }
}

// Guardrail Comparison: Clear all chats
function clearAllChats() {
    state.chatHistories = {
        no_moderation: [],
        openai_moderation: [],
        lionguard: []
    };
    
    document.getElementById('chat-no-mod').innerHTML = '';
    document.getElementById('chat-openai').innerHTML = '';
    document.getElementById('chat-lionguard').innerHTML = '';
}

// Initialize event listeners
function initEventListeners() {
    // Classifier tab
    const analyzeBtn = document.getElementById('analyze-btn');
    const textInput = document.getElementById('text-input');
    const thumbsUpBtn = document.getElementById('thumbs-up');
    const thumbsDownBtn = document.getElementById('thumbs-down');
    
    analyzeBtn.addEventListener('click', analyzeText);
    textInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && e.ctrlKey) {
            analyzeText();
        }
    });
    thumbsUpBtn.addEventListener('click', () => submitFeedback(true));
    thumbsDownBtn.addEventListener('click', () => submitFeedback(false));
    
    // Guardrail Comparison tab
    const sendBtn = document.getElementById('send-btn');
    const messageInput = document.getElementById('message-input');
    const clearBtn = document.getElementById('clear-btn');
    
    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });
    clearBtn.addEventListener('click', clearAllChats);
}

// Dark mode toggle
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    if (!themeToggle) return;

    const themeIcon = themeToggle.querySelector('.theme-icon');
    const updateIcon = (isDark) => {
        themeToggle.setAttribute('aria-pressed', isDark ? 'true' : 'false');
        if (themeIcon) {
            // Toggle class for boxicons
            themeIcon.className = isDark ? 'bx bx-moon theme-icon' : 'bx bx-sun theme-icon';
            themeIcon.textContent = ''; // clear text content
        }
    };

    const savedTheme = localStorage.getItem('theme') || 'light';
    const shouldStartDark = savedTheme === 'dark';
    if (shouldStartDark) {
        document.body.classList.add('dark-mode');
    }
    updateIcon(shouldStartDark);

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        updateIcon(isDark);
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
}

// Code snippet tabs for Get Started
function initCodeTabs() {
    const tabs = document.querySelectorAll('.code-tab');
    const blocks = document.querySelectorAll('.code-block');

    if (!tabs.length) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            tab.classList.add('active');

            // Hide all blocks
            blocks.forEach(b => b.classList.remove('active'));

            // Show target block
            const targetId = `code-${tab.dataset.code}`;
            const targetBlock = document.getElementById(targetId);
            if (targetBlock) {
                targetBlock.classList.add('active');
            }
        });
    });
}

// Copy Code Functionality
function initCopyButton() {
    const copyBtn = document.getElementById('copy-code-btn');
    if (!copyBtn) return;

    copyBtn.addEventListener('click', async () => {
        // Find active code block
        const activeBlock = document.querySelector('.code-block.active code');
        if (!activeBlock) return;

        const textToCopy = activeBlock.textContent;

        try {
            await navigator.clipboard.writeText(textToCopy);
            
            // Provide feedback
            const originalHtml = copyBtn.innerHTML;
            copyBtn.innerHTML = `<i class='bx bx-check'></i> Copied!`;
            copyBtn.classList.add('success');
            
            setTimeout(() => {
                copyBtn.innerHTML = originalHtml;
                copyBtn.classList.remove('success');
            }, 2000);
        } catch (err) {
            console.error('Failed to copy:', err);
            copyBtn.innerHTML = `<i class='bx bx-x'></i> Failed`;
            
            setTimeout(() => {
                copyBtn.innerHTML = `<i class='bx bx-copy'></i> Copy`;
            }, 2000);
        }
    });
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initNavDropdown();
    initModelSelector();
    initModelSelectorGC();
    initEventListeners();
    initThemeToggle();
    initCodeTabs();
    initCopyButton();

    console.log('LionGuard 2 app initialized');
});
