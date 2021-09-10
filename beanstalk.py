import greenstalk


class Beanstalk:
    def __init__(self, host='localhost', port=11300, tube='test_default'):
        self.host = host
        self.port = port
        self.tube = tube
        self.client = self.connect()

    def connect(self):
        return greenstalk.Client((self.host, self.port), use=self.tube)

    def push(self, body, priority=1, ttr=3600):
        try:
            self.client.put(body=body, priority=priority, ttr=ttr)
            print("success insert job {}".format(body))
        except:
            print("failed insert job {}".format(body))

    def close(self):
        self.client.close()
