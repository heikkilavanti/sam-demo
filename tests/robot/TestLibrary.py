import logging
import requests
import json


class TestLibrary(object):
    base_url = "http://localhost:3000"

    def create_task_table(self):
        return self.send_req("post", f"{self.base_url}/table")

    def create_task(self, task_title, task_details):
        payload = {"taskTitle": task_title, "taskDetails": task_details}
        return self.send_req("post", f"{self.base_url}/task", payload)

    def get_all_tasks(self):
        return self.send_req("get", f"{self.base_url}/tasks".format(self.base_url))

    def delete_task(self, task_id):
        return self.send_req("delete", f"{self.base_url}/task/{task_id}")

    def delete_task_table(self):
        return self.send_req("delete", f"{self.base_url}/table")

    def send_req(self, method, endpoint, payload=None):
        if method == "post":
            response = requests.post(endpoint, data=json.dumps(payload))
        elif method == "delete":
            response = requests.delete(endpoint)
        else:
            response = requests.get(endpoint)
        logging.info(response.text)
        try:
            resp_json = response.json()
            return response.status_code, resp_json
        except json.JSONDecodeError:
            return response.status_code, ""
