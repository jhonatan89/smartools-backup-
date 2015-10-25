from cloudProject.applications.Account.Cookie_utils import delete_cookie
from cloudProject.applications.Account.cachiersm import Connection_cache


class Session():
    @staticmethod
    def do_login(user_id):
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        if not logged_users:
            print "creo array"
            logged_users = []
        try:
            logged_users.index(id)
        except ValueError:
            logged_users.append(id)
            Connection_cache().set_cache('logged', logged_users)

    @staticmethod
    def do_logout(response,user_id):
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        if logged_users:
            logged_users.remove(id)
            Connection_cache().set_cache('logged', logged_users)
            delete_cookie(response,user_id)

    @staticmethod
    def verify_current_session(user_id):
        print "llego al verify" + user_id
        id = str(user_id)
        logged_users = Connection_cache().get_cache('logged')
        print logged_users
        if logged_users:
            try:
                logged_users.index(id)
                user = {'isverify': True,'name': user_id}
                return user
            except:
                user = {'isverify': False,'name': ""}
                return user
        else:
            return {'isverify': False,'name': ""}