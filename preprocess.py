from nltk.tokenize import TweetTokenizer
import string

def removeTargetWordandHashTags(word,tweet):
    newList = [];
    for i in range(len(tweet)):
        x = tweet[i];
        if x[0] != '#':
            newList.append(x);
    return newList;
def changeNumberToken(tweet):
    newList = [];
    for token in tweet:
        if token.isnumeric():
            newList.append('2');
        else:
            newList.append(token);
    return newList;
def alignCase(tweet):
    newList = [];
    for token in tweet:
        if token.isupper():
            newList.append(token);
        else:
            newList.append(token.lower());
    return newList;
def removeMentions(tweet):
    for token in tweet:
        if token[0] == '@':
            tweet.remove(token);
    return tweet;
def removePunctuations(tweet):
    newList = [];
    punctuations = string.punctuation;
    for token in tweet:
        if token[0] not in punctuations:
            newList.append(token);
    return newList;
def preprocess(line):
    x = line.split('\t');
    targetWord = x[0];
    tokenizer = TweetTokenizer();
    try:    
        tweet_v1 = tokenizer.tokenize(x[2]);
    except IndexError:
        return None;
    tweet_v2 = removeTargetWordandHashTags(targetWord,tweet_v1);
    tweet_v3 = changeNumberToken(tweet_v2);
    tweet_v4 = alignCase(tweet_v3);
    tweet_v5 = removeMentions(tweet_v4);
    tweet_v6 = removePunctuations(tweet_v5);
    return (tweet_v6);

