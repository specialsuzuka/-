import pandas as pd
df=pd.read_csv('data.csv',header=None,sep=',')
datelist=[]
for i in range(1,len(df[0])):
    if (eval(df[9][i])-eval(df[6][i]))/eval(df[6][i])>0.05:
        datelist.append(df[0][i])
print(datelist)




