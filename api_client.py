from googleapiclient import discovery


class ApiClient:
    def __init__(self, key):
        self.client = discovery.build(
            'youtube',
            'v3',
            developerKey=key
        )

    def find_chat_id(self, video_id):
        request = self.client.videos().list(id=video_id, part='id,snippet,liveStreamingDetails')
        response = request.execute()
        return response['items'][0]['liveStreamingDetails']['activeLiveChatId']

    def fetch_messages(self, chat_id):
        messages = self.client.liveChatMessages()
        request = messages.list(liveChatId=chat_id, part='snippet')
        return request.execute()['items']
