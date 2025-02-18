# renamed-photo


一个简单而实用的图片批量重命名工具，支持随机命名和指定前缀的序号命名两种模式。

## 功能特点

- 支持 JPG、JPEG 和 PNG 格式图片
- 两种命名模式：
  - 随机命名：生成包含字母和数字的随机文件名
  - 指定命名：使用指定前缀加序号（如：吃饭1、吃饭2）
- 交互式操作界面
- 自动处理文件名冲突
- 保留原始文件扩展名

## 环境要求

- Python 3.6 或更高版本
- 无需额外依赖包

## 安装方法

1. 克隆仓库到本地：
```bash
git clone https://github.com/lry666666/renamed-photo.git
```

2. 进入项目目录：
```bash
cd image-renamer
```

## 使用方法

1. 运行脚本：
```bash
python renamed-photo.py
```

2. 按照提示进行操作：
   - 输入图片所在的目录路径
   - 选择命名模式（1: 随机命名，2: 指定命名）
   - 如果选择指定命名，输入名称前缀

## 使用示例

```
请输入图片所在的目录路径: C:\Photos

请选择命名模式：
1. 随机命名
2. 指定命名
请输入选项（1或2）: 2

请输入指定的名称前缀（如"吃饭"）: 旅行照片

已重命名: IMG_001.jpg -> 旅行照片1.jpg
已重命名: IMG_002.jpg -> 旅行照片2.jpg
已重命名: IMG_003.png -> 旅行照片3.png
```

## 注意事项

- 使用前请确保对目标目录有读写权限
- 建议在重命名前备份重要文件
- 程序会自动跳过不支持的文件格式

## 贡献

欢迎提交 Issues 和 Pull Requests 来帮助改进这个项目。

## 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
