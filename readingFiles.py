from sys import argv

script, filename = argv

#txt = open(filename)
#
#print(f"Here's your file {filename}:")
#print(txt.read())


#• close – Closes the file. Like File->Save.. in your editor.
#• read – Reads the contents of the file. You can assign the result to a variable.
#• readline – Reads just one line of a text file.
#• truncate – Empties the file. Watch out if you care about the file.
#• write('stuff') – Writes ”stuff” to the file.
#• seek(0) – Move the read/write location to the beginning of the file.

#txt = open(filename, 'w')
#
## delete the content
#txt.truncate()
#
#line1 = input('line 1: ')
#line2 = input('line 2: ')
#line3 = input('line 3: ')
#
#txt.write(line1)
#txt.write(line2)
#txt.write(line3)