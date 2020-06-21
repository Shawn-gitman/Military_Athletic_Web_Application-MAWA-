# Athletic_Web_Application(Major features : Authentication, CRUD, Comment functions)
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

* Run main.py to implement Athletic_Web_Application. Enroll membership from enroll box in 127.0.0.0/main. As soon as, user registered to this web-application, find menu_icon on right-top to access login service(127.0.0.0/login). Users are available to use CRUD(create, read, update, delete) service by entering third option from the navigation bar. Writing comments are available for each post whenever users intend. All comment datas are deleted as the post had deleted. See roulette service(127.0.0.0/lottery) from fourth option, to set up strngth(Low, midium, high) and start running the feature.

## Break down into end to end tests

No Break down into end to end tests required.

## And coding style tests

No coding style tests required.

## Built With

* Python (3.8.2) : Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
* Flask : Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[3] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more frequently than the core Flask program.
* Flask-SQLAlcehmy : SQLAlchemy is an open-source SQL toolkit and object-relational mapper (ORM) for the Python programming language released under the MIT License.
* EC2(Amazon Elastic Compute Cloud) : EC2 is a part of Amazon.com's cloud-computing platform, Amazon Web Services (AWS), that allows users to rent virtual computers on which to run their own computer applications. EC2 encourages scalable deployment of applications by providing a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which Amazon calls an "instance", containing any software desired. A user can create, launch, and terminate server-instances as needed, paying by the second for active servers – hence the term "elastic". EC2 provides users with control over the geographical location of instances that allows for latency optimization and high levels of redundancy.
* Visual Studio Code : Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes embedded Git and support for debugging, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open-source, released under the permissive MIT License. The compiled binaries are freeware for any use.

## Contributing

Please read README.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

* 1.0.0 - Accessing bugs updated
* 1.0.1 - Login problems updated
* 1.0.2 - Permanent Session(to 5days) updated

## Authors

* **Shawn Kang**,  *Initial work*,  *email : taegue52@daum.net*
