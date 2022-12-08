
import numpy as np
import pandas as pd

#UTF-8編碼格式csv檔案資料讀取
f = open('商店.csv')
df = pd.read_csv(f,header=None)
df.columns=["Col1","Col2"]#命名行名稱
X = df[["Col1","Col2"]] #抽取前兩列作為訓練資料的各屬性值
facility = np.array(X)
#print("----------------facility-----------------")
#print (facility)

f2 = open('已刪圖的內部 - 經緯度1401-2941.csv')
df2 = pd.read_csv(f2,header=None)
df2.columns=["Col1","Col2"]
hou = df2[["Col1","Col2"]] #抽取前兩列作為訓練資料的各屬性值
house = np.array(hou)
#print("----------------house--------------------")
#print (house)

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2): # 經度1,緯度1,經度2,緯度2 (十進位制度數) 
#Calculate the great circle distance between two points on the earth (specified in decimal degrees) 
#將十進位制度數轉化為弧度 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) # haversine公式 
    dlon = lon2 - lon1#經度
    dlat = lat2 - lat1#緯度
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 # haversine公式 
    c = asin(sqrt(a)) 
    r = 6371 # 地球平均半徑,單位為公里 
    return (2 * r *c * 1000) #公尺

count=0
number=""
Total=0
Toprt=""
with open('商店距離2.csv','w') as distance:
    for i in range(0,len(df2)):#租房
        Total=0
        for j in range(0,len(df)):#外部因素
            dis=haversine(house[i][1],house[i][0],facility[j][1],facility[j][0]) #經[i,1]緯[i,0]
            #print(dis)
            print("{}".format(dis),file=distance)
            if dis<= ((4.2*1000/60) *20): #在附近(20分鐘距離以內)(交通每小時公里數*1000/60分鐘*允許時間(min))
                count=count+1
                number=number+"第"+str(i+701)+"租屋點"+"與第"+str(j+1)+"個因素點"+"距離"+str(round(dis,2))+"公尺"+'\n'
                Total=Total+1                    
        print('第'+str(i+1401)+'間:'+str(Total))#各間符合條件全部數量
        Toprt=Toprt+'第'+str(i+1401)+'間:'+str(Total)+'\n'
    print('\n'+'符合條件'+'\n'+str(number))#與各間符合外部因素距離
    print('全部符合條件:'+str(count)+"個")
    
    with open('商店符合條件2.csv','w') as final:
        print("{}{}{}".format(Toprt,'\n',number),file=final)
    

    
                
            