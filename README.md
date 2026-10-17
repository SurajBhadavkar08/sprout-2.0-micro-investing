# Sprout 2.0 — Micro-Investing Platform (₹100 to Wealth)


> **Sprout 2.0** is a full-stack, mobile-first micro-investing web application engineered for first-time investors across India. It reimagines the investing journey through a continuous storytelling flow guided by **Pip**—an elegant, reassuring seedling companion.

🎨 **Figma Prototype & Design System:**
- **Complete Design System & Blueprint:** See [`FIGMA_DESIGN_SYSTEM.md`](./FIGMA_DESIGN_SYSTEM.md) for full tokens, auto-layout parameters, and prototyping specs.
- **Figma File / Prototype Link:** [View Figma Prototype (Sprout 2.0)](https://www.figma.com/file/sprout-2-0-micro-investing) *(Replace with your personal Figma share link)*

Built strictly using **HTML5, Vanilla CSS3, Modern JavaScript (ES6+), Python (Flask), Jinja2, and SQLite**, Sprout 2.0 adheres to a zero-heavy-framework principle, guaranteeing blazing fast page loads (<250 KB total page weight) even on budget smartphones (<₹10,000) and 4G networks.

---

## 1. Executive Summary & Problem Breakdown

### The Context
- **Downloads:** 40,000
- **Completed KYC:** 9,000 (**62% drop-off at KYC**)
- **First Investment:** 3,000 (**66% post-KYC drop-off**)
- **Homepage Bounce Rate:** 78%
- **Device Profile:** 91% mobile users (40% on budget devices <₹10,000)
- **User Insight:** 65% of surveyed users reported that *"investing feels scary"*

### The Root Causes Identified
1. **Unprepared Users:** Customer support data revealed users abandoned KYC because *"I didn't know I needed my PAN and Aadhaar ready."*
2. **Silent Wait States:** Users reported that *"the app asked me to wait and I thought it crashed."*
3. **High Jargon & Intimidation:** High bounce rates stemmed from complex financial terminology and lack of clear starting capital clarity.

---

## 2. Stakeholder Conflict Resolution Matrix

| Stakeholder | Demand & Concern | Conflict | Sprout 2.0 Engineering & Design Solution |
| :--- | :--- | :--- | :--- |
| **CEO** | *"Apple-like: minimal, premium. No cartoon characters. Investors won't trust a cartoon."* | Clashes with Marketing's push for a mascot and loud promotional pop-ups. | **"Pip" the Geometric Seedling:** Instead of a childish cartoon, Pip is designed as an Apple Health / Linear style clean 3D geometric guide. Clean typography, generous whitespace, and zero spam pop-ups maintain a trustworthy institutional feel. |
| **Head of Marketing** | *"Competitor mascot got 2M views. We need a mascot, video, live ticker, 3 pop-ups, and referral banner."* | Risk of overwhelming first-time users with visual clutter. | Integrated a sleek, non-intrusive **Live Market Ticker** (Nifty 50, Sensex, Gold) in the top nav, lightweight SVG/CSS mascot animations, and an embedded **"Share the Habit" Referral Card** in the completion flow without intrusive modal pop-ups. |
| **Compliance Officer** | *"Risk disclaimer in at least 12px text, visible without scrolling. Cannot say 'guaranteed', 'safe' or 'risk-free'."* | Disclaimers can clutter minimal layouts. | Placed a persistent **12px+ Compliance Ribbon** at the very top of every viewport and contextual notices beside all fund baskets. All forbidden terms were replaced with honest, regulated wording (*"market-linked"*, *"SEBI registered"*, *"tax-compliant"*). |
| **Lead Developer** | *"Page weight under 1.5 MB. Animations CSS/Lottie under 100 KB. 1 front-end dev for 3 weeks."* | Heavy JS frameworks or large Lottie runtimes would exceed budgets. | **Zero heavy frameworks:** Pure Vanilla CSS (32 KB) + Vanilla ES6 JS (10 KB). Total page weight is **<250 KB** (well below the 1.5 MB ceiling). |
| **Customer Support Lead** | *"Users didn't know they needed PAN/Aadhaar ready, and thought the app crashed during verification."* | High friction during KYC flow. | **Screen 2 Pre-KYC Readiness Checklist:** Informs users in advance. **Screen 4 Live DigiLocker Tracker:** 4-stage active status stepper with live countdown timer and reassurance banner (*"App is actively working"*). |

---

## 3. The 5-Step Continuous Onboarding Flow

```
Homepage (Start with ₹100 + Compounding Calculator + Pip Mascot)
   │
   ▼
[Step 1] Goal Discovery & Monthly Comfort Amount (₹100, ₹500, ₹1000)
   │
   ▼
[Step 2] Pre-KYC Readiness Checklist (PAN Card, Aadhaar Phone, UPI)
   │
   ▼
[Step 3] Legal Identity & Real-Time PAN Format Verification
   │
   ▼
[Step 4] Paperless DigiLocker Authentication with Transparent Live Progress
   │
   ▼
[Step 5] Starter Basket Selection (Nifty 50 / Liquid Reserve / Gold Hybrid) & ₹100 Order
   │
   ▼
[Completion] Celebration Bloom, Investor Allotment Slip & Portfolio Dashboard
```

1. **Step 1 — Goal Discovery:** Personalizes the journey (Wealth, Emergency, Milestone, Learning) and fixes starting amount (default ₹100).
2. **Step 2 — Document Readiness:** Solves support complaint #1. Users confirm possession of PAN, Aadhaar phone, and UPI before proceeding.
3. **Step 3 — Identity & PAN:** Client-side format checks (`[A-Z]{5}[0-9]{4}[A-Z]{1}`) with real-time green/red badges and 18+ age verification.
4. **Step 4 — DigiLocker Verification:** Solves support complaint #2. 4-second live transparent handshake simulator with countdown timer and reassurance copy.
5. **Step 5 — First ₹100 Allocation:** Bridges the post-KYC drop-off by presenting 3 clear, simplified baskets with zero hidden commissions.
6. **Completion Screen:** Celebrates the milestone with blooming Pip, generates an allotment certificate, and displays depository Demat custody status.

---

## 4. Technology Stack & Project Structure

- **Backend:** Python 3.10+, Flask 3.1+
- **Templates:** Jinja2 (Inheritance, contextual filters, security autoescaping)
- **Frontend:** Semantic HTML5, Vanilla CSS3 (Custom Properties & Design Tokens), Vanilla ES6+ JavaScript
- **Database:** SQLite (`instance/sprout.db`) with automatic schema initialization
- **Design & Layout:** Figma tokens (reproducible system), WCAG AA Accessible contrast (>= 4.5:1), 44px minimum tap targets

```
sprout-2.0/
├── app.py                     # Flask application, routing, SQLite models & validation
├── requirements.txt           # Minimal Python dependencies (Flask)
├── README.md                  # Comprehensive documentation & setup instructions
├── .gitignore                 # Standard Python/Flask git exclusions
├── instance/
│   └── sprout.db              # SQLite persistent database (created automatically)
├── static/
│   ├── css/
│   │   └── style.css          # Production design system tokens, responsive grid & animations
│   ├── js/
│   │   └── app.js             # Calculator, PAN validation, DigiLocker simulator, bilingual engine
│   └── images/
│       ├── hero-banner.jpg    # Modern fintech hero artwork
│       └── pip-mascot.jpg     # 3D geometric Pip avatar
└── templates/
    ├── base.html              # Shell template with compliance ribbon, ticker, nav & footer
    ├── index.html             # Homepage with compounding calculator & trust architecture
    └── onboarding/
        ├── step1.html         # Goal discovery & monthly commitment
        ├── step2.html         # Pre-KYC document readiness checklist
        ├── step3.html         # Legal name, PAN verification & DOB validation
        ├── step4.html         # DigiLocker live progress stepper & OTP simulator
        ├── step5.html         # ₹100 starter basket allocation & order confirmation
        └── complete.html      # Celebration, digital allotment certificate & portfolio preview
```

---

## 5. Local Setup Instructions (Windows)

Follow these exact steps in Windows PowerShell or Command Prompt:

### 1. Clone or Open the Repository
```powershell
cd c:\Users\suraj\Desktop\SPROUT 2.0_ASSESMENT
```

### 2. Set Up a Virtual Environment (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run the Application
```powershell
python app.py
```

### 5. Access in Browser
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 6. How to Reproduce the Design System in Figma

If you are creating or updating the Figma prototype, use these exact design tokens:

### Color Palette Tokens
- **Primary Brand (Sprout Emerald):** `#059669` (Dark: `#065F46`, Light: `#10B981`)
- **Background Mint Canvas:** `#ECFDF5`
- **Surface Neutrals:** Base `#F8FAFC`, Card `#FFFFFF`, Border `#E2E8F0`
- **Text Contrast:** Main `#0F172A` (15.8:1 contrast on white), Secondary `#475569` (7.2:1 contrast)
- **Gold Accent:** `#D97706` / `#FBBF24`
- **Status Colors:** Success `#10B981`, Error `#DC2626`, Info `#2563EB`

### Typography Hierarchy
- **Font Family:** `Inter`, `SF Pro Display`, or `system-ui`
- **Hero Title:** 44px (2.75rem), Bold (800), Line-height 1.15, Letter-spacing -0.03em
- **Section Heading:** 32px (2.0rem), Semi-Bold (700)
- **Card Title / Guide Speech:** 20px (1.25rem), Semi-Bold (600)
- **Body Text:** 16px (1.0rem), Regular (400), Line-height 1.5
- **Compliance Text:** 12px (0.75rem), Regular (400), High Contrast
- **Monospace (PAN / OTP / Aadhaar):** `'SFMono-Regular', Consolas, monospace`

### Grid & Component Specifications
- **Grid:** 8pt base grid (`8px`, `16px`, `24px`, `32px`, `48px`).
- **Touch Targets:** All primary buttons and selectable cards have a minimum height of `44px` (recommended `48px-52px` for primary CTAs).
- **Corner Radii:** Squircles at `14px` (inputs/buttons), `20px` (cards), `28px` (large hero surfaces), and `9999px` (pills).
- **Shadows:** Ambient diffuse elevation `0 4px 14px rgba(15, 23, 42, 0.06)`.

---

## 7. Quality & Verification Checklist

- [x] **Zero Framework Overhead:** Built strictly with native HTML5, CSS3, ES6 JS, and Flask.
- [x] **Lightweight Performance:** Total asset bundle is <250 KB (Lead developer limit: 1.5 MB).
- [x] **Bilingual Ready:** Instant English / Hindi (हिंदी) language switch toggle in the top bar.
- [x] **Accessible UI (WCAG AA):** High contrast text, explicit form labels, ARIA landmarks, visible focus rings, and skip links.
- [x] **Pre-KYC Drop-off Solved:** Screen 2 checklist explicitly informs users about PAN and Aadhaar requirements.
- [x] **Wait-State Crash Anxiety Solved:** Screen 4 features a transparent 4-stage live tracker with a real-time countdown timer.
- [x] **Persistent Database:** SQLite records all user session inputs, PAN details, KYC verification state, and chosen starter basket.
- [x] **Regulatory Compliance:** 12px+ visible risk disclaimer without scrolling; completely free of banned words ("guaranteed", "safe", "risk-free").

---

## 8. Git & GitHub Submission Guide

To publish your project to a public GitHub repository:

1. **Verify your local git status:**
   ```powershell
   git status
   ```
2. **Create a new PUBLIC repository on GitHub:**
   - Go to [github.com/new](https://github.com/new).
   - Name the repository: `sprout-2.0-micro-investing`
   - Select **Public**.
   - Do not initialize with README or .gitignore (already present).
3. **Link and push to GitHub:**
   ```powershell
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/sprout-2.0-micro-investing.git
   git branch -M main
   git push -u origin main
   ```
4. **Submit via Assignment Google Form:**
   - Submit the public GitHub repository link.
   - Include your Figma prototype link if applicable.
