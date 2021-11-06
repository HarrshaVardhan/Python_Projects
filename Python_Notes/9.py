
#if it's hot
#    It's a hot day
#    Drink plenty of water
#otherwise if it's cold
#    It's a cold day
#    Wear warm clothes
#otherwise
#    It's a lovely day

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day")

print("Enjoy your day")

print("-" * 30)

#exercise
#Price of a house is $1M
#if buyer has good credit
#   they need to put down 10%
#Otherwise
#   they need to put down 20%
#Print the down payment
#

good_credit = True
bad_credit = False
down_payment = 1_000_000

if good_credit:
    print("Good credit, down payment from $1M is ", int(down_payment * 0.1), sep="$")
else:
    print("Bad credit, down payment from $1M is ", int(down_payment * 0.2), sep="$")

print("-" * 30)

#Mosh solution
price = 10000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
