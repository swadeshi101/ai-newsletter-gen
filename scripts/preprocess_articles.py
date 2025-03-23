import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import json

# Download NLTK stopwords
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and lemmatize
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return " ".join(tokens)


def preprocess_articles():
    # Load articles from the JSON file
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "r") as file:
        articles = json.load(file)

    # Preprocess each article
    for article in articles:
        article["cleaned_text"] = clean_text(article["title"] + " " + article["summary"])

    # Save the preprocessed articles back to the JSON file
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "w") as file:
        json.dump(articles, file, indent=4)
    print("Articles preprocessed and saved to data/articles.json.")


if __name__ == "__main__":
    preprocess_articles()