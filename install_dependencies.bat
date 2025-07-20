@echo off
chcp 65001 >nul
echo 🚀 CoreSky 依赖安装器
echo ================================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未找到Python，请先安装Python 3.7或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ 检测到Python，开始安装依赖...
echo.

REM 运行Python安装脚本
python install_dependencies.py

echo.
echo 安装完成！按任意键退出...
pause >nul 