from replit.web import user


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(func):
    def wrap(*args, **kwargs):
        if args[0].is_logged_in==True:
            func(args[0])
    return wrap
@is_authenticated_decorator
def crete_blog_post(user):
    print(f"this is {user.name}'s new blog post")

new_user = User("shayan")
new_user.is_logged_in = True
crete_blog_post(new_user)