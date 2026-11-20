from .algebra import linear_regression, pearson_correlation

__all__ = ['linear_regression', 'pearson_correlation',
           'line_plot', 'scatter_plot', 'bar_plot']


def __getattr__(name):
    #模块级的 __getattr__ 是个新写法（Python 3.7 以后才有）：
    #只有真的用到画图函数时，才去把 plot.py 拉进来。
    #plot 依赖 matplotlib，一 import 就要等一两秒，而 import bio_utils 会顺带进到这个包，
    #纯序列处理不该被画图的依赖拖慢，所以这里做成"用到了才加载"。
    if name in ('line_plot', 'scatter_plot', 'bar_plot'):
        from . import plot
        return getattr(plot, name)
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
