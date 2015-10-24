from cloudProject.applications.Account.cachiersm import Connection_cache


class Session():
    @staticmethod
    def do_login(user_id):
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

    def do_logout(self, user_id):
        print "llego al logout"
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        if logged_users:
            logged_users.remove(id)
            Connection_cache().set_cache('logged', logged_users)

    @staticmethod
    def verify_current_session(self, user_id):
        print "llego al verify" + user_id
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        print logged_users
        if logged_users:
            try:
                logged_users.index(id)
                print "llego a logged"
                return True
            except:
                print "llego a exception"
                return False
        else:
            print "porqueee"
            return False