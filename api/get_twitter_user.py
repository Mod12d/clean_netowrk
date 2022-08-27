import tweepy
from os import getenv
from hello_neo4j import App
from dotenv import load_dotenv
from import_data import session

load_dotenv()
# 同じフォルダに.envファイルを入れておくと読み込んでくれる。

consumer_key = getenv('consumer_key')
consumer_secret = getenv('consumer_secret')
access_token = getenv('access_token')
access_token_secret = getenv('access_token_secret')

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

# idからfollowerを取得
def follower_get(screen_name):
    followers = api.get_followers(screen_name = screen_name)
    return followers

def get_follower_name_list(followers):
    follower_names = []
    for follower in followers:
        follower_names.append(follower.name)
    return follower_names

def get_follower_description_list(followers):
    follower_description = []
    for follower in followers:
        follower_description.append(follower.desctiption)
    return follower_description

def get_follower_profile_image_url(followers):
    follower_profile_image = []
    for follower in followers:
        follower_profile_image.append(follower.profile_image)
    return follower_profile_image


# descriptions = get_follower_description_list(followers)
# urls = get_follower_profile_image_url(followers)

if __name__ == "__main__":

    followers = follower_get("shimabu_it")
    names = get_follower_name_list(followers)

    for name in names:
        session.run(
            "CREATE (person:Person {name: $name) RETURN person",
            name=name)

# if __name__ == "__main__":
#
#     app = App("bolt://localhost:57687", "neo4j", "password")
#     follower_list = follower_get("shimabu_it")
#
#     for follower in follower_list:
#         app.create_friendship(follower, "しまぶー", "follow")
#
#     app.close()

