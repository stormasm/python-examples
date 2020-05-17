import os

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


def example():
    """
    Some example usage of different twilio resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Get all messages
    all_messages = client.messages.list()
    print('There are {} messages in your account.'.format(len(all_messages)))

    # Get only last 10 messages...
    some_messages = client.messages.list(limit=10)
    print('Here are the last 10 messages in your account:')
    for m in some_messages:
        sid = m.sid
        print(sid)
        mymsg = client.messages(sid).fetch()
        print(mymsg.body)

if __name__ == '__main__':
    example()
