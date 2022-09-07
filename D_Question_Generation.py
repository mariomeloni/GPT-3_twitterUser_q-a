import openai
import pandas as pd

from credentials import OPENAI_API_KEY

# Autenticazione
openai.api_key = OPENAI_API_KEY


def ask_q_to_conan(q):

    """function to ask a question to Conan O Brien, replicated artificially."""

    response = openai.Completion.create(
        model="davinci:ft-personal:conanobrien-q-a-2022-08-11-11-03-44",
        prompt=f"Answer only the following question concisely: \n\nQ: {q} \n\nA:->",
        max_tokens=100,
        n=1,
        temperature = 0.5,
        frequency_penalty = 1,
        presence_penalty = 2
    )

    #print(response["choices"][0]["text"])

    return response["choices"][0]["text"]

def ask_q_to_Neil(q):

    """Function to ask a question to Neil deGrass Tyson, replicated artificially"""

    response = openai.Completion.create(
        model="davinci:ft-personal:neiltyson-q-a-2022-08-11-12-43-14",
        prompt=f"Answer only the following question concisely: \n\nQ: {q}\n\nA: ->",
        max_tokens=100,
        n=1,
        temperature=0.5,
        frequency_penalty = 1,
        presence_penalty = 2
    )

    #print(response["choices"][0]["text"])

    return response["choices"][0]["text"]


def ask_q_to_Biden(q):

    """Function to ask a question to Neil deGrass Tyson, replicated artificially"""

    response = openai.Completion.create(
        model="davinci:ft-personal:joebiden-q-a-2022-08-11-12-52-05",
        prompt=f"Answer only the following question concisely: \n\nQ: {q}\n\nA: ->",
        max_tokens=100,
        n=1,
        temperature=0.5,
        frequency_penalty = 1,
        presence_penalty = 2
    )

    #print(response["choices"][0]["text"])
    return response["choices"][0]["text"]

# Formulazione delle stesse 10 domande a ciascun target user
questions = ["What are your plans for today?",
             "How are you feeling today?",
             "What do you think about climate change?",
             "What's an important thing that happened last week?",
             "What do you think about conservative republicans?",
             "What do you think about current gas prices?",
             "What did you talk about in your last interview?",
             "What do you think of the current COVID situation?",
             "What do you like about your job?",
             "What do you think about the current inflation?"]

data = [[question, ask_q_to_Biden(question),  ask_q_to_conan(question), ask_q_to_Neil(question)]
for question in questions]

# Generazione di un json avente le domande e le risposte date dai tre diversi modelli
df = pd.DataFrame(data, columns = ["Question", "Biden", "Conan", "Neil"])
df.to_json("Q&A.json", indent = 4, orient = 'records')


