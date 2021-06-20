class Order(object):
    def __init__(self,orderId,orderName):
       self.orderId = orderId
       self.orderName = orderName

    def get_order(self):
        self.orderId = 14
        self.orderName = "Oil"
        return Order(self.orderId, self.orderName)

    def get_order_id(self):
        return self.orderId

    def get_order_name(self):
        return self.orderName

    def set_order_name(self,orderName):
        self.orderName = orderName
    
    def set_order_id(self,orderId):
        self.orderId = orderId

sum = 0
def recursion_add(n):
    if n < 1:
        return n
    else:
        return (n*n)+recursion_add(n-1)



print(f"Sum of 10 numbers = {recursion_add(2)} ")

objects = Order(12,'Rice') 
objects1 = Order(13,'Wheat') 
new_order = objects.get_order()


print(f"{objects.get_order_name()} is Order with Order Id {objects.get_order_id()}")
print(f"{objects1.get_order_name()} is Order with Order Id {objects1.get_order_id()}")
print(f"{new_order.get_order_name()} is Order with Order Id {new_order.get_order_id()}")

