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
project/src
    |——main.py
    |——loader.py
    |——cleaner.py
    |——analyzer.py
    |——plotter.py
    |——database.py
    |——report_generator.py
app

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
python -m pip install -r requirements.txt
```

# 运行

## 运行命令行版本

```bash
python main.py
```

## 运行网页版本
```bash
python3 -m streamlit run app.py

# 功能展示

![alt text](output/平台_播放量.png)


# 输入数据字段

示例数据需要包含以下字段：
｜字段名｜说明｜
｜----｜----｜
｜标题｜内容标题｜
｜平台｜抖音 / 小红书 /快手等｜
｜内容类型 | 视频 / 图文 |
| 点赞 | 点赞数量 |
| 收藏 | 收藏数量 |
| 评论 | 评论数量 |
| 分享 | 分享数量 |
| 播放量 | 内容播放量 |
| 发布时间 | 发布时间 |

## 项目亮点

- 使用pandas对短视频数据进行清洗、字段加工和聚合分析
- 支持自动生成总互动量、互动率、播放等级、互动等级等分析字段
- 使用matplotlib 自动生成图表
- 使用SQLite 保存清洗后的数据，并支持 SQL 查询
- 使用openpyxl 优化 Excel报告，包括多 sheet、冻结首行、自动列宽
- 使用 argparse 支持命令行传入数据文件