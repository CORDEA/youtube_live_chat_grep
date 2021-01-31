from googleapiclient import discovery


class ApiClient:
    def __init__(self, key):
        self.client = discovery.build(
            'youtube',
            'v3',
            developerKey=key
        )

    def fetch_messages(self, id):
        messages = self.client.liveChatMessages()
        request = messages.list(liveChatId=id, part='snippet')
        response = request.execute()
