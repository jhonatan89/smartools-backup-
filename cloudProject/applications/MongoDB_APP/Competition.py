from cloudProject.applications.MongoDB_APP.connection_params import Connection

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
        print "Method get:"
        print "id:"
        print id
        competition = Connection().db.Competition.find_one({'_id' : ObjectId(id)})

        self.id = id
        self.name = competition['name']
        self.image = competition['image']
        self.startDate = competition['startDate']
        self.endDate = competition['endDate']
        self.description = competition['description']
        self.url = competition['url']
        self.active = competition['active']
        self.videos = []

    def get_all(self):
        competitions_ids = Connection().db.Competition.find({'active' : 'true' })['_id']
        return self.get_all_by_ids(competitions_ids)

    def get_all_by_ids(self, competitions_ids):
        competitions = []

        for current_id_competition in competitions_ids:
            self.get(current_id_competition)

            competitions.append(self)
        print "Method:get_all_by_ids"
        print "competitions"
        print competitions
        return competitions

    def update(self, id, name, description):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'name' : name, 'description' : description } })

    def finish(self, id):
        Connection().db.Competition.update({"_id" : id }, {"$set": {'active' : 'false'} })
