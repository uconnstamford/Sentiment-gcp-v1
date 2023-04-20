from google.cloud import language
from google.cloud import language_v1
import six
import pandas as pd

data = pd.read_csv("all-data.csv", encoding="ISO-8859-1")

data.columns = ['sentiment', 'text']
data2 = data.columns[1]

#This format data.loc[1].at['text'] can be used to access the data at that element

def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")


def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))


text = "During the last quarter of 2016, the loans outpaced leases for the first time. Despite the significant market share, SolarCity’s solar panel installations during the first quarter declined around 39% year over year during the first quarter of 2017. The company has revealed sleek new solar roof panels that it claims are more efficient and cost-competitive compared to regular roofing products."

analyze_text_sentiment(text)
#for x in range(20):
#    val = data.loc[x].at['text']  #stores the data at that point in val
#    analyze_text_sentiment(val)


#text = "Guido van Rossum is great!"
#analyze_text_sentiment(text)
