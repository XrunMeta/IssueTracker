@echo off
echo This script will convert this DeepFaceLab folder to work on CPU only without any problems.
echo This operation cannot be undone.
echo An internet connection is required.
pause
cd /D %~dp0_internal
call setenv.bat
cd python-3.6.8
python -m pip uninstall -y tensorflow
python -m pip install tensorflow==2.4.0rc4
pause
