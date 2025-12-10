#!/bin/bash
# Local Setup Script for Hire_Harsh
# This script helps set up the Hire_Harsh application for local testing

set -e  # Exit on any error

echo "🚀 Hire_Harsh Local Setup Script"
echo "============================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.10"
if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Error: Python 3.10+ is required. Found: $python_version"
    exit 1
fi
echo "✅ Python version OK: $python_version"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install requirements
echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Create necessary directories
echo "📁 Creating required directories..."
mkdir -p logs
mkdir -p data/vector_db
echo "✅ Directories created"
echo ""

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo ""
    echo "Creating .env file template..."
    cat > .env << 'EOF'
# Required: OpenAI API Key
OPENAI_API_KEY="your_openai_api_key_here"

# Optional: LangSmith for advanced analytics
LANGSMITH_API_KEY=""
LANGSMITH_TRACING=false

# Optional: Guardrails AI for content safety
GUARDRAILS_TOKEN=""

# Optional: LLM Provider (default: openai)
LLM_PROVIDER=openai

# Environment
ENVIRONMENT=development

# Optional: Invite codes ({} for public access)
INVITE_CODES={}
EOF
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your OPENAI_API_KEY!"
    echo "   You can do this by running: nano .env"
else
    echo "✅ .env file already exists"
fi
echo ""

# Check if OpenAI API key is set
if grep -q "your_openai_api_key_here" .env 2>/dev/null || ! grep -q "OPENAI_API_KEY=" .env 2>/dev/null; then
    echo "⚠️  WARNING: Please update OPENAI_API_KEY in .env file before running the application!"
fi
echo ""

# Summary
echo "============================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OPENAI_API_KEY:"
echo "   nano .env"
echo ""
echo "2. (Optional) Install Guardrails (requires token):"
echo "   guardrails configure"
echo "   guardrails hub install hub://guardrails/toxic_language"
echo ""
echo "3. Activate virtual environment and run:"
echo "   source venv/bin/activate"
echo "   uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "4. Open your browser to: http://localhost:8000"
echo ""
echo "For more details, see LOCAL_DEPLOYMENT.md"
echo ""

