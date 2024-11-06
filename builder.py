class Watch:
    def __init__(self, case, dial, movement, strap):
        self._case = case
        self._dial = dial 
        self._movement = movement
        self._strap = strap
    def __str__(self):
        return f'The watch consists {self._case}, {self._dial}, {self._movement} and {self._strap}.'

class Builder:
    def build_case(self):
        raise NotImplementedError
    def build_dial(self):
        raise NotImplementedError
    def build_movement(self):
        raise NotImplementedError
    def build_strap(self):
        raise NotImplementedError
    def create_watch(self):
        raise NotImplementedError
    
class SwissWatchBuilder(Builder):
    def build_case(self):
        return 'Steel case'
    def build_dial(self):
        return 'Copper dial'
    def build_movement(self):
        return 'Swiss movement'
    def build_strap(self):
        return 'Leather strap'
    def create_watch(self):
        case = self.build_case()
        dial = self.build_dial()
        movement = self.build_movement()
        strap = self.build_strap()

        return Watch(case, dial, movement, strap)

builder = SwissWatchBuilder()
watch = builder.create_watch()

print(watch)