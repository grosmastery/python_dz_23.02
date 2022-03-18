import os
import csv
import requests


TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
USERS_URL = 'https://jsonplaceholder.typicode.com/users'


def get_users(user: str) -> list:
    user_request = requests.get(user)
    users = user_request.json()
    return users

def get_todos(todo: str) -> list:
    todo_request = requests.get(todo)
    todos = todo_request.json()
    return todos

def main(user: str, todo: str) ->None:
    count = 0
    username = get_users(user)
    todos = get_todos(todo)
    os.makedirs('users', exist_ok=True)
    for users in username:
        with open(os.path.join('users', f'{users["id"]} - {users["username"]}.csv'), 'w', encoding='utf8') as f:
            for does in todos:
                if does['userId'] == users['id']:
                    fieldnames = ['id', 'title', 'completed']
                    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                    if count == 0:
                        writer.writeheader()
                        writer.writerow(does)
                        count +=1
                    elif count == 1:
                        writer.writerow(does)




if __name__ in '__main__':
    main(USERS_URL, TODOS_URL)