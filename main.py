from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip



urls= ['https://www.youtube.com/watch?v=V5M2WZiAy6k']
resolucao = 1080


for url in urls:
    if(resolucao != 360 ):
        destino = "videos"
        titulo = ''
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        titulo = yt.title
        # video 1080p
        ys = yt.streams.get_by_itag(137)
        ys.download(output_path=destino)
        #audio
        ysa = yt.streams.filter(only_audio=True).first()
        ysa.download(output_path=destino)

        #juntando os 2

        video = VideoFileClip(f"{destino}/{titulo}.mp4")
        audio = AudioFileClip(f"{destino}/{titulo}.m4a")
        video = video.with_audio(audio)
        output_path = f"{destino}/{titulo} com audio.mp4"
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        video.close()
        audio.close()
        print(f'finalizou a url:{url}')

    else:
        destino = "videos"
        titulo = ''
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        titulo = yt.title
        ys = yt.streams.get_by_itag(18)
        ys.download(output_path=destino)
