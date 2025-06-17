import tweepy

BEARER_TOKEN = "TU_BEARER_TOKEN_AQUI"


def fetch_tweets(query="Hyperliquid", max_results=50):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    search_query = f"{query} -is:retweet"
    tweets = client.search_recent_tweets(query=search_query, max_results=max_results)
    return tweets.data or []


if __name__ == "__main__":
    for tweet in fetch_tweets():
        print(f"{tweet.id}: {tweet.text}\n")
