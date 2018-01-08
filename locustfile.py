from locust import HttpLocust, TaskSet


def tweets(l):
    l.client.get("/v1/api/news")


class UserBehavior(TaskSet):
    tasks = {tweets: 2}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 600000
