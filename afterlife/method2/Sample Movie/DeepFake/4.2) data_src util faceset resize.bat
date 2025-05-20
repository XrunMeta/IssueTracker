@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" facesettool resize ^
    --input-dir "%WORKSPACE%\data_src\aligned"

pause