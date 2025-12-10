#!/usr/bin/env python3
"""
Quick verification script to check if Hire_Harsh is ready to run.
"""

import sys
import os
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists."""
    if Path(filepath).exists():
        print(f"✅ {description}: Found")
        return True
    else:
        print(f"❌ {description}: Missing ({filepath})")
        return False

def check_dir_exists(dirpath, description):
    """Check if a directory exists."""
    if Path(dirpath).is_dir():
        print(f"✅ {description}: Found")
        return True
    else:
        print(f"⚠️  {description}: Missing ({dirpath}) - will be created automatically")
        return False

def check_python_version():
    """Check Python version."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro} (requires 3.10+)")
        return False

def check_env_file():
    """Check if .env file exists and has required keys."""
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file: Missing - create it from the template")
        return False
    
    with open(env_file) as f:
        content = f.read()
        if "your_openai_api_key_here" in content or "OPENAI_API_KEY" not in content:
            print("⚠️  .env file: Exists but OPENAI_API_KEY needs to be set")
            return False
        else:
            print("✅ .env file: Exists and configured")
            return True

def check_imports():
    """Check if required packages can be imported."""
    required_packages = [
        "fastapi",
        "uvicorn",
        "langchain",
        "chromadb",
        "pypdf",
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ Package: {package}")
        except ImportError:
            print(f"❌ Package: {package} - not installed")
            missing.append(package)
    
    return len(missing) == 0

def main():
    print("🔍 Hire_Harsh Setup Verification")
    print("=" * 50)
    print()
    
    all_ok = True
    
    # Check Python version
    print("Python Environment:")
    if not check_python_version():
        all_ok = False
    print()
    
    # Check required files
    print("Required Files:")
    check_file_exists("main.py", "Main application file")
    check_file_exists("requirements.txt", "Requirements file")
    check_file_exists("app/config.py", "Configuration module")
    check_file_exists("data/Harsh_Jaiswal_Resume.md", "CV file")
    print()
    
    # Check directories
    print("Directories:")
    check_dir_exists("logs", "Logs directory")
    check_dir_exists("data/vector_db", "Vector database directory")
    print()
    
    # Check .env
    print("Configuration:")
    check_env_file()
    print()
    
    # Check packages (optional - might not be in venv)
    print("Python Packages (checking if installed):")
    try:
        if not check_imports():
            print("⚠️  Some packages missing - run: pip install -r requirements.txt")
    except Exception as e:
        print(f"⚠️  Could not check packages: {e}")
    print()
    
    print("=" * 50)
    if all_ok:
        print("✅ Setup looks good! You can run the application.")
        print("\nTo start the app:")
        print("  uvicorn main:app --reload --host 0.0.0.0 --port 8000")
    else:
        print("⚠️  Some issues found. Please address them before running.")
    print()

if __name__ == "__main__":
    main()

