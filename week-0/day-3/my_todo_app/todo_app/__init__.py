import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    def todo_view(todos):
        the_view = 'List of my todos:' + '<br/>'
        for todo in todos:
            the_view += (todo + '<br/>')
        the_view += '--------LIST ENDS HERE----------'
        return (the_view)
    

    def get_todos_by_name(name):
        if name == 'depo':
            return ['Go for run', 'Listen rock music']
        elif name == 'sanket':
            return ['Go for mess', 'Listen jazz music']
        else:
            return []

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)

        person_todo_list = get_todos_by_name(name)
   
        return todo_view(person_todo_list)
    

    return app

