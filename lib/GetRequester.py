import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response_body = requests.get(self.url)
        return response_body.content

    def load_json(self):
        people_list = []
        people = json.loads(self.get_response_body())
        for person in people:
            people_list.append(person)

        return people_list
    
