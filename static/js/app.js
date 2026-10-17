/**
 * Sprout 2.0 - Core Frontend Application
 * Handles client-side validation, compounding calculator, DigiLocker live progress,
 * and bilingual language switching.
 */

document.addEventListener('DOMContentLoaded', () => {
  initLanguageSwitcher();
  initCompoundingCalculator();
  initPanValidation();
  initDigiLockerSimulator();
  initAutoSave();
  initResetButton();
});

/* ==========================================================================
   1. BILINGUAL LANGUAGE SWITCHER (English / हिंदी)
   Enables seamless language switching without page reloads or redesigns
   ========================================================================== */
const TRANSLATIONS = {
  en: {
    lang_btn: 'हिंदी',
    hero_badge: 'SEBI Registered Partners • Start with ₹100',
    hero_title_1: 'Plant your wealth.',
    hero_title_2: 'Start with just ₹100.',
    hero_sub: "India's friendliest micro-investing journey. No confusing jargon, no big money needed. Grow with India's top 50 companies with the spare change in your pocket.",
    cta_start: 'Start with ₹100 Now',
    cta_sub: 'Takes 2 mins • Zero paperwork',
    mascot_quote: "Hi, I'm Pip! I'm here to make investing simple, transparent, and fearless for you.",
    calc_tag: 'The Power of Consistency',
    calc_title: 'See what ₹100 can grow into',
    calc_desc: 'You do not need lakhs of rupees to build wealth. Small seeds planted regularly create mighty financial trees.',
    prep_title: 'Before you start: 2-Minute KYC Checklist',
    prep_desc: 'To prevent unexpected pauses, keep these 2 items handy:',
    prep_pan: 'PAN Card Number',
    prep_aadhaar: 'Aadhaar-linked Mobile',
    prep_upi: 'UPI / Bank for ₹100'
  },
  hi: {
    lang_btn: 'English',
    hero_badge: 'SEBI रजिस्टर्ड पार्टनर्स • केवल ₹100 से शुरुआत',
    hero_title_1: 'अपनी संपत्ति का बीज बोएं.',
    hero_title_2: 'शुरुआत करें सिर्फ ₹100 से.',
    hero_sub: 'भारत का सबसे आसान माइक्रो-इन्वेस्टिंग ऐप। न कोई कठिन शब्द, न लाखों रुपयों की जरूरत। अपनी जेब खर्च से भारत की टॉप 50 कंपनियों में निवेश करें।',
    cta_start: 'अभी ₹100 से शुरू करें',
    cta_sub: 'सिर्फ 2 मिनट • जीरो पेपरवर्क',
    mascot_quote: 'नमस्ते, मैं हूँ पिप (Pip)! निवेश को आपके लिए आसान और बिना किसी डर के समझाना मेरा काम है।',
    calc_tag: 'नियमित बचत की ताकत',
    calc_title: 'देखें ₹100 कितना बढ़ सकता है',
    calc_desc: 'धन बनाने के लिए लाखों की जरूरत नहीं है। नियमित रूप से बोए गए छोटे बीज एक दिन विशाल वृक्ष बन जाते हैं।',
    prep_title: 'शुरू करने से पहले: 2-मिनट KYC चेकलिस्ट',
    prep_desc: 'प्रक्रिया बिना रुकावट पूरी करने के लिए ये 2 चीजें अपने पास रखें:',
    prep_pan: 'पैन कार्ड नंबर',
    prep_aadhaar: 'आधार से लिंक मोबाइल फोन',
    prep_upi: '₹100 ट्रांसफर हेतु UPI / बैंक'
  }
};

function initLanguageSwitcher() {
  const toggleBtn = document.getElementById('lang-toggle-btn');
  if (!toggleBtn) return;

  const savedLang = localStorage.getItem('sprout_lang') || 'en';
  applyLanguage(savedLang);

  toggleBtn.addEventListener('click', () => {
    const currentLang = localStorage.getItem('sprout_lang') || 'en';
    const nextLang = currentLang === 'en' ? 'hi' : 'en';
    localStorage.setItem('sprout_lang', nextLang);
    applyLanguage(nextLang);
  });
}

function applyLanguage(lang) {
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  const btnLabel = document.getElementById('lang-btn-label');
  if (btnLabel) {
    btnLabel.textContent = lang === 'en' ? 'हिंदी' : 'English';
  }
}

/* ==========================================================================
   2. COMPOUNDING SEED CALCULATOR (Homepage)
   Calculates SIP future value based on 12% broad equity index CAGR
   ========================================================================== */
function initCompoundingCalculator() {
  const slider = document.getElementById('calc-amount-slider');
  const yearsSlider = document.getElementById('calc-years-slider');
  const amountBadge = document.getElementById('calc-amount-display');
  const yearsBadge = document.getElementById('calc-years-display');
  const totalInvestedEl = document.getElementById('calc-total-invested');
  const wealthGainsEl = document.getElementById('calc-wealth-gains');
  const finalValueEl = document.getElementById('calc-final-value');

  if (!slider) return;

  function updateCalculation() {
    const monthlyAmt = parseInt(slider.value, 10) || 100;
    const years = yearsSlider ? parseInt(yearsSlider.value, 10) : 5;
    const annualRate = 0.12; // 12% benchmark historical equity returns (not guaranteed)
    const monthlyRate = annualRate / 12;
    const totalMonths = years * 12;

    // Future Value of Monthly SIP formula: P * [((1 + r)^n - 1) / r] * (1 + r)
    const futureValue = monthlyAmt * ((Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate) * (1 + monthlyRate);
    const totalInvested = monthlyAmt * totalMonths;
    const gains = Math.max(0, futureValue - totalInvested);

    if (amountBadge) amountBadge.textContent = `₹${monthlyAmt.toLocaleString('en-IN')}`;
    if (yearsBadge) yearsBadge.textContent = `${years} ${years === 1 ? 'Year' : 'Years'}`;
    if (totalInvestedEl) totalInvestedEl.textContent = `₹${Math.round(totalInvested).toLocaleString('en-IN')}`;
    if (wealthGainsEl) wealthGainsEl.textContent = `+₹${Math.round(gains).toLocaleString('en-IN')}`;
    if (finalValueEl) finalValueEl.textContent = `₹${Math.round(futureValue).toLocaleString('en-IN')}`;
  }

  slider.addEventListener('input', updateCalculation);
  if (yearsSlider) yearsSlider.addEventListener('input', updateCalculation);

  // Preset buttons
  document.querySelectorAll('.preset-btn[data-amt]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.preset-btn[data-amt]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      slider.value = btn.getAttribute('data-amt');
      updateCalculation();
    });
  });

  updateCalculation();
}

/* ==========================================================================
   3. PAN & FORM VALIDATION (Step 3)
   ========================================================================== */
function initPanValidation() {
  const panInput = document.getElementById('pan_number');
  const panBadge = document.getElementById('pan-status-badge');
  if (!panInput) return;

  const panRegex = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;

  panInput.addEventListener('input', () => {
    panInput.value = panInput.value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 10);
    const val = panInput.value;

    if (val.length === 10) {
      if (panRegex.test(val)) {
        panInput.classList.remove('is-invalid');
        panInput.classList.add('is-valid');
        if (panBadge) {
          panBadge.textContent = '✓ Valid PAN format';
          panBadge.style.color = '#059669';
        }
      } else {
        panInput.classList.remove('is-valid');
        panInput.classList.add('is-invalid');
        if (panBadge) {
          panBadge.textContent = '✕ Invalid PAN structure';
          panBadge.style.color = '#DC2626';
        }
      }
    } else {
      panInput.classList.remove('is-valid', 'is-invalid');
      if (panBadge) {
        panBadge.textContent = `${val.length}/10 characters`;
        panBadge.style.color = '#64748B';
      }
    }
  });
}

/* ==========================================================================
   4. DIGILOCKER TRANSPARENT PROGRESS SIMULATOR (Step 4)
   Solves customer support complaint: "The app asked me to wait and I thought it crashed."
   Provides real-time feedback with live steps, timer, and reassurance.
   ========================================================================== */
function initDigiLockerSimulator() {
  const triggerBtn = document.getElementById('btn-verify-digilocker');
  const progressBox = document.getElementById('digilocker-progress-box');
  const otpSection = document.getElementById('digilocker-otp-section');
  const statusStep1 = document.getElementById('step-track-1');
  const statusStep2 = document.getElementById('step-track-2');
  const statusStep3 = document.getElementById('step-track-3');
  const countdownEl = document.getElementById('digilocker-countdown');
  const form = document.getElementById('form-step4');

  if (!triggerBtn || !progressBox) return;

  triggerBtn.addEventListener('click', () => {
    triggerBtn.disabled = true;
    triggerBtn.textContent = 'Connecting securely...';
    progressBox.style.display = 'block';

    let secondsLeft = 4;
    const interval = setInterval(() => {
      secondsLeft--;
      if (countdownEl && secondsLeft > 0) {
        countdownEl.textContent = `${secondsLeft}s remaining...`;
      }
    }, 1000);

    // Stage 1: Initiated
    setTimeout(() => {
      if (statusStep1) {
        statusStep1.classList.remove('active');
        statusStep1.classList.add('completed');
        statusStep1.querySelector('.tracker-icon').textContent = '✓';
      }
      if (statusStep2) {
        statusStep2.classList.add('active');
      }
    }, 1400);

    // Stage 2: UIDAI gateway checked
    setTimeout(() => {
      if (statusStep2) {
        statusStep2.classList.remove('active');
        statusStep2.classList.add('completed');
        statusStep2.querySelector('.tracker-icon').textContent = '✓';
      }
      if (statusStep3) {
        statusStep3.classList.add('active');
      }
    }, 2800);

    // Stage 3: Completed & show OTP entry
    setTimeout(() => {
      clearInterval(interval);
      if (statusStep3) {
        statusStep3.classList.remove('active');
        statusStep3.classList.add('completed');
        statusStep3.querySelector('.tracker-icon').textContent = '✓';
      }
      if (countdownEl) {
        countdownEl.textContent = 'Handshake verified!';
      }

      // Reveal OTP section smoothly
      if (otpSection) {
        otpSection.style.display = 'block';
        otpSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      triggerBtn.style.display = 'none';
      const submitBtn = document.getElementById('btn-submit-step4');
      if (submitBtn) {
        submitBtn.style.display = 'inline-flex';
      }
    }, 4000);
  });
}

/* ==========================================================================
   5. FORM STATE AUTOSAVE
   Preserves entered data so navigating back or refreshing never loses state.
   ========================================================================== */
function initAutoSave() {
  const inputs = document.querySelectorAll('input[name], select[name]');
  if (!inputs.length) return;

  let debounceTimer;
  inputs.forEach(input => {
    input.addEventListener('change', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        saveField(input.name, input.value);
      }, 500);
    });
  });

  function saveField(name, value) {
    if (!name || value === undefined) return;
    fetch('/api/autosave', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ [name]: value })
    }).catch(() => {
      // Graceful offline fallback: store in sessionStorage
      sessionStorage.setItem(`sprout_${name}`, value);
    });
  }
}

/* ==========================================================================
   6. RESET ONBOARDING DEMO
   ========================================================================== */
function initResetButton() {
  const resetBtns = document.querySelectorAll('.btn-reset-onboarding');
  resetBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (confirm('Reset onboarding state to start from Screen 1?')) {
        fetch('/api/reset', { method: 'POST' })
          .then(() => {
            sessionStorage.clear();
            window.location.href = '/onboarding/step1';
          });
      }
    });
  });
}
