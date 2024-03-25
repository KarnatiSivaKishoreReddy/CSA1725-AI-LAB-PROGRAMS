class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.location = (0, 0)  # Starting location of the vacuum cleaner

    def clean(self):
        while True:
            if self.environment[self.location[0]][self.location[1]] == 'Dirty':
                print(f"Current location: {self.location}. Cleaning...")
                self.environment[self.location[0]][self.location[1]] = 'Clean'
            else:
                print(f"Current location: {self.location}. Already clean.")
            
            # Move to the next cell
            if self._move():
                print("Moved to the next cell.")
            else:
                print("No more dirty cells. Cleaning complete.")
                break

    def _move(self):
        # Check if there are any dirty cells left
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                if self.environment[i][j] == 'Dirty':
                    next_location = (i, j)
                    if next_location[0] < self.location[0]:
                        print("Moving up.")
                    elif next_location[0] > self.location[0]:
                        print("Moving down.")
                    elif next_location[1] < self.location[1]:
                        print("Moving left.")
                    elif next_location[1] > self.location[1]:
                        print("Moving right.")
                    self.location = next_location
                    return True
        return False


# Example environment
environment = [
    ['Dirty', 'Clean', 'Dirty'],
    ['Clean', 'Clean', 'Dirty'],
    ['Dirty', 'Clean', 'Clean']
]

# Create a vacuum cleaner instance
vacuum_cleaner = VacuumCleaner(environment)

# Start cleaning
vacuum_cleaner.clean()
