# Data Preprocessing

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
# Importing the dataset
data = pd.read_csv('train.csv')
numberofcolumns=data.shape[1]


#Giving Average Rating for the reviews not present.
data['review_scores_rating']=data['review_scores_rating'].fillna(50)
#Squaring to add weightage
data['review_scores_rating']=data['review_scores_rating']**2
data['number_of_reviews']=data['number_of_reviews'].fillna(0)


data['thumbnail_url'] = data['thumbnail_url'].fillna('0')
data['description'] = data['description'].fillna('0')
data=data.iloc[:,2:]
data.to_csv('train_with_no_NaN.csv' , encoding="utf-8")
print("File Created :  train_with_no_NaN.csv ")

import CombiningColumns 
