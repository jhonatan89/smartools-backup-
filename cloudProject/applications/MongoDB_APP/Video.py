from cloudProject.applications.MongoDB_APP.connection_params import Connection

from bson.objectid import ObjectId

class Competition():

    clientfirtsName = ""
    clientLastName = ""
    clientEmail = ""
    title = ""
    description = ""
    uploadDate = ""
    originalVideoPath = ""
    convertedVideoPath = ""
    state = ""


    def create(self, clientfirtsName, clientLastName, clientEmail, title, description, uploadDate,
               originalVideoPath, convertedVideoPath, state):

        video = {
            'clientfirtsName' : clientfirtsName,
            'clientLastName' : clientLastName,
            'clientEmail' : clientEmail,
            'title' : title,
            'description' : description,
            'uploadDate' : uploadDate,
            'originalVideoPath' : originalVideoPath,
            'convertedVideoPath' : convertedVideoPath,
            'state' : state
        }

        id_competition = Connection().db.Video.insert_one(video).inserted_id