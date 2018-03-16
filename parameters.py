import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# NLTK Downloads

nltk.download([
    'punkt',
    'averaged_perceptron_tagger',
    'stopwords',
    'wordnet',
    'maxent_ne_chunker',
    'words'
])

# High level parameters

user = 'realDonaldTrump'   # Twitter user
number_of_tweets = 10000   # Number of tweets to retrieve

# Data cleaning & structure parameters

remove_words = stopwords.words('english')                                # Removing stopwords (e.g. if, then, a, and etc.)
remove_words_title = [word.title() for word in remove_words]             # Creating title case stopwords
remove_words_caps = [word.upper() for word in remove_words]              # Creating capitalised stopwords
remove_words_all = remove_words + remove_words_title + remove_words_caps # Combined stopwords
remove_punc = RegexpTokenizer(r'\w+')                        # Removing punctuation from a string (note will also remove @ and #)
remove_numbers = str.maketrans(dict.fromkeys('0123456789'))  # Removing numbers
remove_emojis = emoji_pattern = re.compile("["               # Removing emojis
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
"]+", flags=re.UNICODE)

# NER corpus

ner_corpus_root = "ner_corpus/gmb-2.2.0"