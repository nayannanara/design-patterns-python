from observer.interface.observer import Observer


class Person(Observer):
    def __init__(self) -> None:
        self.wake_up = False

    def is_wake_up(self):
        return self.wake_up
    
    def update(self):
        print('Acordei')
        self.wake_up = True