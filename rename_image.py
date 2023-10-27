import os
import shutil

# 指定要重命名的图片文件夹
image_folder = 'D:/123pan/Downloads/test/test'

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(image_folder) if f.endswith('.bmp') or f.endswith('.png')]  # 根据实际图片格式扩展

count = 0

# 遍历图片文件并重命名
for old_name in image_files:
    suffix = os.path.splitext(old_name)[1]
    suffix_without_dot = suffix[1:]   #没有dot的后缀名
    old_path = os.path.join(image_folder, old_name)
    new_name = f'{count}.{suffix_without_dot}'  # 你可以根据需要选择不同的文件扩展名
    new_path = os.path.join(image_folder, new_name)

    shutil.move(old_path, new_path)

    count += 1

print(f' {count} picture successful。')
