class Car(object):
    def __init__(self, color, model, company, speedLimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit

    def start(self):
        print("Car has started")
    
    def stop(self):
        print("Car has stopped")

city=Car("Brown", "City1", "Honda", "80")
print(city.stop())