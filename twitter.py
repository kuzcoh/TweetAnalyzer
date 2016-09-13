from TwitterSearch import *
try:
    tuo = TwitterUserOrder('HillaryClinton')

    ts = TwitterSearch(
        consumer_key = "",
        consumer_secret = "",
        access_token = "",
        access_token_secret = ""
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tuo):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['created_at'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)