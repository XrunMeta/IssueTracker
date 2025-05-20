@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" extract ^
    --input-dir "%WORKSPACE%\data_dst" ^
    --output-dir "%WORKSPACE%\data_dst\aligned" ^
    --output-debug ^
    --detector s3fd ^
    --max-faces-from-image 0 ^
    --manual-fix

pause