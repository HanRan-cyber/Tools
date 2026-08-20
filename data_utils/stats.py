import statistics  #statistics模块是做基础数学统计的

def standardize(data):
    """
    标准化数据（Z-score）
    参数:
        data: list of numbers
    返回:
        list of floats, 均值为0，标准差为1
    """
    avg_data = statistics.mean(data)  #.mean函数用于计算平均值
    std_data = statistics.pstdev(data)  #.pstdev函数用于计算总体标准差
    for i in range(len(data)):
        data[i] = (data[i] - avg_data)/std_data  #进行Z-score归一化
    return data


def outlier_iqr(data, k=1.5):  #四分位距法（IQR）检测异常值的方法
    """
    使用IQR方法剔除异常值
    参数:
        data: list of numbers
        k: 倍数（默认1.5）
    返回:
        (cleaned_list, outliers_list)
    """
    outliers_list = []
    cleaned_list = []
    q_list = statistics.quantiles(data, n = 4)  #.quantiles函数可把数据按比例切成n等份，并返回各个切割点的数值
    q1 = q_list[0]
    q3 = q_list[2]

    _ = statistics.median(data)  #.median函数用于计算一组数据的中位数，此处_表示我调用了却不使用这个值

    #计算IQR和边界
    iqr = q3 - q1
    lower = q1 - k*iqr
    upper = q3 + k*iqr
    for item in data:
        if item < lower or item > upper:
            outliers_list.append(item)
        else:
            cleaned_list.append(item)
    return cleaned_list, outliers_list


