from abc import ABC,abstractmethod


class Button(ABC):

    def __init__(self,setLink):
        self.link = setLink

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    
    def click(self):
        print("Go To {}".format(self.link))

    @Button.link.getter
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, input):
        self.__link = input


tombol1 = PushButton("www.yabsiraditya.my.id")
tombol1.click()