"""
a function that returns Fizz if the combined length of the lists is
divisible by 3,  Buzz if it is divisible by 5, Fizzbuzz if it is divisible
by both 5 and 3  or the combined length of the list
"""
def fizzbuzz(list1, list2):
    "method that returns Fizz, Buzz and FizzBuzz"
    length_list1 = len(list1)
    length_list2 = len(list2)
    combined_length = length_list1 + length_list2
    divisible_by_3 = combined_length%3
    divisible_by_5 = combined_length%5
    divisible_by_combined_length = combined_length%combined_length
    
    if divisible_by_3 == 0:#if combined list length is divisible by 3
        print("fizz")
        return "fizz"
    elif divisible_by_5 == 0:#if combined list length is divisible by 5
        print("buzz")
        return "buzz"
    elif divisible_by_3 == 0 and divisible_by_5 == 0 or divisible_by_combined_length == 0:#if combined list length is divisible by 3 and 5 or the the combined length of the list
        print("fizzbuzz")
        return "fizzbuzz"
    else:
        print("Not divisible by any")

fizzbuzz([1, 2, 3], [ ])    # will return “fizz”
fizzbuzz([1, 2, 3], [1, 2])  # will return “buzz”  
fizzbuzz([1, 2, 3], [1]) # will return 4 
