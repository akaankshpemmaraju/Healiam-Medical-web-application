import csv

from drugprediction.models import DrugReviewModel
from drugprediction.sentimentanalyzer import getCommentSentiment

def loadData():
    
    #DrugReviewModel.objects.all().delete()
# To be able to add services.
    with open(file=''C:\\Users\\tejitha reddy\\PycharmProjects\\DrugPredictionBasedOnSentimentAnalysisOfReviews\\dataset\\drugsComTrain_raw.csv',mode='r',encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
           model=DrugReviewModel()
           model.drugname=row[0]
           model.condition=row[1]
           model.review=row[2]
#getting the comments for the sentiment
           model.sentiment=getCommentSentiment(row[2])
           model.save()
