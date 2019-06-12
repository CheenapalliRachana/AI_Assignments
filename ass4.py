import pandas as pd
data=[{'year':1990,'name':'alice','department':'HR','age':25,'salary':50000},
     {'year':1990,'name':'Bob','department':'RD','age':30,'salary':48000},
      {'year':1990,'name':'charlie','department':'Admin','age':45,'salary':55000},
      {'year':1991,'name':'alice','department':'HR','age':26,'salary':52000},
      {'year':1991,'name':'Bob','department':'RD','age':31,'salary':50000},
      {'year':1991,'name':'charlie','department':'Admin','age':46,'salary':60000},
      {'year':1992,'name':'alice','department':'HR','age':27,'salary':60000},
      {'year':1992,'name':'Bob','department':'RD','age':32,'salary':52000},
      {'year':1992,'name':'charlie','department':'Admin','age':28,'salary':62000}]
info=pd.DataFrame(data,index=[0,1,2,3,4,5,6,7,8])
print(info)
x=info.groupby(['year'])['salary'].sum()
print(x)
y=info.groupby(['name'])['salary'].sum()
print(y)
z=info.groupby(['year','department'])['salary'].sum()
print(z)
