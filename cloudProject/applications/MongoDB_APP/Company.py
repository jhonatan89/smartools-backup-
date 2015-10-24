from cloudProject.applications.MongoDB_APP.connection_params import Connection

class Company():

    companyName = ""
    username = ""
    email = ""
    password = ""

    def create(self, companyName, username, email, password):
        print "to connect"
        conn = Connection()
        print "conected"
        client = {
            'companyName' : companyName,
            'username' : username,
            'email' : email,
            'password' : password
        }
        print "client"
        print client

        conn.db.Company.insert(client)

    def username_exist(self, username):
        connection = Connection()
        user_count = connection.db.Company.find({ "username" : username }).count()

        if user_count > 0:
            return True
        else :
            return False

    def validate_signin(self, username,password):
        connection = Connection()

        user_count = connection.db.Company.find({ "username" : username, "password": password }).count()

        if user_count > 0:
            return True
        else :
            return False

    def get_id_by_username(self, username):
        connection = Connection()
        return connection.db.Company.find_one({ "username" : username })['_id']
