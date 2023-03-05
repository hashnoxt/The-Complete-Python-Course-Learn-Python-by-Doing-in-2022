import functools

user = {'username': 'jose123', 'access_level': 'admin'}

def third_level(access_level: str):

    def user_has_permission(func):
        @functools.wraps(func)
        # if user.get('access_level') == 'admin':
        #     return func
        # raise RuntimeError
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return user_has_permission
    
@third_level('admin')
def my_function(panel: str):
    """ 
    Allows us to retrive admin pass
    """
    return f'Password for admin {panel} panel is 1234.'

"""

user_has_permission = third_level('admin')

my_function = user_has_permission(my_function)

Meaning of @third_level

"""
print(my_function.__name__)

print(my_function('movies'))
