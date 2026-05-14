import streamlit as st
import pandas as pd

from src.cleaner import clean_data
from src.analyzer import (get_basic_summary,get_platform_analysis,get_top_posts)
from src.report_generator import export_report
from pathlib import Path

st.title("短视频数据分析工具")

uploaded_file = st.file_uploader(
    "上传 Excel 或 CSV 文件",
    type = ["xlsx","csv"]
)

if uploaded_file is not None:
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    st.sidebar.header("筛选条件")
    preview_rows = st.sidebar.slider(
            "预览行数",
            min_value=5,
            max_value=50,
            value=10
        )
    cleaned_df = clean_data(df)
   
    platform_options = ["全部"]+ cleaned_df["平台"].dropna().unique().tolist()
    selected_platform = st.sidebar.selectbox(
        "选择平台",
        platform_options
    )

    content_options = ["全部"]+cleaned_df["内容类型"].dropna().unique().tolist()
    selected_content_type = st.sidebar.selectbox(
        "选择内容类型",
        content_options
    )



    st.subheader("原始数据预览")
    st.dataframe(df.head(preview_rows),hide_index= True)

    #过滤数据
    filtered_df = cleaned_df.copy()

    if selected_platform != "全部":
        filtered_df = filtered_df[filtered_df["平台"] == selected_platform ]

    if selected_content_type!= "全部":
        filtered_df = filtered_df[filtered_df["内容类型"] == selected_content_type ]    


    st.write(f"当前筛选后共有{len(filtered_df)}条数据")

    if filtered_df.empty:
        st.warning("当前筛选条件下没有数据")
    else:
    
        st.subheader("清洗后数据预览")
        st.dataframe(filtered_df.head(preview_rows),hide_index= True)


        platform_df = get_platform_analysis(filtered_df)
        st.subheader("平台分析")
        st.dataframe(platform_df.head(),hide_index= True)


        top_df = get_top_posts(filtered_df,top_n= 3).reset_index(drop= True)
        st.subheader("根据互动量排名前三分析")
        st.dataframe(top_df.head(),hide_index= True)
        
        summary = get_basic_summary(filtered_df)

    #用streamlit 做图
        if not platform_df.empty and "平台" in platform_df.columns and "平均互动量" in platform_df.columns:
            chart_df = platform_df.set_index("平台")["平均互动量"]

            st.subheader("各平台平均互动量图")
            st.bar_chart(chart_df)
        

        st.subheader("基础概览")
        col1, col2 , col3 = st.columns(3)
        col1.metric("总作品数",summary.get("总作品数",0))
        col2.metric("总播放量",int(summary.get("总播放量",0)))
        col3.metric("平均互动量",round(summary.get('平均互动量',0),2))
        col4, col5 , col6 = st.columns(3)
        col4.metric("总点赞数", int(summary.get("总点赞数", 0)))
        col5.metric("总收藏数", int (summary.get("总收藏",0)))
        col6.metric ("平均互动率",f"{summary.get("平均互动率",0):.2%}")
        st.write(summary)

         #一键生成报告
        if st.button("生成 Excel 分析报告"):
            export_report(filtered_df)
            st.success("报告生成完成,可以下载")
            report_path = Path("output/report.xlsx")

            with open(report_path,"rb")as f:
                st.download_button(
                    label="下载分析报告",
                    data=f,
                    file_name="another_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
else:
    st.info("请先上传一个 Excel 或 CSV 文件")