import os
import random
import string
from pathlib import Path

def generate_random_name(length=8):
    """生成指定长度的随机字符串"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_images(directory, name_type='random', prefix=None):
    """
    批量重命名图片文件
    
    参数:
    directory: 图片所在目录
    name_type: 命名类型 ('random' 或 'sequential')
    prefix: 指定命名时的前缀
    """
    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    # 获取目录下所有图片文件
    image_files = []
    for ext in image_extensions:
        image_files.extend(list(Path(directory).glob(f'*{ext}')))
    
    if not image_files:
        print(f"在目录 {directory} 中没有找到图片文件")
        return
    
    # 记录已使用的文件名避免重复
    used_names = set()
    
    # 用于顺序命名的计数器
    counter = 1
    
    for image_file in image_files:
        old_path = image_file
        extension = image_file.suffix.lower()
        
        # 生成新文件名
        while True:
            if name_type == 'random':
                new_name = generate_random_name()
            else:  # sequential
                new_name = f"{prefix}{counter}"
                counter += 1
            
            # 检查文件名是否已存在
            if new_name not in used_names:
                used_names.add(new_name)
                break
        
        # 构建新的文件路径
        new_path = old_path.parent / f"{new_name}{extension}"
        
        try:
            # 重命名文件
            old_path.rename(new_path)
            print(f"已重命名: {old_path.name} -> {new_path.name}")
        except Exception as e:
            print(f"重命名 {old_path.name} 时出错: {str(e)}")

def main():
    # 获取图片目录路径
    while True:
        directory = input("请输入图片所在的目录路径: ").strip()
        if os.path.isdir(directory):
            break
        print("目录不存在，请重新输入！")
    
    # 选择命名模式
    while True:
        print("\n请选择命名模式：")
        print("1. 随机命名")
        print("2. 指定命名")
        choice = input("请输入选项（1或2）: ").strip()
        
        if choice in ['1', '2']:
            break
        print("无效的选择，请重新输入！")
    
    # 设置命名参数
    if choice == '1':
        name_type = 'random'
        prefix = None
    else:
        name_type = 'sequential'
        prefix = input('请输入指定的名称前缀（如"吃饭"）: ').strip()
        while not prefix:
            print("前缀不能为空！")
            prefix = input('请输入指定的名称前缀（如"吃饭"）: ').strip()
    
    # 执行重命名操作
    rename_images(directory, name_type, prefix)
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()