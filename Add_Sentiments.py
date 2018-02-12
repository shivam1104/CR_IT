from aylienapiclient import textapi
import pandas as pd


nonsentimatedcolumn=12

data=pd.read_csv('train.csv')

nonsentimateddata=data.iloc[:,(nonsentimatedcolumn-1):nonsentimatedcolumn] #Non Sentimated Data

print(nonsentimateddata.shape[0])

sentimentedscore = pd.DataFrame(columns=['description_score'])





#client = textapi.Client("abbe6827", "c9c89b0e0063a21969964b33602cbb1b")
'''
for index,datasend in nonsentimateddata.iterrows():
	sentiment = client.Sentiment({'text': datasend})
	print(sentiment)
	#print(datasend['description'].encode("utf-8"))
	sentimentedscore.append({'description_score': sentiment}, ignore_index=True)


print ("Completed")
print(sentimentedscore[:,:])
'''
#+ sentimentedscore[:,:] 


newdataframe=(data.iloc[:,:nonsentimatedcolumn-1])
#newdatadrame=(pd.concat([newdatadrame, sentimentedscore], axis=1, join='inner'))
#newdatadrame=(pd.concat([newdataframe.iloc[:,:], data.iloc[:,(nonsentimatedcolumn+1):]], axis=1, join='inner'))
newdataframe.to_csv("Sentimented_Data.csv" ,encoding="utf-8")
print("Completed")

