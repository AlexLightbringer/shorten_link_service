from locust import HttpUser, between, task
import random
import string

class CrateUrlUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def test_create_short_url(self):
        long_url = self.generate_long_url()
        short_url = self.generate_short_url()

        response = self.client.post('/shorten', json={'long_url': long_url, 'short_url': short_url})
        if response.status_code == 200:
            response.success()

    @task
    def test_create_custom_url(self):
        long_url = self.generate_long_url()
        short_url = self.generate_short_url()

        response = self.client.post('/custom', json={'long_url': long_url, 'short_url': short_url})
        if response.status_code == 200:
            response.success()

    def generate_long_url(self):
        return 'http://' + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + '.com'

    def generate_short_url(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(5))