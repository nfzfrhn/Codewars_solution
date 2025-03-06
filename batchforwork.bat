@echo off
setlocal enabledelayedexpansion

:: Input file
set "inputFile=hexdata.txt"

:: Check if file exists
if not exist "%inputFile%" (
    echo File "%inputFile%" not found!
    exit /b 1
)

:: Read the content of the file
set "hexData="
for /f "delims=" %%A in (%inputFile%) do set "hexData=%%A"

:: Calculate current size of hex data in bytes
set /a currentSize=(len(hexData) / 2)

:: Calculate number of padding bytes needed
set /a paddingSize=4096 - currentSize

:: If the data is already 4KB or more, no padding needed
if %paddingSize% LEQ 0 (
    echo File already 4KB or more, no padding needed.
    exit /b 0
)

:: Create padding (two '0' hex digits = 1 byte)
set "padding="
for /l %%I in (1,1,%paddingSize%) do set "padding=!padding!00"

:: Combine original data and padding
set "paddedHexData=%hexData%%padding%"

:: Write back to the same file
echo %paddedHexData% > %inputFile%

echo File successfully padded to 4KB.
endlocal