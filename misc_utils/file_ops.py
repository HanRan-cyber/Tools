import os


def ensure_dir(path):
    """
    确保文件夹存在，不存在就创建（路径里缺的父文件夹也会一起建好）
    参数:
        path: str, 文件夹路径
    返回:
        str, 原样返回传进来的路径，方便连着往下写
    """
    if not path:  #边界处理：空字符串直接返回，别建出个奇怪的东西
        return path
    os.makedirs(path, exist_ok = True)  #exist_ok=True：已经存在也不报错，继续往下走
    return path


def _match_suffix(name, suffixes):
    """
    内部函数：判断文件名是不是以给定的后缀结尾（不区分大小写）
    参数:
        name: str, 文件名
        suffixes: tuple 或 None, 允许的后缀；None 表示不过滤
    返回:
        bool
    """
    if suffixes is None:
        return True
    return name.lower().endswith(suffixes)  #endswith的参数可以是元组，命中其中任意一个就返回True


def list_files(folder, suffix = None, recursive = False):
    """
    列出文件夹里的文件（只要文件，不要文件夹）
    参数:
        folder: str, 文件夹路径
        suffix: str 或 tuple, 后缀过滤，例如 '.fasta' 或 ('.fa', '.fasta')
        recursive: bool, 是否递归进子文件夹
    返回:
        list of str, 排好序的完整路径
    """
    if not os.path.isdir(folder):  #先确认这个路径确实是个文件夹
        raise FileNotFoundError(f'文件夹不存在:{folder}')

    if isinstance(suffix, str):  #只传一个字符串的情况，统一成元组，后面只写一份判断
        suffix = (suffix,)
    if suffix is not None:
        suffix = tuple(item.lower() for item in suffix)

    result = []
    if recursive:
        for root, dirs, files in os.walk(folder):  #os.walk 会自己一层层走进子文件夹
            dirs.sort()  #排序是为了每次运行的顺序都一样，结果可复现
            for name in files:
                if _match_suffix(name, suffix):
                    result.append(os.path.join(root, name))
    else:
        for name in os.listdir(folder):
            full_path = os.path.join(folder, name)
            if not os.path.isfile(full_path):  #是子文件夹就跳过
                continue
            if _match_suffix(name, suffix):
                result.append(full_path)

    return sorted(result)  #sorted 返回的是新列表，不会把原来的改动


def batch_rename(folder, prefix = '', suffix = None, start = 1, digits = 3, dry_run = True):
    """
    批量重命名文件夹里的文件，新名字 = prefix + 编号 + 后缀
    参数:
        folder: str, 文件夹路径
        prefix: str, 新文件名前缀，例如 'sample_'
        suffix: str, 新文件名后缀（要带点，例如 '.fasta'）；None 表示保留原来的后缀
        start: int, 编号从几开始
        digits: int, 编号补零的位数，digits=3 就是 001、002
        dry_run: bool, 默认 True 只返回计划、不动文件；看清楚了再传 False 真正改名
    返回:
        list of (old_path, new_path)，dry_run=True 时是"打算怎么改"
    注意:
        新名字会先整体检查一遍：只要有一个会撞名或者新名字重复，就一个都不改，直接报错。
        以点开头的隐藏文件不参与改名，免得把 .DS_Store 改成 sample_001。
    """
    files = [path for path in list_files(folder)
             if not os.path.basename(path).startswith('.')]
    old_set = set(os.path.abspath(path) for path in files)  #abspath 用于统一成绝对路径，比较时不会因为写法不同而漏掉
    plan = []
    used_names = set()  #新名字单独去重，防止 digits 太小导致两个文件撞名

    for number, old_path in enumerate(files, start = start):  #enumerate 能同时拿到下标和值，start 指定从几开始数
        if suffix is None:
            ext = os.path.splitext(old_path)[1]  #splitext 把路径拆成 (前面的名字, 后缀) 返回元组
        else:
            ext = suffix
        new_name = prefix + str(number).zfill(digits) + ext
        #zfill 会在左边补零，例如 str(7).zfill(3) 得到 '007'
        new_path = os.path.join(folder, new_name)

        if new_name in used_names:  #正常情况下不会撞，留着兜底，以后改命名规则也不会出事
            raise ValueError(f'新文件名重复了:{new_name}，检查一下 prefix 和 suffix 的设置')
        if os.path.abspath(new_path) in old_set:
            raise ValueError(f'新名字和文件夹里原有的文件撞了:{new_path}，先手动处理一下再批量改')
        used_names.add(new_name)
        plan.append((old_path, new_path))

    if not dry_run:  #真正动文件，改名前已经把上面的坑都检查过了
        for old_path, new_path in plan:
            os.rename(old_path, new_path)

    return plan


if __name__ == '__main__':
    #简单自测：在临时文件夹里造几个文件，看看列举和批量改名对不对
    import tempfile

    demo_dir = tempfile.mkdtemp()  #mkdtemp 会建一个临时文件夹并返回路径，用完不用自己删
    for name in ('b.txt', 'a.txt', 'c.txt', '.DS_Store'):
        open(os.path.join(demo_dir, name), 'w').close()  #建空文件

    print('列出的 .txt 文件：')
    for path in list_files(demo_dir, suffix = '.txt'):
        print('  ', os.path.basename(path))

    print('改名计划（dry_run 默认不真改）：')
    for old_path, new_path in batch_rename(demo_dir, prefix = 'sample_', suffix = '.txt'):
        print('  ', os.path.basename(old_path), '->', os.path.basename(new_path))
