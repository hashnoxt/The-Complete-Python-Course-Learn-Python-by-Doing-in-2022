# my_var = 4
# print(my_var['key'])
#

class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = MyCustomError('An error happend', 500)
print(err.__doc__) # print a doc string

# raise MyCustomError('OuCH! An error happened', 500)
"""
try : Method to check
except <Error> : Error to raise
finally: always run
"""