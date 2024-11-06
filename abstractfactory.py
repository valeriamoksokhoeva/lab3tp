from abc import abstractmethod, ABC
class Mouse(ABC):
    @abstractmethod
    def create_mouse(self):
        pass

class WhiteMouse(Mouse):
    def create_mouse(self):
        print('You created a white mouse.')
class BlackMouse(Mouse):
    def create_mouse(self):
        print('You created a black mouse.')

class Keyboard(ABC):
    @abstractmethod
    def create_keyboard(self):
        pass

class WhiteKeyboard(Keyboard):
    def create_keyboard(self):
        print('You created a white keyboard.')
class BlackKeyboard(Keyboard):
    def create_keyboard(self):
        print('You created a black keyboard.')

class AbstractFactory:
    def createMouse(self):
        pass
    def createKeyboard(self):
        pass

class WhiteSetFactory(AbstractFactory):
    def createMouse(self):
        return WhiteMouse()
    def createKeyboard(self):
        return WhiteKeyboard()
class BlackSetFactory(AbstractFactory):
    def createMouse(self):
        return BlackMouse()
    def createKeyboard(self):
        return BlackKeyboard()

class Application:
    def __init__(self, factory):
        self.mouse = factory.createMouse()
        self.keyboard = factory.createKeyboard()
    def create(self):
        self.mouse.create_mouse()
        self.keyboard.create_keyboard()

whiteset = WhiteSetFactory()
app1 = Application(whiteset)

blackset = BlackSetFactory()
app2 = Application(blackset)

app1.create()
app2.create()