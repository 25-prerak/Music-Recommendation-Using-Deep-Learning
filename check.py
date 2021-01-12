import ffmpeg
import librosa
stream = ffmpeg.input('031888.mp3')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.ogg')
#a,b = librosa.load("output.ogg")
#print(a,b)

