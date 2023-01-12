class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n = input()
        n = int(n)
        list = []
        for i in range(n):
            if (i % 3 == 0 and i % 5 == 0):
                list.append("FizzBuzz")
            elif (i % 3 == 0):
                list.append("Fizz")
            elif (i  % 5 == 0):
                list.append("Buzz")
        return list
            
