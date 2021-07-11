# Two friends Anna and Brian, are deciding how to split the bill at a dinner.
# Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion.
# You must determine if his calculation is correct.

# For example, assume the bill has the following prices: 'bill = [2, 4, 6]'.
# Anna declines to eat item 'k = bill[2]' which costs '6'.
# If Brian calculates the bill correctly, Anna will pay '(2 + 4) / 2 = 3'.
# If he includes the cost of 'bill[2]', he will calculate '(2 + 4 + 6) / 2'.
# In the second case, he should refund '3' to Anna.

# INPUT FORMAT
# The first line contains two space-separated integers 'n' and 'k',
# the number of items ordered and the '0'-based index of the item that Anna did not eat.
# The second line contains 'n' space-separated integers 'bill[i]' where '0 ≤ i < n'.
# The third line contains an integer, 'b', the amount of money
# that Brian charged Anna for her share of the bill.

# OUTPUT FORMAT
# If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise,
# print the difference (i.e., 'b charged - b actual' ) that Brian must refund to Anna. This will always be an integer.

# SAMPLE INPUT 0
# 4 1
# 3 10 2 9
# 12
# Result: 5
# Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian.
# The total cost of the shared items is '3 + 2 + 9 = 14' and, split in half,
# the cost per person is 'b actual = 7'. Brian charged her 'b charged = 12'
# for her portion of the bill. We print the amount Anna was overcharged,
# 'b charged - b actual = 12 - 7 = 5', on a new line.

# SAMPLE INPUT 1
# 4 1
# 3 10 2 9
# 7
# Result: Bon Appetit
# Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian.
# The total cost of the shared items is '3 + 2 + 9 = 14' and, split in half,
# the cost per person is 'b actual = 7'. Because 'b actual = b charged = 7',
# we print Bon Appetit on a new line.


def bonAppetit(bill: list, k: int, b: int):
    bill.pop(k)

    annaBill = sum(bill) / 2
    result = int(b - annaBill)

    if annaBill == b:
        print('Bon Appetit')
    else:
        print(result)