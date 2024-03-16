from flask import Flask
import pages

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    app.run(debug=True)
