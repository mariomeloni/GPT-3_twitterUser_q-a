# Importazione librerie

import tweepy
import pandas as pd
from credentials import TWITTER_ACCESS_TOKEN, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY


# Autenticazione
auth = tweepy.OAuthHandler(
 TWITTER_CONSUMER_KEY,
 TWITTER_CONSUMER_SECRET
)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

twitterAPI = tweepy.API(auth)


def create_df_from_user(username, count):

 """Creates a dataframe containing tweets of a Twitter User

 parameters:
 - username: username of the Twitter Account
 - count: number of tweets to gather

 """

 columns = ["User", "Tweet"]
 data = [[tweet.user.screen_name, str(tweet.full_text)]
         for tweet in tweepy.Cursor(twitterAPI.user_timeline,
                                    screen_name = username,
                                    include_rts = False,
                                    exclude_replies = True,
                                    tweet_mode = "extended").items(count) ]

 return pd.DataFrame(data, columns = columns)


# Creazione dei csv degli user scelti.
target_users = ["JoeBiden" , "ConanOBrien" , "neiltyson"]

for user in target_users:
 df = create_df_from_user(user, 150)
 df.to_csv(f"{user}.csv", sep = ";", index = False)
