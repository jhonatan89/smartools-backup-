from cloudProject.applications.MongoDB_APP.connection_params import Connection

from bson.objectid import ObjectId
from datetime import datetime

class Video():

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
            'uploadDate' : datetime.now().strftime(),
            'originalVideoPath' : originalVideoPath,
            'convertedVideoPath' : '',
            'state' : 'WFC'
        }

        id_video = Connection().db.Video.insert_one(video).inserted_id

        videos = Connection().db.Competition.find_one({ "_id" : ObjectId(id_competition)})['videos']
        videos.append(id_video)
        Connection().db.Competition.update( { "_id" : ObjectId(id_competition) }, { "$set" : { 'videos' : videos } } )

