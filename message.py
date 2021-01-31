from dataclasses import dataclass


@dataclass(init=False)
class Message:
    published_at: str
    display_message: str
    author_channel_id: str

    def __init__(self, data):
        snippet = data['snippet']
        self.published_at = snippet['publishedAt']
        self.display_message = snippet['displayMessage']
        self.author_channel_id = snippet['authorChannelId']
