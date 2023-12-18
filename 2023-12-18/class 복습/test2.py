from test import calculator

class completedCalculator(calculator):
  def pow(self, num):
    return self.result ** num

cal1 = completedCalculator()
cal2 = completedCalculator()

if __name__ == "__main__":
  print("계산기 1 : ", cal1.add(3))
  print("계산기 2 : ", cal2.add(5))

  print("계산기 1 : ", cal1.pow(3))
  print("계산기 2 : ", cal2.pow(2))
