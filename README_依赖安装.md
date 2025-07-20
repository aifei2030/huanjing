## 📋 项目依赖

- **requests** - HTTP请求库
- **pycryptodome** - 加密库（提供Crypto模块）
- **ddddocr** - OCR验证码识别库
- **eth-account** - 以太坊账户管理
- **openpyxl** - Excel文件处理

## 🚀 自动安装方法

### 方法一：使用批处理文件（推荐Windows用户）

1. 双击运行 `install_dependencies.bat`
2. 脚本会自动检查Python环境并安装所有依赖
3. 安装完成后会显示结果

### 方法二：使用Python脚本

```bash
python install_dependencies.py
```

### 方法三：使用pip直接安装

```bash
pip install -r requirements.txt
```

## 🔧 手动安装

如果自动安装失败，可以手动安装每个包：

```bash
pip install requests
pip install pycryptodome
pip install ddddocr
pip install eth-account
pip install openpyxl
```

## ⚠️ 注意事项

1. **Python版本要求**：需要Python 3.7或更高版本
2. **网络连接**：安装过程需要网络连接下载包
3. **权限问题**：如果遇到权限错误，请以管理员身份运行
4. **代理设置**：如果使用代理，请确保pip能正常访问PyPI

## 🧪 验证安装

安装完成后，可以运行以下命令验证：

```python
python -c "
import requests
from Crypto.Cipher import AES
import ddddocr
from eth_account import Account
from openpyxl.reader.excel import load_workbook
print('✅ 所有依赖安装成功！')
"
```

## 📞 常见问题

### Q: 安装pycryptodome时出错
A: 尝试先卸载pycrypto（如果已安装）：
```bash
pip uninstall pycrypto
pip install pycryptodome
```

### Q: ddddocr安装失败
A: 可能需要安装Visual C++ Build Tools，或者使用预编译版本：
```bash
pip install ddddocr --only-binary=all
```

### Q: 网络连接问题
A: 可以尝试使用国内镜像源：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 📝 更新日志

- 2025-01-XX: 创建自动安装脚本
- 支持Windows和Linux系统
- 添加依赖检查和验证功能 
