import praw
import prawcore
import random

while True:
    reddit = praw.Reddit('bot2')
    subreddit_list = '''funny+pics+watchpeopledieinside+blackpeopletwitter+wellthatsucks+publicfreakout
                        +instantkarma+assholedesign+idiotsincars+tihi+gamingcirclejerk+facepalm+videos+iamverysmart
                        +oddlyterrifying+youshouldknow+blursedimages'''
    post_list = []

    for submission in reddit.subreddit(subreddit_list).top('all'):
        post_list.append(submission)

    try:
        post = random.choice(post_list)
        print(post.title)
        print(post.url)
        print(post.subreddit)

        post_title = post.title
        url = post.url
        sub = post.subreddit
        sub.submit(post_title, selftext=None, url=url, flair_id=None, flair_text=None,
                   resubmit=True, send_replies=True, nsfw=False, spoiler=False, collection_id=None)
    except:
        print('Post failed')
