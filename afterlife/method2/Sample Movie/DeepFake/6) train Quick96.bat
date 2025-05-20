@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" "%DFL_ROOT%\main.py" train ^
    --training-data-src-dir "%WORKSPACE%\data_src\aligned" ^
    --training-data-dst-dir "%WORKSPACE%\data_dst\aligned" ^
    --pretraining-data-dir "%INTERNAL%\pretrain_faces" ^
    --pretrained-model-dir "%INTERNAL%\pretrain_Quick96" ^
    --model-dir "%WORKSPACE%\model" ^
    --model Quick96

pause