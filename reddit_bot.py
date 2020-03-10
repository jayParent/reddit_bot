import praw
import prawcore

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('all')
comment_count = 0


for submission in subreddit.stream.submissions():
    title = submission.title
    subreddit = submission.subreddit
    normalized_title = title.lower()

    if 'coronavirus' in normalized_title or 'covid-19' in normalized_title:
        try:
            submission.reply('Wash your hands!')
            comment_count += 1
            print(comment_count)
        except:
            print('Error')
