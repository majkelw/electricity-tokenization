import requests
import json
import time


def main():
    f = open('config.json')
    cfg = json.load(f)
    start = time.time()
    elapsed, counter = 0, 0
    host = cfg["host"]
    port = cfg["port"]

    while elapsed < cfg["duration"]:
        if counter == cfg["delta"]:
            for user in cfg["users"]:
                response = requests.post(url=f"http://{host}:{port}/create-token",
                                         json={"user_id": user, "energy_amount": cfg["kwh"]})
                message = response.json()["detail"]
                print(f"For user {user} {message}")
            counter = 0
        elapsed = time.time() - start
        time.sleep(1)
        counter += 1


if __name__ == "__main__":
    main()
