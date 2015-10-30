from cloudProject.applications.MongoDB_APP.connection_params import Connection

from bson.objectid import ObjectId
from datetime import datetime

class Video():

    id=""
    clientfirtsName = ""
    clientLastName = ""
    clientEmail = ""
    title = ""
    description = ""
    uploadDate = ""
    originalVideoPath = ""
    convertedVideoPath = ""
    state = ""

    def create(self, id_competition, clientfirtsName, clientLastName, clientEmail, title, description,
               originalVideoPath):

        video = {
            'clientfirtsName' : clientfirtsName,
            'clientLastName' : clientLastName,
            'clientEmail' : clientEmail,
            'title' : title,
            'description' : description,
            'uploadDate' : datetime.now(),
            'originalVideoPath' : originalVideoPath,
            'convertedVideoPath' : '',
            'state' : 'WFC'
        }

        id_video = Connection().db.Video.insert_one(video).inserted_id

        videos = Connection().db.Competition.find_one({ "_id" : ObjectId(id_competition)})['videos']
        videos.append(id_video)
        Connection().db.Competition.update( { "_id" : ObjectId(id_competition) }, { "$set" : { 'videos' : videos } } )

    def get(self, id, status):
        if status=="ANY":
            video = Connection().db.Video.find_one({'_id' : ObjectId(id)})
        elif status =="CON":
            video = Connection().db.Video.find_one({'_id' : ObjectId(id), 'state':'CON'})
        else:
            video = Connection().db.Video.find_one({'_id' : ObjectId(id)})

        print "video"

        if video:
            self.id = id
            self.clientfirtsName = video['clientfirtsName']
            self.clientLastName = video['clientLastName']
            self.clientEmail = video['clientEmail']
            self.title = video['title']
            self.description = video['description']
            self.uploadDate = video['uploadDate']
            self.originalVideoPath = video['originalVideoPath']
            self.convertedVideoPath = video['convertedVideoPath']
            self.state = video['state']
        else:
            self.description="62e12228-200e-4160-b3b7-571fdd70d434"

    def get_all_by_ids(self, videos_ids, status):
        videos = []

        for current_id_video in videos_ids:
            obj_video = Video()
            obj_video.get(current_id_video, status)

            if obj_video.description!="62e12228-200e-4160-b3b7-571fdd70d434":
                print "video appended"
                videos.append(obj_video)

        return videos

