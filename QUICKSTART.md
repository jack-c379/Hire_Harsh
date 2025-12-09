# Quick Start Guide - Hire_Harsh Local Testing

## 🚀 Fastest Way to Get Started

### Option 1: Automated Setup (Recommended)

```bash
cd Hire_Harsh
./setup_local.sh
```

This script will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install dependencies
- ✅ Create required directories
- ✅ Create .env template

**After running the script**, edit `.env` and add your OpenAI API key:
```bash
nano .env  # or use your favorite editor
```

Then run:
```bash
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Manual Setup

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file**:
   ```bash
   cat > .env << 'EOF'
   OPENAI_API_KEY="your_key_here"
   ENVIRONMENT=development
   LLM_PROVIDER=openai
   INVITE_CODES={}
   EOF
   ```
   **Replace `your_key_here` with your actual OpenAI API key!**

4. **Create directories**:
   ```bash
   mkdir -p logs data/vector_db
   ```

5. **Run the app**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## ✅ Verify Setup

Run the verification script:
```bash
python3 verify_setup.py
```

## 🌐 Access the Application

Once running, open your browser:
- **Main App**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📚 More Information

- See [LOCAL_DEPLOYMENT.md](LOCAL_DEPLOYMENT.md) for detailed deployment guide
- See [README.md](README.md) for project overview and features

## 🐛 Troubleshooting

**Missing OpenAI API Key?**
- Make sure `.env` file exists in the project root
- Add `OPENAI_API_KEY="your_actual_key"` to the file

**Packages not installed?**
- Make sure virtual environment is activated: `source venv/bin/activate`
- Run: `pip install -r requirements.txt`

**Port already in use?**
- Change the port: `uvicorn main:app --port 8001`

