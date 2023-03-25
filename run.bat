@echo off
title Compilation...
set "yes=yes"
set "no=no"

set /p conf=Confirmation? 
if %conf% EQU %no% (
exit
)

xcopy /E /I G:\Exe\Editor G:\Exe\Edit < t

set /p auto=ModeAuto? 
if %auto% EQU %yes% (
set "zip=yes"
set "comp=yes"
set "inst=yes"
set "open=yes"
set "pause=no"
)
if %auto% EQU %no% (
set /p zip=Zip? 
set /p comp=Compilation? 
set /p inst=Installer? 
set /p open=Ouvrir? 
set /p pause=Pause? 
)

rd G:\Exe\Edit\build /S /Q

if %zip% EQU %yes% (
"C:\Program Files\7-Zip\7z.exe" a "N:\source\Edit_31.1_20230324.zip" G:\Exe\Edit
)

if %pause% EQU %yes% (
start N:\source\
pause
)

if %comp% EQU %yes% (
G:\Exe\Edit\setup.py build
)

if %pause% EQU %yes% (
start G:\Exe\Edit\build\exe.win-amd64-3.10\
pause
)

if %inst% EQU %yes% (
"C:\Program Files (x86)\Inno Setup 6\iscc.exe" G:\Exe\Edit\compilation.iss
"C:\Program Files\7-Zip\7z.exe" a "N:\setup\setup_31_win.zip" "N:\setup\setup_31_win.exe"
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