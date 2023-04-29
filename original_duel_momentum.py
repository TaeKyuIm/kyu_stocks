import pandas as pd

stock_list = ['SPY 과거 데이터', 'EFA 과거 데이터', 'BIL 과거 데이터', 'AGG 과거 데이터']

def numeric(percent):
    if percent[0] == '-':
        percent = percent.replace('-', '')
        return float(percent[:-1]) * -1
    else:
        return float(percent[:-1])


def return_rate(numeric_list):
    score = 1
    for i in range(12):
        score *= (100 + numeric_list[i]) / 100
    return score


result_original: dict[str, float] = {}

for i in stock_list:
    df = pd.read_csv('2023_03/' + i + '.csv')
    df['numeric'] = df['변동 %'].map(numeric)
    return_rate_ = return_rate(list(df['numeric']))
    result_original[i[:3]] = return_rate_

print(result_original)

"""
{'SPY': 0.9065199430821703, 
'EFA': 0.9717578047458261, 
'BIL': 1.0042006329027349, 
'AGG': 0.9303268592421526}
"""