import pandas as pd

def generate_month_range(beginDate: str, endDate: str) -> list:
    '''
    Function: 输入'yyyy-mm-dd'格式的开始与结束日期，返回其间中每个月份起始日期的列表
    '''
    date_index = pd.date_range(beginDate, endDate)
    days = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in date_index.values]

    tmp = []
    for index , v in enumerate(days):
        if index == len(days)-1:
            tmp.append(days[index])
        if index == 0:
            tmp.append(days[0])
        else:
            _ = v.split('-')[2]
            if _ == '01':
                tmp.append(days[index-1])
                tmp.append(days[index])

    month_rng_list: list = []
    for i in range(len(tmp)//2):
        # out_str = str(tmp[i*2]) + ' 至 ' + str(tmp[i*2+1])
        month_rng_list.append([tmp[i * 2], tmp[i * 2 + 1]])

    return month_rng_list
