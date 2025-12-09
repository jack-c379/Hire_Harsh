# Local Deployment Guide for Hire_Harsh

This guide will help you set up and test Hire_Harsh locally.

## Prerequisites

1. **Python 3.12+** (or Python 3.10+)
2. **pip** (Python package manager)
3. **OpenAI API Key** (required for the LLM)
4. (Optional) Docker & Docker Compose if using containerized deployment

## Quick Start (Non-Docker)

### Step 1: Create Environment File

Create a `.env` file in the project root:

```bash
cd Hire_Harsh
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

# Optional: Ollama endpoint (if using Ollama)
OLLAMA_ENDPOINT=http://localhost:11434

# Environment
ENVIRONMENT=development

# Optional: Invite codes ({} for public access)
INVITE_CODES={}
EOF
```

**Important**: Replace `your_openai_api_key_here` with your actual OpenAI API key!

### Step 2: Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Step 3: Optional - Install Guardrails (Skip if not needed)

Guardrails is optional. Only install if you have a Guardrails AI token:

```bash
guardrails configure  # Interactive - you'll need a token
guardrails hub install hub://guardrails/toxic_language
guardrails hub install hub://guardrails/reading_time
guardrails hub install hub://guardrails/profanity_free
```

**You can skip this step** - the app works fine without Guardrails.

### Step 4: Verify Directories

Ensure these directories exist:

```bash
mkdir -p logs data/vector_db
```

### Step 5: Customize Your Resume (Optional)

1. Replace `data/CV_Demo.pdf` with your actual resume PDF
2. Edit `data/about_me.md` with additional information
3. Replace `static/default-avatar.png` with your profile picture
4. Update candidate info in `config/base.yml`:
   ```yaml
   candidate:
     name: "Your Name"
     email: "your.email@example.com"
     linkedin: "https://linkedin.com/in/your-profile"
     github: "https://github.com/your-username"
   ```

### Step 6: Run the Application

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reload during development.

### Step 7: Access the Application

Open your browser and navigate to:
- **Main Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (development only)
- **Health Check**: http://localhost:8000/health

## Docker Deployment

### Using Docker Compose

1. **Set up environment variables**:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   export LLM_PROVIDER="openai"
   export ENVIRONMENT="development"
   export GUARDRAILS_TOKEN=""  # Optional
   ```

2. **Build and run**:
   ```bash
   docker compose up --build
   ```

3. **Access**: http://localhost:8000

### Using Docker directly

```bash
# Build the image
docker build -t hire_harsh-app .

# Run the container
docker run -p 8000:8000 \
  -e OPENAI_API_KEY="your_openai_api_key_here" \
  -e ENVIRONMENT="development" \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  hire_harsh-app
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `LLM_PROVIDER` | No | `openai` or `ollama` (default: `openai`) |
| `OLLAMA_ENDPOINT` | No | Ollama endpoint (default: `http://localhost:11434`) |
| `ENVIRONMENT` | No | `development` or `production` (default: `development`) |
| `LANGSMITH_API_KEY` | No | For advanced analytics |
| `GUARDRAILS_TOKEN` | No | For content safety features |
| `INVITE_CODES` | No | JSON object with invite codes (use `{}` for public) |

### Access Control

**Public Access** (default):
```bash
INVITE_CODES={}
```

**Restricted Access** with invite codes:
```bash
INVITE_CODES={"RECRUITER1": {"company": "TechCorp", "recruiter": "Jane Smith", "active": true}}
```

## Testing

### Test the Health Endpoint

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "healthy", "service": "Hire_Harsh"}
```

### Test Chat API

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is your background?"}'
```

## Troubleshooting

### Issue: Missing OpenAI API Key

**Error**: `OPENAI_API_KEY not found`

**Solution**: Make sure your `.env` file exists and contains a valid `OPENAI_API_KEY`.

### Issue: Module not found

**Error**: `ModuleNotFoundError`

**Solution**: 
```bash
pip install -r requirements.txt
```

### Issue: Vector database errors

**Error**: Issues with ChromaDB

**Solution**: 
```bash
rm -rf data/vector_db/*  # Clear vector database
# Restart the application to rebuild
```

### Issue: Port already in use

**Error**: `Address already in use`

**Solution**: Use a different port:
```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

### Issue: Permission errors (Docker)

**Solution**: Check file permissions:
```bash
sudo chown -R $USER:$USER logs data
```

## Development Mode

For development with hot-reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

This will automatically reload when you make code changes.

## Next Steps

1. **Customize your resume**: Replace the demo files with your own
2. **Test the chat**: Try asking questions about the resume
3. **Test job matching**: Upload a job description and see the analysis
4. **Deploy**: When ready, deploy to your preferred cloud platform

## Support

- Check the main [README.md](README.md) for more information
- Review the API documentation at `/docs` when running in development mode

