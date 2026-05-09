import pandas as pd

def get_basic_summary(df: pd.DataFrame) -> dict:
    summary = {}

    summary["总作品数"] = len(df)
    summary["总点赞数"] = df["点赞"].sum() if "点赞" in df.columns else 0
    summary["总收藏"] = df["收藏"].sum() if "收藏" in df.columns else 0
    summary["总评论"] = df["评论"].sum() if "评论" in df.columns else 0
    summary["总分享"] = df["分享"].sum() if "分享" in df.columns else 0
    summary["总播放量"] = df["播放量"].sum() if "播放量" in df.columns else 0
    summary["平均互动量"] = df["总互动量"].mean() if "总互动量" in df.columns else 0
    summary["平均互动率"] = df["互动率"].mean() if "互动率" in df.columns else 0

    return summary

def get_top_posts(df: pd.DataFrame , top_n : int = 5) -> pd.DataFrame:
    if "总互动量" not in df.columns:
        return pd.DataFrame()
    
    cols = ["标题", "平台", "总互动量", "互动率", "播放量", "发布时间段"]
    existing_cols = [col for col in cols if col in df.columns]

    return df.sort_values(by= "总互动量",ascending= False)[existing_cols].head(top_n)

def get_platform_analysis(df: pd.DataFrame) -> pd.DataFrame:
    if "平台" not in df.columns or "总互动量" not in df.columns:
        return pd.DataFrame()
    

    result = df.groupby("平台").agg(
        作品数=("平台", "count"),
        平均互动量=("总互动量", "mean"),
        总点赞=("点赞", "sum"),
        总收藏=("收藏", "sum"),
        总评论=("评论", "sum"),
        总分享=("分享", "sum"),
    )

    return result.reset_index()

def get_platform_analysis_from_bofang(df : pd.DataFrame) -> pd.DataFrame:
    if "平台" not in df.columns or "播放量" not in df.columns:
        return pd.DataFrame() 
    
    result = df.groupby("平台").agg(
        平均总播放量=("播放量","mean"),
        内容类型 = ("内容类型","count")
    )

    return result.reset_index()

def get_time_period_analysis(df: pd.DataFrame) -> pd.DataFrame:
    if "发布时间段" not in df.columns or "总互动量" not in df.columns:
        return pd.DataFrame()
    

    result = df.groupby("发布时间段").agg(
        作品数=("发布时间段", "count"),
        平均互动量=("总互动量", "mean"),
        平均互动率=("互动率", "mean"),
    )

    return result.reset_index()




#筛选函数
def get_douyin_video(df: pd.DataFrame):
    """ 只保留抖音
        只保留视频
    返回标题、播放量、总互动量"""
    #方法一：普通筛选
    # result = df[(df["平台"]=="抖音")&
    #             (df["内容类型"]=='视频')]
   

    #方法二：使用.query
    result = df.query("平台 == '抖音' and 内容类型 == '视频'" )

    #方法三：使用.isin()
    # result = df[df["平台"].isin(["抖音"])
    #    & df["内容类型"].isin(["视频"])]


    required_cols = ["标题","播放量","总互动量"]
    if all(col in result.columns for col in required_cols):
        return result[required_cols].sort_values(by="总互动量",ascending=False).head(3)

def get_high_play_posts(df :pd.DataFrame):
    """只保留播放量 > 10000
    返回标题、平台、播放量"""
    #方法1:
    # result = df[df["播放量"] >= 10000]

    #方法2:
    result = df.query("播放量 >= 10000")
    required_cols = ["标题","播放量","平台","互动率"]
    if all(col in result.columns for col in required_cols):
        return result[required_cols].sort_values(by="互动率",ascending=False).head(5)
    
def analyze_play_level(df: pd.DataFrame):
    if "播放等级" not in df.columns:
        return pd.DataFrame()
    
    result = df.groupby("播放等级").agg(
        个数 = ("播放等级","count"),
        平均播放量 =("播放量","mean"),
        平均互动量 = ("总互动量","mean")
    ).reset_index()
    return result
    
def get_hot_xiaohongshu_posts(df : pd.DataFrame):
    if "平台" not in df.columns or "互动等级" not in df.columns:
        return pd.DataFrame()
    
    
    result = df.query("平台 == '小红书' and 互动等级 in ['热门','爆款']")

    existing_cols = ["标题","平台","总互动量","互动等级"]
    if all(col in result.columns for col in existing_cols):
        return result[existing_cols].sort_values(by="总互动量",ascending=False).head(5)

def get_high_play_video_posts(df: pd.DataFrame):
    if "内容类型" not in df.columns or "播放等级" not in df.columns:
        return pd.DataFrame()
    
    result = df[(df["内容类型"] == "视频") & (df["播放等级"] == "高")]

    existing_cols = ["标题","平台","播放量","互动率","播放等级"]
    if all(col in result.columns for col in existing_cols):
        return result[existing_cols].sort_values(by="互动率",ascending=False).head(5)
    

def analyze_interaction_level(df: pd.DataFrame):
    if "互动等级" not in df.columns:
        return pd.DataFrame()
    
    result = df.groupby("互动等级").agg(
        个数 = ("互动等级","count"),
        平均播放量 = ("播放量","mean"),
        平均互动量 = ("总互动量","mean"),
    ).reset_index()

    return result


#平台分析
def generate_platform_report(df: pd.DataFrame):
    if "平台" not in df.columns:
        return pd.DataFrame()
    result = df.groupby("平台").agg(
        平均播放量 = ("播放量","mean"),
        平均互动量 = ("总互动量","mean"),
        作品数 = ("平台","count")
    ).reset_index()
    return result



#热门内容Top 10
def generate_top_report(df: pd.DataFrame,top_N = 10):
    #根据总互动量判定前十内容
    if "总互动量" not in df.columns:
        return pd.DataFrame()
    
    result  = df.sort_values(by="总互动量",ascending=False).head(top_N)
    return result


#不同时段分析
def diff_time_analysis(df: pd.DataFrame):
   required_cols = ["发布时间段","播放量","总互动量"]
   if not all (col in df.columns for col in required_cols):
       return pd.DataFrame()
   
   result = df.groupby("发布时间段").agg(
        作品数 = ("发布时间段","count"),
        平均播放量 = ("播放量","mean"),
        平均互动量 = ("总互动量","mean")    
   ).sort_values(by="平均互动量",ascending=False).reset_index()

   return result


#播放等级分析
def generate_play_level_report(df: pd.DataFrame):
    required_cols = ["播放等级","播放量","总互动量"]
    if not all (col in df.columns for col in required_cols):
       return pd.DataFrame()
    
    result = df.groupby("播放等级").agg(
        作品数 = ("播放等级","count"),
        平均播放量 = ("播放量","mean"),
        平均互动量 = ("总互动量","mean")   
    ).reset_index()

    return result

def diy_table(df: pd.DataFrame,index: str,columns: str,values: str,aggfunc:str)->pd.DataFrame:
    required_cols = [index,columns,values]
    if not all(col in df.columns for col in required_cols):
        return pd.DataFrame()
    result = df.pivot_table(
        index = index,
        columns = columns,
        values = values,
        aggfunc = aggfunc
    ).reset_index()
    return result