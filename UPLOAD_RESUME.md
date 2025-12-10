# How to Upload Your Resume to Hire_Harsh

## Step-by-Step Guide

### 1. Prepare Your Resume
- Your resume must be in **PDF format**
- Make sure it's readable and properly formatted

### 2. Replace the Demo Resume

**Option A: Direct File Replacement (Easiest)**
```bash
cd /Users/maya/Documents/Github/Hire_Harsh

# Copy your resume PDF to the data directory
cp /path/to/your/resume.pdf data/Your_Resume.pdf

# Update the config file (see Step 3)
```

**Option B: Use the Existing File Name**
```bash
# If you want to replace the existing resume file directly
cp /path/to/your/resume.pdf data/Harsh_Jaiswal_Resume.md
# Or if you have a markdown/text resume:
# cp /path/to/your/resume.md data/Harsh_Jaiswal_Resume.md

# No need to update cv_path in config if you use the existing filename
```

### 3. Update Configuration (Required)

Edit `config/base.yml` and update the candidate information:

```yaml
data:
  # CV file path (update to match your resume filename)
  cv_path: "data/Your_Resume.pdf"  # Update this to match your actual resume filename

# === Personalized Information ===
candidate:
  name: "Your Full Name"
  email: "your.email@example.com"
  linkedin: "https://linkedin.com/in/your-profile"
  github: "https://github.com/your-username"
```

### 4. Update About Me (Optional)

Edit `data/about_me.md` to add any additional information not in your resume:
- Personal interests
- Additional projects
- Certifications
- Volunteer work
- Anything else relevant

### 5. Rebuild the Vector Database

**IMPORTANT:** After replacing your resume, you need to rebuild the vector database so the AI can search through your new resume.

```bash
cd /Users/maya/Documents/Github/Hire_Harsh
source .venv/bin/activate

# Delete the old vector database
rm -rf data/vector_db/*

# The vector database will be automatically rebuilt the next time you:
# - Start the application, OR
# - Ask your first question in the chat
```

### 6. Start the Application

```bash
# Make sure you're in the Hire_Harsh directory
cd /Users/maya/Documents/Github/Hire_Harsh

# Activate virtual environment
source .venv/bin/activate

# Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or use the run script:
```bash
./run.sh
```

### 7. Test It Out

1. Open http://localhost:8000 in your browser
2. The vector database will be automatically created/updated on first use
3. Try asking questions about your resume, for example:
   - "What is my work experience?"
   - "What programming languages do I know?"
   - "Tell me about my education"

## Quick Commands Summary

```bash
# 1. Navigate to project
cd /Users/maya/Documents/Github/Hire_Harsh

# 2. Copy your resume (replace with your actual path and filename)
cp ~/Downloads/MyResume.pdf data/Your_Resume.pdf

# 3. Update config (edit config/base.yml with your info)
# Use any text editor or: nano config/base.yml

# 4. Delete old vector database
rm -rf data/vector_db/*

# 5. Start the app
source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

**Issue: Application still shows old resume**
- Make sure you deleted `data/vector_db/*`
- Restart the application
- The vector DB will rebuild automatically

**Issue: Resume not loading**
- Check that the PDF is in the `data/` directory
- Verify the filename matches what's in `config/base.yml` (cv_path setting)
- Check file permissions: `ls -la data/` (list all files to see your resume)

**Issue: Error reading PDF**
- Make sure your PDF is not password-protected
- Try converting it to PDF again if it's corrupted
- Check the application logs for specific error messages

## Notes

- The vector database stores embeddings of your resume for fast semantic search
- If you update your resume, always delete `data/vector_db/*` and let it rebuild
- The `about_me.md` file supplements your resume with additional context
- Your candidate info in `config/base.yml` is displayed in the chat interface

