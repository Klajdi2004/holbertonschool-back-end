#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    response = requests.get("{}users/{}/todos".format(API_URL, user_id),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()
        name = data[0]["user"]["name"]
        task_done = [task for task in data if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(task_done), len(data)))
        for task in task_done:
            print("\t {}".format(task["title"]))

    else:
        print("Error: {}".format(response.status_code))