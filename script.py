import logging
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from yt_dlp.utils import YoutubeDLError
import os
import settings


def dir_listing(path):
    return sorted([(f, os.stat(f'{path}/{f}').st_size) for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]])


def df():  # return list [free_disk_space, total_disk_space]
    path = settings.videosDir
    res = os.statvfs(path)
    return [res.f_bavail * res.f_frsize, res.f_blocks * res.f_frsize]  # Free blocks available to non-super user * Fundamental file system block size, Total number of blocks in the filesystem * Fundamental file system block size; bytes


def download(videoURLs, formatSelector, dwnOptions=settings.defaultOptions.copy()):

    formatTranslate = {
        'best': '',
        'audio': 'bestaudio',
        '720p': '22'
    }

    # Setting up logging
    logger = logging.getLogger('yt-dlp_func')
    logger.handlers = []  # clearing, to avoid duplicating logger every time when function download() get called
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f'{settings.logsDir}/{videoURLs[-11:]}_log.txt')
    handler.setFormatter(logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s'))
    logger.addHandler(handler)

    if formatSelector != 'best':
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