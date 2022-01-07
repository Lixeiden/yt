from flask import Flask, render_template, request, redirect, url_for
import os
import script


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
            os.remove(f'./videos/{selectedFile}')
        return render_template('purge.html', fileListVideos=[f for f in os.listdir('./videos') if os.path.isfile(os.path.join('./videos', f))], fileListLogs=[f for f in os.listdir('./videos/logs') if os.path.isfile(os.path.join('./videos/logs', f))])

    @app.route('/list')
    def list():
        return render_template('list.html')

    return app

# if __name__ == '__main__':
#     app.run(debug=True)
