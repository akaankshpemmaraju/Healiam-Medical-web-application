import re
from textblob import TextBlob

def cleanComment(cmnt):
    '''
    Utility function used to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cmnt).split())

def getCommentSentiment(cmnt):
    '''
    Utility function will classify sentiment of passed tweets
    using textblob's sentiment method
    this helps in reducing complexity
    '''
    # creating TextBlob object of passed tweet text
    analysis = TextBlob(cleanComment(cmnt))
    # set sentiment on the required analytics
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negation'
