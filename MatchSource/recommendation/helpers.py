import gensim
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
  # Remove punctuations and convert text to lowercase
  words = gensim.utils.simple_preprocess(text, deacc=True)
  # Remove stop words & punctuation 
  words = [word for word in words if word not in stop_words]
  # Lemmatize
  words = [lemmatizer.lemmatize(word) for word in words]
  return words


