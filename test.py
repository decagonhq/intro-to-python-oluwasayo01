class MyClass:
    AGE = 23

    @classmethod
    def get_computed_age(cls):
        return cls.AGE

a = MyClass()

print(a.get_computed_age())