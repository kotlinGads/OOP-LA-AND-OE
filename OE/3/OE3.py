class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Logging in as {self.username}")

    def post(self, content):
        print(f"Posting: {content}")


class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story):
        print(f"Sharing story: {story}")


class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_text):
        print(f"Tweeting: {tweet_text}")

insta = InstagramAccount("Paul", "password123", 1500)
insta.login()
insta.post("Hello from Instagram!")
insta.share_story("Yabmats lang!")

twitter = TwitterAccount("Paul", "securepass", 5000)
twitter.login()
twitter.post("Hello from Twitter!")
twitter.tweet("Just had a great coffee!")