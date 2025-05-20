@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" util ^
    --input-dir "%WORKSPACE%\data_dst\aligned" ^
    --unpack-faceset

pause