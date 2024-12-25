class Vehicle:
  color = "white"

  def __init__(self, max_speed, mileage ):
    self.max_speed = max_speed
    self.mileage = mileage
    self.seating_capacity = None

  def assign_seating_capacity(self, seating_capacity):
    self.seating_capacity = seating_capacity

  def display_properties(self):
    print('Properties of Vehicle')
    print('Color: ', self.color)
    print("Maximum Speed: ", self.max_speed)
    print("Mileage: ", self.mileage)
    print("Seating Capacity: ", self.seating_capacity)


V1 = Vehicle(200, 20)
V1.seating_capacity = 4
V1.display_properties()