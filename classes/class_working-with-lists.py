recent = ''
runtime = 0
length = 0

def main():
    alph = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']

    def find_ob(arr, k):
        ind = -1
        for i in arr:
            ind += 1
            if i == k:
                return ind

    def get_var(alph):
        # recent = ''
        global recent
        global runtime
        runtime += 1
        if runtime > 27:
            return 'You cant run this code more than 27 times'
        # print(recent)
        leng =''
        if len(recent) < 2:
            c = find_ob(alph, recent)
            if c < 26:
                recent = alph[c+1]
                return alph[c+1]
            else:
                recent = 'aa'
                return 'aa'
    return get_var(alph)


class array:
    def __init__(self):
        global length
        print("Here you go to create an instance of data type array. ")
        print('Please enter the values one by one when prompted')
        print('You can only give str input and to stop input give quit as input. ')
        for i in range(27):
            string = str(input('Please enter the value : '))
            if string == 'quit':
                return
            else:
                var = main()
                length += 1
                exec('self.' + var + '= string')
    def len(self):
        return length
    def append(self, val):
        var = main()
        exec('self.' + var + ' = ' + str(val))

instance = array()
instance.append('hello')
print(exec('self.' + var))
