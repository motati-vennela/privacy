# Privacy-Preserving Customer Data Platform

A working end-to-end prototype where downstream applications operate on protected customer data by default, and original sensitive data is accessed only through controlled, authorized and auditable workflows.

---

## How to Run (Your Friend's Guide)

### Prerequisites
- **Python 3.9+** must be installed
- Download from: https://www.python.org/downloads/
- **IMPORTANT:** Check "Add Python to PATH" during installation

### Step 1: Copy the entire `privacy-cdp` folder to your system

### Step 2: Open terminal/command prompt in that folder

### Step 3: Run the one-click script

**Windows:**
```
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Step 4: Browser opens automatically
- Go to: `http://localhost:8000`
- Login: `admin` / `admin123`

### That's it! The dashboard is ready to use.

---

## What You'll See

### Login Page
Enter `admin` / `admin123` and click Sign In.

### Dashboard Tab
- Click **"Seed Sample Data"** → loads 10 fake customers
- Click **"Discover PII"** → finds email, phone, name fields
- Click **"Run Batch Protection"** → creates protected copy

### Protected DB Tab
Shows scrambled data:
- `John Smith` → `NAME_394B72` (tokenized)
- `john@example.com` → `EMAIL_4B53D2` (tokenized)
- `9876543210` → `3077875916` (FPE - stays 10 digits)

### Reveal Tab
- Select a customer and field
- Click **Reveal** → shows the real value (if you have permission)
- All reveals are logged in the audit trail

### Marketing Tab
- Pick a token recipient
- Click **Send Email** → sends real email, marketing app never sees the address
- Simulate bounce → watch it map back to the token

### Audit Tab
Shows every sensitive operation: who did what, when, why, and the outcome.

---

## Demo Flow (Step by Step)

1. Login → `admin` / `admin123`
2. Click **Seed Sample Data** → 10 customers loaded
3. Click **Discover PII** → 3 fields detected
4. Click **Run Batch Protection** → all records protected
5. Go to **Protected DB** → verify no real emails/names
6. Go to **Marketing** → send email using token
7. Go to **Reveal** → reveal a real email (audited)
8. Go to **Audit** → see all operations logged

---

## Tech Stack

- **Backend:** Python + FastAPI
- **Database:** SQLite (no setup needed)
- **FPE:** Format-Preserving Encryption for phone numbers
- **Tokenization:** Stable token generation for email/name
- **Frontend:** Single-page HTML dashboard

---

## Project Structure

```
privacy-cdp/
├── run.bat              ← Windows one-click launcher
├── run.sh               ← Mac/Linux one-click launcher
├── build_dashboard.py   ← Builds the dashboard HTML
├── requirements.txt     ← Python dependencies
├── app/
│   ├── main.py          ← Server entry point
│   ├── core/
│   │   ├── config.py    ← Configuration
│   │   ├── database.py  ← Database setup
│   │   └── security.py  ← FPE, Tokenization, Encryption
│   ├── models/          ← Database models
│   ├── services/        ← Business logic
│   │   ├── pii_discovery.py
│   │   ├── batch_processor.py
│   │   ├── privacy_gateway.py
│   │   ├── email_service.py
│   │   └── audit_service.py
│   └── api/routes/main.py  ← API endpoints
└── app/static/dashboard.html  ← Dashboard UI (auto-generated)
```

---

## Troubleshooting

**"Python not found"**
- Install Python from python.org
- Check "Add Python to PATH" during install
- Restart terminal after install

**"Port 8000 already in use"**
- Close other programs using port 8000
- Or change port in the run script

**Dashboard buttons not working**
- Make sure you clicked "Seed Sample Data" first
- Then "Discover PII"
- Then "Run Batch Protection"
- Data must be seeded before other actions work
