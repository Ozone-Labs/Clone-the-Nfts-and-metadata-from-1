import json
import os
import shutil





def remove():
  o1=os.listdir("./")
  for i in o1:
    if i =='generated':
      shutil.rmtree('generated')
      print(o1)


def copying():
  f1=open("main.json","r+")
  f2=json.load(f1)




  f3=os.mkdir("generated")

  for i in range (0,10):
    f2["name"]=""+"Ozone labs #"+str(i)
    f2["image"]=""+str(i)+".png"
    f2["edition"]=i


  ####if you wants to change in another line you can simply do like it or contact on discord Web3developer#3984
    f2["attributes"][2]["display_type"]=str(i) 

    
    f3=open("generated/"+str(i)+".json","w")
    json.dump(f2,f3)

    shutil.copy("main.png","generated/"+ str(i)+".png")
    
    print(f3)



remove()
copying()
