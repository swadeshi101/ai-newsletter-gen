import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the model and tokenizer
model_name = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def generate_summary(text, max_length=3000):
    """
    Generate a detailed summary of the given text using the FLAN-T5 model.
    """
    # Prepare the input for the model
    input_text = f"Summarize the following article in 7-8 sentences:\n\n{text}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # Generate the summary
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=max_length, num_beams=4, early_stopping=True)

    # Decode the output
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary


def personalize_content(user, articles):
    """
    Generate personalized newsletter content for a user.
    """
    # Group articles by category
    categorized_articles = {}
    for article in articles:
        category = article["predicted_category"]
        if category not in categorized_articles:
            categorized_articles[category] = []
        categorized_articles[category].append(article)

    # Generate the newsletter
    newsletter = f"# Personalized Newsletter for {user}\n\n"

    # Add a concise summary at the top
    newsletter += "## Top Highlights\n"
    top_articles = sorted(articles, key=lambda x: len(x["cleaned_text"]), reverse=True)[:3]  # Top 3 longest articles
    for article in top_articles:
        summary = generate_summary(article["cleaned_text"])
        newsletter += f"- **{article['title']}**: {summary}\n"
    newsletter += "\n---\n\n"

    # Add categorized sections
    for category, articles_in_category in categorized_articles.items():
        newsletter += f"## {category}\n"
        for article in articles_in_category:
            summary = generate_summary(article["cleaned_text"])
            newsletter += f"### {article['title']}\n"
            newsletter += f"{summary}\n"
            newsletter += f"[Read more]({article['link']})\n\n"
        newsletter += "\n"

    return newsletter