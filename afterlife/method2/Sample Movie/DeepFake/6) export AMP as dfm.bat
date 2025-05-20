@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" exportdfm ^
    --model-dir "%WORKSPACE%\model" ^
    --model AMP

pause