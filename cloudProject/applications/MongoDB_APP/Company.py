from cloudProject.applications.MongoDB_APP.connection_params import Connection
from cloudProject.applications.MongoDB_APP.Competition import Competition

class Company():

    companyName = ""
    username = ""
    email = ""
    password = ""
    competitions = []

    def create(self, companyName, username, email, password):
        conn = Connection()

        company = {
            'companyName' : companyName,
            'username' : username,
            'email' : email,
            'password' : password,
            'competitions' : []
        }

        conn.db.Company.insert(company)

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

    def get_competitions(self, username):

        competitions_ids = Connection().db.Company.find_one({ "username" : username, 'active' : 'true' })['competitions']
        self.competitions = Competition().get_all_by_ids(competitions_ids)

