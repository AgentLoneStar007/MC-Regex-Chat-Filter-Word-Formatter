# Defines the function that splits the input into individual characters in a list.
def split(word):
    return [char for char in word]

# Opens the file, and assigns the words inside to a list.
with open("input.txt", "r") as file:
    inputArgs = file.read()#.splitlines()
    data = split(inputArgs)

# Adds Regex formatting to the characters in the list.
data2 = [char + '+(\W|\d|_)*' for char in data]

# Fixes any broken "\n" statements, and adds a ) to the end of each word/line, and adds "- \b(" to it.
for n, i in enumerate(data2):
    if i == '\n+(\\W|\\d|_)*':
        data2[n] = ')\n- ?b('

# Adds "- \b" to the first character.
data2[0] = '- ?b(' + data2[0]

# Fixes the last "\n" so it correctly formats.
if data2[-1] == ')\n- ?b(':
    data2[-1] = ')\n'

# Converts the list back into a string.
output = ''.join(data2)

# Writes the output to a file named "output.txt."
with open("output.txt", "w") as file2:
    file2.write(output)

print('Words successfully formatted.')
