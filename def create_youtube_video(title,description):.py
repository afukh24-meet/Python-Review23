def create_youtube_video(title,description):
	youtube_video = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{} }
	return (youtube_video)

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtube_video,username,comment_text):
	youtube_video.setdefault("comments", {}).setdefault(username,comment_text)
	return youtube_video

youtube_video_1 = create_youtube_video("jack_is_cooking","im cooking seefood today please watch !")
youtube_video_1 = like(youtube_video_1)
youtube_video_1 = dislike(youtube_video_1)
youtube_video_1 = add_comment(youtube_video_1,"afu","im watching its realy fun")

for i in range (495):
	youtube_video_1 = like(youtube_video_1)
