import subprocess

def Download(videoUrl, format):

    mode = {
        'best':['bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio', '--merge-output-format', 'mp4'],
        'audio':['140',]
    }

    with open(f'./videos/{videoUrl[-11:]}_log.txt', 'a') as logFile:
        subprocess.run(['youtube-dl', '--format', *mode[format],'--output', './videos/%(uploader)s-%(title)s-%(id)s.%(ext)s', videoUrl], stdout=logFile, stderr=logFile)