import random

class RoomCleanerAgent:
  def __init__(self,room_size=(10,10)):
    self.room_size = room_size
    # Initialize the room as a 10×10 grid with random 0 (clean) and 1 (dirty) cells
    self.grid = [[random.choice([0,1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
    # Initialize the agent's position randomly
    self.current_position = (random.randint(0, room_size[0] - 1), random.randint(0, room_size[1]-1))

  def display_room(self):
    # Display the current status of the room grid 
    for row in self.grid:
      for cell in row:
        print(str(cell), end=" ")
        print("\n")

  def run(self):
    # Display initial status of the room
    print("Initial Room status:")
    self.display_room()
# Create and run the room Cleaner Agent
agent = RoomCleanerAgent()
agent.run()
