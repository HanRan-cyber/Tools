import os
import pandas as pd

def read_data(filepath, **kwargs):
    """
        根据文件后缀自动读取数据文件

        参数:
            filepath: str, 文件路径
            **kwargs: 传递给底层 pandas 读取函数的额外参数（如 encoding='gbk'）
    """
    #检查文件是否存在 os.path.exists函数判断路径的存在性
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'文件不存在:{filepath}')
    
    #os.path.splitext()函数用于分离文件名和拓展名，返回元组
    ext = os.path.splitext(filepath)[1].lower()
    
    #CSV默认逗号分隔，但可通过kwargs传入';'覆盖
    if ext == '.csv':
        return pd.read_csv(filepath, **kwargs)
    #TSV本质是制表符号分隔的CSV，默认 sep='\t'
    elif ext == '.tsv':
        return pd.read_csv(filepath, sep = '\t' , **kwargs)
    elif ext in ['.xlsx', '.xls']:
        return pd.read_excel(filepath, **kwargs)
    #不支持的格式，抛出错误
    else:
        raise ValueError(f'不支持的文件格式：{ext}，请使用 .csv .tsv .xlsx')

def save_data(df, filepath, **kwargs):
    """
    根据文件后缀自动保存 DataFrame

    参数:
        df: pd.DataFrame, 要保存的数据
        filepath: str, 保存路径
        **kwargs: 传递给底层 pandas 保存函数的额外参数（如 index=False）
    """
    #确保传入的是DataFrame格式
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f'{df}类型错误，参数必须为pandas.DataFrame类型')
    # os.path.dirname用于从完整路径中提取文件所在的文件夹路径
    dir_name =  os.path.dirname(filepath)  

    if dir_name:  #os.makedirs函数不仅可创建最后一层文件夹，还会把路径中所有不存在的父文件夹一并创建。
        os.makedirs(dir_name, exist_ok = True)  #exist_ok=True：意思如果文件夹已经存在，不要报错，继续往下走
    #提取拓展名    
    ext = os.path.splitext(filepath)[1].lower()
    #
    if ext == '.csv':
        df.to_csv(filepath, **kwargs)
        
    elif ext == '.tsv':
        kwargs.setdefault('sep', '\t')  #.setdefault用于获取或初始化键值对，若没有指定，就为'\t'
        df.to_csv(filepath, **kwargs)
    
    elif ext in ['.xlsx', '.xls']:
        df.to_excel(filepath, **kwargs)
        
    else:
        raise ValueError(f'不支持的文件格式：{ext}，请使用 .csv .tsv .xlsx')

