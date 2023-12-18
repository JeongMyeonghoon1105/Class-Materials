class calculator:
  def __init__(self):
    self.result = 0
  
  def add(self, num):
    self.result += num
    return self.result
  
  def sub(self, num):
    self.result -= num
    return self.result
  
  def mul(self, num):
    self.result *= num
    return self.result
  
  def div(self, num):
    self.result /= num
    return self.result

if __name__ == "__main__":
  cal1 = calculator()
  cal2 = calculator()

  print("계산기 1 : ", cal1.add(3))
  print("계산기 2 : ", cal2.sub(5))

  print("계산기 1 : ", cal1.add(6))
  print("계산기 2 : ", cal2.sub(7))
