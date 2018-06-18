
class Sint():
    def __init__(self, int_num):
        self.int_num = int_num

    def __add__(self, other):
        return Sint(int(str(self.int_num) + str(other.int_num)))

    def __sub__(self, other):
        temp_value = list(str(self.int_num))
        temp_value.reverse()
        [temp_value.remove(i) for i in list(str(other.int_num)) if i in temp_value]
        temp_value.reverse()
        temp_value = ''.join(temp_value)
        return Sint(int(temp_value))

    def __mul__(self, other):
        temporary = [int(i) for i in list(str(other.int_num))]
        multiplier = int(sum(temporary)/len(temporary))
        return Sint(int(str(self.int_num)*multiplier))

    def __truediv__(self, other):
        temporary = [int(i) for i in list(str(other.int_num))]
        divider = str(int(sum(temporary)/len(temporary)))
        return Sint(int(str(self.int_num).replace(divider,'0')))


    def __str__(self):
        return str(self.int_num)


    def __int__(self):
        return self.int_num

def main():
    x = Sint(123)
    print(x)
    y = Sint(456)
    print(y)

    e = x+y
    print(e)

    e = x-y
    print(e)

    e = x*y
    print(e)

    e /= e
    print(e)


if __name__ == '__main__':
    main()
