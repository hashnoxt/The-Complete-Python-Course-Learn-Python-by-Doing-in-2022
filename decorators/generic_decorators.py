import functools

user = {'username': 'jose123', 'access_level': 'admin'}

def user_has_permission(func):

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)

    return secure_func
    
@user_has_permission
def my_function(panel: str):
    """ 
    Allows us to retrive admin pass
    """
    return f'Password for admin {panel} panel is 1234.'


@user_has_permission
def another():
    return 'Yes'

print(another())