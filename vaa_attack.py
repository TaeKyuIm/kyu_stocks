import pandas as pd

stock_list = ['SPY 역사적 자료', 'EFA 역사적 자료', 'EEM 역사적 자료', 'AGG 역사적 자료',
              'LQD 역사적 자료', 'IEF 역사적 자료', 'SHY 역사적 자료'] # vaa 공격형 포트폴리오 구성에 사용할 종목 목록

def momentum_score(data):
    basic = data['종가'][0]
    return ((data['종가'][1]-basic)/basic)*12 + ((data['종가'][3]-basic)/basic)*4 + ((data['종가'][6] - basic)/basic)*2 + (data['종가'][12] - basic)/basic


result_vaa = {}
for i in stock_list:
    df = pd.read_csv('2022_11/'+i+'.csv')
    ticker = i[:3]
    score = momentum_score(df)
    result_vaa[ticker] = score

print(result_vaa)

"""
{'SPY': -0.36688787811000895, 
'EFA': -1.3569498649054341, 
'EEM': -0.4106433677521864, 
'AGG': 0.006017951856384318, 
'LQD': -0.3007330425907025, 
'IEF': 0.144475337246421, 
'SHY': 0.13597733711048238}
"""