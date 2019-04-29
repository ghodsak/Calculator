





import math



class Functions():

    def click_btn(self, value):

        # Get the current value in the entry
        entry_val = self.entry.get()

        entry_val += str(value)

        # Clear the entry box
        self.entry.delete(0, "end")

        # Insert the new value going from left to right
        self.entry.insert(0, entry_val)


    # Returns True or False if the string is a float
    def isfloat(self, str_val):
        try:
            # If the string isn't a float float() will throw a
            # ValueError
            float(str_val)

            # If there is a value you want to return use return
            return True
        except ValueError:
            return False


    # Handles logic when math buttons are pressed
    def math_button_press(self, math_value):
        # Only do anything if entry currently contains a number
        if self.isfloat(str(self.entry.get())):

            # make false to cancel out previous math button click
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False

            # Get the value out of the entry box for the calculation
            self.calc_value = float(self.text_input.get())

            # Set the math button click so when equals is clicked
            # that function knows what calculation to use
            if math_value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif math_value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif math_value == "+":
                print("+ Pressed")
                self.add_trigger = True
            elif math_value == "-":
                print("- Pressed")
                self.sub_trigger = True
            else:
                if math_value == "":
                    print("Please press math button! IdioT")


            # Clear the entry box
            self.entry.delete(0, "end")


    def equal_button_press(self):


        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

            if self.add_trigger:
                solution = self.calc_value + float(self.text_input.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.text_input.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.text_input.get())
            else:
                solution = self.calc_value / float(self.text_input.get())

            print(self.calc_value, " ", float(self.text_input.get()),
                  " ", solution)

            # Clear the entry box
            self.entry.delete(0, "end")

            self.entry.insert(0, solution)


    def all_clear_btn(self):
        self.value = ''
        self.text_input.set(self.value)


    def negative_btn(self):
        self.negative_num = eval((self.text_input.get() + '*(-1)'))
        self.value = str(self.negative_num)
        self.text_input.set(self.value)
        print(self.value)


    def square_root(self):
        self.current_value = self.text_input.get()
        self.current_value = math.sqrt(int(self.current_value))
        self.text_input.set(self.current_value)


    def base_ten(self):
        base = 10
        value = int(self.text_input.get())
        self.entry.delete(0, "end")
        self.entry.insert(0,base**value)

    def Pi(self):
        self.pi_value = math.pi
        self.entry.insert(0, self.pi_value)
