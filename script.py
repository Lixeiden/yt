import subprocess
import os


def dir_listing(path):
    return sorted([(f, os.stat(f'{path}/{f}').st_size) for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]])


def df():  # return list [free_disk_space, total_disk_space]
    path = '/'
    res = os.statvfs(path)
    return [res.f_bavail * res.f_frsize, res.f_blocks * res.f_frsize]  # Free blocks available to non-super user * Fundamental file system block size, Total number of blocks in the filesystem * Fundamental file system block size; bytes


def Download(videoUrl, format):

    mode = {
        'best': ['bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio', '--merge-output-format', 'mp4'],
        'audio': ['140', ]
    }

    with open(f'./videos/logs/{videoUrl[-11:]}_log.txt', 'a') as logFile:
        subprocess.run(['yt-dlp', '--format', *mode[format], '--output', './videos/%(uploader)s-%(title)s-%(id)s.%(ext)s', videoUrl], stdout=logFile, stderr=logFile)
