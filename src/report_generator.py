import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path
rcParams["font.family"] = ["Arial Unicode MS"]
rcParams["axes.unicode_minus"] = False
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok= True)
from src.analyzer import(generate_platform_report,
                     generate_play_level_report,
                     generate_top_report,
                     diff_time_analysis)

def adjust_columns(worksheet):
    worksheet.freeze_panes = "A2"

    for column_cells in worksheet.columns:
        length = max(len(str(cell.value))if cell.value else 0
                     for cell in column_cells)
        worksheet.column_dimensions[
            column_cells[0].column_letter
        ].width = length + 5

    for cell in worksheet["K"]:
        cell.number_format = "0.00%"
#导出.xlsx
def export_report(df):
    with pd.ExcelWriter(OUTPUT_DIR/"report.xlsx") as writer:
        
        
        generate_platform_report(df).to_excel(
            writer,
            sheet_name="平台分析",
            index=False
        )
        adjust_columns(writer.sheets["平台分析"])
        generate_top_report(df).to_excel(
            writer,
            sheet_name="热门内容分析",
            index=False
        )
        adjust_columns(writer.sheets["热门内容分析"])
        diff_time_analysis(df).to_excel(
            writer,
            sheet_name="时段分析",
            index=False
        )
        adjust_columns(writer.sheets["时段分析"])

        generate_play_level_report(df).to_excel(
            writer,
            sheet_name="播放等级分析",
            index=False
        )
        adjust_columns(writer.sheets["播放等级分析"])
    print("报告已导出：output/report.xlsx")