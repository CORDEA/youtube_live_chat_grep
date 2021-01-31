import os
import re
import sys

from api_client import ApiClient


def grep(messages, query):
    p = re.compile(query)
    result = []
    for m in messages:
        if p.search(m.display_message):
            result.append(m)
    return result


def main():
    client = ApiClient(os.environ['YOUTUBE_API_KEY'])
    chat_id = client.find_chat_id(sys.argv[1])
    messages = client.fetch_messages(chat_id)
    print(grep(messages, sys.argv[2]))


if __name__ == '__main__':
    main()
