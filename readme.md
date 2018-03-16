# Twitter Analysis

This repo contains my work to extract, clean and apply Entity Extraction to the tweets from the current POTUS, Donald Trump.<br/>

Note that the entity extraction model is based upon [this excellent tutorial](http://nlpforhackers.io/named-entity-extraction/).

## Setup

1. [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [Download & install Anaconda](https://conda.io/docs/user-guide/install/download.html)
3. [Register for a Twitter access token](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)
4. Clone this repo: ```git clone https://github.com/Tommo565/twitter-analysis```
5. Navigate to the cloned folder: ```cd twitter-analysis```
6. Create a directory for the entity recognition corpus: ```mkdir ner_corpus```
7. [Download the Gronigen Meaning Bank](http://gmb.let.rug.nl/releases/gmb-2.2.0.zip) and unzip it into the ner_corpus folder
8. Install the dependencies: `pip install -r requirements.txt`
9. Open the core/secrets_example.py file with a text editor and update it with your twitter credentials
10. Rename the secrets_example.py file to secrets.py
11. Start the Jupyter Notebook: `jupyter notebook`
12. Away you go =)


## Entity Extraction

Entity Extraction Explanation goes here...


## Useful links & Further Reading


Generating an access token: https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/<br/>
Dive into NLTK: http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization<br/>
The NLTK.tag Stanford package: http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford<br/>
Download the Stanford Core NLP tools: https://stanfordnlp.github.io/CoreNLP/<br/>
Standford Core NLP Github: https://github.com/stanfordnlp/CoreNLP<br/>
Installing Core NLP: https://stanfordnlp.github.io/CoreNLP/cmdline.html<br/>
Sentiment Analysis on Trumps Tweets using Python: https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-<br/>
NLTK POS Tag list: https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/<br/>
Word Class descriptions: https://en.oxforddictionaries.com/grammar/word-classes-or-parts-of-speech<br/>
Flattening Trees: https://www.packtpub.com/books/content/python-text-processing-nltk-2-transforming-chunks-and-trees<br/>
Entity Extraction: http://nlpforhackers.io/named-entity-extraction/<br/>




