from facade.repository.select import Select

class Usacase:
    def __init__(self) -> None:
        self.select = Select()

    def get(self):
        return self.select.select_single_element()
    
    def query(self):
        return self.select.select_many_element()