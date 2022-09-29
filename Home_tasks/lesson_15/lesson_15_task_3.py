"""Create a simple prototype of a TV controller in Python."""


class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def __init__(self):
        self.index_channel = 0

    def first_channel(self):
        first_channel = TVController.CHANNELS[0]
        print(f'The first channel is {first_channel}')
        return first_channel

    def last_channel(self):
        last_channel = TVController.CHANNELS[-1]
        print(f'The last channel is {last_channel}')
        return last_channel

    def turn_channel(self, N):
        self.index_channel = N-1

        print(f'Turned channel is {TVController.CHANNELS[self.index_channel]}')
        return TVController.CHANNELS[self.index_channel]

    def next_channel(self):
        self.index_channel += 1
        if self.index_channel >= len(TVController.CHANNELS):
            self.index_channel = 0

        print(f'Next channel is {TVController.CHANNELS[self.index_channel]}')
        return TVController.CHANNELS[self.index_channel]

    def previous_channel(self):
        self.index_channel -= 1
        if self.index_channel < 0:
            self.index_channel = len(TVController.CHANNELS) - 1

        print(f'Previous channel is {TVController.CHANNELS[self.index_channel]}')
        return TVController.CHANNELS[self.index_channel]

    def current_channel(self):
        print(f'Current channel is {TVController.CHANNELS[self.index_channel]}')
        return TVController.CHANNELS[self.index_channel]

    def is_exist(self, N):
        if 0 <= N - 1 < len(TVController.CHANNELS):
            print('Yes,the channel exists in the list')
        else:
            print('No,the channel dose not exists in the list')

controller = TVController()

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)