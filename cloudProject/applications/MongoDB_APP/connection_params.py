from pymongo import MongoClient

class Connection():

    client = MongoClient('mongodb://smart:focus2015@ds041154.mongolab.com:41154/smarttoolstest?connectTimeoutMS=30000&authMechanism=SCRAM-SHA-1')
    #client = MongoClient('ds041154.mongolab.com:41154')
    #db = client.smarttoolstest.authenticate('smart', 'focus2015', mechanism='SCRAM-SHA-1')

    db = client.smarttoolstest

    def set_client(self, host, port):
        self.client = MongoClient(host, port)

    def set_database(self, database):
        self.db = self.client[database]
