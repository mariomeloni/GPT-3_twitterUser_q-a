import pandas as pd
import nltk
import re

def remove_emojis(string):

    """ Removes emojis from a string."""

    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
                      "]+", flags= re.UNICODE)
    return re.sub(emoj, '', string)

def clean_text(tweet):
    '''
    Removes links and special characters from tweet.
    For Hashtags, only the symbol # is removed, since the hashtag itself could contain precious info.
    Same with mentions.
    Links are removed completely.
    Newlines characters are also removed, for data-formatting reasons.
    '''
    try:
        cleaned_tweet = re.sub("#", " ", tweet)                  # rimozione simbolo "#"
        cleaned_tweet = re.sub("@"," ", cleaned_tweet)           # rimozione simbolo "@"
        cleaned_tweet = re.sub("https?\S+", " ", cleaned_tweet)  # rimozione links
        cleaned_tweet = re.sub("\n", " ", cleaned_tweet)         # rimozione new lines
        cleaned_tweet = remove_emojis(cleaned_tweet)             # rimozione emoji
        cleaned_tweet = re.sub('\s+',' ',cleaned_tweet)          # rimozione spazi multipli
    except Exception:
        cleaned_tweet = ''
    return cleaned_tweet


def remove_punct(tokens):

    """remove punctuation from a list of tokens"""

    return [token for token in tokens if token.isalpha()]


def clean_csv(filename, min_token = 10):

    """ returns the input csv with Tweets cleaned from special characters.
    This function also adds a new column to the csv file, that contains the number of tokens. In this way,
    we can filter rows based on the number of tokens, and choose only tweets that have a certain number of tokens."""

    df = pd.read_csv(filename, delimiter = ";", encoding = "utf8" , on_bad_lines= "skip")
    df_cleaned = df
    df_cleaned["Tweet"] = [clean_text(tweet) for tweet in df_cleaned["Tweet"]]
    df_cleaned["Tokens"] = [len(remove_punct(nltk.word_tokenize(tweet))) for tweet in df_cleaned["Tweet"]]
    df_cleaned = df_cleaned[df["Tokens"] > min_token] # filtraggio dei tweet in base al numero di token

    df_cleaned.to_csv(f"{filename.replace('.csv','')}_cleaned.csv", sep = ";" , index= True, encoding = "utf8")

    return df_cleaned

from A_Twitter_extraction import target_users

for user in target_users:
    clean_csv(f"{user}.csv", 10)

