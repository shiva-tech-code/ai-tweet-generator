/**
 * TweetForge AI - Main JavaScript
 * Professional Tweet Generator Application
 */

// DOM Elements - will be null if not on generator page
const brandForm = document.getElementById('brandForm');
const submitBtn = document.getElementById('submitBtn');
const defaultState = document.getElementById('defaultState');
const loadingState = document.getElementById('loadingState');
const resultsState = document.getElementById('resultsState');
const errorState = document.getElementById('errorState');
const downloadBtn = document.getElementById('downloadBtn');
const copyAllBtn = document.getElementById('copyAllBtn');
const resetBtn = document.getElementById('resetBtn');
const retryBtn = document.getElementById('retryBtn');
const toast = document.getElementById('toast');
const toastMessage = document.getElementById('toastMessage');

// Store current results
let currentResults = null;
let currentFormData = null;

// Loading steps animation
const loadingSteps = ['step1', 'step2', 'step3'];
let stepInterval = null;

/**
 * Initialize the application
 */
function init() {
    // Only initialize form handling if on generator page
    if (brandForm) {
        brandForm.addEventListener('submit', handleFormSubmit);
    }
    
    // Button handlers - only if elements exist
    if (downloadBtn) downloadBtn.addEventListener('click', handleDownload);
    if (copyAllBtn) copyAllBtn.addEventListener('click', handleCopyAll);
    if (resetBtn) resetBtn.addEventListener('click', handleReset);
    if (retryBtn) retryBtn.addEventListener('click', handleRetry);
    
    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            // Only prevent default if it's an anchor on the same page
            if (href.startsWith('#') && !href.includes('.html')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });
    
    console.log('🚀 TweetForge AI initialized');
}

/**
 * Handle form submission
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(brandForm);
    const data = Object.fromEntries(formData);
    currentFormData = data;
    
    // Validate required fields
    if (!data.campaign_objective || !data.product_description) {
        showError('Please fill in all required fields (Campaign Objective and Product Description)');
        return;
    }
    
    // Show loading state
    showState('loading');
    startLoadingAnimation();
    
    // Disable submit button
    submitBtn.disabled = true;
    submitBtn.querySelector('.btn-content').style.display = 'none';
    submitBtn.querySelector('.btn-loader').style.display = 'flex';
    
    try {
        // Send request to API
        const response = await fetch('/api/generate-tweets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (!response.ok || !result.success) {
            throw new Error(result.error || 'Failed to generate tweets');
        }
        
        // Store results
        currentResults = {
            brand_name: data.brand_name || 'Unknown Brand',
            industry: data.industry || 'General',
            campaign_objective: data.campaign_objective,
            brand_voice_summary: result.brand_voice_summary,
            tweets: result.tweets,
            generated_at: new Date().toISOString()
        };
        
        // Display results
        displayResults(result);
        showState('results');
        showToast('Tweets generated successfully!');
        
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('errorMessage').textContent = error.message;
        showState('error');
    } finally {
        // Reset submit button
        submitBtn.disabled = false;
        submitBtn.querySelector('.btn-content').style.display = 'flex';
        submitBtn.querySelector('.btn-loader').style.display = 'none';
        stopLoadingAnimation();
    }
}

/**
 * Display generated results
 */
function displayResults(result) {
    const summary = result.brand_voice_summary || {};
    const tweets = result.tweets || [];
    
    // Update brand voice summary
    document.getElementById('tone').textContent = summary.tone || 'Professional and engaging';
    document.getElementById('audience').textContent = summary.target_audience || 'Brand audience';
    document.getElementById('style').textContent = summary.communication_style || 'Social media focused';
    document.getElementById('themes').textContent = summary.key_themes || 'Brand promotion and engagement';
    
    // Update tweet count
    document.getElementById('tweetCount').textContent = `${tweets.length} tweets`;
    
    // Display tweets
    const container = document.getElementById('tweetsContainer');
    container.innerHTML = '';
    
    // Tweet type mapping
    const tweetTypes = [
        'engaging', 'conversational', 'promotional', 'promotional',
        'witty', 'witty', 'informative', 'informative',
        'creative', 'creative'
    ];
    
    tweets.forEach((tweet, index) => {
        const tweetText = typeof tweet === 'string' ? tweet : tweet.text;
        const charCount = tweetText.length;
        const charStatus = charCount > 280 ? 'warning' : 'ok';
        const tweetType = tweetTypes[index] || 'creative';
        
        const card = document.createElement('div');
        card.className = 'tweet-card';
        card.innerHTML = `
            <div class="tweet-header">
                <span class="tweet-number">
                    <i class="fab fa-twitter"></i>
                    Tweet ${index + 1}
                </span>
                <span class="tweet-type ${tweetType}">${capitalize(tweetType)}</span>
            </div>
            <div class="tweet-text">${escapeHtml(tweetText)}</div>
            <div class="tweet-footer">
                <span class="char-count ${charStatus}">${charCount}/280 characters</span>
                <button class="copy-tweet-btn" onclick="copyTweet(${index})" title="Copy tweet">
                    <i class="fas fa-copy"></i>
                </button>
            </div>
        `;
        
        container.appendChild(card);
    });
}

/**
 * Show specific state (default, loading, results, error)
 */
function showState(state) {
    defaultState.style.display = state === 'default' ? 'flex' : 'none';
    loadingState.style.display = state === 'loading' ? 'flex' : 'none';
    resultsState.style.display = state === 'results' ? 'flex' : 'none';
    errorState.style.display = state === 'error' ? 'flex' : 'none';
}

/**
 * Start loading animation
 */
function startLoadingAnimation() {
    let currentStep = 0;
    
    loadingSteps.forEach((stepId, index) => {
        const step = document.getElementById(stepId);
        step.classList.remove('active', 'done');
        step.querySelector('i').className = index === 0 ? 'fas fa-check-circle' : 'fas fa-circle';
    });
    
    document.getElementById('step1').classList.add('active');
    
    stepInterval = setInterval(() => {
        if (currentStep < loadingSteps.length - 1) {
            const currentStepEl = document.getElementById(loadingSteps[currentStep]);
            currentStepEl.classList.remove('active');
            currentStepEl.classList.add('done');
            currentStepEl.querySelector('i').className = 'fas fa-check-circle';
            
            currentStep++;
            const nextStepEl = document.getElementById(loadingSteps[currentStep]);
            nextStepEl.classList.add('active');
            nextStepEl.querySelector('i').className = 'fas fa-check-circle';
        }
    }, 2000);
}

/**
 * Stop loading animation
 */
function stopLoadingAnimation() {
    if (stepInterval) {
        clearInterval(stepInterval);
        stepInterval = null;
    }
}

/**
 * Handle download
 */
function handleDownload() {
    if (!currentResults) return;
    
    const dataStr = JSON.stringify(currentResults, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    const brandName = (currentResults.brand_name || 'brand').replace(/\s+/g, '_').toLowerCase();
    link.href = url;
    link.download = `${brandName}_tweets_${Date.now()}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    
    showToast('Tweets exported as JSON!');
}

/**
 * Handle copy all tweets
 */
function handleCopyAll() {
    if (!currentResults || !currentResults.tweets) return;
    
    const allTweets = currentResults.tweets
        .map((tweet, index) => {
            const text = typeof tweet === 'string' ? tweet : tweet.text;
            return `Tweet ${index + 1}:\n${text}`;
        })
        .join('\n\n');
    
    const summary = `Brand Voice Summary:\n• Tone: ${currentResults.brand_voice_summary?.tone || 'N/A'}\n• Audience: ${currentResults.brand_voice_summary?.target_audience || 'N/A'}\n• Style: ${currentResults.brand_voice_summary?.communication_style || 'N/A'}\n• Themes: ${currentResults.brand_voice_summary?.key_themes || 'N/A'}\n\n`;
    
    navigator.clipboard.writeText(summary + allTweets).then(() => {
        showToast('All tweets copied to clipboard!');
    }).catch(() => {
        showToast('Failed to copy tweets');
    });
}

/**
 * Copy single tweet
 */
function copyTweet(index) {
    if (!currentResults || !currentResults.tweets[index]) return;
    
    const tweet = currentResults.tweets[index];
    const text = typeof tweet === 'string' ? tweet : tweet.text;
    
    navigator.clipboard.writeText(text).then(() => {
        showToast(`Tweet ${index + 1} copied!`);
    }).catch(() => {
        showToast('Failed to copy tweet');
    });
}

/**
 * Handle reset
 */
function handleReset() {
    brandForm.reset();
    currentResults = null;
    currentFormData = null;
    showState('default');
    
    // Scroll to generator
    document.getElementById('generator').scrollIntoView({ behavior: 'smooth' });
}

/**
 * Handle retry
 */
function handleRetry() {
    if (currentFormData) {
        // Fill form with previous data
        Object.keys(currentFormData).forEach(key => {
            const input = brandForm.elements[key];
            if (input) {
                input.value = currentFormData[key];
            }
        });
    }
    showState('default');
}

/**
 * Show error message
 */
function showError(message) {
    document.getElementById('errorMessage').textContent = message;
    showState('error');
}

/**
 * Show toast notification
 */
function showToast(message) {
    toastMessage.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

/**
 * Capitalize first letter
 */
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Escape HTML characters
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', init);

// Make copyTweet available globally
window.copyTweet = copyTweet;
