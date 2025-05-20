@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" xseg editor ^
    --input-dir "%WORKSPACE%\data_dst\aligned"

if %errorlevel% NEQ 0 (
  pause
)