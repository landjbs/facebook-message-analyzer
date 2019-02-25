import os
import json
import numpy as np
import pylab as pl
import datetime
import pandas as pd
import string

CURRENT_DIRECTORY = os.getcwd()
NUMBER_TO_ANALYZE = 10000
MESSAGE_THRESHOLD = 100

def get_json_data(chat):
    try:
        json_location = CURRENT_DIRECTORY + "/messages/" + chat + "/message.json"
        with open(json_location) as json_file:
            json_data = json.load(json_file)
            return json_data
    except IOError:
        pass # some things the directory aren't messages (DS_Store, stickers_used, etc.)

def process_message(message):
    """
    Split message from dict into list of lowercase words
    """
    curMessage = (message['content']).split()
    cleanedWord = lambda item : item.lower().translate(None, string.punctuation)
    curMessage_processed = [cleanedWord(item) for item in curMessage]
    return curMessage_processed

def all_words_used(unfiltered_messages):
    """
    Function to find set of all words used in all messages
    """
    words_used = []
    errors = 0
    for chat in unfiltered_messages:
        for message in chat:
            try:
                words_used += process_message(message)
            except:
                errors += 1
    print(f"{errors} errors when reading messages")
    return (set(words_used))

chats = os.listdir(CURRENT_DIRECTORY + "/messages/")[:NUMBER_TO_ANALYZE]

chat_names = []
number_messages = []
unfiltered_messages = []
invalid_message_count = 0

print('Analyzing ' + str(min(NUMBER_TO_ANALYZE, len(chats))) + ' chats...')

# load chats into lists
for chat in chats:
    json_data = get_json_data(chat)
    if json_data != None:
        messages = json_data["messages"]
        if len(messages) >= MESSAGE_THRESHOLD:
            chat_names.append(chat)
            number_messages.append(len(messages))
            unfiltered_messages.append(messages)


words_used = (all_words_used(unfiltered_messages))

for chat_num, chat in enumerate(unfiltered_messages):
    for message in chat:
        processed_message = process_message(message)
        for word in processed_message:
            print(word)
