import json
import bottle

from bottle import route, run, template, static_file, request

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():
    message = " "
    return template('home', message=message)

@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./css')


# Run the web application
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, template_path='./views')
