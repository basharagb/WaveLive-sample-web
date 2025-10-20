// WaveLive Agents Website JavaScript

// Language switching functionality
const LanguageSwitcher = {
    init() {
        this.setupLanguageDetection();
        this.setupSmoothScrolling();
        this.setupAnimations();
        this.setupFormValidation();
    },

    setupLanguageDetection() {
        // Auto-detect user's preferred language
        const userLang = navigator.language || navigator.userLanguage;
        const isArabic = userLang.startsWith('ar');
        
        // Store language preference
        localStorage.setItem('preferredLanguage', isArabic ? 'ar' : 'en');
        
        // Add language class to body
        document.body.classList.add(isArabic ? 'lang-ar' : 'lang-en');
    },

    switchLanguage(lang) {
        localStorage.setItem('preferredLanguage', lang);
        
        if (lang === 'ar') {
            window.location.href = 'index.html';
        } else {
            window.location.href = 'index-en.html';
        }
    },

    setupSmoothScrolling() {
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    },

    setupAnimations() {
        // Intersection Observer for fade-in animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                }
            });
        }, observerOptions);

        // Observe all sections
        document.querySelectorAll('section').forEach(section => {
            observer.observe(section);
        });

        // Add CSS for animations
        const style = document.createElement('style');
        style.textContent = `
            .animate-fade-in {
                animation: fadeInUp 0.8s ease-out forwards;
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            section {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.8s ease-out;
            }
            
            section.animate-fade-in {
                opacity: 1;
                transform: translateY(0);
            }
        `;
        document.head.appendChild(style);
    },

    setupFormValidation() {
        // Add form validation if registration forms exist
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', this.validateForm);
        });
    },

    validateForm(e) {
        const form = e.target;
        const inputs = form.querySelectorAll('input[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.classList.add('border-red-500');
                
                // Remove error class on input
                input.addEventListener('input', () => {
                    input.classList.remove('border-red-500');
                });
            }
        });

        if (!isValid) {
            e.preventDefault();
            this.showMessage('يرجى ملء جميع الحقول المطلوبة', 'error');
        }
    },

    showMessage(message, type = 'success') {
        const messageDiv = document.createElement('div');
        messageDiv.className = `fixed top-4 right-4 p-4 rounded-lg z-50 ${
            type === 'success' ? 'bg-green-500' : 'bg-red-500'
        } text-white`;
        messageDiv.textContent = message;
        
        document.body.appendChild(messageDiv);
        
        setTimeout(() => {
            messageDiv.remove();
        }, 3000);
    }
};

// Commission Calculator
const CommissionCalculator = {
    levels: {
        D: { points: 0, rate: 4 },
        C: { points: 2000000, rate: 8 },
        B: { points: 10000000, rate: 12 },
        A: { points: 50000000, rate: 16 },
        S: { points: 150000000, rate: 20 }
    },

    calculateLevel(points) {
        let level = 'D';
        for (const [levelName, levelData] of Object.entries(this.levels)) {
            if (points >= levelData.points) {
                level = levelName;
            }
        }
        return level;
    },

    calculateCommission(points, earnings) {
        const level = this.calculateLevel(points);
        const rate = this.levels[level].rate;
        return (earnings * rate) / 100;
    },

    addCalculatorWidget() {
        const calculatorHTML = `
            <div class="bg-white p-6 rounded-lg shadow-lg max-w-md mx-auto mt-8">
                <h3 class="text-lg font-semibold mb-4">حاسبة العمولة</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-sm font-medium mb-2">النقاط المحققة (30 يوم)</label>
                        <input type="number" id="points-input" class="w-full p-2 border rounded-lg" placeholder="0">
                    </div>
                    <div>
                        <label class="block text-sm font-medium mb-2">أرباح المضيفين</label>
                        <input type="number" id="earnings-input" class="w-full p-2 border rounded-lg" placeholder="0">
                    </div>
                    <div class="bg-gray-50 p-4 rounded-lg">
                        <div class="flex justify-between">
                            <span>المستوى:</span>
                            <span id="level-result" class="font-semibold">D</span>
                        </div>
                        <div class="flex justify-between">
                            <span>نسبة العمولة:</span>
                            <span id="rate-result" class="font-semibold">4%</span>
                        </div>
                        <div class="flex justify-between">
                            <span>العمولة المتوقعة:</span>
                            <span id="commission-result" class="font-semibold text-purple-600">$0</span>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const earningsSection = document.getElementById('earnings');
        if (earningsSection) {
            earningsSection.insertAdjacentHTML('beforeend', calculatorHTML);
            this.setupCalculatorEvents();
        }
    },

    setupCalculatorEvents() {
        const pointsInput = document.getElementById('points-input');
        const earningsInput = document.getElementById('earnings-input');
        const levelResult = document.getElementById('level-result');
        const rateResult = document.getElementById('rate-result');
        const commissionResult = document.getElementById('commission-result');

        const updateCalculation = () => {
            const points = parseInt(pointsInput.value) || 0;
            const earnings = parseFloat(earningsInput.value) || 0;
            
            const level = this.calculateLevel(points);
            const rate = this.levels[level].rate;
            const commission = this.calculateCommission(points, earnings);

            levelResult.textContent = level;
            rateResult.textContent = `${rate}%`;
            commissionResult.textContent = `$${commission.toFixed(2)}`;
        };

        pointsInput.addEventListener('input', updateCalculation);
        earningsInput.addEventListener('input', updateCalculation);
    }
};

// Scroll to top button
const ScrollToTop = {
    init() {
        this.createButton();
        this.setupScrollListener();
    },

    createButton() {
        const button = document.createElement('button');
        button.innerHTML = '↑';
        button.className = 'fixed bottom-6 left-6 bg-purple-600 text-white w-12 h-12 rounded-full shadow-lg hover:bg-purple-700 transition-all duration-300 opacity-0 pointer-events-none z-50';
        button.id = 'scroll-to-top';
        
        button.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        document.body.appendChild(button);
    },

    setupScrollListener() {
        const button = document.getElementById('scroll-to-top');
        
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                button.classList.remove('opacity-0', 'pointer-events-none');
                button.classList.add('opacity-100');
            } else {
                button.classList.add('opacity-0', 'pointer-events-none');
                button.classList.remove('opacity-100');
            }
        });
    }
};

// Statistics Counter Animation
const StatsCounter = {
    init() {
        this.setupCounters();
    },

    setupCounters() {
        const counters = document.querySelectorAll('[data-count]');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        });

        counters.forEach(counter => observer.observe(counter));
    },

    animateCounter(element) {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current).toLocaleString();
        }, 16);
    }
};

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    LanguageSwitcher.init();
    ScrollToTop.init();
    StatsCounter.init();
    CommissionCalculator.addCalculatorWidget();
});

// Export for use in other files
window.WaveLiveAgents = {
    LanguageSwitcher,
    CommissionCalculator,
    ScrollToTop,
    StatsCounter
};
