# 图库展示工具

这个简单的小项目能够帮助你在浏览器中展示位于复杂目录结构下的图库图片。它通过用户定义的通配符来自动生成一个HTML文件，使得图片的展示变得简单直观。

## 🚀开始之前

在开始之前，请确保你的系统满足以下需求：

- Python 3.6 或更高版本
- numpy 

## 🛠️安装

首先，克隆这个仓库到你的本地机器：

```bash
git clone https://github.com/xiaoye-hhh/Image_shower.git
cd Image_shower
```

## 🔥使用说明
要使用这个工具生成图片展示的HTML文件，请遵循以下步骤：
1. 修改`image_shower.py`的图像通配符，例如：
```python
if __name__ == '__main__':
    dirname_2_paths = collect_paths(r"E:\数据集\D9\*.jpg", 4)
    builder(dirname_2_paths, 4)
```
2. 运行脚本：
```shell
python image_shower.py
```
3. 打开生成的`shower.html`，使用浏览器查看你的图片。
## 🎨 特性
- 支持自定义通配符，灵活适应不同的文件命名规则
## 👏 贡献
如果你有好的建议或功能请求，欢迎通过Issues或Pull Requests参与贡献。
## 📄 许可证
本项目采用[MIT](LICENSE)许可证。

