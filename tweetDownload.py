import tweepy
import time
#we removed the keys and and showing you the default code which we used
def get_tweets(tweetID):
    consumer_key = "ConsumerKeyOfTheTwitterAPI"
    consumer_secret = "SecretConsumerKeyOfTheTwitterAPI"
    access_key = "AccessKeyOfTheTwitterAPI"
    access_secret = "SecretAccessKeyOfTheTwitterAPI"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:        
        tweetObj = api.get_status(tweetID);
        tweet = (tweetObj._json['text']);
    except tweepy.TweepError:
        return None;
    return tweet

def main():
    file = open('TEST_tweet.SENTIMENT.all.id.test','r');
    lines = file.readlines();
    print(len(lines));
    writelines = [];
    notfound = [];
    count = 0;
    for instance in lines:
        count += 1;
        x = instance.split("\t");
        tweet = get_tweets(x[1]);
        if tweet is not None:
            print(x[0],"\t",tweet);
            writelines.append(x[0]+"\t"+tweet+"\n");
        else:
            notfound.append(x[1]);
        if (count%40) == 0:
            print('Count',count,'.. going to sleep..');
            time.sleep(5);
            print('Awake!');
    print(len(writelines));
    file = open('TEST_tweet.SENTIMENT.all.id.file','w');
    file.writelines(writelines);
    file.close();
    print('Not Found List',notfound);

main();
