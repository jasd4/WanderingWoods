class Stats:
    def __init__(self):
        self.steps = 0  # Initialize step counter

    def increment_steps(self):
        self.steps += 1  # Increase step count

    def get_steps(self):
        return self.steps  # Return current step count
