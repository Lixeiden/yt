import logging
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from yt_dlp.utils import YoutubeDLError
import os
import settings
import time


def dir_listing(path):
    return sorted([(f, os.stat(f'{path}/{f}').st_size) for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]])


def df():  # return list [free_disk_space, total_disk_space]
    path = settings.videosDir
    res = os.statvfs(path)
    return [res.f_bavail * res.f_frsize, res.f_blocks * res.f_frsize]  # Free blocks available to non-super user * Fundamental file system block size, Total number of blocks in the filesystem * Fundamental file system block size; bytes


def download(videoURLs, formatSelector='best', dwnOptions=settings.defaultOptions.copy()):

    formatTranslate = {
        'best': 'bestvideo+bestaudio/best',
        '720p': '22',
        'audio': 'bestaudio',
    }

    # Setting up logging
    logger = logging.getLogger(f'yt-dlp_func_{time.time()}')  # generate unique logger name
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f'{settings.logsDir}/{videoURLs[-11:]}_log.txt')
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))  # [%(name)s] %(levelname)s
    logger.addHandler(handler)

    dwnOptions['format'] = formatTranslate[formatSelector]
    dwnOptions['logger'] = logger

    try:
        with YoutubeDL(dwnOptions) as ydl:
            ydl.download(videoURLs)
    except YoutubeDLError as e:
        if 'File name too long' in str(e):
            logger.warning('Trying a shorter file name...')
            dwnOptions['outtmpl'] = settings.shortFilenameTemplate
            with YoutubeDL(dwnOptions) as ydl:
                ydl.download(videoURLs)

    # Clean up the logger
    handler.close()
    logger.removeHandler(handler)


if __name__ == "__main__":
    user_url = input("URL: ")
    download(user_url)
