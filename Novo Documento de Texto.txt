@echo off
:loop
python "C:\Users\55519\Desktop\PROJETOS [DEV]\sistemas python [DESKTOP]\Disparador_de_emails\main.py"
timeout /t 1000 > nul
goto loop
