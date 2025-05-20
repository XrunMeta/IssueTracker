@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" xseg apply ^
    --input-dir "%WORKSPACE%\data_dst\aligned" ^
    --model-dir "%INTERNAL%\model_generic_xseg"

pause