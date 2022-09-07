# Progetto Mario Meloni

Il progetto consiste nell'estrazione di Tweet dai profili di tre user, per l' addestramento di 3 diversi modelli GPT-3, uno per ciascun
user. L'obiettivo è creare un modello di Q&A, che impari a rispondere a domande formulate dell'utente usando un linguaggio e uno stile
simile a quello del twitter user.


Il progetto è articolato in 4 parti:

## 1) Estrazione dei tweet di 3 user.

Tale fase è svolta nello script "A_Twitter_extraction.py"

- scelta dei 3 personaggi per il training del  modello GPT-3
  - Joe Biden
  - Neil deGrasse Tyson
  - Conan O' Brien

- estrazione di 150 tweet per personaggio per l'addestramento del modello.
L'estrazione di tweet avviene mediante la libreria tweepy.


## 2) Pulizia dei dati

Tale fase avviene nello script "B_data_cleaning.py".

- eliminazione caretteri speciali
- eliminazione links
- Tokenizzazione
- Filtraggio dei tweet in base al numero di token

## 3) Addestramento del modello GPT-3

Script di riferimento: "C_GPT-3", "D_question_generation.py". 

L'obiettivo è addestrare dei modelli in grado di rispondere a delle domande poste dall'utente come se a rispondere fosse
il twitter-user con cui il modello stesso è stato addestrato. Nella sua risposta, il modello dovrà utilizzare il lessico e lo stile dell'utente twitter.

Per la creazione e l'addestramento del modello saranno utilizzato le API di OpenAI.
In particolare, verrà addestrato un fine-tuned model, utilizzando come training data un file jsonl avente due colonne: 
- prompt: la domanda formulata "manualmente".
- completion: il tweet, che corrisponderebbe alla risposta della domanda.

Gli step saranno:

1) Predisposizione  dei training data, caratterizzati da 75 tweet per ciascun utente. Per ciascun tweet verrà manualmente formulata una domanda di modo che il Tweet risulti come risposta
2) Addestramento del modello

## 4) Test dei modelli mediante la sottoposizione di 10 domande a ciascuno. Analisi delle risposte ottenute

A ciascun Twitter-user artificiale verranno sottoposte le medesime 10 domande.
Verrano poi analizzate e confrontate le risposte date dai tre diversi modelli mediante diversi strumenti di NLP e di sentiment Analysis.


### Librerie utilizzate:

- tweepy
- pandas
- re
- nltk
- openai
- vaderSentiment



