def get_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type =='logout' and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user) 
    return machines

def gen_report(machiens):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ', '.join(users)
            print('{}: {}'.format(machine, user_list))
            
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
        
events = [
    Event('2020-01-01', 'login', 'myworkstation', 'jordan'),
    Event('2022-02-02', 'login' , 'hellapella', 'ladnon'),
    Event('2023-01-05', 'logout', 'gigachad', 'chad'),
    Event('2012-02-02', 'logout' , 'gucciapog', 'brad'),
    ]

users = current_users(events)

print(users)
                                    