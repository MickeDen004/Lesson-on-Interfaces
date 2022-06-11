from Interfaces import InterfaceInput

class Input(InterfaceInput):

    def input_operation(self, text, num):

        if 1 < num > 3:
            print("Error. Enter number from 1 to 3")
        else:
            if num == 1:
                return text.encode()

            elif num == 2:
                return text.count()

            elif num == 3:
                return text.upper()


input1 = Input().input_operation("uhrvpiewgbpyg4072t34ficyuwgoergf", 1 )
print(input1)