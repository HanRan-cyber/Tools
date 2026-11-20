import os

import matplotlib.pyplot as plt

from misc_utils.file_ops import ensure_dir

#中文字体：matplotlib 默认字体里没有中文，标题会显示成方块，这里按系统里常见的字体依次找
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Microsoft YaHei',
                                   'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  #负号显示成方块的时候，要把它关掉


def _check_xy(x, y):
    """
    内部函数：检查 x 和 y 是不是等长，不等长就没法画
    参数:
        x, y: list of numbers
    """
    if len(x) != len(y):
        raise ValueError(f'x 和 y 长度不一致：x 有 {len(x)} 个，y 有 {len(y)} 个')
    if len(x) == 0:
        raise ValueError('x 和 y 都是空的，没有东西可画')


def _save_or_show(fig, save_path, show):
    """
    内部函数：要保存就保存，要显示就显示，两个都不做就把图关掉，免得占内存
    参数:
        fig: matplotlib 的画布对象
        save_path: str 或 None
        show: bool
    """
    if save_path:
        ensure_dir(os.path.dirname(save_path))  #目录不存在就先建出来
        fig.savefig(save_path, dpi = 150, bbox_inches = 'tight')  #bbox_inches 把多余的白边裁掉
    if show:
        plt.show()
    else:
        plt.close(fig)  #不显示的时候手动关掉，画很多张图时不会越攒越多


def line_plot(x, y, title = '', xlabel = '', ylabel = '', save_path = None, show = True):
    """
    画折线图
    参数:
        x, y: list of numbers, 等长的横纵坐标
        title: str, 图标题
        xlabel, ylabel: str, 两个轴的名称
        save_path: str, 保存路径；None 表示不保存
        show: bool, 是否弹窗显示；只想存成图片就传 False
    返回:
        (fig, ax) 元组，拿到之后还能接着往上加东西，比如 ax.legend()
    """
    _check_xy(x, y)
    fig, ax = plt.subplots(figsize = (6, 4))  #fig 是整张画布，ax 是里面的坐标系
    ax.plot(x, y, marker = 'o', markersize = 4, linewidth = 1.5)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle = '--', alpha = 0.5)  #alpha 是透明度，0.5 就是半透明
    _save_or_show(fig, save_path, show)
    return fig, ax


def scatter_plot(x, y, title = '', xlabel = '', ylabel = '', save_path = None, show = True):
    """
    画散点图
    参数:
        x, y: list of numbers, 等长的横纵坐标
        title: str, 图标题
        xlabel, ylabel: str, 两个轴的名称
        save_path: str, 保存路径；None 表示不保存
        show: bool, 是否弹窗显示
    返回:
        (fig, ax) 元组
    """
    _check_xy(x, y)
    fig, ax = plt.subplots(figsize = (6, 4))
    ax.scatter(x, y, s = 25, alpha = 0.8)  #s 是点的大小
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle = '--', alpha = 0.5)
    _save_or_show(fig, save_path, show)
    return fig, ax


def bar_plot(labels, values, title = '', xlabel = '', ylabel = '', save_path = None, show = True):
    """
    画柱状图
    参数:
        labels: list of str, 每个柱子下面的标签
        values: list of numbers, 每个柱子的高度
        title: str, 图标题
        xlabel, ylabel: str, 两个轴的名称
        save_path: str, 保存路径；None 表示不保存
        show: bool, 是否弹窗显示
    返回:
        (fig, ax) 元组
    """
    _check_xy(labels, values)  #标签和高度的个数必须一样，正好也能用这个检查
    fig, ax = plt.subplots(figsize = (6, 4))
    ax.bar(labels, values, width = 0.6)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, axis = 'y', linestyle = '--', alpha = 0.5)  #只画横向的网格线，柱状图看起来更干净
    _save_or_show(fig, save_path, show)
    return fig, ax


if __name__ == '__main__':
    #简单自测：画两张图存到临时文件夹里，看看能不能正常出图
    import tempfile

    demo_dir = tempfile.mkdtemp()
    line_plot([1, 2, 3, 4], [2.1, 4.0, 5.9, 8.2], title = '标准曲线',
              xlabel = '浓度', ylabel = '吸光度',
              save_path = os.path.join(demo_dir, 'line.png'), show = False)
    bar_plot(['A', 'B', 'C'], [3, 7, 5], title = '柱状图示例',
             xlabel = '分组', ylabel = '数量',
             save_path = os.path.join(demo_dir, 'bar.png'), show = False)
    print('图片已经保存到：', demo_dir)
