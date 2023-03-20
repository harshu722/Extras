from pytube import youTube
import pytube
import os


def main():
    video_url = input('https://www.youtube.com/watch?v=Yrtm7d3TJbs: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    youTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'

    if os.name == 'nt':
        os.system('ren {0} {1}'. format(location,renametomp3))
    else:
        os.system('mv {0} {1}'. format(location,renametomp3))

if __name__ == '__main__':

    main()    
