from mycroft import MycroftSkill, intent_file_handler


class CarControlExample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('example.control.car.intent')
    def handle_example_control_car(self, message):
        self.speak_dialog('example.control.car')


def create_skill():
    return CarControlExample()

