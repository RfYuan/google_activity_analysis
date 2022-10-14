from utils import  *
import pandas as pd
from datetime import  datetime,timedelta

def read_from_csv(path):
    data = pd.read_csv(path)
    # Ignore timezone cause we are looking at larger scope
    data['TIME']=pd.to_datetime(data['TIME'])
    data['date']=data['TIME'].dt.date
    print(data.info())
    data.drop('TIME', inplace=True, axis = 1 )
    # print(data.head())

    return data

def get_one_week_data(df, start_date):
    start_date_obj = datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date_obj = start_date_obj+ timedelta(days=7)

    filtered_date = df.loc[(df['date']>=start_date_obj )&(df['date']<end_date_obj)]
    return filtered_date



if __name__ == "__main__":
    df = read_from_csv(SEARCH_ACTIVITY_CSV_PATH)
    filter_df = get_one_week_data(df,"2020-12-01")
    print(filter_df.head())