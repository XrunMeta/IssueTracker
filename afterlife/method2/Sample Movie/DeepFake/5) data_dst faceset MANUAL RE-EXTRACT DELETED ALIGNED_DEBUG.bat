@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" extract ^
    --input-dir "%WORKSPACE%\data_dst" ^
    --output-dir "%WORKSPACE%\data_dst\aligned" ^
    --detector manual ^
    --max-faces-from-image 0 ^
    --output-debug ^
    --manual-output-debug-fix
    

pause