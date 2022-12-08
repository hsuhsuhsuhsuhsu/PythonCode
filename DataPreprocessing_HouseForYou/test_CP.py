
import numpy as np
import statistics as st

    
def spearman (rank1,rank2):
    d2=0
    for a,b in zip(rank1,rank2):
        d2 = d2 + pow(a-b,2)       
    r = 1 - (6*d2)/(len(rank1)*(pow(len(rank1),2)-1))
    return r
    
def standard_add3 (data):
    std=st.stdev(data)
    mean=st.mean(data)
    stdData = []
    for i in data:
        stdData.append(((i-mean)/std)+3)
    return stdData

house = []
Total_equip = []
n=10
with open ("test4.csv","r",encoding = "big5") as f:
    for line in f :  
        row = []     
        temp = 0
        for word in line.split(","):
            if word == '0' :
                word = 0          
            elif word == '1':
                word = 1
                temp=temp+1
            elif word=='2':
                word=2
            
            elif word == '1\n':
                word = 1
                temp=temp+1
            elif word == "0\n":
                word = 0
            row.append(word)
        Total_equip.append(temp)
        house.append(row)

#算TF值
idf=[0]    
X = []
price=[]
size=[]
count = 1
for HouseNumber in house[1:]:     
    #print(HouseNumber)
    temp=[] 
    tf = []    
    size.append(float(HouseNumber[1]))
    price.append(int(HouseNumber[0]))
    for equip in HouseNumber[2:]:        
        temp.append(equip)
        tf.append(float(equip)/float(Total_equip[count]))
    print(temp)
    idf = np.asarray(idf) + np.asarray(temp)
    #print(row)
    #print("count= " ,count)
    #print(type(count))    
    count+=1
    X.append(tf)
IDF = []
for i in idf :
    if i != 0:
        IDF.append(np.log(n/i))
    else:        
        IDF.append(0)
PDF = np.exp(np.asarray(idf)/n)
TF=[0]
for row in range(len(X)):
    TF = np.asarray(TF)+np.asarray(X[row])

print("TF = " +str(TF))
print("沒標準化的PDF = " + str(PDF))
print("沒標準化的IDF = " + str(IDF))
#print(TF)
TFIDF = standard_add3(TF*IDF)
print("TFIDF = " + str(TF*IDF))
print("TFPDF = " + str(np.sqrt(TF)*PDF))
print()
print("=====標準化後====")
print()
TFPDF = standard_add3(np.sqrt(TF)*PDF)
size = standard_add3(size)
price = standard_add3(price)
print("TFIDF = "+str(TFIDF))
print("TFPDF = "+str(TFPDF))
print("坪數 = "+str(size))
print("價格 = "+str(price))
IDF2 = standard_add3(IDF)
PDF2 = standard_add3(PDF)

cp=[]
for HouseNumber in house[1:]:
    temp=0
    tempp=0
    current=0
    for equip in HouseNumber[2:]:
        if equip == 1:
            temp = temp + TFIDF[current]
            #temp = temp + TFPDF[current]
        elif equip == 0:
            tempp = tempp - TFPDF[current]
        elif equip == 2:
            continue
        #else:
            #print("wrong")
        current+=1
    print("TFIDF加總="+str(temp))
    print("TFPDF加總="+str(tempp))        
    cp.append(temp+tempp)

cp = (np.asarray(cp) + np.asarray(size))/np.asarray(price)
print("CP值 = "+str(cp))
'''
#相關係數可用10人平均排名嗎
goal= [2,9,1,10,5,7,4,6,3,8]#CP值算出來的排名(沒有美觀)
rank=[7,10,8,1,2,3,9,6,5,4]#7人平均排名
#7人各自排名
p1=[8,10,7,5,6,3,9,2,1,4]
p2=[8,10,7,3,2,1,4,5,6,9]
p3=[10,7,8,9,1,2,3,5,6,4]
p4=[7,1,3,2,10,9,8,4,6,5]
p5=[7,1,3,6,2,10,5,8,9,4]
p6=[10,7,8,2,6,9,1,3,4,5]
p7=[2,1,10,7,9,8,6,3,5,4]
team = [p1,p2,p3,p4,p5,p6,p7]
'''

elo=[2,3,5,1,4,6]
p21=[1,2,6,5,4,3]
p22=[1,5,3,2,6,4]
p23=[2,4,1,3,5,6]
p24=[1,5,4,2,3,6]
p25=[2,3,1,4,6,5]
p26=[2,3,6,1,4,5]
p27=[1,2,4,6,3,5]
woelorank=[1,4,5,2,3,6]
avgRANK=[1,3,4,2,5,6]
welorank=[2,3,5,1,4,6]
team1=[p21,p22,p23,p24,p25,p26,p27]

print("spearman : ")
a = []
for i in team1:              
    a.append(spearman(i,welorank)) 
    print(spearman(i,welorank))
print("goal Average = ",round(st.mean(a),4))      
  

print(spearman(avgRANK,welorank))
print("test for spearman",spearman(welorank,welorank))


