#Game plan

to add import support across languages:

for python import sys

sys.modules <- gives you a dict of all modules loaded into memory.  

Class interoperatibility:

a class written in python should be usable in ruby.  This means translating all key words in python to all keys in ruby (for instance).  Should be true of C++, Java, etc.

Create a tmp file for each class, do the translation while writing to the file.  Then import the object into the current namespace.

