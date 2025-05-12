class Person:
    def __init__(self, name):
        self.name = name     # Public attribute, Instance Variable
        self.state = "Idle"  # Default state

    def running(self):
        self.state = "Running"
        print(f"{self.name} is now running.")

    def walking(self):
        self.state = "Walking"
        print(f"{self.name} is now walking.")

    def sleeping(self):
        self.state = "Sleeping"
        print(f"{self.name} is now sleeping.")

    def show_state(self):
        print(f"{self.name} is currently in '{self.state}' state.")


f1 = Person("vikram")
print(f1.name)
print(f1.state)
print(f1.walking())
print(f1.running())