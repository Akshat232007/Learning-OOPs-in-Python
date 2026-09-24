class ex:
    a = 23

    @classmethod
    def show(cls):
        print(f"The class attribute value is {cls.a}")

    def show_2(self):
        print(f"The attribute value using self is {self.a}")


e = ex()

e.a = 66

e.show()
e.show_2()


# a = 23 is a class attribute.

# e.a = 66 does NOT change the class attribute.
# It creates a new attribute for the object e.

# So:
# Employee.a = 23
# e.a = 66

# @classmethod uses cls to refer to the class.
# So cls.a gives the class value: 23.

# self refers to the object.
# So self.a gives the object's value: 66.