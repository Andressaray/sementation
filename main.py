import pandas as pd
import re
import nltk
import ssl
from nltk.corpus import stopwords
import spacy
from deep_translator import GoogleTranslator
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

file = pd.read_csv("Sentimientos.tsv", sep='\t')
pStemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# class main:
def traslate_word(text = ''):
  new_text = GoogleTranslator(source='auto', target='es').translate(text)
  return new_text

def delete_accents(text = ''):
  replacements = (
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
  )
  for a, b in replacements:
    text = text.replace(a, b).replace(a, b)
  return text
def conver_verbs(list_words = []):
  list_verbs = []
  for word in list_words:
    aux_text = pStemmer.stem(word)
    aux_text = lemmatizer.lemmatize(word)
    list_verbs.append(aux_text)
  return list_verbs

def delete_emojis(text = ''):
  emoji_pattern = re.compile("["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      u"\U00002500-\U00002BEF"  # chinese char
      u"\U00002702-\U000027B0"
      u"\U00002702-\U000027B0"
      u"\U000024C2-\U0001F251"
      u"\U0001f926-\U0001f937"
      u"\U00010000-\U0010ffff"
      u"\u2640-\u2642" 
      u"\u2600-\u2B55"
      u"\u200d"
      u"\u23cf"
      u"\u23e9"
      u"\u231a"
      u"\ufe0f"  # dingbats
      u"\u3030"
      "]+", flags=re.UNICODE)
  return emoji_pattern.sub(r'', text)

def clean_tweets(key = ''):
  # text_separator = re.split(' ', texts)
  spacy.prefer_gpu()
  ssl._create_default_https_context = ssl._create_unverified_context
  tokenizer = nltk.tokenize.WhitespaceTokenizer()
  es_stopwords = set(stopwords.words('spanish'))
  tokenizer = nltk.tokenize.WordPunctTokenizer()
  list_words_dirty = []
  for text in file[key]:
    if pd.isnull(text) == False:
      aux_text = re.sub("([0-9]+)", '', text)
      aux_text = re.sub("'[^A-Za-z]+'", '', aux_text)
      aux_text = aux_text.lower()
      aux_text = re.sub("([.;,:¡!¿?()@*$-//…])+", ' ', aux_text)
      aux_text = delete_emojis(aux_text)
      aux_text = delete_accents(aux_text)
      # aux_text = self.traslate_word(aux_text)
      aux_text = ' '.join(aux_text.split())
      tokens = tokenizer.tokenize(aux_text)
      aux_text = [aux_text for aux_text in tokens if not aux_text in es_stopwords]
      list_words_dirty.append(conver_verbs(aux_text))
  return list_words_dirty
listWordsTitle = clean_tweets('Title')
print(listWordsTitle)
# listWordsOpinion = clean_tweets('Opinion')

