videosDir = './videos'
logsDir = './logs'

defaultFilenameTemplate = f'{videosDir}/[%(uploader)s] %(title)s [%(id)s].%(ext)s'
shortFilenameTemplate = f'{videosDir}/[%(uploader)s] %(title).50s [%(id)s].%(ext)s'

defaultOptions = {
    'outtmpl': defaultFilenameTemplate,
#    'restrictfilenames': True
}