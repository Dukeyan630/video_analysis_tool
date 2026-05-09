from pathlib import Path
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """读取Excel或者CSV文件 ，并返回 DataFrame"""
    path = Path(file_path)
    
    
    if not path.exists():
            raise FileNotFoundError(f"文件不存在：{file_path}")
    
    if path.suffix.lower() == ".xlsx":
          return pd.read_excel(path)
    if path.suffix.lower() == ".csv":
          return pd.read_csv(path)
    
    raise ValueError("暂时只支持.xlsx 或者 .csv 文件")
