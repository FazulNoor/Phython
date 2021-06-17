import logging

a = 10.20
b = 10.30
total_qty = 0

def sum(v1, v2):
    return v1+v2

# while a != 0:   
#     try:
#         a = int(input("Enter Value for A\n"))
#         b = int(input("Enter Value for B\n"))
#     except ValueError: 
#         print("Enter the Number to sum!!")


    print(f"Sum of values {sum(a,b)}")

# list_of_number = input("Enter the list of numbers")
list_of_number  = ["10","20","30","10","40"]
sum = 0
for number in set(list_of_number):
    sum = sum + int(number)

print(f"Sum of number in list ={sum}")

list_of_order = [{"orderId":123,"ItemNo":234,"ItemName":"Rice","Qty":2},
                {"orderId":234,"ItemNo":234,"ItemName":"Oil","Qty":3},
                {"orderId":345,"ItemNo":234,"ItemName":"Sugar","Qty":4},
                {"orderId":456,"ItemNo":234,"ItemName":"Millets","Qty":4}]
for listItem in list_of_order:
    for item in listItem:
        print(f"Order Key {item} values {listItem[item]}")
    total_qty = total_qty + listItem["Qty"]

print(f"Total qty {total_qty}")
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

logger = logging.getLogger("SAMPLEFUNC")
logger.info("Log ::Total qty {total_qty}")
logger.debug("Error on this order")