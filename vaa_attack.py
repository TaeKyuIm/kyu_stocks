import pandas as pd

stock_list = ['SPY 역사적 자료', 'EFA 역사적 자료', 'EEM 역사적 자료', 'AGG 역사적 자료',
              'LQD 역사적 자료', 'IEF 역사적 자료', 'SHY 역사적 자료'] # vaa 공격형 포트폴리오 구성에 사용할 종목 목록

def momentum_score(data):
    basic = data['종가'][0]
    return ((data['종가'][1]-basic)/basic)*12 + ((data['종가'][3]-basic)/basic)*4 + ((data['종가'][6] - basic)/basic)*2 + (data['종가'][12] - basic)/basic


result_vaa = {}
for i in stock_list:
    df = pd.read_csv('2023_02/'+i+'.csv')
    ticker = i[:3]
    score = momentum_score(df)
    result_vaa[ticker] = score

print(result_vaa)

"""
{'SPY': 0.5211982031999203, 
'EFA': 0.08723864455659835, 
'EEM': 1.4025634318597977, 
'AGG': 0.6031240365841122, 
'LQD': 0.8717900302114806, 
'IEF': 0.788638262322471, 
'SHY': 0.21743425114211737}
"""