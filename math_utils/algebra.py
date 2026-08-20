def linear_regression(x,y):
    """
    简单线性回归(y = slope * x + intercept)
    参数：
        x,y:list of numbers, 等长
    返回：
        (slope, intercept)
    """
    sum_x = 0  #用于计算列表x的和
    sum_y = 0  #用于计算列表y的和
    for num_x in x:  #计算x的平均数
        sum_x += num_x
    avg_x = sum_x / len(x)
    for num_y in y:  #计算y的平均数
        sum_y += num_y
    avg_y = sum_y / len(y)
    cov_xy = 0  #cov表示协方差
    var_x = 0  #var表示方差
    for xi, yi in zip (x, y):  #zip函数用于将两个数据变成组元
        cov_xy += (xi - avg_x) * (yi - avg_y)
        var_x += (xi - avg_x) ** 2
    slope = cov_xy / var_x  #计算斜率
    intercept = avg_y - slope * avg_x  #计算截距
    return slope, intercept




def pearson_correlation(x, y):
    """
    计算皮尔逊相关系数（即相关系数r）
    参数:
        x, y: list of numbers
    返回:
        float or None （如果长度<2）
    """
    if len(x) < 2 or len(y) < 2 or len(x) != len(y):  #先对两个列表进行边界处理
        return None
    sum_x = 0  #用于计算列表x的和
    sum_y = 0  #用于计算列表y的和
    for num_x in x:  #计算x的平均数
        sum_x += num_x
    avg_x = sum_x / len(x)
    for num_y in y:  #计算y的平均数
        sum_y += num_y
    avg_y = sum_y / len(y)
    cov_xy = 0
    var_x = 0
    var_y = 0
    for xi, yi in zip (x, y):  #zip函数用于将两个数据变成组元
        cov_xy += (xi - avg_x) * (yi - avg_y)
        var_x += (xi - avg_x) ** 2
        var_y += (yi - avg_y) ** 2
    if var_x * var_y == 0:  #无波动时相关系数为0
        return None
    pearson = cov_xy / ((var_x * var_y)**0.5)
    if pearson > 1.0:  #处理浮点误差
        pearson = 1.0
    elif pearson < -1.0:
        pearson = -1.0
    return pearson
