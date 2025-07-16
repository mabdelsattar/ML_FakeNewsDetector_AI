#!/usr/bin/env python3
"""
Deployment Helper Script for Fake News Detector
This script helps you deploy your application and update the frontend URL.
"""

import os
import sys
import subprocess
import re

def check_git_status():
    """Check if git is initialized and files are committed"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️  You have uncommitted changes. Please commit them first:")
            print(result.stdout)
            return False
        return True
    except FileNotFoundError:
        print("❌ Git is not installed. Please install Git first.")
        return False

def update_frontend_url(backend_url):
    """Update the frontend to use the deployed backend URL"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the fetch URL
        old_pattern = r"fetch\('http://localhost:5000/predict'"
        new_pattern = f"fetch('{backend_url}/predict'"
        
        if old_pattern in content:
            content = re.sub(old_pattern, new_pattern, content)
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated frontend to use backend URL: {backend_url}")
            return True
        else:
            print("⚠️  Could not find localhost URL in index.html")
            return False
            
    except Exception as e:
        print(f"❌ Error updating frontend: {e}")
        return False

def main():
    print("🚀 Fake News Detector Deployment Helper")
    print("=" * 50)
    
    # Check git status
    if not check_git_status():
        return
    
    print("\n📋 Deployment Options:")
    print("1. Railway (Recommended)")
    print("2. Render")
    print("3. Heroku")
    print("4. Update frontend URL only")
    
    choice = input("\nSelect an option (1-4): ").strip()
    
    if choice == "1":
        print("\n🚂 Deploying to Railway...")
        print("1. Go to https://railway.app")
        print("2. Sign up/Login with GitHub")
        print("3. Click 'New Project' → 'Deploy from GitHub repo'")
        print("4. Select your repository")
        print("5. Railway will automatically detect it's a Python app")
        print("6. Wait for deployment to complete")
        print("7. Copy the generated URL (e.g., https://your-app.railway.app)")
        
        backend_url = input("\nEnter your Railway URL: ").strip()
        if backend_url:
            update_frontend_url(backend_url)
            
    elif choice == "2":
        print("\n🎨 Deploying to Render...")
        print("1. Go to https://render.com")
        print("2. Sign up/Login with GitHub")
        print("3. Click 'New' → 'Web Service'")
        print("4. Connect your GitHub repository")
        print("5. Configure:")
        print("   - Build Command: pip install -r requirements.txt")
        print("   - Start Command: python app.py")
        print("6. Click 'Create Web Service'")
        print("7. Copy the generated URL")
        
        backend_url = input("\nEnter your Render URL: ").strip()
        if backend_url:
            update_frontend_url(backend_url)
            
    elif choice == "3":
        print("\n⚡ Deploying to Heroku...")
        print("1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
        print("2. Run these commands:")
        print("   heroku login")
        print("   heroku create your-app-name")
        print("   git push heroku main")
        print("3. Copy the generated URL")
        
        backend_url = input("\nEnter your Heroku URL: ").strip()
        if backend_url:
            update_frontend_url(backend_url)
            
    elif choice == "4":
        backend_url = input("Enter your backend URL: ").strip()
        if backend_url:
            update_frontend_url(backend_url)
    
    print("\n✅ Deployment setup complete!")
    print("\n📝 Next steps:")
    print("1. Test your backend API endpoint")
    print("2. Deploy your frontend (index.html) to a static hosting service")
    print("3. Share your application URL with others!")

if __name__ == "__main__":
    main() 