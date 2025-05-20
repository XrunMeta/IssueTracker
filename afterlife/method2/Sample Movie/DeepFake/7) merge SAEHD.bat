@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" merge ^
    --input-dir "%WORKSPACE%\data_dst" ^
    --output-dir "%WORKSPACE%\data_dst\merged" ^
    --output-mask-dir "%WORKSPACE%\data_dst\merged_mask" ^
    --aligned-dir "%WORKSPACE%\data_dst\aligned" ^
    --model-dir "%WORKSPACE%\model" ^
    --model SAEHD
    
pause