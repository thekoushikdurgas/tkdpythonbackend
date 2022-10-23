@ECHO OFF
set /p id=Enter Port: 
echo %id%
IF %id%==0 (
    start cmd.exe /C "cd %CD% && python manage.py makemigrations && python manage.py migrate && python manage.py runserver"
    start "C://Program Files//Google//Chrome//Application//chrome.exe" http://127.0.0.1:8000
) ELSE (
    start cmd.exe /C "cd %CD% && python manage.py makemigrations && python manage.py migrate && python manage.py runserver %id%"
    start "C://Program Files//Google//Chrome//Application//chrome.exe" http://127.0.0.1:%id%
)