from instaloader import Instaloader, Profile
import os


def get_post(link: str):
    L = Instaloader()
    username = link
    directory = username
    profile = Profile.from_username(L.context, username)

    for post in profile.get_posts():
        if post.is_video:
            continue
        L.download_post(post, target=directory)

    for item in os.listdir(directory):
        if item.endswith('.txt') or item.endswith(".xz"):
            path = os.path.join(directory, item)
            os.remove(path)

    print('Process is completed!!!')


get_post()