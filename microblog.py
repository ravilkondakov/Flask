from cat import create_app, db, cli
from cat.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run()
