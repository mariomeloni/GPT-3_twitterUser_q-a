import openai
import pandas as pd

from credentials import OPENAI_API_KEY



# Creazione di un csv avente i prompt vuoti e le risposte/tweet
def create_empty_prompt_df(file:str):

    """ Returns a csv with two columns: "prompts" and "completion". Prompts will be empty: they have to be
    written manually. """

    df = pd.read_csv(file, sep = ";", index_col= 0)
    df["prompt"] = ""
    df_out = df[["prompt", "Tweet"]]
    df_out.columns = ["prompt", "completion"]

    df_out.to_csv(f"{file.replace('_cleaned.csv', '')}_training.csv", sep = ";" )
    return df_out

#conversione del file csv in un json
def prepare_data(file_training):

    """Returns a raw data training file to a json without empty columns, ready to be formatted in jsonl format via the
    openAI CLI data formatting tool"""

    df = pd.read_csv(file_training, sep = ";", header = 0 , usecols= [1,2])
    df_out = df.dropna()
    df_out.to_json(f"{file_training.replace('.csv','')}_prepared.json", indent = 4)
    print(df_out.shape) # to check number of rows

    return df_out


## Creazione dei prompt vuoti per ciascun target user
from A_Twitter_extraction import target_users

#for user in target_users:
#    create_empty_prompt_df(f"{user}_cleaned.csv")

### I prompts andranno formulati manualmente nel csv

## Convertiamo i csv in json

#prepare_data("data/training_data/ConanOBrien_training.csv")
#prepare_data("data/training_data/neiltyson_training.csv")
#prepare_data("data/training_data/JoeBiden_training.csv")



#Primo utilizzo dei modelli, per dimostrare il loro funzionamento

openai.api_key = OPENAI_API_KEY

# Conan
response = openai.Completion.create(
    model= "davinci:ft-personal:conanobrien-q-a-2022-08-11-11-03-44",
    prompt="Conan, answer this question concisely: \n\n Q: What are your plans for today? ->",
    max_tokens = 100,
    n = 1,
    frequency_penalty = 1
    )

print(response["choices"][0]["text"])


# Neil de Grasse Tyson

response = openai.Completion.create(
    model= "davinci:ft-personal:neiltyson-q-a-2022-08-11-12-43-14",
    prompt="Neil, answer this question concisely: \n\n Q: What are your plans for today? ->",
    max_tokens = 100,
    n = 1,
    frequency_penalty = 1
    )

print(response["choices"][0]["text"])


# Joe Biden
response = openai.Completion.create(
    model= "davinci:ft-personal:joebiden-q-a-2022-08-11-12-52-05",
    prompt="President Biden, answer this question concisely: \n\n Q: What are your plans for today? ->",
    max_tokens = 100,
    n = 1,
    frequency_penalty = 1
    )

print(response["choices"][0]["text"])
