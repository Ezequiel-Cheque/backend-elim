from ..dto import team_create_schema, teamCreate, team_points, teamPoints
from ..models import Teams
from ..exceptions.catalogue_exceptions import CatalogsExceptions

class Teams_service:

    def create(self, body: team_create_schema):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        body = teamCreate.create(body)

        result = Teams.save(**body)

        create_response["data"] = result
        
        return create_response
    
    def getPositions(self):
        teams = Teams.get_all()
        result = sorted(teams, key=lambda team: team['point'], reverse=True)
        return result
    
    def addPoints(self, body: team_points):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        team = Teams.get_by_id(body.team)
        
        if not team:
            CatalogsExceptions.userNotExist()

        newPoints = team['point']+body.point
        # positions = self.getPositions()
        # newPosition = 0
        # for index, value in enumerate(positions):
        #     if newPoints > value['point']:
        #         newPosition = index+1
        #         break

        result = Teams.updatePoints(id=body.team, points=newPoints, position=0)

        create_response["data"] = result
        
        return create_response

    def get_all(self):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None

        teams = Teams.get_all()

        for team in teams:
            team["id"] = str(team["_id"])
            del team["_id"]

        create_response["data"] = teams
        
        return create_response

    def get_by_id(self, id: str):
        create_response = {}
        create_response["success"] = True
        create_response["data"] = None
        
        team = Teams.get_by_id(id)
        
        if not team:
            CatalogsExceptions.userNotExist()

        team["id"] = str(team["_id"])
        del team["_id"]
        create_response["data"] = team
        
        return create_response
  
    def delete(self, id: str):
        delete_response = {}
        delete_response["success"] = True
        delete_response["data"] = None
        
        team = Teams.get_by_id(id)
        
        if not team:
            CatalogsExceptions.userNotExist()
        
        result = Teams.delete_user(id)
        
        delete_response["data"] = {
            "message": "User delete successfully",
            "id": id
        }

        return delete_response
