from flask import Flask, render_template, request, redirect, url_for
import os, glob
import script

fileListLogs = [f for f in os.listdir('./videos/logs') if os.path.isfile(os.path.join('./videos/logs', f))]
fileListVideos = [f for f in os.listdir('./videos') if os.path.isfile(os.path.join('./videos', f))]

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST' and request.form['videoUrl']:
            script.Download(videoUrl=request.form['videoUrl'], format=request.form['selectFormat'])
            return redirect(url_for('list'))
        return render_template('index.html')

    @app.route('/purge', methods=['POST', 'GET'])
    def purge():
        if request.method == 'POST' and request.form['selectFile'] != 'default':
            selectedFile = request.form['selectFile']  # variable to avoid escaping in f-string
            if selectedFile == 'ALL logs':
                for f in glob.glob('./videos/logs/*'):
                    os.remove(f)
            else:
                os.remove(f'./videos/{selectedFile}')
        return render_template('purge.html', fileListVideos = fileListVideos, fileListLogs = fileListLogs)

    @app.route('/list')
    def list():
        return render_template('list.html', fileListVideos = fileListVideos)

    @app.route('/list/logs')
    def logs():
        return render_template('logs.html', fileListLogs = fileListLogs)

    @app.route('/list/logs/logview-<string:filename>')
    def logview(filename):
        with open(f'./videos/logs/{filename}', 'r') as f:
            data_from_file = f.read()
        return render_template('logview.html', filename = filename, logtext = data_from_file)

    return app

# if __name__ == '__main__':
#     app.run(debug=True)
