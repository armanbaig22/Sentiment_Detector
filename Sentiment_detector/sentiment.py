import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# download the required data for NLP
nltk.download('vader_lexicon')

# create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# get input text from the user
text = input("Enter some text to analyze the sentiment: ")

# perform sentiment analysis using the SentimentIntensityAnalyzer
scores = sia.polarity_scores(text)

# extract the compound score, which ranges from -1 to 1
# where -1 indicates a negative sentiment and 1 indicates a positive sentiment
compound_score = scores['compound']

# print the compound score
print("The sentiment score of the text is:", compound_score)
# ajhsas 

