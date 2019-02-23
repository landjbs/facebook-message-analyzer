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

def all_words_used(unfiltered_messages):
    """
    Function to find set of all words used in all messages
    """
    words_used = []
    errors = 0
    for chat in unfiltered_messages:
        for message in chat:
            try:
                curMessage = (message['content']).split()
                curMessage_processed = [(item.lower()) for item in curMessage]
                words_used += curMessage_processed
            except:
                errors += 1
        print(f"{errors} errors when reading messages")
    return (set(words_used))

chats = os.listdir(CURRENT_DIRECTORY + "/messages/")[:NUMBER_TO_ANALYZE]

sorted_chats = []
chat_names = []
number_messages = []
unfiltered_messages = []
final_data_messages = {}
final_data_times = {}
final_data_words = {}
invalid_message_count = 0

print('Analyzing ' + str(min(NUMBER_TO_ANALYZE, len(chats))) + ' chats...')

for chat in chats:
    json_data = get_json_data(chat)
    if json_data != None:
        messages = json_data["messages"]
        if len(messages) >= MESSAGE_THRESHOLD:
            chat_names.append(chat)
            number_messages.append(len(messages))
            unfiltered_messages.append(messages)




print(set(words_used))

df = pd.DataFrame(columns=['chat_names','words vector','number messages'])

# sorted_chats[2][1][2]['content']
#print(f"{'-'*80}\n{unfiltered_messages}\n{'-'*80}")
print(df)

print('Finished processing chats...')
#
# for i, (messages, chat, messages) in enumerate(sorted_chats):
#     number_messages = {}
#     person_to_times = {}
#     number_words = {}
#
#     print(str(i) + " - " + str(len(messages)) + " messages - " + str(chat))
#
#     for message in messages:
#         try:
#             name = message["sender_name"]
#             time = message["timestamp_ms"]
#             message_content = message["content"]
#
#             number_messages[name] = number_messages.get(name, 0)
#             number_messages[name] += 1
#
#             person_to_times[name] = person_to_times.get(name, [])
#             person_to_times[name].append(datetime.datetime.fromtimestamp(time/1000.0))
#
#             number_words[name] = number_words.get(name, [])
#             number_words[name].append(len(message_content.split()))
#         except KeyError:
#             # happens for special cases like users who deactivated, unfriended, blocked
#             invalid_message_count += 1
#
#     final_data_messages[i] = number_messages
#     final_data_times[i] = person_to_times
#     final_data_words[i] = number_words
#
# print('Found ' + str(invalid_message_count) + ' invalid messages...')
# print('Found ' + str(len(sorted_chats)) + ' chats with ' + str(MESSAGE_THRESHOLD) + ' messages or more')

### PLOTTING FUNCITONS ###
#
# def plot_num_messages(chat_number):
#     plotted_data = final_data_messages[chat_number]
#     X = np.arange(len(plotted_data))
#     pl.bar(X, list(plotted_data.values()), align='center', width=0.5, color = 'r', bottom = 0.3)
#     pl.xticks(X, plotted_data.keys(), rotation = 90)
#     pl.title('Number of Messages Sent')
#     pl.tight_layout()
#     pl.show()
#
# def plot_histogram_time(chat_number):
#     person_to_times = final_data_times[chat_number]
#     pl.xlabel('Time')
#     pl.ylabel('Number of Messages')
#     pl.title('# of Messages Over Time')
#     colors = ['b', 'r', 'c', 'm', 'y', 'k', 'w', 'g']
#     for i , person in enumerate(person_to_times):
#         plotted_data = person_to_times[person]
#         pl.hist(plotted_data, 100, alpha=0.3, label=person, facecolor=colors[i % len(colors)])
#     pl.legend()
#     pl.xticks(rotation=90)
#     pl.tight_layout()
#     pl.show()
#
# def plot_histogram_words(chat_number):
#     temp = {}
#     for person in final_data_words[chat_number]:
#         temp[person] = np.average(final_data_words[chat_number][person])
#     plotted_data = temp
#     X = np.arange(len(plotted_data))
#     pl.bar(X, list(plotted_data.values()), align='center', width=0.5, color = 'r', bottom = 0.3)
#     pl.xticks(X, plotted_data.keys(), rotation = 90)
#     pl.title('Average Word Count')
#     pl.tight_layout()
#     pl.show()
#
# def plot(chat_number):
#     plot_num_messages(chat_number)
#     plot_histogram_time(chat_number)
#     plot_histogram_words(chat_number)
#
# plot(4)
