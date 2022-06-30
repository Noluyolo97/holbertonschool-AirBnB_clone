#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.city import City
# from models.place import Place --manque
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    """ console class """


prompt = "(hbnb)"
# mise en place des functionnalites de notre console -interpreter
# create -update -destroy -all (SHOW all instances saved)-quit- EndOfFIle (EOF)


def do_quit(self, arg):
    """quit the program"""
    return True


def do_EOF(self, arg):
    """Quit the program"""

    print('')
    return True


# fin du programme de la  console
if __name__ == '__main__':
    HBNBCommand().cmdloop()