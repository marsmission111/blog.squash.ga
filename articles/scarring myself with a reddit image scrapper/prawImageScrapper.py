import praw
import urllib
import os

r = praw.Reddit(client_id='none of yur business', client_secret='none of yur business', password='none of yur business', user_agent='none of yur business', username='none of your business')
subreddit = r.subreddit(raw_input('Enter subreddit: '))
extentions = ['jpg', 'png', 'gif']

for submission in subreddit.hot():
	try:
		print submission.url
	except:
		print 'Skipping'
	if submission.url.split('.')[-1] not in extentions:
		continue

	if not os.path.exists(str(subreddit)):
		os.mkdir(str(subreddit))

	#creates file
	f = open(str(subreddit)+'/'+str(submission)+'.'+submission.url.split('.')[-1],"w+")
	f.close()

	#downloads file
	urllib.urlretrieve(submission.url, str(subreddit)+'/'+str(submission)+'.'+submission.url.split('.')[-1])