from cloudProject.applications.MongoDB_APP.connection_params import Connection
from cloudProject.applications.MongoDB_APP.Video import Video

from bson.objectid import ObjectId

from django.utils.encoding import smart_unicode

class Competition():

    id = ""
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

    def __unicode__(self):
        title = "%s" % (smart_unicode(self.name))
        return title

    def get_competition_url(self):
        # return "http://" + platform.node() + ":8000" + "/competitions/%s/" % (self.id)
        return "/competitions/%s/show/" % (self.id)

    def get_finish_competition_url(self):
        return "/competitions/%s/finish/" % (self.id)

    def get_edit_competition_url(self):
        return "/competitions/%s/edit/" % (self.id)

    def get_upload_video_url(self):
        return "/competitions/%s/upload/" % (self.id)

    def update_url(self, id, url):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'url':url}})

    def get(self, id):
        competition = Connection().db.Competition.find_one({'_id' : ObjectId(id), 'active':'true'})

        if competition :
            self.id = id
            self.name = competition['name']
            self.image = competition['image']
            self.startDate = competition['startDate']
            self.endDate = competition['endDate']
            self.description = competition['description']
            self.url = competition['url']
            self.active = competition['active']
            self.videos = []
        else:
            self.name="62e12228-200e-4160-b3b7-571fdd70d434"

    def mongo_to_model(self, competition):
        self.id = competition['_id']
        self.name = competition['name']
        self.image = competition['image']
        self.startDate = competition['startDate']
        self.endDate = competition['endDate']
        self.description = competition['description']
        self.url = competition['url']
        self.active = competition['active']
        self.videos = []

    def get_all(self):
        competitions_ids = Connection().db.Competition.find({'active' : 'true' })
        competitions = []

        for current_id_competition in competitions_ids:
            obj_competition = Competition()
            obj_competition.mongo_to_model(current_id_competition)
            competitions.append(obj_competition)

        return competitions

    def get_all_by_ids(self, competitions_ids):
        competitions = []

        for current_id_competition in competitions_ids:
            obj_competition = Competition()
            obj_competition.get(current_id_competition)

            if obj_competition.name!="62e12228-200e-4160-b3b7-571fdd70d434":
                competitions.append(obj_competition)

        return competitions

    def update(self, id, name, description):
        Connection().db.Competition.update({"_id" : ObjectId(id) }, {"$set": {'name' : name, 'description' : description } })

    def finish(self, id):
        Connection().db.Competition.update({"_id" : ObjectId(id) }, {"$set": {'active' : 'false'} })

    def get_videos(self,id, status):
        competitions_ids = Connection().db.Competition.find_one({ "_id" : ObjectId(id) })['videos']
        self.videos = Video().get_all_by_ids(competitions_ids, status)
