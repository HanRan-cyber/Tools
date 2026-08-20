import time

def timer(func):  #装饰器的写法需要熟练掌握
    """
    装饰器：打印函数执行耗时
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter() #开始计时
        result = func(*args, **kwargs)  #真正执行原函数，*按位置，**带名字
        end = time.perf_counter()  #结束计时
        print(f'{func.__name__}耗时：{end - start}秒')  #格式化写法
        return result
    return wrapper