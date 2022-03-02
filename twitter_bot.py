import tweepy;
from tkinter import *;

CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secrets'
ACCESS_KEY = 'access token'
ACCESS_SECRET = 'access token secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) 

user = api.me()
root = Tk()

#Create GUI
label1 = Label(root, text='Key Word')
E1 = Entry(root, bd=5)

label2 = Label(root, text='Tweets Number')
E2 = Entry(root, bd=5)

label3 = Label(root, text='Response')
E3 = Entry(root, bd=5)

label4 = Label(root, text='Reply')
E4 = Entry(root, bd=5)

label5 = Label(root, text='Retweet')
E5 = Entry(root, bd=5)

label6 = Label(root, text='Liked')
E6 = Entry(root, bd=5)

label7 = Label(root, text='Follow')
E7 = Entry(root, bd=5)

def getKeyWord():
    return E1.get()

def getTweetNum():
    return E2.get()

def getResponse():
    return E3.get()

def getReply():
    return E4.get()

def getRetweet():
    return E5.get()

def getLikes():
    return E6.get()

def getFollow():
    return E7.get()


#Follow everyone follow me
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(f"Followed everyone that is following {user.name}")



#Favorite and retweet based on keyword
def twitterBot():
    search = getKeyWord()
    numberofTweets = int(getTweetNum())
    phrase = getResponse()
    reply = getReply()
    retweet = getRetweet()
    liked = getLikes()
    follow = getFollow()
    
    if retweet.lower() == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
                print('Retweeted')

            except tweepy.TweepError as exception:
                print(exception.reason)

            except StopIteration:
                    break

    if liked.lower() == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.favorite()
                print('Tweet Liked')

            except tweepy.TweepError as exception:
                print(exception.reason)

            except StopIteration:
                    break
    
    if follow.lower() == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.user.follow()
                print(f'@{tweet.user} followed')

            except tweepy.TweepError as exception:
                print(exception.reason)

            except StopIteration:
                    break

    #reply to user based on keyword
    if reply.lower() == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweetID = tweet.user.id
                username = tweet.user.screen_name
                api.update_status(f"@ {username} {phrase}", in_reply_to_status_id = tweetID)
                print(f"Replied with {phrase}")

            except tweepy.TweepError as exception:
                print(exception.reason)

            except StopIteration:
                    break

submit = Button(root, text ="Submit", command = twitterBot)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side =BOTTOM)
root.mainloop()