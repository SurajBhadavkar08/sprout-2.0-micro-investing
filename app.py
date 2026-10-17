"""
Sprout 2.0 - Micro-Investing Web Application
=============================================
A modern, accessible, and high-performance micro-investing platform
tailored for first-time investors in India (starting from ₹100).

Resolves key stakeholder requirements:
- CEO: Apple-like minimal, premium aesthetic with subtle, elegant mascot guidance.
- Head of Marketing: High engagement mascot ('Pip'), live market ticker, referral cards.
- Compliance Officer: Prominent >=12px risk disclaimers, no banned terms ('guaranteed', 'risk-free').
- Lead Developer: Zero frontend framework overhead, ultra-fast load (<1.5MB total weight).
- Customer Support: Solves KYC readiness drop-offs and DigiLocker wait-state anxieties.
"""

import os
import re
import sqlite3
import uuid
from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'sprout-seed-super-secure-key-2026')

DB_PATH = os.path.join(app.instance_path, 'sprout.db')

# Ensure instance directory exists
os.makedirs(app.instance_path, exist_ok=True)


def get_db():
    """Returns a SQLite database connection with row factory configured."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database schema if tables do not exist."""
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                name TEXT,
                mobile TEXT,
                investment_goal TEXT,
                monthly_amount INTEGER DEFAULT 100,
                checklist_agreed INTEGER DEFAULT 0,
                pan_number TEXT,
                dob TEXT,
                aadhaar_last_four TEXT,
                digilocker_verified INTEGER DEFAULT 0,
                basket_choice TEXT,
                investment_amount INTEGER DEFAULT 100,
                payment_method TEXT,
                status TEXT DEFAULT 'in_progress',
                created_at TEXT,
                updated_at TEXT
            )
        ''')
        conn.commit()


# Initialize database at startup
init_db()


def get_session_id():
    """Retrieves or creates a unique session UUID for tracking user onboarding progress."""
    if 'user_session_id' not in session:
        session['user_session_id'] = str(uuid.uuid4())
    return session['user_session_id']


def get_user_record(session_id):
    """Retrieves existing user data from database or creates a default record."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE session_id = ?', (session_id,))
        row = cursor.fetchone()
        if not row:
            now = datetime.utcnow().isoformat()
            cursor.execute('''
                INSERT INTO users (session_id, monthly_amount, investment_amount, status, created_at, updated_at)
                VALUES (?, 100, 100, 'in_progress', ?, ?)
            ''', (session_id, now, now))
            conn.commit()
            cursor.execute('SELECT * FROM users WHERE session_id = ?', (session_id,))
            row = cursor.fetchone()
        return dict(row)


def update_user_record(session_id, **kwargs):
    """Updates user attributes in database."""
    if not kwargs:
        return
    kwargs['updated_at'] = datetime.utcnow().isoformat()
    fields = [f"{k} = ?" for k in kwargs.keys()]
    values = list(kwargs.values()) + [session_id]
    query = f"UPDATE users SET {', '.join(fields)} WHERE session_id = ?"
    with get_db() as conn:
        conn.execute(query, values)
        conn.commit()


# --- VALIDATION HELPERS ---

def validate_pan(pan):
    """Validates Indian Permanent Account Number (PAN) format: 5 letters, 4 digits, 1 letter."""
    if not pan:
        return False, "PAN number is required."
    clean_pan = pan.strip().upper()
    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', clean_pan):
        return False, "Please enter a valid 10-character PAN (e.g., ABCDE1234F)."
    return True, clean_pan


def validate_dob(dob_str):
    """Validates Date of Birth format (YYYY-MM-DD or DD/MM/YYYY) and ensures user is >= 18."""
    if not dob_str:
        return False, "Date of birth is required for SEBI-compliant KYC."
    dob_str = dob_str.strip()
    parsed_date = None
    for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y'):
        try:
            parsed_date = datetime.strptime(dob_str, fmt).date()
            break
        except ValueError:
            continue

    if not parsed_date:
        return False, "Invalid date format. Please use DD/MM/YYYY."

    today = date.today()
    age = today.year - parsed_date.year - ((today.month, today.day) < (parsed_date.month, parsed_date.day))
    if age < 18:
        return False, "You must be at least 18 years old to invest in mutual funds and securities."
    if age > 110:
        return False, "Please check the entered birth year."

    return True, parsed_date.isoformat()


def validate_mobile(mobile):
    """Validates 10-digit Indian mobile number."""
    if not mobile:
        return False, "Mobile number is required."
    clean_mobile = re.sub(r'[\s\-\+]', '', mobile)
    if clean_mobile.startswith('91') and len(clean_mobile) == 12:
        clean_mobile = clean_mobile[2:]
    if not re.match(r'^[6-9]\d{9}$', clean_mobile):
        return False, "Please enter a valid 10-digit Indian mobile number."
    return True, clean_mobile


# --- CONTEXT PROCESSOR ---

@app.context_processor
def inject_global_data():
    """Injects live ticker and compliance disclaimer data into all templates."""
    return {
        'market_ticker': [
            {'symbol': 'NIFTY 50', 'value': '24,852.15', 'change': '+0.42%', 'positive': True},
            {'symbol': 'SENSEX', 'value': '81,224.75', 'change': '+0.38%', 'positive': True},
            {'symbol': 'GOLD (10g)', 'value': '₹76,420', 'change': '+0.15%', 'positive': True},
            {'symbol': 'NIFTY NEXT 50', 'value': '71,190.40', 'change': '-0.12%', 'positive': False},
        ],
        'compliance_disclaimer': (
            "Investments in securities market are subject to market risks. "
            "Read all the scheme related documents carefully before investing. "
            "Sprout Financial Technologies Pvt. Ltd. is an AMFI-registered mutual fund distributor (ARN-289412). "
            "Past performance does not indicate future returns."
        )
    }


# --- ROUTES ---

@app.route('/')
def index():
    """Homepage showcasing Sprout 2.0 value proposition, mascot guide, and ₹100 compounding calculator."""
    session_id = get_session_id()
    user = get_user_record(session_id)
    return render_template('index.html', user=user)


@app.route('/onboarding')
def onboarding_root():
    """Redirects user to the active onboarding step."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    # Smart resume based on user progress
    if user.get('status') == 'completed':
        return redirect(url_for('onboarding_complete'))
    if user.get('digilocker_verified'):
        return redirect(url_for('onboarding_step5'))
    if user.get('pan_number'):
        return redirect(url_for('onboarding_step4'))
    if user.get('checklist_agreed'):
        return redirect(url_for('onboarding_step3'))
    if user.get('investment_goal'):
        return redirect(url_for('onboarding_step2'))

    return redirect(url_for('onboarding_step1'))


# STEP 1: Goal Setting & Starting Amount
@app.route('/onboarding/step1', methods=['GET', 'POST'])
def onboarding_step1():
    """Screen 1: Welcome & Goal Discovery - Starting small with ₹100."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        goal = request.form.get('investment_goal', '').strip()
        monthly_amount = request.form.get('monthly_amount', '100').strip()

        errors = {}
        if not goal:
            errors['investment_goal'] = "Please select what you would like to achieve."

        try:
            amt = int(monthly_amount)
            if amt < 100:
                errors['monthly_amount'] = "Minimum starting amount is ₹100."
        except ValueError:
            errors['monthly_amount'] = "Please choose a valid investment amount."

        if errors:
            return render_template('onboarding/step1.html', user=user, errors=errors, form_data=request.form)

        update_user_record(
            session_id,
            name=name if name else user.get('name', ''),
            investment_goal=goal,
            monthly_amount=int(monthly_amount)
        )
        return redirect(url_for('onboarding_step2'))

    return render_template('onboarding/step1.html', user=user, current_step=1)


# STEP 2: Document Readiness Checklist (Solves Customer Support Pain Point 1)
@app.route('/onboarding/step2', methods=['GET', 'POST'])
def onboarding_step2():
    """Screen 2: Pre-KYC Checklist - 'Keep PAN & Aadhaar ready'."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    if request.method == 'POST':
        checklist_pan = request.form.get('has_pan') == 'on'
        checklist_aadhaar = request.form.get('has_aadhaar') == 'on'
        checklist_upi = request.form.get('has_upi') == 'on'

        if not (checklist_pan and checklist_aadhaar):
            flash("Please confirm that you have both your PAN card and Aadhaar-linked mobile ready.", "error")
            return render_template('onboarding/step2.html', user=user, current_step=2)

        update_user_record(session_id, checklist_agreed=1)
        return redirect(url_for('onboarding_step3'))

    return render_template('onboarding/step2.html', user=user, current_step=2)


# STEP 3: Identity & PAN Verification
@app.route('/onboarding/step3', methods=['GET', 'POST'])
def onboarding_step3():
    """Screen 3: Identity & PAN Verification with live validation."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    if request.method == 'POST':
        full_name = request.form.get('name', '').strip()
        pan = request.form.get('pan_number', '').strip().upper()
        dob = request.form.get('dob', '').strip()
        mobile = request.form.get('mobile', '').strip()

        errors = {}
        if not full_name:
            errors['name'] = "Full legal name as per PAN card is required."

        is_valid_pan, pan_result = validate_pan(pan)
        if not is_valid_pan:
            errors['pan_number'] = pan_result

        is_valid_dob, dob_result = validate_dob(dob)
        if not is_valid_dob:
            errors['dob'] = dob_result

        is_valid_mobile, mobile_result = validate_mobile(mobile)
        if not is_valid_mobile:
            errors['mobile'] = mobile_result

        if errors:
            form_data = {
                'name': full_name,
                'pan_number': pan,
                'dob': dob,
                'mobile': mobile
            }
            return render_template('onboarding/step3.html', user=user, errors=errors, form_data=form_data, current_step=3)

        update_user_record(
            session_id,
            name=full_name,
            pan_number=pan_result,
            dob=dob_result,
            mobile=mobile_result
        )
        return redirect(url_for('onboarding_step4'))

    return render_template('onboarding/step3.html', user=user, current_step=3)


# STEP 4: DigiLocker Aadhaar Verification & Live Progress (Solves Customer Support Pain Point 2)
@app.route('/onboarding/step4', methods=['GET', 'POST'])
def onboarding_step4():
    """Screen 4: Paperless DigiLocker Aadhaar with live progress feedback."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    if request.method == 'POST':
        aadhaar_last_four = request.form.get('aadhaar_last_four', '').strip()
        otp = request.form.get('otp', '').strip()

        errors = {}
        if not re.match(r'^\d{4}$', aadhaar_last_four):
            errors['aadhaar_last_four'] = "Please provide the last 4 digits of your Aadhaar."

        if not re.match(r'^\d{6}$', otp):
            errors['otp'] = "Please enter the 6-digit OTP sent to your Aadhaar-linked mobile (Use 123456 for demo)."

        if errors:
            return render_template('onboarding/step4.html', user=user, errors=errors, form_data=request.form, current_step=4)

        update_user_record(
            session_id,
            aadhaar_last_four=aadhaar_last_four,
            digilocker_verified=1
        )
        return redirect(url_for('onboarding_step5'))

    return render_template('onboarding/step4.html', user=user, current_step=4)


# STEP 5: ₹100 Investment Allocation & Confirmation
@app.route('/onboarding/step5', methods=['GET', 'POST'])
def onboarding_step5():
    """Screen 5: First ₹100 Investment Selection & Setup."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    if request.method == 'POST':
        basket_choice = request.form.get('basket_choice', 'nifty50').strip()
        payment_method = request.form.get('payment_method', 'upi').strip()

        valid_baskets = ['nifty50', 'emergency_fund', 'gold_hybrid']
        if basket_choice not in valid_baskets:
            basket_choice = 'nifty50'

        update_user_record(
            session_id,
            basket_choice=basket_choice,
            payment_method=payment_method,
            investment_amount=100,
            status='completed'
        )
        return redirect(url_for('onboarding_complete'))

    return render_template('onboarding/step5.html', user=user, current_step=5)


# COMPLETION: Celebration & Active Investor Dashboard Preview
@app.route('/onboarding/complete')
def onboarding_complete():
    """Celebratory screen with mascot bloom animation, investment certificate, and portfolio preview."""
    session_id = get_session_id()
    user = get_user_record(session_id)

    basket_names = {
        'nifty50': 'Sprout India Top 50 Index Basket',
        'emergency_fund': 'Instant Liquid Emergency Shield',
        'gold_hybrid': 'Gold & Bluechip Growth Hybrid'
    }

    basket_title = basket_names.get(user.get('basket_choice'), 'Sprout India Top 50 Index Basket')
    return render_template('onboarding/complete.html', user=user, basket_title=basket_title)


# --- API ENDPOINTS FOR CLIENT-SIDE AUTOSAVE & DEMO INTERACTIONS ---

@app.route('/api/autosave', methods=['POST'])
def api_autosave():
    """Autosaves draft field values asynchronously so user never loses entered progress."""
    session_id = get_session_id()
    data = request.get_json(silent=True) or {}
    allowed_keys = ['name', 'mobile', 'investment_goal', 'monthly_amount', 'pan_number', 'dob', 'basket_choice']
    update_data = {k: v for k, v in data.items() if k in allowed_keys and v is not None}
    if update_data:
        update_user_record(session_id, **update_data)
    return jsonify({'success': True, 'saved': list(update_data.keys())})


@app.route('/api/reset', methods=['POST'])
def api_reset():
    """Resets user onboarding state for seamless evaluation and testing."""
    session_id = get_session_id()
    with get_db() as conn:
        conn.execute('DELETE FROM users WHERE session_id = ?', (session_id,))
        conn.commit()
    session.clear()
    return jsonify({'success': True, 'message': 'Onboarding data reset successfully.'})


if __name__ == '__main__':
    # Local development server with auto-reload
    port = int(os.environ.get('PORT', 5000))
    print(f"Sprout 2.0 running locally at http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)
