from aylienapiclient import textapi
import pandas as pd
#from textprocessingdotcom import SentimentProcessor
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nonsentimentedcolumn=12

data=pd.read_csv('train.csv')

nonsentimateddata=data.iloc[:,(nonsentimentedcolumn-1):nonsentimentedcolumn] #Non Sentimated Data

#print(nonsentimateddata.shape[0])

sentimentedscore = pd.DataFrame(columns=['description_score'])


counter=0
#Attempt 3 
Analyzer = SentimentIntensityAnalyzer()
#nltk.download()
for index,datasend in nonsentimateddata.iterrows():
		counter+=1
		print("Calling API ..... " + str(counter))
		sentiment = Analyzer.polarity_scores(datasend)
		print(sentiment)
		#print(datasend['description'].encode("utf-8"))
		sentimentedscore.append({'description_score': '{0}: {1}, '.format(k, ss[k])})



print ("Completed calling API - In finally right now")
#print(sentimentedscore[:,:])
dataafterdesc=data.iloc[:,nonsentimentedcolumn:]
newdataframe=(data.iloc[:,:nonsentimentedcolumn-1])
newdataFrame=(pd.concat([newdataframe, sentimentedscore], axis=1))
newdataframe=(pd.concat([newdataframe, dataafterdesc], axis=1))
newdataframe.to_csv("Sentimented_Data.csv" ,encoding="utf-8")
print("Completed")

'''
#for sentence in sentences:
     #print(sentence)
     ss = Analyzer.polarity_scores(sentence)
     for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
'''     



#Attempt 2 
'''
processor = SentimentProcessor()

text = "Please kill me now"
print(processor.process(text))

'''

#Attempt 1 
'''
client = textapi.Client("abbe6827", "c9c89b0e0063a21969964b33602cbb1b")
counter=-1
try:
	for index,datasend in nonsentimateddata.iterrows():
		counter+=1
		print("Calling API ..... " + str(counter))
		sentiment = client.Sentiment({'text': datasend})
		#print(sentiment)
		#print(datasend['description'].encode("utf-8"))
		sentimentedscore.append({'description_score': sentiment}, ignore_index=True)

except IOError:
	print("IO ERROR")

finally:
	print ("Completed calling API - In finally right now")
	#print(sentimentedscore[:,:])
	dataafterdesc=data.iloc[:,nonsentimentedcolumn:]
	newdataframe=(data.iloc[:,:nonsentimentedcolumn-1])
	newdataFrame=(pd.concat([newdataframe, sentimentedscore], axis=1))
	newdataframe=(pd.concat([newdataframe, dataafterdesc], axis=1))
	newdataframe.to_csv("Sentimented_Data.csv" ,encoding="utf-8")
	print("Completed")
'''


'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from textprocessingdotcom import SentimentProcessor

processor = SentimentProcessor()

text = "It helps me saving money"
print(processor.process(text))
'''