import tweepy

class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

    def tweet_img(self, filename):
        self.api.update_with_media(filename)

if __name__ == "__main__":
    twitter = TwitterAPI()
    # twitter.tweet("Bot post? #AScriptADay")
    path = "E://Test/1.PNG"
    twitter.tweet_img(path)


