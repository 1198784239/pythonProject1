import os

# 定义目标目录路径
abs_path = r"C:\Users\李克聪\Desktop\重命名文件夹"

try:
    # 切换到目标目录
    os.chdir(abs_path)
    # 获取当前工作目录
    current_dir = os.getcwd()

    # 获取目标目录下的所有文件和文件夹
    items = os.listdir()
    m = 1

    for item in items:
        # 拼接完整路径
        full_path = os.path.join(abs_path, item)

        # 检查是否为目录
        if os.path.isdir(full_path):
            try:
                # 进入子目录
                os.chdir(full_path)
                # 获取子目录的当前工作目录
                sub_dir = os.getcwd()

                # 使用条件表达式判断目录是否为空并进行相应操作
                os.chdir(abs_path)
                os.rmdir(full_path) if len(os.listdir(sub_dir)) == 0 else None
                print(f"已删除空目录: {full_path}") if len(os.listdir(sub_dir)) == 0 else None

            except PermissionError:
                print(f"没有权限操作目录: {full_path}")
        # 如果是 .txt 文件，进行重命名操作
        elif item.endswith(".txt"):
            new_name = f"第{m + 5}章节.txt"
            os.rename(full_path, os.path.join(abs_path, new_name)) if item.endswith(".txt") else None
            print(f"已将 {full_path} 重命名为 {new_name}")
            m += 1

except FileNotFoundError:
    print(f"指定的目录 {abs_path} 不存在。")