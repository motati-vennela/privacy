#!/bin/bash
echo "============================================"
echo " Privacy-Preserving CDP - One-Click Setup"
echo "============================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 not found!"
    echo "Install: sudo apt install python3 python3-pip (Linux)"
    echo "Install: brew install python (Mac)"
    exit 1
fi
echo "[OK] Python found"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install fastapi uvicorn sqlalchemy python-dotenv python-multipart pydantic httpx
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "[OK] Dependencies installed"

# Clean old data
echo ""
echo "Cleaning old data..."
rm -f source.db protected.db vault.db
echo "[OK] Clean"

# Build dashboard
echo ""
echo "Building dashboard..."
python3 build_dashboard.py
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to build dashboard"
    exit 1
fi
echo "[OK] Dashboard built"

# Start server
echo ""
echo "============================================"
echo " Starting Privacy-Preserving CDP..."
echo " Open browser: http://localhost:8000"
echo " Login: admin / admin123"
echo "============================================"
echo ""
xdg-open http://localhost:8000 2>/dev/null || open http://localhost:8000 2>/dev/null
uvicorn app.main:app --host 127.0.0.1 --port 8000
