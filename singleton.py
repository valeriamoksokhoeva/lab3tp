class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            object.__new__(cls)
        return cls._instance

first = Singleton()
second = Singleton()
print(first is second)