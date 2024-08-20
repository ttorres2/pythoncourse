# module = a file containing Python code. May contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts.

import messages as msg #imports the module name and shortens it to msg.
from messages import hello,bye #imports select functions.

msg.hello() #uses function from messages module and executes it.
msg.bye() #same thing.

#allows you to do this:
hello()
bye()

help("modules") #populates a list of available modules.

#you can also find in Python's official documentation for all the different modules and what they do.