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
        line = line.strip()
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
        float
    """
    pass  # TODO: 实现

def reverse_complement(seq):
    """
    返回反向互补序列
    参数:
        seq: str
    返回:
        str
    """
    pass  # TODO: 实现