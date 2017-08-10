class Bicycle:
    def __init__(self, gear, diameter, speed, color):
        self.gear = gear
        self.diameter = diameter
        self.speed = speed
        self.color = color
    def __str__(self):
        gearInfo = "Gear: " + str(self.gear)
        diameterInfo = " Diameter: " + str(self.diameter)
        speedInfo = " Speed: " + str(self.speed)
        colorInfo = " Color: " + self.color
        return gearInfo + diameterInfo + speedInfo + colorInfo
    def shiftGear(self, gearshift):
        self.gear = gearshift
    def changeColor(self, changecolor):
        self.color = changecolor


fionabike = Bicycle(3, 27, 2000, "purple")
print(fionabike)
fionabike.changeColor("blue")
print(fionabike)
fionabike.shiftGear(20000)
print(fionabike)
