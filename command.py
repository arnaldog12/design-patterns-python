from abc import abstractmethod


# Receivers
class Light:
    def on(self):
        print("light is on")

    def off(self):
        print("light is off")


class GarageDoor:
    def up(self):
        print("garage door is up")

    def down(self):
        print("garage door is down")


# Command Pattern
class Command:
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoorUpCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class NoCommand(Command):
    pass


# Invoker
class RemoteControl:
    def __init__(self, n_buttons):
        self.list_on = [NoCommand()] * n_buttons
        self.list_off = [NoCommand()] * n_buttons
        self.undo_command = NoCommand()

    def set_command(self, index, on_command, off_command):
        self.list_on[index] = on_command
        self.list_off[index] = off_command

    def push_on_button(self, index):
        self.list_on[index].execute()
        self.undo_command = self.list_on[index]

    def push_off_button(self, index):
        self.list_off[index].execute()
        self.undo_command = self.list_off[index]

    def push_undo_button(self):
        self.undo_command.undo()


light = Light()
garage_door = GarageDoor()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

garage_door_up = GarageDoorUpCommand(garage_door)
garage_door_down = GarageDoorDownCommand(garage_door)

remote_control = RemoteControl(n_buttons=7)
remote_control.set_command(0, light_on, light_off)
remote_control.set_command(1, garage_door_up, garage_door_down)

remote_control.push_on_button(0)
remote_control.push_off_button(0)
remote_control.push_undo_button()

remote_control.push_on_button(1)
remote_control.push_off_button(1)
remote_control.push_undo_button()

remote_control.push_on_button(2)
