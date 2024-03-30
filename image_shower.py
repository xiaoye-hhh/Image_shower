import os
import glob
import numpy as np

def collect_paths(pattern: str, num_per_dir: int):
    """ 通过通配符去匹配所有的文件夹，每个文件夹保留num_per_dir张图片

    Args:
        pattern (str): 通配符
        num_per_dir (int): 保留几张图片
    """
    # 加载所有符合的文件
    paths = glob.glob(pattern)

    # 按文件夹分类
    dirname_2_paths = {}
    for path in paths:
        dirname = os.path.dirname(path)
        if dirname not in dirname_2_paths:
            dirname_2_paths[dirname] = []

        dirname_2_paths[dirname].append(path)
    
    # 每个文件夹只保留一部分：随机挑选
    for dirname, paths in dirname_2_paths.items():
        paths = np.random.choice(paths, num_per_dir, len(paths) < num_per_dir)
        dirname_2_paths[dirname] = paths

    return dirname_2_paths 

def builder(dirname_2_paths: dict, num_per_dir: int, max_row: int = 200,
            image_height: int = 200, image_width: int = 100, out_file: str = "shower.html"):
    """  加载模板，生成一个新的html文件来展示图片
        
    """

    # 数据
    content = ""
    for dirname, paths in dirname_2_paths.items():
        for path in paths:
            content += f'\t<div id="image-container"><img src="{path}" alt="图片"><div class="image-text">{path}</div></div>\n'

        max_row -= 1
        if max_row == 0:
            break

    # 加载模板
    with open('Template.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        html = ''.join(lines) 

    # 替换参数
    html = html.replace('$num_of_col$', f'{num_per_dir}')
    html = html.replace('$image_height$', f'{image_height}')
    html = html.replace('$image_width$', f'{image_width}')
    html = html.replace('$content$', content)

    # 输出
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    dirname_2_paths = collect_paths(r"E:\数据集\ReID数据集\VCM_RESIZE\**\rgb\D9\*.jpg", 4)
    builder(dirname_2_paths, 4)