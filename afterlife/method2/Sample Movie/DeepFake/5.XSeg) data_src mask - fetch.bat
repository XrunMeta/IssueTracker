@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" xseg fetch ^
    --input-dir "%WORKSPACE%\data_src\aligned"

pause