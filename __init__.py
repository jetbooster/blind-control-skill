from mycroft import MycroftSkill, intent_file_handler


class BlindControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.blind.intent')
    def handle_control_blind(self, message):
        self.speak_dialog('control.blind')


def create_skill():
    return BlindControl()

