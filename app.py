from scripts.fetch_articles import fetch_articles
from scripts.preprocess_articles import preprocess_articles
from scripts.categorize_articles import categorize_articles
from scripts.personalize_newsletter import generate_newsletter


def main():
    # Step 1: Fetch articles
    print("Fetching articles...")
    fetch_articles()

    # Step 2: Preprocess articles
    print("Preprocessing articles...")
    preprocess_articles()

    # Step 3: Categorize articles
    print("Categorizing articles...")
    categorize_articles()

    # Step 4: Generate personalized newsletters
    print("Generating newsletters...")
    generate_newsletter()

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    main()