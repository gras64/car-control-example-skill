from mycroft import MycroftSkill, intent_file_handler


class CarControlExample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        ### list off all possible funktions. uncomment to deaktivate
        self.register_intent_file('light.on.intent', self.handle_light_on)
        self.register_intent_file('light.off.intent', self.handle_light_off)
        self.register_intent_file('start.loading.intent', self.handle_start_loading)
        self.register_intent_file('stop.loading.intent', self.handle_stop_loading)
        self.register_intent_file('batt.state.intent', self.handle_batt_state)
        self.register_intent_file('temperature.up.intent', self.handle_temperature_up)
        self.register_intent_file('temperature.down.intent', self.handle_temperature_down)
        self.register_intent_file('set.cruise.control.intent', self.handle_set_cruise_control)
        self.register_intent_file('unset.cruise.control.intent', self.handle_unset_cruise_control)
        self.register_intent_file('set.leds.intent', self.handle_set_leds)
        self.register_intent_file('leds.off.intent', self.handle_leds_off)
        self.register_intent_file('windshield.wipers.on.intent', self.handle_windshield_on_wipers)
        self.register_intent_file('windshield.wipers.off.intent', self.handle_windshield_off_wipers)
        self.register_intent_file('windshield.wipers.faster.intent', self.handle_windshield_faster_wipers)
        self.register_intent_file('windshield.wipers.lower.intent', self.handle_windshield_lower_wipers)

    def handle_light_on(self, message):
        self.speak_dialog('light.on')

    def handle_light_off(self, message):
        self.speak_dialog('light.off')

    def handle_start_loading(self, message):
        percent = "30"
        self.speak_dialog('start.loading', data={'percent':percent})

    def handle_stop_loading(self, message):
        percent = "30"
        self.speak_dialog('stop.loading', data={'percent':percent})

    def handle_batt_state(self, message):
        percent = "30"
        range = "120"
        self.speak_dialog('bat.state', data={'percent':percent, 'range':range})

    def handle_temperature_up(self, message):
        temperature = "20"
        self.speak_dialog('temperature', data={'temperature':temperature})

    def handle_temperature_down(self, message):
        temperature = "20"
        self.speak_dialog('temperature', data={'temperature':temperature})

    def handle_set_cruise_control(self, message):
        speed = "120"
        self.speak_dialog('set.cruise.control', data={'speed':speed})

    def handle_unset_cruise_control(self, message):
        self.speak_dialog('unset.cruise.control')

    def handle_set_leds(self, message):
        color = "red"
        self.speak_dialog('leds', data={'red':red})

    def handle_leds_off(self, message):
        self.speak_dialog('leds.off')

    def handle_windshield_on_wipers(self, message):
        speed = "3"
        self.speak_dialog('windshield.wipers', data={'speed':speed})

    def handle_windshield_off_wipers(self, message):
        speed = "0"
        self.speak_dialog('windshield.wipers', data={'speed':speed})

    def handle_windshield_faster_wipers(self, message):
        speed = "4"
        self.speak_dialog('windshield.wipers', data={'speed':speed})

    def handle_windshield_lower_wipers(self, message):
        speed = "1"
        self.speak_dialog('windshield.wipers', data={'speed':speed})



def create_skill():
    return CarControlExample()

