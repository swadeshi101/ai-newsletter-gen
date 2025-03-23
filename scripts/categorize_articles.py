from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json


def categorize_articles():
    # Load articles from the JSON file
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "r") as file:
        articles = json.load(file)

    # Prepare data for training
    texts = [article["cleaned_text"] for article in articles]
    categories = [article["category"] for article in articles]

    # Create a pipeline with TF-IDF and Naive Bayes
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(texts, categories)

    # Predict categories for all articles
    for article in articles:
        article["predicted_category"] = model.predict([article["cleaned_text"]])[0]

    # Save the categorized articles back to the JSON file
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "w") as file:
        json.dump(articles, file, indent=4)
    print("Articles categorized and saved to data/articles.json.")


if __name__ == "__main__":
    categorize_articles()