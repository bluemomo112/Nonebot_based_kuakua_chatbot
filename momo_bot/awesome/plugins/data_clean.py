import os,json


datalist=[]

with open("kuakua.txt","r+",encoding="utf-8") as f:
    data=f.readlines()
    for line in data:
        text=json.loads(line)
        try:
            praise=text['replies'][0]["content"]
        except:
            pass
        datalist.append(praise)
        # break

with open("kuakua_clean.txt","w",encoding="utf-8") as f:
    f.write('\n'.join(datalist))

