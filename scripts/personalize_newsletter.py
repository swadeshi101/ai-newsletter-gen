import json
from utils.llm_helper import personalize_content
import os

def generate_newsletter():
    # Load user profiles and articles
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/user_profiles.json", "r") as file:
        user_profiles = json.load(file)
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "r") as file:
        articles = json.load(file)

    # Match articles to users
    user_articles = {user: [] for user in user_profiles}
    for article in articles:
        for user, interests in user_profiles.items():
            if article["predicted_category"] in interests:
                user_articles[user].append(article)

    # Generate newsletters
    for user, articles in user_articles.items():
        # Generate personalized content using LLM
        newsletter = personalize_content(user, articles)

        # Ensure the "newsletters" directory exists
        newsletters_dir = "C:/Users/shend/PycharmProjects/AI Newsletter Generator/newsletters"
        os.makedirs(newsletters_dir, exist_ok=True)

        # Correct file path with a proper slash
        file_path = os.path.join(newsletters_dir, f"{user.replace(' ', '_')}.md")

        # Save the newsletter as a Markdown file
        with open(file_path, "w") as file:
            file.write(newsletter)

        print("Newsletters generated and saved to newsletters/ folder.")


if __name__ == "__main__":
    generate_newsletter()


