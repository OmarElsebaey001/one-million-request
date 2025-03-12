from locust import HttpUser, between, task

class ApiUser(HttpUser):
    host = "https://w6pxpz9qiq.eu-west-1.awsapprunner.com"
    wait_time = between(1, 2)
    
    @task
    def get_asset_detail(self):
        self.client.get("/api/assets/1/")
