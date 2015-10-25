from cloudProject.applications.MongoDB_APP.connection_params import Connection

from bson.objectid import ObjectId

class Competition():

    name = ""
    image = ""
    startDate = ""
    endDate = ""
    description = ""
    url = ""
    active = ""
    videos = []

    def create(self, username, name, image, startDate, endDate, description, url, active ):

        competition = {
            'name' : name,
            'image' : image,
            'startDate' : startDate,
            'endDate' : endDate,
            'description' : description,
            'url' : url,
            'active' : active,
            'videos' : []
        }

        id_competition = Connection().db.Competition.insert_one(competition).inserted_id
        self.update_url(id_competition, "/competitions/" + str(id_competition))

        competitions = Connection().db.Company.find_one({ "username" : username})['competitions']
        competitions.append(id_competition)
        Connection().db.Company.update( { "username" : username }, { "$set" : { 'competitions' : competitions } } )

    def update_url(self, id, url):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'url':url}})

    def get(self, id):
        competition = Connection().db.Competition.find_one({'_id' : ObjectId(id), "active" : "true"})
        print competition

        self.name = competition['name']
        self.image = competition['image']
        self.startDate = competition['startDate']
        self.endDate = competition['endDate']
        self.description = competition['description']
        self.url = competition['url']
        self.active = competition['active']
        self.videos = []

    def get_all(self):
        competitions_ids = Connection().db.Company.find({'active' : 'true' })['_id']
        return self.get_all_by_ids(competitions_ids)

    def get_all_by_ids(self, competitions_ids):
        competitions = []

        for current_id_competition in competitions_ids:
            self.get(current_id_competition)
            competitions.append(self)

        return competitions

    def update(self, id, name, description):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'name' : name, 'description' : description } })

    def finish(self, id):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'active' : 'false'} })
