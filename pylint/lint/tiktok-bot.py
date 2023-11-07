import requests
import time

def get_user_info(username):
    url = "https://www.tiktok.com/api/user/info/?username=" + username
    response = requests.get(url)
    data = response.json()
    return data

def follow_user(username):
    url = "https://www.tiktok.com/api/user/follow/?username=" + username
    response = requests.post(url)
    data = response.json()
    return data

def like_video(video_id):
    url = "https://www.tiktok.com/api/video/like/?video_id=" + video_id
    response = requests.post(url)
    data = response.json()
    return data

def main():
    username = "your_username"
    password = "your_password"

    # احصل على معلومات المستخدم
    user_info = get_user_info(username)

    # احصل على قائمة بالمستخدمين الذين يتابعونك
    following_users = user_info["following"]

    # ابدأ متابعة المستخدمين الذين يتابعونك
    for following_user in following_users:
        follow_user(following_user)

    # احصل على قائمة بمقاطع الفيديو التي شاهدتها
    watched_videos = user_info["videos"]

    # ابدأ الإعجاب بمقاطع الفيديو التي شاهدتها
    for watched_video in watched_videos:
        like_video(watched_video["id"])

if _name_ == "_main_":
    main()
