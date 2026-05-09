# Video Analysis Tool

一个基于 Python + pandas + SQLite 的短视频数据分析工具。

支持：
- Excel/CSV 数据读取
- 数据清洗
- 数据聚合分析
- 自动生成图表
- SQLite 数据库存储
- 自动导出 Excel 分析报告




---

# 项目结构：
——video analysis
project/
|——main.py
|——loader.py
|——cleaner.py
|——analyzer.py
|——plotter.py
|——database.py
|——report_generator.py


## main.py

命令行入口。

负责：
* 接受用户输入文件
* 调用对应模块
* 输出想要结果


## loader.py

* 接收文件路径
* 判断路径名称
* 选择合适方法解析

## cleaner.py

负责：

* 删除空白行
* 去掉列名前空格
* 转换输入格式
* 新增列

## analyzer

负责：
* 分析数据
* 聚合数据


## plotter

负责：
* 绘制图像展示

## database

负责：
* 和sql数据库交互
* 保存到数据库
* 查询数据库

## report_generator
负责：
* 生成总结报告

# 安装

建议使用 Python 3.12

## 创建虚拟环境


```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 安装依赖

```bash
python -m pip install -U pip
python -m pip install pandas matplotlib
```

# 运行

## 运行命令行版本

```bash
python main.py
```

# 功能展示

![alt text](output/平台_播放量.png)