function Order(orderNo, orderName) {
    this.orderNo = orderNo; 
    this.orderName = orderName;
    this.getOrderName = function() { 
        console.log(this.orderName); 
    }; 
} 

Order.prototype.getOrderNo = function() { 
    console.log(this.orderNo); 
}

Order.prototype.printThis = function() {
    console.log(this);
}

var ord1 = new Order(123, "Oil");
ord1.getOrderName();
ord1.getOrderNo();
ord1.printThis();
