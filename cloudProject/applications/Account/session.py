from cloudProject.applications.Account.cachiersm import Connection_cache


class Session():
    def do_login(self, user_id):
        id = str(user_id)
        logged_users = Connection_cache().get('logged')
        if not logged_users:
            logged_users = []
            try:
                logged_users.index(id)
            except ValueError:
                logged_users.append(id)
                Connection_cache().set('logged', logged_users)
