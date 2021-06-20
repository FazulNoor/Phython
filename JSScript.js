function cubeSum(n) {
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum = + (2 * i) + (2 * i) + (2 * i);
    }
    return sum;
}

function checkValue(n){
    if (n == true) return true;
}
var number = Window.prompt("Enter the number to sum");
console.log(cubeSum(number));
console.log(checkValue(10>20));

