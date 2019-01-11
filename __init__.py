from mycroft import MycroftSkill, intent_file_handler
import googlemaps
from datetime import datetime


class GoogleMapsServices(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        if self.settings.get("google_api_key") is None:
            self.log.info('Missing API key. Go to home.mycroft.ai and enter your google api key')
            exit()
        self.gmaps = googlemaps.Client(key=self.settings["google_api_key"])

    @intent_file_handler('traveltime.intent')
    def handle_services_maps_google(self, message):
        now = datetime.now()
        if message.data.get("fromadr") is None:
            fromadr = "lergravsvej 14"
        else:
            fromadr = message.data.get("fromadr")
        toadr = message.data.get("toadr")
        if message.data.get("mode") is None:
            mode = "driving"
        else:
            mode = message.data.get("mode")
        result = self.gmaps.distance_matrix(fromadr, toadr, mode=mode, departure_time=now)
        answer = result["rows"][0]["elements"][0]["duration"]["text"]
        self.speak_dialog('traveltime', data={'fromadr': fromadr, 'toadr': toadr, 'time': answer, 'mode': "by " + mode})


def create_skill():
    return GoogleMapsServices()

