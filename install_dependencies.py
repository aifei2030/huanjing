#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动安装 coresky_daily.py 所需的依赖包
"""

import subprocess
import sys
import importlib
import os

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 7):
        print("❌ 错误：需要Python 3.7或更高版本")
        print(f"当前版本：{sys.version}")
        return False
    print(f"✅ Python版本检查通过：{sys.version}")
    return True

def install_package(package_name, pip_name=None):
    """安装单个包"""
    if pip_name is None:
        pip_name = package_name
    
    try:
        # 尝试导入包
        importlib.import_module(package_name)
        print(f"✅ {package_name} 已安装")
        return True
    except ImportError:
        print(f"📦 正在安装 {package_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            print(f"✅ {package_name} 安装成功")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ {package_name} 安装失败：{e}")
            return False

def install_dependencies():
    """安装所有依赖"""
    print("🔍 开始检查和安装依赖包...")
    print("=" * 50)
    
    # 检查Python版本
    if not check_python_version():
        return False
    
    # 定义需要安装的包
    packages = [
        ("requests", "requests"),
        ("Crypto", "pycryptodome"),  # Crypto模块来自pycryptodome
        ("ddddocr", "ddddocr"),
        ("eth_account", "eth-account"),
        ("openpyxl", "openpyxl"),
    ]
    
    success_count = 0
    total_count = len(packages)
    
    for package_name, pip_name in packages:
        if install_package(package_name, pip_name):
            success_count += 1
        print("-" * 30)
    
    print("=" * 50)
    print(f"📊 安装结果：{success_count}/{total_count} 个包安装成功")
    
    if success_count == total_count:
        print("🎉 所有依赖包安装完成！现在可以运行 coresky_daily.py 了")
        return True
    else:
        print("⚠️ 部分依赖包安装失败，请检查网络连接或手动安装")
        return False

def test_imports():
    """测试所有导入是否正常"""
    print("\n🧪 测试导入功能...")
    
    try:
        import json
        import os
        import random
        import time
        import requests
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        import base64
        import ddddocr
        from eth_account import Account
        from eth_account.messages import encode_defunct
        from openpyxl.reader.excel import load_workbook
        
        print("✅ 所有模块导入成功！")
        return True
    except ImportError as e:
        print(f"❌ 导入测试失败：{e}")
        return False

def main():
    """主函数"""
    print("🚀 CoreSky 依赖安装器")
    print("=" * 50)
    
    # 安装依赖
    if install_dependencies():
        # 测试导入
        if test_imports():
            print("\n🎊 环境配置完成！可以开始使用 coresky_daily.py")
        else:
            print("\n⚠️ 导入测试失败，请检查安装")
    else:
        print("\n❌ 依赖安装失败，请检查错误信息")

if __name__ == "__main__":
    main() 