class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        number_to_string = {3 : "Fizz", 5 : "Buzz"}
        fizz_buzz = []
        for i in range(1, n+1):
            current_fizz_buzz = ""
            for number in number_to_string.keys():
                if i % number == 0:
                    current_fizz_buzz += number_to_string[number]
            
            if current_fizz_buzz != "":
                fizz_buzz.append(current_fizz_buzz)
            else:
                fizz_buzz.append(str(i))
        
        return fizz_buzz
        