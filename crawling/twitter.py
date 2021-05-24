from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# Authenticate
consumer_key = '${consumer_key}'
consumer_secret = '${consumer_secret}'

access_token = '${access_token}'
access_token_secret = '${access_token_secret}'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    # stream by keyword & user
    stream.filter(follow=['#{twitter_id}'], track=['#{keyword_0}', '#{keyword_n}'])