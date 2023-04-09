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
"C:\Program Files\7-Zip\7z.exe" a "N:\source\Edit_32.3_20230403.zip" G:\Exe\Edit
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

rd N:\last_version /S /Q
mkdir N:\last_version
copy "N:\setup\setup_32_win.exe" "N:\last_version\setup_32_win.exe"
copy "N:\setup\setup_32_win.zip" "N:\last_version\setup_32_win.zip"
copy "N:\source\Edit_32.3_20230403.zip" "N:\last_version\Edit_32.3_20230403.zip"
copy "N:\mobile\mobile_32_win.zip" "N:\last_version\mobile_32_win.zip"

if %open% EQU %yes% (
start N:\last_version\
)