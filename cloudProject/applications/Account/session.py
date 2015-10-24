from django.core.cache import cache


class Session():
    def do_login(self, user_id):
        id = str(user_id)
        logged_list = cache.get('logged')
        if not logged_list:
            logged_list = []
            try:
                logged_list.index(id)
            except ValueError:
                logged_list.append(id)
                cache.set('logged', logged_list)
