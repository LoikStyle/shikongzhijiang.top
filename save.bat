@echo off
chcp 65001 >nul
echo 📦 开始保存项目...

cd /d "%~dp0"

git add -A

git diff --cached --quiet && (
    echo ✅ 没有需要保存的更改
    pause
    exit /b 0
)

if "%~1"=="" (
    set commit_msg=update: 项目更新 %date% %time%
) else (
    set commit_msg=%~1
)

git commit -m "%commit_msg%"

echo 🚀 推送到 GitHub...
git push origin master

if errorlevel 1 (
    echo ❌ 推送失败
    pause
    exit /b 1
)

echo ✅ 保存完成!
pause
