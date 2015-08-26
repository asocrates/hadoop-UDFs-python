

# A custom parser for contact updates. In principle, can make one for each LOAD in pig

@outputSchema("user_id: chararray, posted_time: double, event: chararray, recv: chararray, action: chararray")
def parse_contact(contact_update):

    update_dict = dict(contact_update)

    user_id = str(update_dict['user_id'])
    event = str(update_dict['event'])
    recv = str(update_dict['updates'].keys()[0])
    posted_time = float(update_dict['posted_time'])
    if update_dict['updates'][recv]['add'] == []:
        action = 'add'
    else:
        action = 'bad'

    return user_id, posted_time, event, recv, action
