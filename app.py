from flask import Flask, render_template, request, redirect, url_for, abort
import os, glob
import script


def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST' and request.form['videoUrl']:
            script.Download(videoUrl=request.form['videoUrl'], format=request.form['selectFormat'])
            return redirect(url_for('list'))
        return render_template('index.html', diskFreeSpaceAndTotal = script.df())

    @app.route('/purge', methods=['POST', 'GET'])
    def purge():
        if request.method == 'POST' and request.form['selectFile'] != 'default':
            selectedFile = request.form['selectFile']  # variable to avoid escaping in f-string
            if selectedFile == 'ALL logs':
                for f in glob.glob('./logs/*'):
                    os.remove(f)
            elif selectedFile == 'ALL vids':
                for f in glob.glob('./videos/*'):
                    os.remove(f)
            else:
                os.remove(f'./videos/{selectedFile}')
        fileListVideosAndSizes = script.dir_listing('./videos')
        fileListLogsAndSizes = script.dir_listing('./logs')
        return render_template('purge.html', fileListVideosAndSizes = fileListVideosAndSizes, fileListLogsAndSizes = fileListLogsAndSizes)

    @app.route('/list')
    def list():
        fileListVideosAndSizes = script.dir_listing('./videos')
        return render_template('list.html', fileListVideosAndSizes = fileListVideosAndSizes)

    @app.route('/list/logs')
    def logs():
        fileListLogsAndSizes = script.dir_listing('./logs')
        return render_template('logs.html', fileListLogsAndSizes = fileListLogsAndSizes)

    @app.route('/list/logs/logview-<string:filename>')
    def logview(filename):
        try:
            with open(f'./logs/{filename}', 'r') as f:
                data_from_file = f.read()
        except FileNotFoundError:
            data_from_file = 'ERROR: File not found'
            abort(404)
        return render_template('logview.html', filename = filename, logtext = data_from_file)

    return app

# if __name__ == '__main__':
#     app.run(debug=True)
