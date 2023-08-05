import pandas as pd
import praw

# add client_id and client_secret, generated from reddit.
reddit = praw.Reddit(   client_id="",  # your client id
                        client_secret="",   # your client secret
                        user_agent="F10 by /u/Artistic_Banana5093",
                    )

subreddit = reddit.subreddit("vegetarian")


top_posts_dict = {
                "Title": [],
                "Author":[],
                "ID": [],
                "Score": [],
                "Total Comments": [],
                "Post URL": [],
                "Post Text": []
            }
 
for post in subreddit.top(limit=501):
    top_posts_dict["Title"].append(post.title)
     
    # Text inside a post
    top_posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    top_posts_dict["ID"].append(post.id)
     
    # The score of a post
    top_posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    top_posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    top_posts_dict["Post URL"].append(post.url)

    # Author of post
    top_posts_dict["Author"].append(post.author)



hot_posts_dict = {
                "Title": [],
                "Author":[],
                "ID": [],
                "Score": [],
                "Total Comments": [],
                "Post URL": [],
                "Post Text": []
            }

for post in subreddit.hot(limit=501):
    # Post title
    hot_posts_dict["Title"].append(post.title)
     
    # Text inside a post
    hot_posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    hot_posts_dict["ID"].append(post.id)
     
    # The score of a post
    hot_posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    hot_posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    hot_posts_dict["Post URL"].append(post.url) 

    # Author of post
    hot_posts_dict["Author"].append(post.author) 

    

top_posts = pd.DataFrame(top_posts_dict)

hot_posts = pd.DataFrame(hot_posts_dict)


top_posts.to_csv("Top_Posts.csv", index=True)
hot_posts.to_csv("Hot_Posts.csv", index=True)