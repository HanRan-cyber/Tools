# Tools —— 个人生物信息学与数据分析工具集

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个轻量级的 Python 工具库，整合了我在生物信息学、数据分析和日常开发中积累的常用函数与算法。项目强调 **“从零实现”** 以加深对底层原理的理解，同时保持代码的模块化与可复用性，致力于为 **“生物 + 计算”** 交叉方向的科研工作提供灵活的基础组件。

---
## 主要功能

###  生物信息学工具 (`bio_utils/`)
- **序列处理** (`sequence.py`)：支持 FASTA 文件的解析与格式化，包含 GC 含量计算、反向互补、窗口gc含量计算等常用操作。
- **序列比对** (`alignment.py`)：手动实现了经典的 **Needleman-Wunsch 全局比对算法**（支持自定义打分矩阵与空位罚分），深入理解动态规划在生物序列分析中的应用。
- **酶动力学** (`kinetics.py`)：包含米氏方程（Michaelis-Menten）及相关酶促反应动力学计算（还没完成，正在计划中）工具。

###  数据处理与统计 (`data_utils/`)
- **文件读写** (`io.py`)：提供统一的接口，支持多种格式（如 excel、CSV、TXT）的数据读取与写出。
- **统计工具** (`stats.py`)：包含平均值、方差、滑动窗口统计等基础数据分析函数。（计划中）

###  数学计算与可视化 (`math_utils/`)
- **代数运算** (`algebra.py`)：线性回归、皮尔逊相关系数及数值计算辅助函数。
- **绘图工具** (`plot.py`)：基于 Matplotlib 的简洁封装，用于快速绘制序列特征图、动力学曲线等。（计划中）

###  实用工具 (`misc_utils/`)
- **文件操作** (`file_ops.py`)：批量文件重命名、路径管理、目录创建等。
- **计时装饰器** (`timer.py`)：一个 Python 装饰器，用于函数运行耗时统计，方便代码性能调试。

***

## 安装

### 环境要求
- Python 3.8 或更高版本
- 推荐使用 Conda 或 venv 管理虚拟环境

***

### 从源码安装（开发模式）

```bash
git clone https://github.com/HanRan-cyber/Tools.git
cd Tools
pip install -e .
```

安装后即可在任意 Python 脚本中导入使用：

```python
from bio_utils import sequence
from bio_utils.alignment import needleman_wunsch
```

## 快速开始示例

```python
# 1. 读取 FASTA 文件
from bio_utils.sequence import read_fasta
seqs = read_fasta("data_test/single.fasta")
print(seqs.keys())

# 2. 计算 GC 含量
from bio_utils.sequence import gc_content
print(gc_content(seqs["gene1"]))

# 3. 双序列全局比对
from bio_utils.alignment import needleman_wunsch
seq1 = "ATCGTAGCTAG"
seq2 = "ATCGTAGCTAG"
score, aligned1, aligned2 = needleman_wunsch(seq1, seq2)
print(f"Alignment Score: {score}")

# 4. 统计运行时间（装饰器）
from misc_utils.timer import timer
@timer
def my_function():
    # do something
    pass
my_function()
```
***

## 项目结构

```text
Tools/
├── bio_utils/                  # 生物信息学核心工具
│   ├── __init__.py
│   ├── alignment.py            # 序列比对算法（Needleman-Wunsch）
│   ├── kinetics.py             # 酶动力学计算（米氏方程）
│   └── sequence.py             # 序列处理（FASTA 解析、GC 含量等）
├── data_utils/                 # 数据处理工具
│   ├── __init__.py
│   ├── io.py                   # 文件读写（FASTA / CSV / TXT）
│   └── stats.py                # 统计工具（均值、方差、滑动窗口）
├── math_utils/                 # 数学计算与可视化
│   ├── __init__.py
│   ├── algebra.py              # 基础数学统计运算
│   └── plot.py                 # 基于 Matplotlib 的绘图封装
├── misc_utils/                 # 杂项工具
│   ├── __init__.py
│   ├── file_ops.py             # 批量文件操作
│   └── timer.py                # 函数计时装饰器
├── data_test/                  # 测试数据（FASTA 文件）
│   ├── single.fasta
│   ├── multiple.fasta
│   └── complex.fasta
├── test.py                     # 基础功能测试（后续迁移至 pytest）
├── requirements.txt            # 项目依赖清单
├── setup.py                    # 安装配置文件
└── README.md                   # 项目说明文档
```
***
##  依赖

- **numpy** —— 数值计算与矩阵运算  
- **matplotlib** —— 数据可视化绘图  
- **biopython** —— 生物信息学标准库（用于对照验证）  

完整依赖清单详见 [`requirements.txt`](./requirements.txt)。
(其实还没有写)
---

##  贡献与反馈

本项目是我个人的学习与实践项目，主要用于本科阶段科研技能积累。  
欢迎通过 [Issue](../../issues) 提出建议或报告问题，也欢迎导师和师兄师姐给予指导与建议。  
（想多了，其实我不会有任何的悔改）
---

##  License

本项目采用 **MIT 许可证**，允许自由使用、修改与分发。

---

##  作者

**杨昊然** · 大连理工大学生物制造专业 2026 级  
 邮箱：[邮箱]  
 GitHub：[ GitHub 主页链接]
