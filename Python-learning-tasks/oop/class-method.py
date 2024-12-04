# Calculator class

class my_Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2!=0:
            return self.num1 / self.num2
        else:
            return 'Error: Division by zero is not allowed.'

def main():
    print('Hello from the main() method')
    calc1 = my_Calculator(20, 10)
    totalAdd1 = calc1.add()
    totalSub1 = calc1.subtract()
    print('Total: ', totalAdd1)
    print('Total: ', totalSub1)

    print('-----------------------------------')

    calc2 = my_Calculator(25, 5)
    totalAdd2 = calc2.add()
    totalSub2 = calc2.subtract()
    print('Total: ', totalAdd2)
    print('Total: ', totalSub2)

if __name__ == '__main__':
    main()