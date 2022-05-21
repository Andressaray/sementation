import pandas as pd
import re
import nltk
nltk.download()
import ssl
from nltk.corpus import stopwords
import spacy
from deep_translator import GoogleTranslator
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('wordnet')
class main:
  pStemmer = PorterStemmer()
  lemmatizer = WordNetLemmatizer()
  list_words = []
  bag_words = {}

  def __init__(self, text):
    self.clean_tweets(self, text)

  def traslate_word(self, text = ''):
    new_text = GoogleTranslator(source='auto', target='es').translate(text)
    return new_text

  def delete_accents(self, text = ''):
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

  def conver_verbs(self, list = []):
    for word in list:
      aux_text = self.pStemmer.stem(word)
      aux_text = self.lemmatizer.lemmatize(word)
      if aux_text in self.bag_words:
        self.bag_words[aux_text] = self.bag_words[aux_text] + 1
      else: 
        self.bag_words[aux_text] = 1
      self.list_words.append(aux_text)

  def delete_emojis(self, text = ''):
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
  
  def clean_tweets(self, _,texts = ''):
    text_separator = re.split(' ', texts)
    spacy.prefer_gpu()
    ssl._create_default_https_context = ssl._create_unverified_context
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    es_stopwords = set(stopwords.words('spanish'))
    tokenizer = nltk.tokenize.WordPunctTokenizer()
    for text in text_separator:
      if pd.isnull(text) == False:
        aux_text = re.sub("([0-9]+)", '', text)
        aux_text = re.sub("'[^A-Za-z]+'", '', aux_text)
        aux_text = aux_text.lower()
        aux_text = re.sub("([.;,:¡!¿?()@*$-//…‼º°´’»|”“ªâ˜ <>\\=#])+", ' ', aux_text)
        aux_text = self.delete_emojis(self, aux_text)
        aux_text = self.delete_accents(self, aux_text)
        aux_text = self.traslate_word(aux_text)
        aux_text = ' '.join(aux_text.split())
        tokens = tokenizer.tokenize(aux_text)
        aux_text = [aux_text for aux_text in tokens if not aux_text in es_stopwords]
        self.conver_verbs(self, aux_text)
    print(self.bag_words)
    return 'Hola'
    # return {
    #   self.bag_words,
    #   self.list_words
    # }


