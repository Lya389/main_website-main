from website import create_app
from flask import Flask
from flask_admin import Admin

app = Flask(__name__,
            static_url_path='',
            static_folder='website/static',
            template_folder='website/templates')


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
