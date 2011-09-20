HSR Tools
=========

HSR Tools is a collection of scripts and tools to simplify life at the
[University of Applied Sciences](http://hsr.ch/) in Rapperswil, Switzerland.

Currently all scripts are written in Python.

Sources can be found at https://github.com/gwrtheyrn/HSR-Tools.


Tools
-----

### hsrmount.py ###

This is a script to simplify mounting of server folders onto your system.

### stundenplan.py ###

This tool queries the https://unterricht.hsr.ch/ website for the current
timetable (Stundenplan) and lists the lectures for the chosen day.


Library
-------

HSR Tools includes a small library that provides common functions that all the
scripts can import and use. You can use it too, if you want to create your own
script.

### config/auth.py ###

This module is used to get user credentials. The username is stored in the main
configuration file. The massword may or may not be stored. If it isn't, the
user is prompted to enter it each time a tool needs to access it.

Usage:

```python
from config import auth
username, password = auth.userinfo()
```


License
-------

All the tools are put under the [LGPLv3](http://www.gnu.org/licenses/lgpl.html)
license, so that everyone can benefit from improvements. Feel free to send me
a pull request on Github if you improved one of the scripts.


Disclaimer
----------

All the scripts are inofficial are not supported by the HSR.
