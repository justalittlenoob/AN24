import AN24
class UiAN24():
    def __init__(self, name, address):
        self.rawAN24= AN24.AN24(address)
        self.address = address
        self.name = name
        self.all_battry_time = 10.0
        self.rest_battry_time = 0
        self.start_time = 0

if __name__ == '__main__':
    an24 = dataAN24()
    an24.addAN24('ffffffffffff')
    print an24.AN24
