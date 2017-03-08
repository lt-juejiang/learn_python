#!/user/bin/python
#coding=utf-8
import hashlib

db = {}
def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    md5 = get_md5(password + username + 'the-Salt')
    if md5 == db[username]:
        print('Success!')
    else:
        print('Fail!')
if __name__ == '__main__':
    register('bob', '123')
    login('bob', '123')
    login('bob', '456')