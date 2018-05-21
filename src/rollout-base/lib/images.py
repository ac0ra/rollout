#!/bin/env python
#
___author__ = 'Adam Grigolato'
__version__ = '0'
#IMPORTS

#


# Classes

class backup(object):
    def __init__(self, output, name):
        self.name = name
        self.output = output

    def write_out(data):
        output.write(data)


class stage4(backup):
    def __init__(self, name, filename):
        import tarfile
        output = tarfile.open(filename, "w:gz")
        backup.__init__(self, output, name)

    def write_out(filelist):
        for file in filelist:
            output.add(file)

