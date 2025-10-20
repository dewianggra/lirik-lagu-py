import time
from threading import Thread
import sys

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def sing_lyric(lyric, delay, speed, line_delay=0):
    time.sleep(delay)
    animate_text(lyric, speed)
    time.sleep(line_delay)

def sing_song():
    lyrics = [
        ("tante...", 0.08),
        ("sudah terbiasa terjadi tante...", 0.09),
        ("teman datang ketika lagi butuh saja...", 0.09),
        ("coba kalo lagi susah...", 0.15),
        ("mereka semua menghilanggggg.....", 0.15),
    ]

    delays = [0, 1.5, 1.5, 1, 2]

    threads = []
import time
import sys

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed, line_delay=0):
    time.sleep(delay)
    animate_text(lyric, speed)
    time.sleep(line_delay)

def sing_song():
    lyrics = [
        ("tante...", 0.08),
        ("sudah terbiasa terjadi tante...", 0.09),
        ("teman datang ketika lagi butuh saja...", 0.09),
        ("coba kalo lagi susah...", 0.15),
        ("mereka semua menghilanggggg.....", 0.15),
    ]
    
    delays = [0, 1.5, 1.5, 1, 2]

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        delay = delays[i] if i < len(delays) else 0
        sing_lyric(lyric, delay, speed)

if __name__ == "__main__":
    sing_song()
