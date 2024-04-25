@echo off
setlocal enabledelayedexpansion

for /f "delims=" %%i in ('git ls-files') do (
    set "file=%%i"
    for /f "delims=" %%l in ('type "!file!" ^| find /c /v ""') do (
        set /a "lines+=%%l"
    )
)

echo total_lines: %lines%
endlocal
