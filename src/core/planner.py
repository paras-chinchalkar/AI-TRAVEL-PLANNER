from langchain_core.messages import HumanMessage
from src.chains.initenery_chain import generate_itinerary

from src.utils.logger import get_logger

from src.utils.custom_exception import CustomException

Logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self,city:str,intrests:list):
        self.messages=[]
        self.city=city
        self.intrests=intrests
        self.itenary=""
        Logger.info("Initilized the teavel planner")

    def set_city(self,city:str):
        try:
            self.city=city
            self.messages.append(HumanMessage(content=f"Set the city to {city}")    )
            Logger.info(f"The city  has beenset successfully")
        except Exception as e:
            Logger.error(f"error while setting city: {e}")
            raise CustomException("Failed to set as an city", e)
        
    def set_intrests(self,intrests_str:str):
        try:
            self.intrests=[i.strip() for i in intrests_str.split(",")]
            self.messages.append(HumanMessage(content=intrests_str))
            Logger.info(f"the info  has be set succesffuly  in here")
        except Exception as e:
            Logger.error(f"The error in here is not being set: {e}")
            raise CustomException("Failed to add city right here", e)
    def create_itenary(self):
        try:
            Logger.info(f"Generating the the itenary for {self.city} and for itnrests : {self.intrests}")
            iternary = generate_itinerary(self.city,self.intrests)
            self.itenary=iternary
            self.messages.append(HumanMessage(content=iternary))
            Logger.info(f"The itenary  has been successfully installed")
            return iternary
        except Exception as e:
            Logger.error(f"Error while generating iternary :{e}")
            raise CustomException("failed to generate the iternary", e)





