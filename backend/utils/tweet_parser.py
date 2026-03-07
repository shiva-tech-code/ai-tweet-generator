import re

class TweetParser:
    @staticmethod
    def parse_tweets(response):
        tweets = []
        lines = response.split('\n')
        
        for line in lines:
            match = re.match(r'^(\d+)\.\s*(.*)', line.strip())
            if match:
                tweet_text = match.group(2).strip()
                if tweet_text and len(tweet_text) <= 280:
                    tweets.append({
                        'text': tweet_text,
                        'char_count': len(tweet_text)
                    })
        
        return tweets[:10]
