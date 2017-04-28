#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf file.
#        py.exe mcb.pyw clear - Deletes all keywords from shelf file.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete keyword from shelf file
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    try:
        del mcbShelf[sys.argv[2]]
    except KeyError:
        print('Key unknown, cannot delete.')
elif len(sys.argv) == 2:
    # List keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Delet all keywords if 'clear' is passed
    elif sys.argv[1].lower() == 'clear':
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]
    # Load content to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
