from math_utils import linear_regression

def enzyme_kinetics(S, v):
    """
    利用 Lineweaver-Burk 线性化计算米氏方程参数
    参数:
        S: list of float, 底物浓度 [S]
        v: list of float, 反应速率 v
    返回:
        (Vmax, Km) 元组
    步骤:
        1. 计算 x = [1/s for s in S], y = [1/vel for vel in v]
        2. 调用 linear_regression(x, y) 得到斜率 a 和截距 b
        3. Vmax = 1 / b
        4. Km = a * Vmax
    注意:
        确保 S 和 v 等长且非空，处理除零情况（理论上浓度不会为零）。
    """
    if not S or not v or len(S) != len(v):
        raise ValueError('S和v不能为空列表，且长度必须相同')
        #raise 是用于手动触发异常的关键字‌，它允许程序在检测到错误条件时主动中断正常流程并抛出异常对象

    reciprocal_S = [1 / s for s in S]  #将底物浓度转化为倒数
    reciprocal_v = [1 / vel for vel in v]  #将反应速率转化为倒数,vel代表velocity

    slope, intercept = linear_regression(reciprocal_S, reciprocal_v)  #调用之前写的函数

    if intercept < 1e-12:  #1e-12代表0.000000000001
        raise ValueError('截距太接近0，Vmax过大，不可信，数据可能存在错误')
    Vmax = 1 / intercept
    Km = slope * Vmax
    return Vmax, Km

