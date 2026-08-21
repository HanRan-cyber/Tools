from misc_utils import *

@timer  #装饰器的运用
def read_fasta(filepath):
    """
    读取FASTA文件，返回 {id: sequence} 字典
    参数:
        filepath: str, 文件路径
    返回:
        dict
    """
    result = {}  #准备一个空字典，用于储存结果
    current_id = None #存放当前序列的ID
    current_seq = [] #存放当前序列
    file = open(filepath, "r") #读取文件。注借助with open(filepath, "r") as f:的写法可不用f.close
    #一行一行地读取文件内容
    for line in file:
        #预处理数据
        line = line.strip()  #strip函数可去除字符串首尾的指定字符
        if not line:
            continue
        elif line.startswith(";"):  #startswith() 用于判断字符串是否以指定前缀开头
            continue
        elif line.startswith(">"):  #startswith() 用于判断字符串是否以指定前缀开头
            if not current_id:
                current_id = line[1:].split()[0]
                #split函数用于把字符串按分隔符拆成列表,括号内可添加指定分隔符，在此用于去除注释
            else:
                result[current_id] = "".join(current_seq)
                #join函数用于将可迭代对象中的字符串元素以指定分隔符号连接成新的字符串
                current_seq = []
                current_id = line[1:].split()[0]  #split函数用于把字符串按分隔符拆成列表，在此用于去除注释
        else:
            current_seq.append(line)
    if current_id is not None:
        result[current_id] = "".join(current_seq) #解决最后一段序列无法添加到字典的问题
    file.close() #关闭文件，释放内存，千万不要忘记
    return result

def gc_content(seq):
    """
    计算GC含量（百分比）
    参数:
        seq: str, DNA序列
    返回:
        float, GC含量百分比
    """
    seq = seq.upper()  #过滤数据，将所有字母大写
    gc_count = 0
    total = 0
    for base in seq:
        if base in 'ATCG':  #非ATCG字符不参与计算
            total += 1
            if base in 'GC':
                gc_count += 1
    if total == 0:
        return 0.0
    return (gc_count / total) * 100

def reverse_complement(seq):
    """
    返回反向互补序列
    参数:
        seq: str
    返回:
        str
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  #碱基互补原则的字典
    result = []
    for base in seq.upper():
        if base in complement:
            result.append(complement[base])
        else:
            result.append(base)   # 非ATCG字符原样保留
    return ''.join(reversed(result))  #reversed函数用于将列表反转

def gc_window(seq, k):
    """
    滑动窗口计算 GC 含量百分比
    参数:
        seq: str, DNA 序列
        k: int, 窗口大小
    返回:
        list of float, 每个窗口的 GC 含量百分比
    """
    if k <= 0 or k > len(seq):  #边界处理
        return []
    seq = seq.upper()  #预处理数据
    window_content = []
    for i in range(len(seq) - k + 1):
        gc_window_content = gc_content(seq[i:i+k])  #调用之前的函数完成gc含量的计算
        window_content.append(gc_window_content)
    return window_content


