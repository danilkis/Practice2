import bottle
from bottle import route, run, template, static_file, request, view

from Graphs.Logic.Var3 import Fill
from Graphs.Logic.complete import draw_graph_complete, create_intersection_graph, create_union_graph
from Graphs.Logic.make import draw_graphs
message = []
@route('/static/<filename:path>')

def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():
    global message
    return template('home', message=message)
@route('/', method='POST')
def handle_build():
    global message
    data = request.json
    matrix1 = data.get('matrix1')
    matrix2 = data.get('matrix2')
    message = draw_graphs(matrix1,matrix2)
    return template('home', message=message)
@route('/operations', method='POST')
def handle_operations():
    data = request.json
    # Retrieve the matrices from the request data
    matrix1 = data.get('matrix1')
    matrix2 = data.get('matrix2')
    draw_graph_complete(matrix1)
    create_union_graph(matrix1, matrix2)
    create_intersection_graph(matrix1, matrix2)
    message = draw_graphs(matrix1, matrix2)
    return template('home', message=message)



@route('/find', method='POST')
def handle_find():
    global message
    data = request.json
    # Retrieve the matrices from the request data
    matrix1 = data.get('matrix1')
    matrix2 = data.get('matrix2')
    message = Fill(matrix1, matrix2)
    return template('home', message=message)
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
    return template('about')
@route('/info')
def info():
    return template('info')

# Run the web application
if __name__ == '__main__':
    message = " "
    run(host='localhost', port=8080, debug=True, template_path='./views')

