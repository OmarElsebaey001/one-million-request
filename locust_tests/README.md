# High-Throughput Django Backend Stress Testing with Locust

This directory contains the necessary files to perform high-throughput stress testing (1000 requests per second) on the Django asset API endpoint using Locust.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Ensure your Django backend has test data:
   - The test assumes asset IDs in the range of 1-100
   - Modify the asset_id range in `locustfile.py` if your data differs

## Running the High-Throughput Tests

To start the Locust web interface:

```
locust -f locustfile.py --host=http://localhost:8000
```

Replace `http://localhost:8000` with the URL of your Django application.

Then open your browser and go to http://localhost:8089 to access the Locust web interface.

### Important Configuration for 1000 RPS

To achieve 1000 requests per second, you'll need to configure Locust properly:

1. Set a high number of users (e.g., 100-200)
2. Use a high spawn rate (e.g., 50 users per second)
3. The script uses `constant_throughput(1000)` to maintain the target rate

## Monitoring and Results

The script includes:
- Real-time logging of request statistics
- Success/failure tracking
- Periodic logging of throughput metrics

## Running Headless Tests

For production-like testing without the web UI:

```
locust -f locustfile.py --host=http://localhost:8000 --headless --users 200 --spawn-rate 50 --run-time 5m
```

## Saving Results

To save test results to CSV files:

```
locust -f locustfile.py --host=http://localhost:8000 --headless --users 200 --spawn-rate 50 --run-time 5m --csv=high_throughput_results
```

## System Preparation

Before running high-throughput tests:

1. Ensure your Django server is properly configured for high load
2. Consider using a production-grade server (e.g., Gunicorn with multiple workers)
3. Monitor server resources during testing (CPU, memory, database connections)
4. You may need to adjust system limits (e.g., open file descriptors)

For more options, run `locust --help`
