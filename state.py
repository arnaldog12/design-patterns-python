class State:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def read_red(self):
        pass

    def read_yellow(self):
        pass

    def read_green(self):
        pass


class RedState(State):
    def read_yellow(self):
        print("[   red -> yellow] something went wrong!")

    def read_green(self):
        print("[   red -> green ] safe to go!")
        self.semaphore.current_state = self.semaphore.green_state


class YellowState(State):
    def read_red(self):
        print("[yellow -> red   ] stop!")
        self.semaphore.current_state = self.semaphore.red_state

    def read_green(self):
        print("[yellow -> green ] something went wrong!")


class GreenState(State):
    def read_red(self):
        print("[ green -> red   ] something went wrong!")

    def read_yellow(self):
        print("[ green -> yellow] slow down!")
        self.semaphore.current_state = self.semaphore.yellow_state


class Semaphore:
    def __init__(self) -> None:
        self.red_state = RedState(self)
        self.yellow_state = YellowState(self)
        self.green_state = GreenState(self)
        self.current_state = self.green_state


semaphore = Semaphore()
semaphore.current_state.read_yellow()
semaphore.current_state.read_red()
semaphore.current_state.read_green()
semaphore.current_state.read_red()
