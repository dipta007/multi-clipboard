#! python3
# mcb.py - Saves and loads pieces of data from clipboard
# Usage -
#       python3 mcb.py save <keyword> - save data from clipboard to <keyword>
#       python3 mcb.py del  <keyword> - delete the data from clipboard associated with <keyword>
#       python3 mcb.py load <keyword> - load the data in clipboard associated with <keyword>
#       python3 mcb.py list           - list all the keywords

import shelve
import pyperclip
import sys


mcbshelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbshelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "del":
    del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 3 and sys.argv[1].lower() == "load":
    pyperclip.copy(mcbshelf.get(sys.argv[2], default="NONE"))
else:
    print(str(list(mcbshelf.keys())))
