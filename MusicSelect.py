### 選曲用関数

import random
import math

# テスト用
# 現在の時刻(開始時刻からの経過時間)
now = 54

from datetime import datetime

# テスト用
textTime = datetime.now()
textStartTime = 1571516344.799226

# timestampをunixtimeに変換
def timeChanger(textTime):
    return textTime.timestamp()

# 経過時間を演算
def ElapsedTime(now):
    return math.floor(timeChanger(textTime) - textStartTime)

# 時刻ごとの盛り上がり度の登録時の演算　（修正あり）
# 盛り上がり度 = 現在時刻でのbpmの平均　と考える
def GetExcitementForTime(now):  # 引数は現在の時刻(開始時刻からの経過時間)
    bpmSum = 0
    
    
    # UserIDごとに[bpm, bpm, bpm, ....]の形式で配列を生成　(修正)
    listDataOfMusicData = []

    # 時刻ごとのbpmの平均
    for data in listDataOfMusicData:
        bpmSum += data[1]
    bpmAverage = bpmSum / len(listDataOfMusicData)


    return [now, bpmAverage]

# 共分散
def GetCovariance(listData):
    averageX = 0
    averageY = 0
    for data in listData:
        averageX += data[0]
        averageY += data[1]

    averageX = averageX / len(listData)
    averageY = averageY / len(listData)

    covariance = 0

    for data in listData:
       covariance += (data[0] - averageX) * (data[1] - averageY)

    return covariance / len(listData) 

# 分散
def GetDispersion(listData):
    averageX = 0
    for data in listData:
        averageX += data[0]

    averageX = averageX / len(listData)

    dispersion = 0
    for data in listData:
        dispersion += (data[0] - averageX) * (data[0] - averageX)
    
    return dispersion / len(listData)

# 最小二乗法による回帰直線の傾きを演算　（修正あり）
def LeastSquareMethod(num):

    # excitementデータベースから取得した盛り上がり度データ(新しい順)
    excitementData = [[5, 100], [6, 80], [7, 90]]

    return GetCovariance(excitementData[:num]) / GetDispersion(excitementData[:num])

# print(LeastSquareMethod(5))

# 乱数
def RandomNumber(num):
    print(num)
    return random.randrange(num)

# 同じ系統の曲を抽出（論理積）
def musicSiftAnd(data, bpm, genre):
    musicData = data
    resultData = []
    for d in musicData:
        if d[1] == bpm and d[2] == genre:
            resultData.append(d)
    return resultData

# 同じ系統の曲を抽出（論理和）
def musicSiftOr(data, bpm, genre):
    musicData = data
    resultData = []
    for d in musicData:
        if d[1] == bpm or d[2] == genre:
            resultData.append(d)
    return resultData


# テスト用
nowMusicID = 100

# 選曲関数　(修正あり)
def SelectMusic(nowMusicID):    # 引数は現在の流れている曲のID
    # 引数のnowMusicIDから現在の曲のbpmを取得する
    musicData = [[222, 1, "free"], [100, 1, "free"], [333, 2, "hhh"], [4444, 3, "ggg"], [555, -1, "free"], [999, 3, "free"], [888, 2, ""]]
    nowMusicBpmType = 0
    nowMusicGenre = ""
    count = 0
    for data in musicData:
        if data[0] == nowMusicID:
            nowMusicBpmType = data[1]
            nowMusicGenre = data[2]
            musicData.pop(count)
        count += 1


    # 最近5回分のデータの傾向を演算
    inclination = LeastSquareMethod(5)

    # 次の曲のbpmを決定
    if nowMusicBpmType == 3:
        if inclination < 0:
            nowMusicBpmType -= 2
    elif nowMusicBpmType == -1:
        if inclination > 0:
            nowMusicBpmType += 1  
    else:
        if inclination > 0.5:
            nowMusicBpmType += 1
        elif inclination < 0.5:
            nowMusicBpmType -= 1 
    

    # musicデータベースからmusicBpmTypeとジャンルが一致するmusicDataのlist
    musicIdListOfMusicBpmType = musicSiftAnd(musicData ,nowMusicBpmType, nowMusicGenre)
    if len(musicIdListOfMusicBpmType) == 0:
        musicIdListOfMusicBpmType = musicSiftOr(musicData ,nowMusicBpmType, nowMusicGenre)
    return musicIdListOfMusicBpmType[RandomNumber(len(musicIdListOfMusicBpmType))][0]


print(SelectMusic(nowMusicID))



# -------------------------------------------------------------------------------
# 以下はいらなくなった関数たち


# # 基準値(大)を抽出
# def GetStandardMax(listData, i):
#     listSort = sorted(listData, reverse = True)
#     maxList = listSort[:i]
#     return sum(maxList) / len(maxList)

# # 平均値を出力
# def GetAverage(listData):
#     return sum(listData) / len(listData)

# # 個人の盛り上がり度を曲内で演算
# def GetExcitementPoint(listData):
#     i = 0
#     standard = GetStandardMin(listData, 5)
#     excitementPointList = []
#     while i < len(listData):
#         if listData[i] - standard > 10:
#             excitementPointList.append(i)
#         i += 1
    
#     return excitementPointList

# # 個人の盛り上がり度を1曲単位で演算
# def GetExcitementFull(listData):
#     standardMin = GetStandardMin(listData, 10)
#     standardMax = GetStandardMax(listData, 10)
#     average = GetAverage(listData)
#     return standardMax - standardMin + average

# # 全体の盛り上がり度を1曲単位で演算
# def GetExcitementFullAll(musicID):
    
#     excitementSum = 0
#     for data in listDataOfMusicData:
#         excitementSum += GetExcitementFull(data[1])
#     return [musicID, excitementSum / len(listDataOfMusicData)]

# # 曲のランキング
# musicRanking = []

# # 曲をランキングする関数
# def MusicRanking(musicID):
#     musicData = GetExcitementFullAll(musicID)
#     i = 0
#     while i < len(musicRanking):7
#         if musicRanking[i][1] < musicRanking[1]:
#             musicRanking.insert(i, musicData)
#             break
#         i += 1
#     if i == len(musicRanking): musicRanking.append(musicData)
#     if len(musicRanking) > 10: musicRanking.pop(10)





# マッチング用リスト追加関数
# def AscendingQuickSort(matchingList):

#     if len(matchingList) < 2: 
#         return matchingList
#     head = matchingList[0][1]
#     left = []
#     middle = []
#     right = []

#     for data in matchingList:
#         if data[1] < head: left.append(data)
#         elif data[1] == head: middle.append(data)
#         else: right.append(data)
    
#     return AscendingQuickSort(left) + middle + AscendingQuickSort(right)


# 変位抽出関数
# def DisplacementChanger(listData):
#     i = 0
#     displacementList = []
#     while i < len(listData) - 2:
#         displacementList.append(listData[i + 1] - listData[i])
#         i += 1
    
#     return displacementList

# displacementList1 = DisplacementChanger(test1)
# displacementList2 = DisplacementChanger(test2)

# print(displacementList1)
# print("\n")
# print(displacementList2)
# print("\n")


# def SelectMusic2(nowMusicID):
#     music = []
#     return music[RandomNumber(len(music))]