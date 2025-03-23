import feedparser
import json

# List of RSS feeds
RSS_FEEDS = {
    "Tech": ["https://techcrunch.com/feed/", "https://www.wired.com/feed/rss"],
    "Finance": ["https://feeds.bloomberg.com/markets/news.rss", "https://cointelegraph.com/rss/tag/blockchain"],
    "Sports": ["http://www.espn.com/espn/rss/news", "http://feeds.bbci.co.uk/sport/rss.xml"],
    "Entertainment": ["https://www.thehollywoodgossip.com/feed/", "https://earmilk.com/feed/"],
    "Science": ["https://www.nature.com/nature.rss","https://www.space.com/feeds/all"]
}

def fetch_articles():
    articles = []
    for category, feeds in RSS_FEEDS.items():
        for feed_url in feeds:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                articles.append({
                    "title": entry.title,
                    "summary": entry.summary if "summary" in entry else "",
                    "link": entry.link,
                    "category": category
                })
    return articles

if __name__ == "__main__":
    articles = fetch_articles()
    with open("C:/Users/shend/PycharmProjects/AI Newsletter Generator/data/articles.json", "w") as file:
        json.dump(articles, file, indent=4)
    print(f"Fetched {len(articles)} articles and saved to data/articles.json.")