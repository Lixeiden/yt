from flask import Flask, render_template, request
import script

flask1 = Flask(__name__)


@flask1.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST' and request.form['videoUrl']:
        script.Download(videoUrl=request.form['videoUrl'], format=request.form['selectFormat'])
    return render_template('index.html')


@flask1.route('/purge', methods=['POST', 'GET'])
def purge():
    if request.method == 'POST' and request.form['selectFile'] != 'default':
        # del files here
        return request.form['selectFile']
    return render_template('purge.html')


@flask1.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    flask1.run(debug=True)
