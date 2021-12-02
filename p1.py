""" Python program """
print("Checkint pylint .")

#pylint: disable=too-few-public-methods
class Hello:
    """ This is hello Docstring """
    def __init__(self , fname  ,lname ):#pylint: disable=unused-argument
        self.fname = fname


hobj = Hello("avdhut", "ulhare")


print(hobj.fname)
print(Hello.__doc__)
