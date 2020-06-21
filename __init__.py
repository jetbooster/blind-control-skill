from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from blind_control import BlindController


class BlindControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        ha_host = self.settings.get('ha_host')
        ha_port = self.settings.get('ha_port')
        api_key = self.settings.get('api_key')
        self.blind_controller = BlindController(ha_host,ha_port,api_key)
        self.register_intent_file('set.blind.intent', self.handle_set_blind)

    @intent_handler(IntentBuilder('Open').require('Blind').require('Open').require('Location'))
    def handle_open_blind(self, message):
        self.speak(f"Opening {location} blind")
        location = message.data.get('Location')
        self.blind_controller.set_blind_state(location,0)

    @intent_handler(IntentBuilder('Close').require('Blind').require('Close').require('Location'))
    def handle_close_blind(self, message):
        self.speak(f"Closing {location} blind")
        location = message.data.get('Location')
        self.blind_controller.set_blind_state(location,10)

    @intent_handler('set.blind.intent')
    def handle_set_blind(self, message):
        location = message.data.get('location')
        number = message.data.get('number')
        self.speak(f"Moving blind to {number}")
        self.log.info(f'Location: {location}, Number: {number}')
        print(f'Location: {location}, Number: {number}')
        self.blind_controller.set_blind_state(location,number)


def create_skill():
    return BlindControl()

