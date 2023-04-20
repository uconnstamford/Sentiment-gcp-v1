from google.cloud import language
from google.cloud import language_v1
import six
import pandas as pd

# for python3
import sys


data = pd.read_excel("solar-city.xlsx")

data.columns = ['text']

def analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}, Magnitude: {}".format(sentiment.score, sentiment.magnitude))
    #print("Magnitude: {}".format(sentiment.magnitude))

print(data.shape)

with open('sentiment-out.txt', 'w') as sys.stdout:
    for x in range(32):
        val = data.loc[x].at['text']  #stores the data at that point in val
        print(val)
        analyze_sentiment(val)
        print('\n')   

#f= open("sentiment-out.txt","w+")
#for x in range(1,32):
#    val = data.loc[x].at['text']  #stores the data at that point in val
#    f.write(val)
#    f.write(str(analyze_sentiment(val)))
    #f.write(analyze_sentiment(val))
    #print('\n')  

#f.close()