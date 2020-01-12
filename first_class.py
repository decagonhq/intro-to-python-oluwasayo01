class FirstClass:
    median = 0
    mean = 0

    def __init__(self):
        self.mode = 0

    @staticmethod
    def calc_mean(data):
        FirstClass.mean = round(sum(data)/len(data), 2)

        

    @classmethod
    def cal_median(cls, data):
        data.sort()
        if len(data)%2 == 1:
            mid_index = int((len(data) + 1)/2)
            cls.median = data[mid_index]
        else:
            mid_index = len(data)/2
            cls.median = (data[mid_index] + data[mid_index + 1])/2
        
        


    def calc_mode(self, data):
        result = {}
        for key in data:
            result[key] = result.get(key) + 1 if result.get(key) != None else 1

        mode_value = max(result.values())
        self.mode = tuple(value for value in result if result.get(value) == mode_value)
         


    
obj1 = FirstClass()
print(obj1.median)
print(obj1.cal_median([2, 2, 3, 3, 4, 5, 11, 13, 15]))
print(obj1.median)
print(obj1.mode)
print(obj1.calc_mode([2, 2, 3, 3, 4, 5, 11, 13, 15]))
print(obj1.mode)
print(obj1.mean)
print(obj1.calc_mean([2, 2, 3, 3, 4, 5, 11, 13, 15]))
print(obj1.mean)

obj2 = FirstClass()
print(obj2.mean)
print(obj2.median)
print(obj2.mode)