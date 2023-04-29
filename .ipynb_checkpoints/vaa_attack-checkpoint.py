import pandas as pd

stock_list = ['SPY 과거 데이터', 'EFA 과거 데이터', 'EEM 과거 데이터', 'AGG 과거 데이터',
              'LQD 과거 데이터', 'IEF 과거 데이터', 'SHY 과거 데이터'] # vaa 공격형 포트폴리오 구성에 사용할 종목 목록

def momentum_score(data):
    basic = data['종가'][0]
    return ((data['종가'][1]-basic)/basic)*12 + ((data['종가'][3]-basic)/basic)*4 + ((data['종가'][6] - basic)/basic)*2 + (data['종가'][12] - basic)/basic


result_vaa = {}
for i in stock_list:
    df = pd.read_csv('2023_03/'+i+'.csv')
    ticker = i[:3]
    score = momentum_score(df)
    result_vaa[ticker] = score

print(result_vaa)

"""
{'SPY': -0.800141674198197, 
'EFA': -1.0975950782997763, 
'EEM': -0.6201216421692868, 
'AGG': -0.3783621035728623, 
'LQD': -0.5837970988048529, 
'IEF': -0.5204802259887009, 
'SHY': -0.22772638753651425}
"""