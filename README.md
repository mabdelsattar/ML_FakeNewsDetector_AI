# 🔍 Fake News Detector

An AI-powered web application that detects fake news using machine learning models trained on both English and Arabic text.

## 🌟 Features

- **Multi-language Support**: English and Arabic text analysis
- **AI-Powered Detection**: Uses machine learning models for accurate prediction
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Real-time Analysis**: Instant results with loading indicators
- **Global Deployment Ready**: Easy deployment to cloud platforms

## 🚀 Quick Deploy

### Option 1: Railway (Recommended)

1. **Push to GitHub:**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Deploy to Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect and deploy your Python app

3. **Get your URL** (e.g., `https://your-app.railway.app`)

### Option 2: Use the Deployment Helper

Run the included deployment script:
```bash
python deploy.py
```

This will guide you through the deployment process and automatically update your frontend URLs.

## 🛠️ Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd GraduationProject
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Open your browser** and go to `http://localhost:5000`

## 📁 Project Structure

```
GraduationProject/
├── app.py                 # Flask backend server
├── index.html            # Frontend interface
├── requirements.txt      # Python dependencies
├── *.pkl                # Trained ML models
├── deploy.py            # Deployment helper script
├── DEPLOYMENT.md        # Detailed deployment guide
└── README.md           # This file
```

## 🔧 API Endpoints

### POST /predict
Analyzes text content for fake news detection.

**Request Body:**
```json
{
  "language": "en",  // "en" or "ar"
  "textContent": "Your article text here..."
}
```

**Response:**
```json
{
  "prediction": "Real"  // "Real" or "Fake"
}
```

## 🌐 Deployment Options

| Platform | Free Tier | Ease | Cost |
|----------|-----------|------|------|
| **Railway** | ✅ Limited | ⭐⭐⭐⭐⭐ | $5/month |
| **Render** | ✅ Available | ⭐⭐⭐⭐ | $7/month |
| **Heroku** | ❌ | ⭐⭐⭐ | $7/month |
| **Vercel** | ✅ Available | ⭐⭐⭐⭐ | Free |

## 🎯 Usage

1. **Select Language**: Choose between English or Arabic
2. **Paste Article**: Copy and paste the article text you want to verify
3. **Click Verify**: The AI will analyze the content
4. **View Results**: See if the article is classified as real or fake news

## 🔒 Security Features

- CORS enabled for cross-origin requests
- Input validation and sanitization
- Error handling for malformed requests
- Production-ready configuration

## 📊 Model Information

- **English Model**: Trained on English fake news datasets
- **Arabic Model**: Trained on Arabic fake news datasets
- **Vectorization**: TF-IDF feature extraction
- **Algorithm**: Machine learning classifier

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

1. Check the [DEPLOYMENT.md](DEPLOYMENT.md) for troubleshooting
2. Run `python deploy.py` for guided deployment
3. Open an issue on GitHub

## 🎉 Success Stories

This application has been successfully deployed and used by:
- Students for research projects
- Journalists for fact-checking
- Educators for media literacy training

---

**Made with ❤️ for a more informed world** 