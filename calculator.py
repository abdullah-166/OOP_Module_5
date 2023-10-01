class claculator:
    brand = 'casio'
    def summation(self, num1, num2):
        sum = num1 + num2
        return sum
    
    def  subtraction(self, num1, num2):
        sub = num1 - num2
        return sub
    
    def multiply(self, num1, num2):
        mult = num1 * num2
        return mult
    
    def division(self, num1, num2):
        div = num1 / num2
        return div
    
my_calculator = claculator()
n = int(input())
m = int(input())
print(my_calculator.summation(n,m))
print(my_calculator.subtraction(n,m))
print(my_calculator.multiply(n,m))
print(my_calculator.division(n,m))


    