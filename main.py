from bottle import route, run, template, static_file, request, view

from Graphs.Danon.complete import draw_graph


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():

    message = " "
    return template('home', message=message)
@route('/', method='POST')
def handle_post():
    data = request.json

    # Retrieve the matrices from the request data
    matrix1 = data.get('matrix1')
    matrix2 = data.get('matrix2')
    print(draw_graph(matrix1))
    print(matrix2)

@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./css')
@route('/graphs_images/<filename>')
def server_static(filename):
    return static_file(filename, root='./graphs_images')

@route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./js')

@route('/image/<filename>')
def server_static(filename):
    return static_file(filename, root='./image')


@route('/about')
def about():

    message = " "
    return template('about', message=message)
@route('/info')
def info():

    message = " "
    return template('info', message=message)

# Run the web application
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, template_path='./views')

