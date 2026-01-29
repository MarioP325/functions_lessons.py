def tea_order(customer_name, tea_type,*args, **kwargs):#args allow any number of arguments to be put into the perimeter *args can have any name but you follow it with *, kwargs need **
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print("    - Add", arg)
    for key, value in kwargs.items():
        print("    - Add", key, ":", value)
print(tea_order("Li", "chamomile", milk="oat"))
print(tea_order("Ce", "chamomile",))
print(tea_order("Al", "chamomile", "oat", sweetner="honey"))




# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    sum=0
    for num in args: #iterate through each argument
        sum += num ** 2 #square then add the number
        #each time goes sum= number+ anumber^2
    return sum 
print(sum_squares(1,2,3))
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    sum=0
    for num in args:
        sum+= abs(num)
    return sum
print(absolute_sum(1,-4,6,-7))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
def personal_numbers(name, *numbers):
    sum=0
    for num in numbers:
        sum+= num

    print(f"{name}, the sum of your numbers is {sum}")
print(personal_numbers("Oguri", 1,8,9,4))