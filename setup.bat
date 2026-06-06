@echo off
REM Portfolio Setup Script for Windows

echo.
echo ======================================
echo   Shalem Sandeep - Portfolio Setup
echo ======================================
echo.

cd myportfolio

echo [1/5] Installing dependencies...
pip install -r ../requirements.txt

echo.
echo [2/5] Running migrations...
python manage.py migrate

echo.
echo [3/5] Collecting static files...
python manage.py collectstatic --noinput

echo.
echo [4/5] Populating portfolio with data...
python manage.py populate_portfolio

echo.
echo ======================================
echo.
echo ✨ Setup Complete! 
echo.
echo Next Steps:
echo   1. Create admin user: python manage.py createsuperuser
echo   2. Run server: python manage.py runserver
echo   3. Visit: http://localhost:8000
echo   4. Admin: http://localhost:8000/admin
echo.
echo ======================================
echo.

pause
