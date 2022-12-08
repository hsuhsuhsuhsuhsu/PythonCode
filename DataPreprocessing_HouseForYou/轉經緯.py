
import geocoder
import time
error=[]
#531

index=0
current=1
with open('工廠地址.csv','r',encoding='utf-8') as fin:
    with open('工廠經緯度.csv','w',encoding='utf-8') as fout:
        for row in fin:             
            #if count == current[index]:
            try:
                a,b = geocoder.arcgis(row.strip()).latlng
                print(row.strip())                
                print("{},{}".format(a,b),file=fout)
            except:        
                print("-----Error occurs-----")
                time.sleep(5)
                print(time.ctime())
                try:
                    a,b = geocoder.arcgis(row.strip()).latlng
                    print(row.strip())                
                    print("{},{}".format(a,b),file=fout)
                except:
                    print("Delay 5s , Error still alive")
                    print("Occurs error in "+str(current))                
                    print("{},{}".format(" "," "),file=fout)
                    error.append(current)  
            #index+=1
            current+=1