import pandas as pd

stock_list = ['SPY 역사적 자료', 'EFA 역사적 자료', 'BIL 역사적 자료', 'AGG 역사적 자료']

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
    df = pd.read_csv('2023_01/' + i + '.csv')
    df['numeric'] = df['변동 %'].map(numeric)
    return_rate_ = return_rate(list(df['numeric']))
    result_original[i[:3]] = return_rate_

print(result_original)

"""
{'SPY': 0.8052933499889806, 
'EFA': 0.8343050632881822, 
'BIL': 1.0003965255946112, 
'AGG': 0.850188301014164}
"""