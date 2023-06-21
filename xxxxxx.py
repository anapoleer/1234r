class Calculator:  
    def __init__(self):  
        self.stack = []  
          
    def add(self, a, b):  
        self.stack.append(a + b)  
          
    def subtract(self, a, b):  
        self.stack.append(a - b)  
          
    def multiply(self, a, b):  
        self.stack.append(a * b)  
          
    def divide(self, a, b):  
        if b == 0:  
            raise ValueError("除数不能为0")  
        self.stack.append(a / b)  
          
    def clear(self):  
        self.stack = []  
          
    def result(self):  
        if len(self.stack) == 1:  
            return self.stack[0]  
        else:  
            raise ValueError("计算结果不是一个数字")  
              
calculator = Calculator()  
  
while True:  
    try:  
        print("请输入要计算的表达式（使用+、-、*、/、C进行操作）：")  
        expression = input()  
        parts = expression.split()  
        for part in parts:  
            if part == "+":  
                calculator.add(float(parts[parts.index(part)+1]), float(parts[parts.index(part)+2]))  
            elif part == "-":  
                calculator.subtract(float(parts[parts.index(part)+1]), float(parts[parts.index(part)+2]))  
            elif part == "*":  
                calculator.multiply(float(parts[parts.index(part)+1]), float(parts[parts.index(part)+2]))  
            elif part == "/":  
                calculator.divide(float(parts[parts.index(part)+1]), float(parts[parts.index(part)+2]))  
            elif part == "C":  
                calculator.clear()  
            else:  
                raise ValueError("无效的操作符")  
        result = calculator.result()  
        print("计算结果为：", result)  
    except ValueError as e:  
        print("错误：", e)
       
