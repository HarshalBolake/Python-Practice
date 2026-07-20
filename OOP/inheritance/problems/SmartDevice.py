class Camera:
    def cameraQuality(self):
        print("48mp")

class MusicPlayer:
    def speakerCompany(self):
        print("dolby Atmos")

class GPS:
    def allowsGPS(self):
        print("Allows GPS Tracking")

class SmartPhone(Camera,MusicPlayer,GPS):
    def __init__(self,battery):
        self.battery = battery

    def charge(self, percentage):
        self.battery += percentage
        
        if self.battery > 100:
            self.battery = 100

    def showBattery(self):
        print(f"Battery: {self.battery}%")

SM1 = SmartPhone(30)
SM1.charge(40)
SM1.showBattery()
SM1.charge(50)
SM1.showBattery()
SM1.charge(50)
SM1.showBattery()