import functools

user = {'username': 'jose123', 'access_level': 'user'}

def user_has_permission(func):
    @functools.wraps(func)
    # if user.get('access_level') == 'admin':
    #     return func
    # raise RuntimeError
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)

    return secure_func
    
@user_has_permission
def my_function(panel: str):
    """ 
    Allows us to retrive admin pass
    """
    return f'Password for admin {panel} panel is 1234.'

@user_has_permission
def another():
    return 'Hello'


print(my_function(panel='movies'))

print(another())

# print(my_function.__name__)
# print(my_function.__doc__)
# print(another.__name__)
