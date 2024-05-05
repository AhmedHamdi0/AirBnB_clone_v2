# `AirBnB Clone v2 - The Console`

![Console](../assets/console.png)

## `Description`
The HBNB Command Interpreter is a command-line tool designed to interact with
a data storage system for managing instances of classes in a Python application.
It provides functionalities such as creating, showing, destroying, updating, and counting instances.

## `Commands`
| Command              | Description                                                                  |
|----------------------|------------------------------------------------------------------------------|
| `create`             | Creates an instance based on given class                                     |
| `destroy`            | Destroys an object based on class and UUID                                   |
| `show`               | Shows an object based on class and UUID                                      |
| `all`                | Shows all objects the program has access to, or all objects of a given class |
| `update`             | Updates existing attributes an object based on class name and UUID           |
| `count`              | Return number of object instances by class                                   |
| `quit`               | Exits the program (EOF will as well)                                         |
| `help`               | Help info for all commands                                                   |

## `Installation`
```shell
$ git clone https://github.com/AhmedHamdi0/AirBnB_clone_v2.git
```
```shell
/AirBnB_clone_v2$ ./console
```


## `Usage`

- `create <class name>` or `<class name>.create()`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) User.create()
38f22813-2753-4d42-b37c-57a17f1e4f88
(hbnb) 
```

- `show <class name> <instance id>` or `<class name>.show(<instance id>)` 
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {
    'first_name': 'Betty',
    'last_name': 'Bar', 
    'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 
    'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 
    'password': '63a9f0ea7bb98050796b649e85481845', 
    'email': 'airbnb@mail.com', 
    'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'
}
(hbnb) User.show("Bar")
** no instance found **
(hbnb) 
```

- `all <class name>` or `<class name>.all()`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) User.all()
[
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {
    'first_name': 'Betty', 
    'last_name': 'Bar',
    'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 
    'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363),
    'password': '63a9f0ea7bb98050796b649e85481845',
    'email': 'airbnb@mail.com',
    'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'
    },
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {
  'first_name': 'Betty', 
  'last_name': 'Bar', 
  'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 
  'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 
  'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 
  'email': 'airbnb@mail.com', 
  'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'
  }
]
(hbnb) 
```

- `count <class name>` or `<class name>.count()`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) count User
2
(hbnb) User.count()
2
(hbnb) 
```

- `<class name>.update(<id>, <attribute name>, <attribute value>)`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {
    'first_name': 'Betty',
    'last_name': 'Bar',
    'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 
    'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 
    'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 
    'email': 'airbnb@mail.com', 
    'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'
}
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {
    'age': 89,
    'first_name': 'John', 
    'last_name': 'Bar',
    'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 
    'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 
    'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 
    'email': 'airbnb@mail.com', 
    'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'
}
(hbnb) 
```

- `destroy <class name> <instance id>` or `<class name>.destroy(<instance id>)`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb) 
```

- `<class name>.update(<id>, <dictionary representation>)`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {
    'age': 23,
    'first_name': 'Bob',
    'last_name': 'Bar',
    'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279),
    'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 
    'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 
    'email': 'airbnb@mail.com',
    'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'
}
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {
    'age': 89, 
    'first_name': 'John', 
    'last_name': 'Bar',
    'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279),
    'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 
    'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 
    'email': 'airbnb@mail.com', 
    'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'
}
(hbnb) 
```

- `help` or `help <command name>`
```shell
~/AirBnB_clone_v2$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) help create
Creates an instance.
(hbnb) help show
Prints the string representation of an instance.
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
$
```


## `Testing`
```shell
~/AirBnB_clone_v2$ python3 -m unittest discover tests
....................................................................................
....................................................................................
..............................
----------------------------------------------------------------------
Ran 198 tests in 1.918s

OK
~/AirBnB_clone_v2$ echo "python3 -m unittest discover tests" | bash
....................................................................................
....................................................................................
..............................
----------------------------------------------------------------------
Ran 198 tests in 1.904s

OK
~/AirBnB_clone_v2$
```
