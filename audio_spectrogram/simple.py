# Writeup : https://github.com/yulyachert/DCTF-writeups/blob/main/BadApple.md
# Video: https://dctf.dragonsec.si/files/230afaac6d3b52b608268829e8aa11d0/Bad_Apple.mp4

import moviepy.editor as mp
import matplotlib.pyplot as plt
import librosa.display

my_clip = mp.VideoFileClip(r"Bad_Apple.mp4")
my_clip.audio.write_audiofile(r"audio.wav")
x, sr = librosa.load('audio.wav', sr=None)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(30, 5),)
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz', cmap='gray_r')
plt.savefig('spectrogramA.png', bbox_inches='tight', transparent=True, pad_inches=0.0)
plt.show()
