from cloudProject.applications.Account.cachiersm import Connection_cache


class Session():
    def do_login(self, user_id):
        print "llego al login"
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        if not logged_users:
            logged_users = []
        try:
            logged_users.index(id)
        except ValueError:
            logged_users.append(id)
            Connection_cache().set_cache('logged', logged_users)