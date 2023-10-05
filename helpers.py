import gensim
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from typing import List

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_documents(documents: List[str]):
  """
  Preprocess a list of documents by removing punctuations, stop words, and lemmatizing the words.
  param documents: List of documents to be preprocessed
  return: List of preprocessed documents, where each document is a list of words
  """

  documents_clean = []

  for document in documents:
    # Remove punctuations and convert text to lowercase
    words = gensim.utils.simple_preprocess(document, deacc=True)
    # Remove stop words & punctuation 
    words = [word for word in words if word not in stop_words]
    # Lemmatize
    words = [lemmatizer.lemmatize(word) for word in words]

    words = ' '.join(words)

    documents_clean.append(words)
  
  return documents_clean


def get_tfidf_representation(documents: List):
  """
  Create a TF-IDF representation of the documents.
  param documents: List of documents to be preprocessed, where each document is a list of words
  return: TF-IDF representation of the documents, bag of words representation of the documents, and the dictionary
  """
  # Create a dictionary from the words
  dictionary = gensim.corpora.Dictionary(documents)

  # filter out tokens that appear too much or too little
  dictionary.filter_extremes(no_below=2, no_above=0.5, keep_n=150000)

  # Create a bag of words representation of the documents
  corpus_bow = [dictionary.doc2bow(document) for document in documents]
  # Create a TF-IDF representation of the documents
  tfidf_encoder = gensim.models.TfidfModel(corpus_bow)
  corpus_tfidf = tfidf_encoder[corpus_bow]
  return corpus_tfidf, corpus_bow, dictionary



