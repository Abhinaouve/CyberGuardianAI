// ========================================
// CYBER GUARDIAN AI - DASHBOARD SCRIPTS
// ========================================

// Dynamic status updates
document.addEventListener('DOMContentLoaded', function() {
    updateSecurityStatus();
    setInterval(updateSecurityStatus, 5000);
});

function updateSecurityStatus() {
    const statusDot = document.querySelector('.status-dot');
    if (statusDot) {
        statusDot.style.animation = 'none';
        statusDot.offsetHeight; // Trigger reflow
        statusDot.style.animation = 'pulse 2s infinite';
    }
}

// Animated counter for stats
function animateCounter(element, target) {
    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.round(current);
    }, 30);
}

// Initialize counter animations
document.addEventListener('DOMContentLoaded', function() {
    const statValues = document.querySelectorAll('.stat-value');
    statValues.forEach(stat => {
        const text = stat.textContent;
        const number = parseInt(text);
        if (!isNaN(number)) {
            animateCounter(stat, number);
        }
    });
});

// Console warning to deter bad actors
console.log('%c⚠️ Cyber Guardian AI Security System Active ⚠️', 
    'color: #ef4444; font-size: 16px; font-weight: bold;');
console.log('%cThis is a protected system. Unauthorized access is prohibited.', 
    'color: #e2e8f0; font-size: 12px;');