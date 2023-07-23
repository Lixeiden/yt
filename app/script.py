import logging
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from yt_dlp.utils import YoutubeDLError
import os
import settings
import time
import zipfile


def dir_listing(path):
    return sorted([(f, os.stat(f'{path}/{f}').st_size) for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]])


def df():  # return list [free_disk_space, total_disk_space]
    path = settings.videosDir
    res = os.statvfs(path)
    return [res.f_bavail * res.f_frsize, res.f_blocks * res.f_frsize]  # Free blocks available to non-super user * Fundamental file system block size, Total number of blocks in the filesystem * Fundamental file system block size; bytes


def download(videoURLs, formatSelector='best', dwnOptions=settings.defaultOptions.copy(), zip=False):
    # Setting up logging
    logger = logging.getLogger(f'yt-dlp_func_{time.time()}')  # generate unique logger name
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f'{settings.logsDir}/{videoURLs[-11:]}_log.txt')
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))  # [%(name)s] %(levelname)s
    logger.addHandler(handler)

    dwnOptions['format'] = settings.formatTranslate[formatSelector]
    dwnOptions['logger'] = logger
    video_files = []

    def replace_hook(status):
        if status['status'] == 'finished':
            new_filename = status['filename'].replace('#', 'N')
            os.rename(status['filename'], new_filename)
            if zip:
                video_files.append(new_filename)

    dwnOptions['progress_hooks'] = [replace_hook]

    try:
        with YoutubeDL(dwnOptions) as ydl:
            ydl.download(videoURLs)
    except YoutubeDLError as e:
        if 'File name too long' in str(e):
            logger.warning('Trying a shorter file name...')
            dwnOptions['outtmpl'] = settings.shortFilenameTemplate
            with YoutubeDL(dwnOptions) as ydl:
                ydl.download(videoURLs)

    # If zip flag is True, zip all downloaded videos
    if zip and video_files:
        # Generate unique name for zip file based on timestamp and number of files
        timestamp = int(time.time())
        zip_filename = f'{settings.videosDir}/session_{timestamp}_{len(video_files)}.zip'
        with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_STORED) as zipf:
            for file in video_files:
                zipf.write(file)

    # Clean up the logger
    handler.close()
    logger.removeHandler(handler)


if __name__ == "__main__":
    user_url = input("URL: ")
    user_format = input(f"format {{{', '.join(settings.formatTranslate.keys())}}}: ")
    user_iszip = input("add to zip? (y/n)").lower() == 'y'
    download(videoURLs=user_url, formatSelector=user_format, zip=user_iszip)
