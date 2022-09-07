import string
import nltk
import pandas as pd
import re
from nltk import word_tokenize , FreqDist
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def clean_string(s):

    """Cleans a string of special characters"""

    cleaned_s = re.sub("#", " ", s)  # rimozione simbolo "#"
    cleaned_s = re.sub("@", " ", cleaned_s)  # rimozione simbolo "@"
    cleaned_s = re.sub("https?\S+", " ", cleaned_s)  # rimozione links
    cleaned_s = re.sub("\n", " ", cleaned_s)  # rimozione new lines
    cleaned_s = re.sub('\s+', ' ', cleaned_s)  # rimozione spazi multipli
    cleaned_s = re.sub("->",' ', cleaned_s) # rimozione delle freccie, particolarmente frequenti nelle risposte di GPT-3

    return cleaned_s

def remove_punct(tokens):

    """remove punctuation from a list of tokens"""

    return [token for token in tokens if token.isalpha()]

def cut_at_last_sent(s:str):

    """Cuts sentence at the last full-stop, since some of the answers are incomplete sentences."""

    i = s.rfind(".")

    return s[0:i+1]

def lexical_diversity(text):

    """Returns the lexical diversity of a text."""

    return len(set(word_tokenize(text))) / len(text)

def sentiment(s):

    """Returns 'positive' if the sentiment of the string is positive, 'neutral' if the sentiment of the string is neutral,
    and negative if the sentiment of the string is negative. The sentiment is based on the compound score of sentiment computed
     by Vader's Sentiment Intensity Analyzer."""

    sia = SentimentIntensityAnalyzer()

    sent = sia.polarity_scores(s)["compound"]

    if sent > 0:
        return "positive"
    elif sent == 0:
        return "neutral"
    else:
        return "negative"


def analyze_answers(df):

    """Takes as input a dataframe of questions and answers. Returns a dataframe having columns with additional information
    about the answers, in particular:
    - number of words of the answers
    - lexical diversity of the answer
    - sentiment value of the answer
    -general sentiment of the answer"""

    sia = SentimentIntensityAnalyzer()

    # cleaning answers
    df["answer"] = df["answer"].apply(lambda row: cut_at_last_sent(clean_string(row)))

    # number of words
    df["n_words"] = df["answer"].apply(lambda row: len(remove_punct(word_tokenize(row))))

    # lexical diversity
    df["lex_diversity"] = df["answer"].apply(lambda row: lexical_diversity(row))

    # sentiment value of answer
    df["sent_score"] = df["answer"].apply(lambda row: sia.polarity_scores(row)["compound"])

    # general sentiment of the answer
    df["sentiment"] = df["answer"].apply(lambda row: sentiment(row))

    return df


def frequency_analysis(df):

    """Plots the frequency distributions of the answers given by the models, considering the most common 10 words,
    escluding stopwords, punctuation, and words having less than 2 characters."""

    raw = " ".join(df['answer'])
    tokens = word_tokenize(raw)
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [t for t in tokens if t not in stopwords and t not in string.punctuation]
    fdist = FreqDist([t for t in tokens if len(t) > 2])
    print(fdist.most_common(10))
    fdist.plot(10, cumulative=True)

    return





## Creazione dei data frame con domande e risposte

df = pd.read_json("data/final_data/Q&A.json", orient ="records")
conan = df[["Question", "Conan"]]
neil = df[["Question", "Neil"]]
biden = df[["Question", "Biden"]]

# Rinominazione delle colonne
dfs = [conan, neil, biden]
for df in dfs:
    df.columns.values[1] = "answer"

# Creazione dei dataframe finali, con le analisi delle risposte
conan_final = analyze_answers(conan)
neil_final = analyze_answers(neil)
biden_final = analyze_answers(biden)
#anlyze_answers(conan).to_csv("conan_final")
#anlyze_answers(neil).to_csv("neil_final")
#anlyze_answers(biden).to_csv("biden_final")

final = [conan_final, neil_final, biden_final]


## Analisi

# Confronto numero parole

print(f'Numero parole medio Conan, Neil, Biden: {[df["n_words"].sum() / df.shape[0] for df in final]}')

# Confronto lexical diversity

print(f'Lexical diversity medio Conan, Neil, Biden: {[df["lex_diversity"].sum() / df.shape[0] for df in final]}')

# Confronto compund sentiment medio

print(f'Compound sentiment medio Conan, Neil, Biden: {[df["sent_score"].sum() / df.shape[0] for df in final]}')


# Confronto numero di risposte con sentiment positivo, neutrale e negativo
print(f'Numero di risposte positive Conan, Neil, Biden: {[df[df["sentiment"] == "positive"].shape[0] for df in final]}')
print(f'Numero di risposte negative Conan, Neil, Biden: {[df[df["sentiment"] == "negative"].shape[0] for df in final]}')
print(f'Numero di risposte neutrali Conan, Neil, Biden: {[df[df["sentiment"] == "neutral"].shape[0] for df in final]}')


### Nltk : FreqDist delle risposte

frequency_analysis(conan)
frequency_analysis(biden)
frequency_analysis(neil)

