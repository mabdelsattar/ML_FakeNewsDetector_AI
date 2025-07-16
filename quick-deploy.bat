@echo off
echo.
echo ========================================
echo    FAKE NEWS DETECTOR - QUICK DEPLOY
echo ========================================
echo.
echo Your project is ready for deployment!
echo.
echo Choose your deployment platform:
echo.
echo 1. Railway (Recommended - Easiest)
echo 2. Render (Free tier available)
echo 3. Vercel (Frontend hosting)
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Opening Railway...
    echo.
    echo STEPS TO FOLLOW:
    echo 1. Sign up with GitHub
    echo 2. Click "New Project"
    echo 3. Select "Deploy from GitHub repo"
    echo 4. Choose your repository
    echo 5. Wait for deployment
    echo 6. Copy the URL provided
    echo.
    start https://railway.app
    pause
) else if "%choice%"=="2" (
    echo.
    echo Opening Render...
    echo.
    echo STEPS TO FOLLOW:
    echo 1. Sign up with GitHub
    echo 2. Click "New" then "Web Service"
    echo 3. Connect your GitHub repository
    echo 4. Set Build Command: pip install -r requirements.txt
    echo 5. Set Start Command: python app.py
    echo 6. Click "Create Web Service"
    echo.
    start https://render.com
    pause
) else if "%choice%"=="3" (
    echo.
    echo Opening Vercel...
    echo.
    echo STEPS TO FOLLOW:
    echo 1. Sign up with GitHub
    echo 2. Click "New Project"
    echo 3. Import your GitHub repository
    echo 4. Deploy automatically
    echo.
    start https://vercel.com
    pause
) else if "%choice%"=="4" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice. Please run the script again.
    pause
) 