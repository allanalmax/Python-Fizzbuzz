def fizzbuzz(my_list1, my_list2):
    combined_list = my_list1 + my_list2
    if len(combined_list) % 5 == 0 and len(combined_list) % 3 == 0:
        print("fizzbuzz")
    elif len(combined_list) % 3 == 0:
        print("fizz")
    elif (combined_list) % 5 == 0:
        print("buzz")
       
my_list1 = input("enter list one: ")
my_list2 = input("enter list two: ")

fizzbuzz(my_list1, my_list2)
    