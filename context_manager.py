
from contextlib import contextmanager


##
##class Open_File():
##    def __init__(self, filename, mode): #mode is for read/write
##        self.filename = filename
##        self.mode = mode
##
##        
##    def __enter__(self):
##        self.file = open(self.filename, self.mode)
##
##        return self.file
##    def __exit__(self, exc_type, exc_val, traceback): #other parameters are for exceptions
##        self.file.close()
##
##
##with Open_File('sample.txt', 'w') as f:
##    f.write('Testing_123')
##
##print(f.closed)


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor')
