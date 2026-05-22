import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")
FILE_CSV = f"daily_market_activity_{today}.csv"


def daily_market_activity():

    df = ak.stock_market_activity_legu()
    d = dict(zip(df.T.values[0], df.T.values[1]))
    df = pd.DataFrame([d])
    
    # 2. 保存/更新 CSV
    try:
        old = pd.read_csv(FILE_CSV)
        # old["统计日期"] = pd.to_datetime(old["统计日期"])
        # df["统计日期"] = pd.to_datetime(df["统计日期"])
        df = pd.concat([old, df]).drop_duplicates(subset="统计日期")
    except FileNotFoundError:
        pass

    df.sort_values("统计日期", inplace=True)
    df.to_csv(FILE_CSV, index=False)

if __name__ == "__main__":
    daily_market_activity()
