import praw
import prawcore
import random
import time

number_of_posts = 0
number_of_fails = 0
failed_in_a_row = 0

while True:
    reddit = praw.Reddit('bot3')

    subreddit_list = ['watchpeopledieinside', 'blackpeopletwitter',
                      'wellthatsucks', 'publicfreakout', 'instantkarma', 'assholedesign', 'idiotsincars', 'tihi', 'gamingcirclejerk',
                      'facepalm', 'videos', 'iamverysmart', 'oddlyterrifying', 'youshouldknow', 'mademesmile', 'kidsarefuckingstupid',
                      'instagramreality', 'oldschoolcool', 'mildlyinfuriating', 'cringe', 'prorevenge', 'nevertellmetheodds',
                      'delusionalartists', 'dontputyourdickinthat', 'aww', 'funny', 'pics']

    random_subreddit = random.choice(subreddit_list)
    post_list = []
    posted_list = []

    for submission in reddit.subreddit(random_subreddit).top(limit=200):
        post_list.append(submission)

    post = random.choice(post_list)

    if post not in posted_list:
        print(post.title)
        print(post.subreddit)

        post_title = post.title
        url = post.url
        sub = post.subreddit
        try:
            sub.submit(post_title, selftext=None, url=url, flair_id=None, flair_text=None,
                       resubmit=True, send_replies=True, nsfw=False, spoiler=False, collection_id=None)

            number_of_posts += 1
            failed_in_a_row = 0
            posted_list.append(post)
            print('Posted. ' + 'Total posted: ' + str(number_of_posts) +
                  ', Total failed: ' + str(number_of_fails) + ' Failed in a row: ' + str(failed_in_a_row))
        except:
            number_of_fails += 1
            failed_in_a_row += 1
            print('Failed. ' + 'Total posted: ' + str(number_of_posts) +
                  ', Total failed: ' + str(number_of_fails) + ' Failed in a row: ' + str(failed_in_a_row))
            if failed_in_a_row > 10:
                time.sleep(3600)
                failed_in_a_row = 0
