# Sprout 2.0 — Figma Design System & Prototype Blueprint

This document provides the complete, production-grade Figma design system, auto-layout specifications, component variants, and interactive prototyping guidelines to create or evaluate the **Sprout 2.0** Figma file.

🔗 **Active Figma File:** [Sprout 2.0 — Micro-Investing Platform (Figma Canvas)](https://www.figma.com/design/tZvn8TYcgbfGX6QrdqFtiu/Sprout-2.0-%E2%80%94-Micro-Investing-Platform--%E2%82%B9100-to-Wealth-?node-id=0-1&t=9nmkGULIVUU0Uivz-1)

---

## 1. Global Design Tokens & Styles

### A. Color Palette (Styles)
Create these Local Styles in your Figma file (`Right Sidebar > Local Styles > Add Color`):

| Token Name | Hex Code | HSL / RGB | Intended Usage | WCAG AA Contrast on White |
| :--- | :--- | :--- | :--- | :--- |
| `Brand/Primary` | `#059669` | `hsl(160, 94%, 31%)` | Primary CTA buttons, active radio borders, key highlights | **4.6:1** (Pass) |
| `Brand/Primary Dark` | `#065F46` | `hsl(164, 88%, 20%)` | Headings, stepper indicators, high-emphasis text | **8.5:1** (Pass) |
| `Brand/Primary Light`| `#10B981` | `hsl(159, 84%, 39%)` | Progress bar gradients, active dot rings, icons | **3.1:1** (Large text/UI) |
| `Brand/Mint Canvas`  | `#ECFDF5` | `hsl(152, 86%, 96%)` | Hero backdrop tint, selected card background | Background surface |
| `Neutral/Text Main`  | `#0F172A` | `hsl(222, 47%, 11%)` | Primary headlines, form labels, body text | **15.8:1** (Pass AAA) |
| `Neutral/Text Muted` | `#475569` | `hsl(215, 19%, 35%)` | Subtitles, supporting copy, helper notes | **7.2:1** (Pass AAA) |
| `Neutral/Text Subtle`| `#64748B` | `hsl(215, 16%, 47%)` | Meta captions, timestamp disclaimers | **4.6:1** (Pass AA) |
| `Neutral/Surface`    | `#FFFFFF` | `hsl(0, 0%, 100%)`   | Primary cards, form input backgrounds | N/A |
| `Neutral/Canvas`     | `#F8FAFC` | `hsl(210, 40%, 98%)` | App background, ticker background | N/A |
| `Neutral/Border`     | `#E2E8F0` | `hsl(214, 32%, 91%)` | Card borders, form input inactive borders | N/A |
| `Accent/Gold`        | `#D97706` | `hsl(38, 92%, 44%)`  | Milestone badges, wealth returns, referral cards | **4.5:1** (Pass AA) |
| `Feedback/Error`     | `#DC2626` | `hsl(0, 72%, 50%)`   | Validation error borders and error text | **4.6:1** (Pass AA) |
| `Feedback/Success`   | `#059669` | `hsl(160, 94%, 31%)` | Verified checkmarks, completed milestones | **4.6:1** (Pass AA) |

---

### B. Typography Hierarchy (Text Styles)
Font Family: **Inter** (Google Font) or **SF Pro Display**

| Style Name | Size | Weight | Line Height | Letter Spacing | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Display/Hero-Desktop` | 44px (2.75rem) | 800 (ExtraBold) | 115% | -0.03em | Homepage Hero headline |
| `Display/Hero-Mobile`  | 32px (2.0rem)  | 800 (ExtraBold) | 120% | -0.02em | Mobile Hero headline |
| `Heading/H1`          | 32px (2.0rem)  | 700 (Bold)      | 125% | -0.02em | Section titles, celebration title |
| `Heading/H2`          | 24px (1.5rem)  | 700 (Bold)      | 130% | -0.01em | Onboarding card titles, speech bubbles |
| `Heading/H3`          | 18px (1.125rem)| 600 (SemiBold)  | 140% | 0em    | Step card titles, basket titles |
| `Body/Regular`        | 16px (1.0rem)  | 400 (Regular)   | 150% | 0em    | General body paragraphs |
| `Body/Medium`         | 15px (0.938rem)| 500 (Medium)    | 150% | 0em    | Form inputs, option descriptions |
| `Body/SemiBold`       | 15px (0.938rem)| 600 (SemiBold)  | 140% | 0em    | Button labels, slider numbers |
| `Caption/Compliance`  | 12px (0.75rem) | 500 (Medium)    | 140% | +0.01em| Mandatory risk notices, ticker text |
| `Data/Monospace`      | 16px (1.0rem)  | 600 (SemiBold)  | 100% | +0.10em| PAN number, OTP input, Aadhaar numbers |

---

### C. Spacing & Grid System (8pt Grid)
- **Base Grid:** `8px` (`8`, `16`, `24`, `32`, `40`, `48`, `64`)
- **Desktop Canvas Frame:** `1440px × 1024px` (Layout Grid: 12 Columns, Margin `80px`, Gutter `24px`)
- **Mobile Canvas Frame:** `390px × 844px` (iPhone 14/15) or `360px × 800px` (Android 10k phone) (Layout Grid: 4 Columns, Margin `16px`, Gutter `12px`)
- **Corner Radii (Squircles):**
  - Inputs & Small Buttons: `14px`
  - Cards & Modal Surfaces: `20px`
  - Hero Highlight Surfaces: `28px`
  - Pill Badges & Rounded Buttons: `9999px`

---

## 2. Reusable Component Library (Figma Components)

### Component 1: `Button / Primary`
- **Auto Layout:** Horizontal, Padding `14px 28px`, Gap `8px`, Align Center.
- **Min Height:** `48px` (exceeds WCAG 44px tap target).
- **Background:** Linear Gradient `135deg: #059669 -> #047857`.
- **Text:** 15px SemiBold, Color `#FFFFFF`.
- **Variants:**
  - `State=Default`: Normal shadow `0 4px 12px rgba(5, 150, 105, 0.25)`
  - `State=Hover`: Shadow `0 6px 16px rgba(5, 150, 105, 0.35)`, Y: -1px
  - `State=Disabled`: Background `#CBD5E1`, Text `#94A3B8`, Cursor: Not-Allowed

### Component 2: `Compliance / Top Ribbon` (Mandatory Regulatory Element)
- **Auto Layout:** Horizontal, Padding `8px 24px`, Align Center, Space Between.
- **Width:** `Fill Container` (Desktop 1440px / Mobile 390px).
- **Background:** `#0F172A`.
- **Text:** 12px Regular, Color `#E2E8F0`, Line Height 1.4. Bold emphasis on *"Market Risk Disclosure"*.

### Component 3: `Mascot / Pip Guidance Bubble`
- **Auto Layout:** Horizontal, Padding `16px`, Gap `16px`, Align Top.
- **Background:** `#FFFFFF` or `#F1F5F9`, Border `1.5px solid #E2E8F0`, Radius `16px`.
- **Avatar:** 48px circle with 3D seedling mascot image/vector, 2px `#10B981` border ring.
- **Text Area:** Auto Layout Vertical, Gap `4px`.
  - Title: 14px Bold (`#0F172A`)
  - Subtitle: 13px Regular (`#475569`)

### Component 4: `Progress Stepper / Onboarding`
- **Auto Layout:** Vertical, Gap `8px`, Width `Fill Container`.
- **Top Row:** Step label (*"Step 2 of 5: Document Checklist"*) on left (13px SemiBold `#475569`), completion badge (*"40% Completed"*) on right (12px SemiBold in `#ECFDF5` pill with `#065F46` text).
- **Progress Track:** Height `6px`, Radius `9999px`, Background `#E2E8F0`.
- **Progress Fill:** Width variant (`20%`, `40%`, `60%`, `80%`, `100%`), Fill Gradient `#10B981 -> #059669`.

### Component 5: `Form Input / Text & Mono`
- **Auto Layout:** Vertical, Gap `6px`.
- **Label:** 14px SemiBold (`#0F172A`), with optional Right Helper (`#64748B`).
- **Input Box:** Height `48px`, Padding `12px 16px`, Radius `14px`, Border `1.5px solid #E2E8F0`, Background `#FFFFFF`.
- **Variants:**
  - `State=Default`
  - `State=Focused`: Border `#059669`, Outer Glow `0 0 0 3px rgba(5, 150, 105, 0.15)`
  - `State=Valid`: Border `#10B981`, Right Icon `✓`
  - `State=Error`: Border `#DC2626`, Red Error Text underneath

### Component 6: `Selection Card / Radio Option`
- **Auto Layout:** Vertical (Step 1) or Horizontal (Step 5), Padding `16px`, Gap `8px`.
- **Radius:** `16px`, Border `1.5px solid #E2E8F0`.
- **Variants:**
  - `Selected=False`: Background `#FFFFFF`, Border `#E2E8F0`.
  - `Selected=True`: Background `#ECFDF5`, Border `#059669`, Box Shadow `0 0 0 1px #059669`.

---

## 3. Screen-by-Screen Layout Specifications

### Frame 1: Homepage (`Homepage — Desktop 1440` & `Homepage — Mobile 390`)
1. **Compliance Ribbon:** Top bar with 12px risk disclaimer visible without scrolling.
2. **Market Ticker:** Live continuous marquee showing NIFTY 50 (+0.42%), SENSEX (+0.38%), GOLD (+0.15%).
3. **Header:** Sprout 2.0 logo, Language Switcher toggle (`🌐 हिंदी`), and *"Start with ₹100"* CTA button.
4. **Hero Section:**
   - Left: Trust pill badge, Hero Title (*"Plant your wealth. Start with just ₹100."*), subheadline, Pip speech callout (*"Hi, I'm Pip! Let's start with ₹100"*), and Primary CTA button.
   - Right: Clean 3D fintech hero card with seedling in geometric pot, ₹100 growth cards, and mint ambient lighting.
5. **Compounding Calculator Card:**
   - Left: Monthly investment slider (`₹100` to `₹5,000`) with quick preset buttons (`₹100`, `₹500`, `₹1,000`, `₹2,500`), and duration slider (`1` to `10` years).
   - Right: Deep forest green projection card showing estimated wealth (`₹13,915` in 5 years from ₹100/mo) with breakdown.
6. **Pre-KYC Readiness Banner (Direct Support Fix):**
   - Highlighting the 2 documents needed (PAN card & Aadhaar mobile) to prevent drop-off.
7. **Footer:** Comprehensive AMFI registration details, risk disclaimer, and 256-bit bank encryption badges.

---

### Frame 2: Onboarding Screen 1 — Goal Discovery (`Onboarding / Step 1`)
- **Stepper:** Step 1 of 5 (20%).
- **Pip Guidance Card:** *"What brings you to Sprout today? Starting with ₹100 builds consistency without stress."*
- **Form Fields:**
  - Optional First Name.
  - 4 Goal Cards (Grid 2×2 on desktop, 1-col on mobile):
    1. Long-Term Wealth Creation
    2. Instant Emergency Shield
    3. Dream Purchase / Travel
    4. Learn Investing with ₹100
  - Monthly starting amount selector pills (`₹100`, `₹500`, `₹1,000`, `₹2,000`).
- **Footer Buttons:** `← Home` (text link) and `Next: Document Checklist →` (Primary Button).

---

### Frame 3: Onboarding Screen 2 — Document Readiness Checklist (`Onboarding / Step 2`)
*Directly resolves Customer Support complaint: "Users didn't know they needed PAN & Aadhaar ready."*
- **Stepper:** Step 2 of 5 (40%).
- **Pip Guidance Card:** *"Let's get you set up in under 2 minutes. Having these 2 documents ready ensures zero delays!"*
- **Interactive Checklists:**
  - [x] **1. PAN Card Number:** 10-digit tax ID.
  - [x] **2. Aadhaar-Linked Mobile:** Ready to receive 6-digit OTP.
  - [x] **3. UPI / Bank Account:** For transferring the first ₹100.
- **Security Callout:** Bank-grade 256-bit encryption through government DigiLocker gateway.
- **Footer Buttons:** `← Back to Step 1` and `I Have These Ready — Continue →`.

---

### Frame 4: Onboarding Screen 3 — Identity & PAN Verification (`Onboarding / Step 3`)
- **Stepper:** Step 3 of 5 (60%).
- **Pip Guidance Card:** *"Enter your legal details. We verify your PAN with the Income Tax Department registry."*
- **Form Fields:**
  - Legal Full Name (as per PAN Card).
  - PAN Number: Monospace text, auto-capitalization, real-time green checkmark (*"✓ Valid PAN format"*).
  - Date of Birth: Date picker ensuring applicant is 18+ years old.
  - Aadhaar Mobile Number: `+91` prefix with 10 digits.
- **Footer Buttons:** `← Back to Checklist` and `Verify & Proceed to DigiLocker →`.

---

### Frame 5: Onboarding Screen 4 — Paperless DigiLocker KYC (`Onboarding / Step 4`)
*Directly resolves Customer Support complaint: "The app asked me to wait and I thought it crashed."*
- **Stepper:** Step 4 of 5 (80%).
- **Pip Guidance Card:** *"Zero paperwork with DigiLocker. Watch the live progress below!"*
- **Aadhaar Entry:** Masked Aadhaar field (`•••• •••• [4321]`).
- **Interactive Trigger:** Button *"Connect to DigiLocker & Fetch OTP"*.
- **Transparent Live Progress Box:**
  - Header: Live Gateway Status with pulsing green indicator and countdown (*"4s remaining..."*).
  - Stage 1: Initiating secure DigiLocker handshake (✓ Checkmark).
  - Stage 2: Querying UIDAI verification server (✓ Checkmark).
  - Stage 3: Matching name & biometric records (Active pulse ring).
  - Reassurance Banner: *"Please stay on this screen. The verification server is responding normally."*
- **OTP Entry:** 6-digit monospace input box (`123456`).
- **Footer Buttons:** `← Back to Step 3` and `Confirm OTP & Choose Basket →`.

---

### Frame 6: Onboarding Screen 5 — Starter Basket Selection & ₹100 Order (`Onboarding / Step 5`)
- **Stepper:** Step 5 of 5 (100% Ready).
- **Pip Guidance Card:** *"KYC Approved! Choose where your ₹100 grows."*
- **3 Curated Starter Baskets (Radio Cards):**
  1. **Sprout India Top 50 Index Basket:** Direct equity index across India's top 50 enterprises (Avg. ~13.8% 5-Yr).
  2. **Instant Liquid Emergency Shield:** Low-risk debt funds, withdrawable in 24 hrs (Avg. ~6.8%).
  3. **Gold & Equity Growth Hybrid:** 50% 24K Digital Gold + 50% Top 50 Index (Avg. ~11.4%).
- **Order Breakdown Box:** First Investment: `₹100.00`, KYC Fee: `₹0.00`, Brokerage: `₹0.00`, Total: `₹100.00`.
- **Payment Method:** UPI (GPay/PhonePe/Paytm) or Net Banking.
- **Footer Buttons:** `← Back to Step 4` and `🌱 Plant My ₹100 Seed Now`.

---

### Frame 7: Completion — Celebratory Bloom & Portfolio Slip (`Onboarding / Complete`)
- **Celebratory Graphic:** Pip mascot blooming with a golden star and ambient green glow.
- **Headline:** *"Congratulations, Priya! Your first ₹100 seed has been planted."*
- **Official Allotment Certificate Card:**
  - Units Allotted: `2.4184 Units` (NAV `₹41.35`)
  - Depository Custody: `CDSL Demat Ready`
  - Registration: `AMFI ARN-289412`
- **Referral Card:** *"Gift a friend ₹50 seed bonus. When they invest ₹100, you both get ₹50."*
- **Action Buttons:** `Return to Home & Portfolio` and `↺ Test Again`.

---

## 4. Prototyping Connections & Interaction Guide

In Figma Prototype Mode (`Shift + E`), connect the screens with these exact settings:

1. **Homepage CTA `[Start with ₹100 Now]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Step 1`
   - **Animation:** `Smart Animate` -> `Ease out (300ms)`
2. **Step 1 `[Next: Document Checklist]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Step 2`
   - **Animation:** `Slide in (From Right, 250ms)`
3. **Step 2 `[I Have These Ready — Continue]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Step 3`
   - **Animation:** `Slide in (From Right, 250ms)`
4. **Step 3 `[Verify & Proceed to DigiLocker]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Step 4`
   - **Animation:** `Slide in (From Right, 250ms)`
5. **Step 4 `[Connect to DigiLocker]` Trigger:**
   - **Interaction:** `On click` -> `Change to` -> `Step 4 (Loading State)`
   - **After Delay (2500ms):** `Navigate to` -> `Step 4 (OTP Revealed)`
6. **Step 4 `[Confirm OTP & Choose Basket]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Step 5`
   - **Animation:** `Slide in (From Right, 250ms)`
7. **Step 5 `[Plant My ₹100 Seed Now]`:**
   - **Interaction:** `On click` -> `Navigate to` -> `Onboarding / Complete`
   - **Animation:** `Smart Animate` -> `Quick Spring (400ms)`

---

## 5. How to Submit Your Figma Link

1. Open your design file in Figma.
2. Click the blue **Share** button in the top right.
3. Under *Who has access*, select: **"Anyone with the link can view"**.
4. Click **Copy link**.
5. Paste the link into:
   - Your assignment submission Google Form.
   - The top of your repository's `README.md` (replace `<YOUR_FIGMA_PROTOTYPE_URL>`).
