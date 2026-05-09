import pandas as pd

def clean_data(df : pd.DataFrame) -> pd.DataFrame:
    """清洗数据"""
    #去掉完全空白的行
    df = df.dropna(how="all")

    #去掉列名前后的空格
    df.columns = df.columns.str.strip()

    #需要转成数字的列
    numeric_columns = ["点赞","收藏","评论","分享","播放量"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col],errors="coerce").fillna(0)


    #发布时间转日期格式
    if "发布时间" in df.columns:
        df["发布时间"] = pd.to_datetime(df["发布时间"],errors="coerce")


    #新增总互动量
    required_cols = ["点赞","收藏","评论","分享"]
    if all(col in df.columns for col in required_cols):
        df["总互动量"] = df["点赞"]+df["收藏"]+df["评论"]+df["分享"]

    #增加互动率
    if "总互动量" in df.columns and "播放量" in df.columns:
        df["互动率"] = df["总互动量"] / df["播放量"].replace(0, pd.NA)
    
    #增加播放量等级
    if "播放量" in df.columns:
        df["播放等级"] = df["播放量"].apply(
            lambda x:
            "低" if x < 5000
            else "中" if x < 20000
            else "高" 
        )

    #增加互动等级
    if "总互动量" in df.columns:
        df["互动等级"] = df["总互动量"].apply(
            lambda x:
            "普通" if x < 1000
            else "热门" if x < 5000
            else "爆款"
        )

    #新增发布时间小时
    if "发布时间" in df.columns:
        df["发布时间段"] = df["发布时间"].dt.hour

        def get_time_period(hour):
            if pd.isna(hour):
                return "未知"
            if 6 <= hour < 12:
                return "早上"
            elif 12 <= hour < 18:
                return "下午"
            elif 18 <= hour < 24:
                return "晚上"
            else:
                return "深夜"
            
        df["发布时间段"] = df["发布时间段"].apply(get_time_period)
    return df