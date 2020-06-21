# Athletic_Web_Application
 Athletic_Web_Appication is realtime application response within specified time constraints. Realtime computing systems such as, Athletic_Web_Application, are often understood to be in the order of miliseconds. This dynamic application was built with micro web framework, Flask written in Python. Web programming language, Flask does not require third-party libraries to implement in Flask itself. This is the reason Athletic_Web_Application has no database abstraction layer or any other compoents where pre-existing thired-party libraries provide common functions. Extensions are available in Flask in for object-relational mappers, upload handling, various authentication technologies and several common framework related tools. Athletic_Web_Application used obejct-oriented programming(OOP) to let objects to interact with one another. This web application is class-based objects are instance of classes which also determine their types. Flask-SQLAlchemy is normally used as classes in this web-application to let the web available procedures for a given type or class of object. Also it contains data, data procedures(class methods), data members, and member functions. This web application server was built in EC2 Amazon Linux AMI normally known as on demand cloud computing service. Amazon Linux AMI was utilized to provide a set of primitive abstract technical infrastructure and distributed computing building blocks and tools.

## Prerequisites

* Python (3.8.2)
* Flask
* Flask-SQLAlchemy
* Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - type : t2.large, network performance : Low to midium, vCPU : 2, Ipv4 support : available
* Visual Studio Code (Recommended but not obligatory)

## Installing

Step One : Clone the repo without checking out a work tree.
```
git clone -n https://github.com/Shawn-gitman/Athletic_Web_Application
```
Step Two : check out the file.
```
git checkout master -- path/within/repo/to/file
```

## Running the tests

* Run main.py to implement the program moving player ship object. It can controlled by pressing a(left),d(right),w(up),s(down) and space(shoot) key. As the space key is pressed, player ship shoots the lasers to remove enemy object as it is collided. As the enemies are all removed in the stage where player is in, player can step into next level. There are boss rounds as the player reaches to the level multiple of 3. Boss is upsized that are supposed to be the original. It shoots the dual bullet that threat player ship object.

## Break down into end to end tests

No Break down into end to end tests required.

## And coding style tests

No coding style tests required.

## Built With

* Python (3.8.2) : Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
* Pygame (1.9.1) : Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
* Visual Studio Code : Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes embedded Git and support for debugging, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open-source, released under the permissive MIT License. The compiled binaries are freeware for any use.

## Contributing

Please read README.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

No Versioning available.

## Authors

* **Shawn Kang**,  *Initial work*,  *email : taegue52@daum.net*
