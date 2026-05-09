from loader import load_data
from cleaner import clean_data
from analyzer import (
    get_basic_summary,
    diy_table
)
from pathlib import Path
import pandas as pd
from database import save_to_sqlite,query_posts

from report_generator import export_report
from plotter import auto_create_plt




def main():
    NEW_EXCEL = Path("output")
    NEW_EXCEL.mkdir(exist_ok=True)
    file_path = "/Users/yanshoulong/Downloads/Code/video_analysis_project/data/test_project.xlsx"
    df = load_data(file_path)
    df = clean_data(df)

    #导入sql
    save_to_sqlite(df,"xiaohongshu_analysis.db","posts")

    print("数据清洗和字段补充完成")

    print("\n字段名:")
    print(df.columns.tolist())

    summary = get_basic_summary(df)
    print("====基础概览====")
    for key,value in summary.items():
        print(f"{key}: {value}")



    print("\n=====合并分析======")  
    diy_table(df,"平台","内容类型","总互动量","mean").to_excel(NEW_EXCEL/"new_result1.xlsx",index=False)


    #测试 generator
    auto_create_plt(df,"平台","播放量")
    export_report(df)

    #新建一个db，把处理好的excel文件，再次导入df，存入db
    report_sheets= pd.read_excel(NEW_EXCEL/"report.xlsx",sheet_name=None)
    for sheet_name,sheet_df in report_sheets.items():
        save_to_sqlite(sheet_df,"new_result.db",sheet_name)
    
    hudong_df_top_5 = query_posts("SELECT * FROM 热门内容分析 ORDER BY 互动率 DESC LIMIT 5","new_result.db")
    print(hudong_df_top_5)

if __name__ == "__main__":
    main()
