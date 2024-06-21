import tweepy

# init
consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

def client():
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    return client

def auth():
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    api = tweepy.API(auth)
    return api


# retrieve media_ids
def uploadImg(media_paths: list[str]):
    media_ids = [auth().media_upload(media_path).media_id for media_path in media_paths]
    return media_ids

# simplified version
def tweet(
        client: tweepy.Client, 
        text: str, 
        media_paths: list[str] = None
    ):
    media_ids = uploadImg(media_paths) if media_paths else None
    response = client.create_tweet(text=text, media_ids=media_ids)
    print(f"https://twitter.com/user/status/{response.data['id']}")
    print("Tweeted successfully!")

if __name__ == '__main__':
    text = "Single image 1!"
    image_paths = ['img/6.jpeg'] # single image
    # image_paths = [f'img/{i}.jpeg' for i in range(7, 11)] # multiple image
    tweet(client(), text, image_paths)
