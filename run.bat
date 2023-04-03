@echo off
title Compilation...
set "yes=yes"
set "no=no"

xcopy /E /I G:\Exe\Editor G:\Exe\Edit < t
cls

set /p conf=Confirmation? 
if %conf% EQU %no% (
exit
)

set /p auto=ModeAuto? 
if %auto% EQU %yes% (
set "zip=yes"
set "comp=yes"
set "inst=yes"
set "open=yes"
set "pause=no"
set "mobile=yes"
)
if %auto% EQU %no% (
set /p zip=Zip? 
set /p comp=Compilation? 
set /p inst=Installer? 
set /p mobile=VersionMobile? 
set /p open=Ouvrir? 
set /p pause=Pause? 
)

rd G:\Exe\Edit\build /S /Q

if %zip% EQU %yes% (
"C:\Program Files\7-Zip\7z.exe" a "N:\source\Edit_32.1_20230330.zip" G:\Exe\Edit
)

if %pause% EQU %yes% (
start N:\source\
pause
)

cd G:\Exe\Edit\

if %comp% EQU %yes% (
setup.py build
)

if %pause% EQU %yes% (
start G:\Exe\Edit\build\exe.win-amd64-3.10\
pause
)

if %mobile% EQU %yes% (
"C:\Program Files\7-Zip\7z.exe" a "N:\mobile\mobile_32_win.zip" G:\Exe\Edit\build\exe.win-amd64-3.10\*
)

if %pause% EQU %yes% (
start N:\mobile\
pause
)

if %inst% EQU %yes% (
"C:\Program Files (x86)\Inno Setup 6\iscc.exe" compilation.iss
"C:\Program Files\7-Zip\7z.exe" a "N:\setup\setup_32_win.zip" "N:\setup\setup_32_win.exe"
)

if %pause% EQU %yes% (
start N:\setup\
pause
)

if %open% EQU %yes% (
start G:\Exe\Edit\build\exe.win-amd64-3.10\
start N:\source\
start N:\setup\
)