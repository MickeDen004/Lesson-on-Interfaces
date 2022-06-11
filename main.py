from Interfaces import InterfaceText, InterfaceInput, Button
import string
import random


class Text(InterfaceText):

    def generate_text(self, k: int) -> str:
        text = ''.join(random.choices(string.ascii_letters + string.digits, k=k))
        return text

class Input(InterfaceInput):

    @staticmethod
    def input_operation(text: str):
        return text.encode()


class Shape(Button):

    def press_the_button(self, text, k):
        return f"You have clicked your mouse.\n" \
               f"{text.center(k)}"

# class Input(InterfaceInput):
#
#     def input_operation(self, text, num):
#
#         if 1 < num > 3:
#             print("Error. Enter number from 1 to 3")
#         else:
#             if num == 1:
#                 return text.encode()
#
#             elif num == 2:
#                 return text.count()
#
#             elif num == 3:
#                 return text.upper()
#
#
# input1 = Input().input_operation("uhrvpiewgbpyg4072t34ficyuwgoergf", 1 )
# print(input1)
        

text1 = Text().generate_text(20)
print(text1)


i = Input()

# new one
encoded_text = Input.input_operation(Text().generate_text(20))
print(str(encoded_text))

# same as text1
encoded_text2 = Input.input_operation(text1)
print(encoded_text2)


shape = Shape().press_the_button(text1, 150)
print(shape)