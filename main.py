import os
import re
from argparse import ArgumentParser

from api_client import ApiClient


def grep(messages, query):
    p = re.compile(query)
    result = []
    for m in messages:
        if p.search(m.display_message):
            result.append(m)
    return result


def main():
    parser = ArgumentParser()
    parser.add_argument('id', help='YouTube video ID')
    parser.add_argument('query', help='Search query')
    args = parser.parse_args()

    client = ApiClient(os.environ['YOUTUBE_API_KEY'])
    chat_id = client.find_chat_id(args.id)
    messages = client.fetch_messages(chat_id)
    print(grep(messages, args.query))


if __name__ == '__main__':
    main()
