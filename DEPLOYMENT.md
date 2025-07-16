# Fake News Detector - Deployment Guide

## Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect your GitHub** repository
3. **Deploy automatically** - Railway will detect it's a Python app
4. **Get your URL** - Railway provides a public URL like `https://your-app.railway.app`

**Steps:**
```bash
# Push your code to GitHub first
git add .
git commit -m "Ready for deployment"
git push origin main

# Then connect to Railway and deploy
```

### Option 2: Render (Free Tier Available)

1. **Sign up** at [render.com](https://render.com)
2. **Create a new Web Service**
3. **Connect your GitHub** repository
4. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. **Deploy** and get your URL

### Option 3: Heroku (Paid)

1. **Sign up** at [heroku.com](https://heroku.com)
2. **Install Heroku CLI**
3. **Deploy:**
```bash
heroku create your-app-name
git push heroku main
```

### Option 4: Vercel (Frontend) + Railway (Backend)

**For better performance, deploy frontend and backend separately:**

1. **Deploy backend** to Railway (as above)
2. **Deploy frontend** to Vercel:
   - Sign up at [vercel.com](https://vercel.com)
   - Connect your GitHub repo
   - Vercel will auto-deploy your HTML file

## Update Frontend for Deployment

After deploying your backend, update the API URL in `index.html`:

```javascript
// Change this line in the verifyArticle function:
fetch('https://your-backend-url.railway.app/predict', {
```

## Environment Variables (Optional)

For production, you might want to add environment variables:

```bash
# In Railway/Render dashboard
FLASK_ENV=production
```

## Testing Your Deployment

1. **Test the API endpoint:**
```bash
curl -X POST https://your-backend-url.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{"language":"en","textContent":"This is a test article"}'
```

2. **Test the frontend** by visiting your deployed URL

## Troubleshooting

### Common Issues:

1. **Model files too large:**
   - Consider using Git LFS for large model files
   - Or host models on cloud storage (AWS S3, Google Cloud Storage)

2. **CORS errors:**
   - The current setup includes CORS, but you might need to configure it for your domain

3. **Memory issues:**
   - Railway/Render have memory limits
   - Consider optimizing your models or using a paid tier

### Performance Tips:

1. **Enable caching** for model predictions
2. **Use CDN** for static assets
3. **Optimize model size** if needed

## Cost Comparison

- **Railway:** Free tier (limited), then $5/month
- **Render:** Free tier available, then $7/month
- **Heroku:** $7/month minimum
- **Vercel:** Free tier available

## Next Steps

1. **Add a domain** (optional)
2. **Set up monitoring** and logging
3. **Add rate limiting** to prevent abuse
4. **Implement caching** for better performance 