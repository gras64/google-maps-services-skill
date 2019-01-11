from mycroft import MycroftSkill, intent_file_handler


class GoogleMapsServices(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('services.maps.google.intent')
    def handle_services_maps_google(self, message):
        self.speak_dialog('services.maps.google')


def create_skill():
    return GoogleMapsServices()

