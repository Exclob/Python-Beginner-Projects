from pytube import YouTube

def downloader(url:str)->str:
    yt = YouTube(url,on_progress_callback=True)
    print(f'Title: {yt.title}')
    print(f'Thumbnail: {yt.thumbnail_url}')
    print(f'Author: {yt.author}')
    minutes, seconds = divmod(yt.length, 60)
    print(f'Length: {minutes:02d}:{seconds:02d}')
    video = yt.streams.get_highest_resolution()
    video.download(filename = 'video.mp4')

downloader('https://www.youtube.com/watch?v=C0DPdy98e4c')
