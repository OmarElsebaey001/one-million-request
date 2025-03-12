from locust import HttpUser, task, constant_throughput, events
import time
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global stats
class Stats:
    total_requests = 0
    successful_requests = 0
    failed_requests = 0

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logger.info("Starting load test targeting asset detail API")
    Stats.total_requests = 0
    Stats.successful_requests = 0
    Stats.failed_requests = 0

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logger.info(f"Test completed. Total requests: {Stats.total_requests}, Successful: {Stats.successful_requests}, Failed: {Stats.failed_requests}")

class AssetAPIUser(HttpUser):
    # Using constant_throughput to achieve a specific request rate
    # 1000 requests per second across all users
    wait_time = constant_throughput(1000)
    
    def on_start(self):
        # This method is called when a user starts
        logger.info("User started")
        # You can add authentication logic here if needed
        # self.client.post("/login", json={"username": "test", "password": "test"})
    
    @task
    def get_asset_detail(self):
        # Assuming there are assets with IDs 1-100 in the database
        # Adjust this range based on your actual data
        asset_id = random.randint(1, 100)
        
        start_time = time.time()
        with self.client.get(f"/api/assets/{asset_id}/", catch_response=True) as response:
            Stats.total_requests += 1
            
            if response.status_code == 200:
                Stats.successful_requests += 1
            else:
                Stats.failed_requests += 1
                response.failure(f"Failed to get asset {asset_id}: HTTP {response.status_code}")
                
        # Log every 1000 requests to avoid excessive logging
        if Stats.total_requests % 1000 == 0:
            logger.info(f"Processed {Stats.total_requests} requests. Success rate: {Stats.successful_requests/Stats.total_requests:.2%}")
            
    # You can add more tasks if needed, but they will reduce the rate of the primary task
