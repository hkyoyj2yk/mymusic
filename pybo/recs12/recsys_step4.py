import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
import warnings
warnings.filterwarnings('ignore')
from model import AE2
from recsys_step1 import recsys_step1
from recsys_step2 import recsys_step2
from recsys_step3 import recsys_step3

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def reco(emotion_list,data):
    if emotion_list[0] == max(emotion_list):  #기쁨
        em1_idx = data[data['emotion max'].str.contains('행복한')].index.to_list()  # 기쁨일 경우 행복한과 경쾌한을 max_tag로 가진 노래를 선택 
        em2_idx = data[data['emotion max'].str.contains('경쾌한')].index.to_list()
        em3_idx = list(set(em1_idx + em2_idx))
       

        rec_data = data.iloc[em3_idx].iloc[:5]  #5개를 먼저 추천 (fin_score 기준)
        idx = list(data.index)
        score=[]
        for i in rec_data['곡 제목']:
            score.append(input(f'{i}의 점수를 입력해주세요! (5점 만점) ', ))  # 사용자에게 곡에 대한 점수를 5점 척도로 받는다.
        rec_data['score']= score
        mx = rec_data[rec_data['score']==max(score)].index.to_list()
        max_ems = [[data['우울한'][i], data['울고싶은'][i], data['긴장되는'][i],data['무서운'][i],data['잔잔한'][i],data['행복한'][i],data['경쾌한'][i],data['편안한'][i]] for i in mx]
        ems = [[data['우울한'][i], data['울고싶은'][i], data['긴장되는'][i],data['무서운'][i],data['잔잔한'][i],data['행복한'][i],data['경쾌한'][i],data['편안한'][i]] for i in idx]

        data['cos']=0
        for n in range(len(mx)):            
            cos = pd.Series([cos_sim(ems[i], max_ems[n]) for i in range(len(data))])  # 사용자가 가장 높은 점수를 준 곡의 8가지 감정을 기준으로 코사인 유사도를 구한다. 
            cos.index = idx
            data['cos']+=cos
            print(f'{n}번째 코사인 유사도 계산완료')

        data = data[5:]  # 현재 추천한 5곡을 제외하여 데이터 다시 설정 
        data = data.sort_values(by='cos', ascending = False)  # 계산한 코사인 유사도를 기준으로 정렬처리 
        # print(data.head())
        return data

    elif emotion_list[1] == max(emotion_list): # 분노 
        em1_idx = data[data['emotion max'].str.contains('긴장되는')].index.to_list()  # 감정에 충실한 데이터셋
        em2_idx = data[data['emotion max'].str.contains('경쾌한')].index.to_list()  # 감정과 반대되는 데이터셋 

        rec_data_s = data.iloc[em1_idx]
        rec_data_d = data.iloc[em2_idx]

        s = rec_data_s.iloc[0]   
        d = rec_data_d.iloc[0]
        c = pd.concat([s,d])
        # ex = [i for i in c.index.to_list()]

        name = list(c['곡 제목'])

        score=[]
        for n,i in enumerate(name):
            print(f'{n+1}번:{i}')
        result = int(input('더 맘에 드는 노래 번호를 입력해주세요'))
        dataset = ''

        # data.drop(index=ex)
        if result == 1:  # 사용자가 감정에 충실한 노래를 선택
            dataset = data.iloc[em1_idx]
            print('긴장되는 노래 선택 dataset = 긴장되는')
        elif result ==2: #사용자가 감정에 반대되는 노래를 선택
            dataset = data.iloc[em2_idx] 
            print('경쾌한 노래 선택 dataset = 경쾌한')
        else:
            print('1 또는 2를 입력하세요!')

        return dataset



    else: # 분노 
        em1_idx = data[data['emotion max'].str.contains('우울한')].index.to_list()  # 감정에 충실한 데이터셋
        em2_idx = data[data['emotion max'].str.contains('울고싶은')].index.to_list()  
        em12_idx = list(set(em1_idx + em2_idx))

        em3_idx = data[data['emotion max'].str.contains('편안한')].index.to_list()  # 감정과 반전되는 데이터셋
        em4_idx = data[data['emotion max'].str.contains('잔잔한')].index.to_list() 
        em34_idx = list(set(em3_idx + em4_idx))


        rec_data_s = data.iloc[em12_idx]
        rec_data_d = data.iloc[em34_idx]

        s = rec_data_s.iloc[0]   
        d = rec_data_d.iloc[0]
        c = pd.concat([s,d])
        # ex = [i for i in c.index.to_list()]

        name = list(c['곡 제목'])

        score=[]
        for n,i in enumerate(name):
            print(f'{n+1}번:{i}')
        result = int(input('더 맘에 드는 노래 번호를 입력해주세요'))
        dataset = ''

        # data.drop(index=ex)
        if result == 1:  # 사용자가 감정에 충실한 노래를 선택
            dataset = data.iloc[em1_idx]
            print('우울한, 울고싶은 노래 선택 dataset = 우울한, 울고싶은')
        elif result ==2: #사용자가 감정에 반대되는 노래를 선택
            dataset = data.iloc[em2_idx] 
            print('편안한, 잔잔한 노래 선택 dataset = 편안한, 잔잔한')
        else:
            print('1 또는 2를 입력하세요!')

        return dataset


def reco2(data):  # 두번째 추천 
    rec_data = data.iloc[:5]

    idx = list(data.index)
    score=[]
    for i in rec_data['곡 제목']:
        score.append(input(f'{i}의 점수를 입력해주세요! (5점 만점) ', ))  # 사용자에게 곡에 대한 점수를 5점 척도로 받는다.
    rec_data['score'] = score
    mx = rec_data[rec_data['score']==max(score)].index.to_list()
    max_ems = [[data['우울한'][i], data['울고싶은'][i], data['긴장되는'][i],data['무서운'][i],data['잔잔한'][i],data['행복한'][i],data['경쾌한'][i],data['편안한'][i]] for i in mx]
    ems = [[data['우울한'][i], data['울고싶은'][i], data['긴장되는'][i],data['무서운'][i],data['잔잔한'][i],data['행복한'][i],data['경쾌한'][i],data['편안한'][i]] for i in idx]

    data['cos']=0
    for n in range(len(mx)):      # 가장 높은 점수를 준 노래의 8가지 감정값을 기준으로 코사인 유사도를 계산한다. 
        cos = pd.Series([cos_sim(ems[i], max_ems[n]) for i in range(len(data))])
        cos.index = idx
        data['cos']+=cos
        print(f'{n}번째 코사인 유사도 계산완료')

    data = data[5:]
    data = data.sort_values(by='cos', ascending = False)
    # print(data.head())

    a = int(input('추천 계속 = 1, 추천 멈추기 = 0',))  # 0입력시 추천 종료
    # mx = rec_data.index(max(score))
    data = data[5:]
    if a == 0:
        return
    else:
        reco2(data)

      
def recsys_step4(emotion_list, text, weights):
    recsys_step3(emotion_list, text, weights)
    data = pd.read_csv('recys_step3_result.csv')  
    data = data.drop_duplicates(['song id'],keep='first')
    data = data.reset_index()
    data = data.drop(['index'],axis = 1)
    rec_data = reco(emotion_list, data)
    rec2_data = reco2(rec_data)
    return rec2_data
        
# 여기서 시작함
# 가사랑 감정 선택하는 거 만들어야함
# nlp 모델은 고정해놓았고 모델 받으면 결과값 넣으면 됨. 
if __name__ == "__main__":
    print('글을 입력해주세요!')
    # 오늘 하루 너무 힘들었다. 과제랑 공부, 할 일들은 많은데 뜻대로 되지 않았다. 공허한 느낌이 들고 어지러웠다.
    text = input()
    print('노래 추천을 받을 때 감정과 가사의 중요도를 알려주세요. ex:"0.3 0.7"')
    weights = list(map(float, input().split()))
    emotion_list = [0.1, 0.88, 0.02]
    print(recsys_step4(emotion_list,text,weights))
    
    