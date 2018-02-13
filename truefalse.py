import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")
df.loc[:,'cleaning_fee'].replace([True,False],[1,0],inplace=True)
df['cleaning_fee'] = (1-df['cleaning_fee'])
#print (df.loc[:,'cleaning_fee'])

df.loc[:,'host_has_profile_pic'].replace(['t','f'],['1','0'],inplace=True)
#print(df.loc[:,'host_has_profile_pic'])

df.loc[:,'host_has_profile_pic'].replace(['t','f'],['1','0'],inplace=True)
#print(df.loc[:,'host_has_profile_pic'])
df.loc[:,'host_identity_verified'].replace(['t','f'],['1','0'],inplace=True)
#print(df.loc[:,'host_identity_verified'])
df.loc[:,'instant_bookable'].replace(['t','f'],['1','0'],inplace=True)
#print(df.loc[:,'instant_bookable'])
df.to_csv("test_tf.csv",encoding='utf-8')


