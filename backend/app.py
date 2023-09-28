from flask import Flask, request, redirect, jsonify
import shortuuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import validators

# initialize the application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres-container:5432/flask'
db = SQLAlchemy(app)


# create the model for db
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    long_url = db.Column(db.String(250))
    short_url = db.Column(db.String(50), unique=True)

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url


def is_valid_url(url):
    return validators.url(url)


@app.route('/shorten', methods=['POST'])
def create_short_url():
    # get the long_url
    long_url = request.json.get('long_url')

    # validate the link
    if not is_valid_url(long_url):
        return jsonify({'error': 'Invalid Url'}), 400

    # check if the db is already exist and create if it doesn't
    with app.app_context():
        if not inspect(db.engine).has_table('link'):
            db.create_all()

    # check if the short link already exists in the database
    existing_link = Link.query.filter_by(long_url=long_url).first()

    if existing_link:
        return {'short_url': f'http://localhost:5000/{existing_link.short_url}'}

    # create the short link
    short_url = shortuuid.uuid(long_url)
    link = Link(long_url=long_url, short_url=short_url)

    # save to the db
    db.session.add(link)
    db.session.commit()

    # return the short link
    return {'short_url': f'http://localhost:5000/{short_url}'}


@app.route('/custom', methods=['GET', 'POST'])
def save_custom_urls():
    # get links
    long_url = request.json.get('long_url')
    short_url = request.json.get('short_url')

    # validate the link
    if not is_valid_url(long_url):
        return jsonify({'error': 'Invalid Url'}), 400

    # pass the data to the db
    links = Link(long_url=long_url, short_url=short_url)

    # check if the db is already exist and create if it doesn't
    with app.app_context():
        if not inspect(db.engine).has_table('link'):
            db.create_all()

    # save to the db
    db.session.add(links)
    db.session.commit()

    # return the custom link
    return {'custom_link': f'http://localhost:5000/{short_url}'}


# handler for redirecting using a short link
@app.route('/<string:short_url>')
def redirect_to_long_url(short_url):
    # look for a short link in the database
    link = Link.query.filter_by(short_url=short_url).first()

    if link:
        return redirect(link.long_url)
    else:
        return 'Link not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)