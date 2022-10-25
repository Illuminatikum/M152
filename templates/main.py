from moviepy.editor import VideoFileClip
from app.py import video_mp4

clip = VideoFileClip(video_mp4)

clip.write_gif('mygif.gif', fps=10)