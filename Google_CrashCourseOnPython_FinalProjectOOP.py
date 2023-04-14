# A report that tracks the use of machines with which users are currently connected to wich machines.

def get_event_date(event):                                      # helper function that we'll use to sort the list.
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}                                               # create dictionary to store names and users of a machine.
    for event in events:                                        # iterate through ou list of events.
        if event.machine not in machines:                       # checks if the machine affected by this event is not in the dictionary and set it as an empty value.
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)             # add user to event if it is "login"
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)          # remove user to event if it is "login"
    return machines                                             # at the end of iteration through the list of events, the dictionary will contain all machine we've seen
                                                                # as keys with a set containing the current users of the machines as the values. This function returns the dictionary.

def generate_report(machines):
    for machine, users in machines.items():                     # returns both the key and value from the dictionary.
        if len(users) > 0:                                      # tells the PC when the set of users has more than 0 elements.
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2023-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2023-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2023-02-21 18:53:21', 'login', 'webserver.local', 'jane'),
    Event('2023-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2023-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2023-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)