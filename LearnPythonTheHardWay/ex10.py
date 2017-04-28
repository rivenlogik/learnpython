# Variables with different escape characters
# \t = tab
# \n = newline
# \a = bell
# \r = carriage return (beginning of current line)
# \\ = backslash
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ /a \\ cat."

# Extended text with triple single or double quotes (matter of style)
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies/
\t* Catnip\n\t* Grass
"""

# Printing variables out either directly or with %s or %r
# %r = programmer's output to see raw output
# %s = normal string
print "%r" % tabby_cat
print persian_cat
print backslash_cat
print "%s" % fat_cat

# Fun text loop
# The \r placement matters, as it will put whatever comes AFTER it
# at the beginning of the line
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r Processing..." % i,
