import requests
import time

def callapi():
    url = "http://localhost:8000/api/live-score/2"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

start_time = time.time()
for i in range(0,1000):
    callapi()
end_time = time.time()
total_time = end_time - start_time

print(f"Total time taken for 1000 API requests: {total_time:.4f} seconds")
