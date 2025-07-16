# 🚀 Deployment Checklist - Fake News Detector

## ✅ Pre-Deployment (Already Done!)
- [x] Git repository initialized
- [x] All files committed
- [x] Deployment files created (Procfile, runtime.txt, etc.)
- [x] App configured for production

## 🎯 Choose Your Deployment Method

### Option A: Railway (Easiest - 5 minutes)
**Steps:**
1. [ ] Go to https://railway.app
2. [ ] Sign up with GitHub account
3. [ ] Click "New Project"
4. [ ] Select "Deploy from GitHub repo"
5. [ ] Choose your repository (GraduationProject)
6. [ ] Wait for automatic deployment
7. [ ] Copy the generated URL (e.g., https://your-app.railway.app)

### Option B: Render (Free Tier - 10 minutes)
**Steps:**
1. [ ] Go to https://render.com
2. [ ] Sign up with GitHub account
3. [ ] Click "New" → "Web Service"
4. [ ] Connect your GitHub repository
5. [ ] Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
6. [ ] Click "Create Web Service"
7. [ ] Wait for deployment and copy URL

### Option C: Vercel (Frontend Only - 3 minutes)
**Steps:**
1. [ ] Go to https://vercel.com
2. [ ] Sign up with GitHub account
3. [ ] Click "New Project"
4. [ ] Import your GitHub repository
5. [ ] Deploy automatically
6. [ ] Copy the generated URL

## 🔧 After Deployment

### Update Frontend URL
After getting your backend URL, update `index.html`:

1. [ ] Open `index.html` in a text editor
2. [ ] Find this line: `fetch('http://localhost:5000/predict'`
3. [ ] Replace with: `fetch('https://your-backend-url.railway.app/predict'`
4. [ ] Save the file

### Test Your Deployment
1. [ ] Test the API endpoint:
   ```bash
   curl -X POST https://your-backend-url.railway.app/predict \
     -H "Content-Type: application/json" \
     -d '{"language":"en","textContent":"This is a test article"}'
   ```
2. [ ] Open your frontend URL in browser
3. [ ] Test with sample text

## 🎉 Success Indicators
- [ ] Backend responds to API calls
- [ ] Frontend loads without errors
- [ ] Fake news detection works
- [ ] Both English and Arabic work
- [ ] URL is accessible globally

## 🆘 Troubleshooting

### Common Issues:
- **"Model files not found"**: Make sure all .pkl files are in the repository
- **"Port already in use"**: Railway/Render will handle this automatically
- **"CORS errors"**: Already configured in app.py
- **"Memory issues"**: Consider upgrading to paid tier if models are large

### Need Help?
1. Check the logs in your deployment platform
2. Run `python deploy.py` for guided help
3. Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

## 📱 Share Your App
Once deployed, share your URL:
- **Backend API:** `https://your-app.railway.app`
- **Frontend:** `https://your-app.vercel.app` (if using Vercel)

---

**🎯 Goal: Get your app live in under 10 minutes!** 