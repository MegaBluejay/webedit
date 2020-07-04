from datetime import datetime
from cork import Cork

password = 'mmm'

cork = Cork('authconf',initialize=True)

cork._store.roles['admin'] = 100
cork._store.save_roles()

tstamp = str(datetime.utcnow())
username = 'admin'
cork._store.users[username] = {
    'role': 'admin',
    'hash': cork._hash(username,password),
    'email_addr': f'{username}@localhost.local',
    'desc': '',
    'creation_date': tstamp
}
cork._store.save_users()
