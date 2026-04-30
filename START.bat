@echo off
echo Django Zavod Ish Haqi Tizimi
echo ============================
echo.
echo Python 3.10.11 + Django 4.2.7
echo.
echo Server ishga tushirilmoqda...
echo.

cd /d "%~dp0"
py -3.10 manage.py runserver

pause
