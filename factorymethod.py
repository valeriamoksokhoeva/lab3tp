from abc import abstractmethod, ABC
class Language(ABC):
    @abstractmethod
    def speak(self):
        pass

class English(Language):
    def speak(self):
        print('Hello!')
class Spanish(Language):
    def speak(self):
        print('Hola!')
class Italian(Language):
    def speak(self):
        print('Buongiorno!')

class LanguageFactory:
    def create_language(self, name):
        if name == 'en':
            return English()
        elif name == 'es':
            return Spanish()
        elif name == 'it':
            return Italian()
        else:
            return None
        
factory = LanguageFactory()

english_person = factory.create_language('en')
english_person.speak()

spanish_person = factory.create_language('es')
spanish_person.speak()