@echo off
call _internal\setenv.bat

start "" /D "%INTERNAL%\EbSynth" /LOW "%INTERNAL%\EbSynth\EbSynth.exe" "%INTERNAL%\EbSynth\SampleProject\sample.ebs"
