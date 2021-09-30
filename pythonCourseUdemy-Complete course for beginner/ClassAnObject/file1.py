class MyComplexNumber:
    # Constructor
    def __init__(self, real =0, imag =0):
        print("MyComplexNumber constructor executing ...")
        self.real = real
        self.imag = imag
    #Print the values with format        
    def displayComplexNumber(self):
        print("{0} + {1}j".format(self.real, self.imag))

#Creating the object
cp = MyComplexNumber(30,40)
#Adding new value called new_attribute
cp.new_attribute = 80
#Deleting a value inside of the object
del cp.real
#Calling the method inside of a class
cp.displayComplexNumber()
#Printing
print(cp.real, cp.imag, cp.new_attribute)