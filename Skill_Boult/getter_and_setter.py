class GetterAndSetter:
    __a = 10

    def get(self):
        return self.__a

# Create an instance of the class
obj = GetterAndSetter()

# Access the value using the get method
print(obj.get())
