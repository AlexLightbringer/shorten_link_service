import unittest
from app import app, db, is_valid_url, Link, create_short_url, save_custom_urls, redirect_to_long_url
from sqlalchemy import inspect


class TestCreateUrl(unittest.TestCase):
    # create a test client and connect to the test database
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    # clear the database after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # send a POST request with a valid long link
    def test_get_long_url(self):
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)

    # send a POST request with an invalid long link
    def test_validate_url(self):
        response = self.app.post('/shorten', json={'long_url': 'invalid-url'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid Url', response.data)

    # check that table 'link' has been created
    def test_create_db(self):
        with app.app_context():
            inspector = inspect(db.engine)
            self.assertTrue('link' in inspector.get_table_names())

    # check that the 'link' table is created after creating a short link
    def test_existing_db(self):
        # check that table 'link' exists before creation
        with app.app_context():
            inspector = inspect(db.engine)
            self.assertTrue('link' in inspector.get_table_names())

        # send a POST request to create a short link
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})

        # check that the 'link' table is created after creating the short link
        with app.app_context():
            inspector = inspect(db.engine)
            self.assertTrue('link' in inspector.get_table_names())

    # check that the short link already exists in the database
    def test_existing_link_in_db(self):
        # add links to database
        link = Link(long_url='http://example.com', short_url='abcd123')
        db.session.add(link)
        db.session.commit()

        # send a POST request with a long link added
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})

        # check that the short link already exists in the database
        self.assertEqual(response.status_code, 200)

    # check that the short link in the response matches the expected format
    def test_correct_short_url(self):
        # send a POST request to create a short link
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)

        # check that the short link in the response matches the expected format
        self.assertTrue(response.json['short_url'].startswith('http://localhost:5000/'))

    # check saving data to database
    def test_data_in_db(self):
        # send a POST request to create a short link
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)

        # get a short link from response
        short_url = response.json['short_url'].split('/')[-1]

        # search for a database entry corresponding to a short link
        link_in_db = Link.query.filter_by(short_url=short_url).first()
        self.assertIsNotNone(link_in_db)

    # check that redirection from a short link to a long one works
    def test_redirect_to_long_url(self):
        # send a POST request to create a short link
        response = self.app.post('/shorten', json={'long_url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)

        # get a short link from response
        short_url = response.json['short_url']

        # send a GET request to the short link and check that it is redirected to the long link
        response_redirect = self.app.get(short_url)
        self.assertEqual(response_redirect.status_code, 302)
        self.assertEqual(response_redirect.location, 'http://example.com')

    # send a POST request to save a custom & original URLs
    def test_get_custom_url(self):
        response = self.app.post('/custom', json={'long_url': 'http://example.com', 'short_url': 'custom123'})
        self.assertEqual(response.status_code, 200)

    # check if the custom URL matches the expected format
    def test_save_custom_url(self):
        # send a POST request to create a short link
        response = self.app.post('/custom', json={'long_url': 'http://example.com', 'short_url': 'custom123'})
        self.assertEqual(response.status_code, 200)

        # get the custom link from response
        custom_url = response.json['custom_link'].split('/')[-1]

        # search for a database entry corresponding to a short link
        link_in_db = Link.query.filter_by(short_url=custom_url).first()
        self.assertIsNotNone(link_in_db)

    # check if retrieve the long URL using the custom URL
    def test_redirect_from_custom_to_long_url(self):
        # send a POST request to save a custom URL
        response = self.app.post('/custom', json={'long_url': 'http://example.com', 'short_url': 'custom123'})
        self.assertEqual(response.status_code, 200)

        # get the custom link from response
        custom_url = response.json['custom_link']

        # send a GET request to retrieve the long URL using the custom URL
        response = self.app.get(f'{custom_url}')
        self.assertEqual(response.status_code, 302)

        # check if the Location header indicates the correct redirection target
        self.assertEqual(response.headers['Location'], 'http://example.com')

    # check generating different short links
    def test_generate_different_short_links(self):
        # send a POST request to create the first short link
        response1 = self.app.post('/shorten', json={'long_url': 'http://example.com'})
        self.assertEqual(response1.status_code, 200)

        # get the short link from response
        short_url1 = response1.json['short_url']

        # send a POST request to create the second short link
        response2 = self.app.post('/shorten', json={'long_url': 'http://example2.com'})
        self.assertEqual(response2.status_code, 200)

        # get the short link from response
        short_url2 = response2.json['short_url']

        # check that the generated short links are different
        self.assertNotEqual(short_url1, short_url2)

if __name__ == '__main__':
    unittest.main()
