import click
import os
import re
import tweepy
from dotenv import load_dotenv
load_dotenv()

class StreamListener(tweepy.StreamListener):
    def __init__(self, verbose, file_obj):
        super().__init__()
        self.verbose = verbose
        self.file_obj = file_obj

    def on_status(self, status):
        text = status.text
        text = re.sub('\n', ' ', text)
        # # Remove RT prefix
        # text = re.sub('RT @?(\w){1,15}: ', '', text)
        if self.verbose:
            print(text)
        click.echo(text, self.file_obj)
        # Look through possible tweets and clean up RTs and stuff

    def on_error(self, status_code):
        print(f'ERROR CODE: {status_code}')
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff

def getTwitterKeys():
    return {
        'consumer_key': os.environ['CONSUMER_KEY'],
        'consumer_secret_key': os.environ['CONSUMER_SECRET_KEY'],
        'access_token': os.environ['ACCESS_TOKEN'],
        'access_token_secret': os.environ['ACCESS_TOKEN_SECRET'],
    }

def setup_stream(verbose, output_file):
    keys = getTwitterKeys()
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret_key'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    try:
        file_obj = open(output_file, 'a+')
        file_obj.truncate(0)   # Erase contents of file if it exists
    except Exception as e:
        print(e)
        raise(e)

    streamListener = StreamListener(verbose, file_obj)
    stream = tweepy.Stream(
        auth=api.auth,
        listener=streamListener,
    )

    return stream
