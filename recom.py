import pandas as pd
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn import neighbors
from scipy import optimize

from wordcloud import WordCloud, STOPWORDS
def find(a):
    df = pd.read_csv("final_review (1).csv")
    def g2(text):
        return TextBlob(text).sentiment.polarity
    def Sort(sub_li):
        sub_li.sort(key = lambda x: (x[1],-x[3],-x[4]))
        return sub_li
    def Sort1(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
        sub_li.sort(key = lambda x: x[5])
        return sub_li
    df.set_index("product_name",inplace = True)
    res=df.loc[a]
    li=[]
    i=4
    lis=[]
    while(i<len(res)):
        if(res[i]!="nan"):
            lis.append(res[i])
            lis.append(res[i+1])
            lis.append(res[i+2])
            lis.append(res[i+3])
            lis.append(res[i+4])
            i=i+5
            li.append(lis)
            lis=[]
    finli=[]
    for i in li:
        if  str(i[1]) != "nan":
            mil=g2(i[4])
            i[4]=mil
            finli.append(i)
    finli1=Sort(finli)
    finli2=[]
    l=len(finli1)
    for i in finli1:
        i[1]=l
        l=l-1
        finli2.append(i)
    finli3=[]
    for i in finli2:
        suma=0.3*i[1]+0.4*i[3]+0.3*i[4]
        i.append(suma)
        finli3.append(i)
    finli4=Sort1(finli3)
    finli4.reverse()
    finli5=[]
    for i in finli4:
        cv=[]
        cv.append(i[0])
        cv.append(i[2])
        cv.append(i[3])
        finli5.append(cv)
    return finli5
    





