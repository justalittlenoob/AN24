import DataHandler, Patient
class UiData():
    def __init__(self, uuid, name):
        self.data_handler= DataHandler.DataHandler()
        self.patient = Patient.Patient()
        self.uuid = uuid
        self.name = name
        self.name = name
        self.all_battry_time = 10.0
        self.rest_battry_time = 0
        self.start_time = 0               
        self.draw_current_time = 0
        self.is_detecting = False
        self.is_infoed = False
        self.is_connected = False
        self.is_checked = False
        self.end_count_pre = 0        


if __name__ == '__main__':
    an24 = UiAN24('likun', 'fdsafsaf')
    print an24.patient.age
