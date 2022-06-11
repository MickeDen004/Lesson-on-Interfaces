from abc import ABC, abstractmethod


class InterfaceText(ABC):

    @abstractmethod
    def generate_text(self, k: int) -> str:
        """This method generates random body of letters and signs"""

        pass


class InterfaceInput(ABC):

    def Input(self, text: str) -> str:
        """Operations with the provided text"""

        pass


class Button(ABC):

    @abstractmethod
    def press_the_button(self, text: str, k: int) -> str:
        pass
