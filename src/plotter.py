from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
rcParams["font.family"] = ["Arial Unicode MS"]
rcParams["axes.unicode_minus"] = False

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok= True)

def plot_platform_post_count(df: pd.DataFrame):
    """平台数据柱状图"""
    if "平台" not in df.columns:
        return 
    
    result = df["平台"].value_counts()

    plt.figure(figsize=(8, 5))
    result.plot(kind= "bar")

    plt.title("各平台作品数")
    plt.xlabel("平台")
    plt.ylabel("作品数")
    plt.tight_layout()

    save_path = OUTPUT_DIR/ "platform_post_count.png"
    plt.savefig(save_path)
    plt.close()

    print(f"已保存图表：{save_path}")

#个人练习：1.生成一个横向柱状图
def platform_horizontal_plot(df: pd.DataFrame):
    result = df.groupby("平台")["总互动量"].sum()

    plt.figure(figsize=(8, 5))
    #数值显示
    ax = result.plot(kind= "barh")
    for i, value in enumerate(result):
        ax.text(value,i,str(value),ha="right",va="center")

    plt.title("各平台互动量")
    plt.xlabel("互动量")
    plt.ylabel("平台")
    plt.tight_layout()
    save_path = OUTPUT_DIR/"platform_horizontal_plot(with num).png"
    plt.savefig(save_path)
    plt.close()
    print(f"已保存图表：{save_path}")

    #2.排序后的柱状图
def sorted_plot(df: pd.DataFrame):
    result = df.groupby("平台")["播放量"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    result.plot(kind="bar")
    plt.title("各平台播放量")
    plt.xlabel("平台")
    plt.ylabel("总播放量")
    plt.tight_layout()

    save_path = OUTPUT_DIR/"sorted_plot.png"
    plt.savefig(save_path)
    plt.close()
    print(f"已保存图表：{save_path}")

    #生成一个饼状图
def creat_a_pie(df :pd.DataFrame):
    result = df["平台"].value_counts()
    plt.figure(figsize=(8,5))
    result.plot(kind="pie", autopct="%1.1f%%")
    plt.title("各平台作品数占比")
    plt.ylabel("")
    plt.tight_layout()

    save_path = OUTPUT_DIR/"pie1.png"
    plt.savefig(save_path)
    plt.close()
    print(f"已保存图表：{save_path}")

    #不同时间段的平均折线图
def dif_time_line_plt(df :pd.DataFrame):
    if "发布时间段" not in df.columns or "播放量" not in df.columns:
        return
    
    result = df.groupby("发布时间段")["播放量"].mean()
    order = ["深夜", "早上", "下午", "晚上"]
    result = result.reindex(order)

    plt.figure(figsize=(8,5))
    result.plot(kind="line",marker="o")

    
    plt.title("不同时间段折线图")
    plt.xlabel("时间段")
    plt.ylabel("平均播放量")

    plt.tight_layout()
    save_path = OUTPUT_DIR/"dif_time_line_plt.png"
    plt.savefig(save_path)
    plt.close()

#堆叠柱状图
def stacked_bar(df: pd.DataFrame):
    pivot_df = df.pivot_table(
        index="平台",
        columns="内容类型",
        values="标题",
        aggfunc="count" 
    ).fillna(0)
    plt.figure(figsize=(8,5))
    pivot_df.plot(kind="bar",stacked=True)   
    
    plt.title("各平台平均互动量堆叠图")
    plt.xlabel("平台")
    plt.ylabel("内容类型")
    plt.tight_layout()

    save_path = OUTPUT_DIR/"stacked_bar"
    plt.savefig(save_path)
    plt.close()

def auto_create_plt(df: pd.DataFrame, row: str,column: str):
    if row not in df.columns or column not in df.columns:
        return 
    result = df.groupby(row)[column].mean()
    plt.figure(figsize= (8,5))
    result.plot(kind= "bar")

    plt.title(f'各{row}的平均{column}柱状图')
    plt.xlabel(row)
    plt.ylabel(column)

    plt.tight_layout()
    save_path = OUTPUT_DIR / f"{row}_{column}.png"
    plt.savefig(save_path)
    plt.close()



