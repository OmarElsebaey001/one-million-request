# Django Backend Stress Testing with Locust

This directory contains the necessary files to perform stress testing on the Django backend using Locust.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Customize the `locustfile.py` to target the specific endpoints you want to test.

## Running the Tests

To start the Locust web interface:

```
locust -f locustfile.py --host=http://localhost:8000
```

Replace `http://localhost:8000` with the URL of your Django application.

Then open your browser and go to http://localhost:8089 to access the Locust web interface.

## Configuration

You can customize the test by:

1. Adding more tasks in the `locustfile.py`
2. Adjusting the wait time between requests
3. Creating different user classes for different user behaviors

## Common Command Line Options

- `--users`: Number of concurrent users (default: 1)
- `--spawn-rate`: Rate at which users are spawned (users per second, default: 1)
- `--run-time`: Stop the test after the specified time (e.g., 1h30m, 60s, etc.)
- `--headless`: Run without web interface
- `--csv=example`: Save results to CSV files with the prefix "example"

For more options, run `locust --help`
