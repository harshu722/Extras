
# importing the vlc module  
import vlc
# creating the vlc media player object
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
my_media = vlc.MediaPlayer("video.mp4")  
  
# playing video  
my_media.play() 
