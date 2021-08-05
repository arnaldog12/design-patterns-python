def singleton(cls):
    """Singleton Decorator."""
    instances = {}

    def wrapper(*args, **kwargs):
        """A wrapper for Singleton instances."""
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class SettingsSingleton:
    def __init__(self, some_value) -> None:
        self.some_value = some_value
        self.debug = True


a = SettingsSingleton()
a.some_value = 10
print("a.some_value:", a.some_value)

b = SettingsSingleton()
b.debug = False
print("b.some_value:", b.some_value)

print(SettingsSingleton().some_value)
print(SettingsSingleton().debug)
