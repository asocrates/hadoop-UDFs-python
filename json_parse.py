

# Custom parsers for varous flume events


# parse contact updates

@outputSchema("user_id: chararray, posted_time: double, event: chararray, recv_array: bag{t:tuple(recv: chararray, action: chararray)}")
def parse_contact(contact_update):

    update_dict = dict(contact_update)

    user_id = str(update_dict['user_id'])
    event = str(update_dict['event'])
    recv = update_dict['updates']
    posted_time = float(update_dict['posted_time'])

    recv_array = []

    for key in recv:

        if recv[key]['add'] == []:
            action = 'add'
            recv_array.append((key, action))
        else:
            action = 'bad'
            recv_array.append((key, action))

    return user_id, posted_time, event, recv_array


# parse match_list updates

@outputSchema("user_id: chararray, posted_time: double, event: chararray, recv_array: bag{t: tuple(recv: chararray)}")
def parse_match(new_match):

    update_dict = dict(new_match)
    user_id = str(update_dict['user_id'])
    event = str(update_dict['event'])
    recv_array =  update_dict['match_list'].keys()
    posted_time = float(update_dict['posted_time'])

    return user_id, posted_time, event, recv_array


