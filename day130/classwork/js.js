// 1
function displayCar(brand = "Toyota", year = 2020, color = "Black") {
    return `Car: ${brand}, Year: ${year}, Color: ${color}`
}
    console.log(displayCar("chevrolet"))
    console.log(displayCar("kamaro", 2022))
    console.log(displayCar("lambo", 2024, "yelow"))
    console.log(displayCar())


// 2
function compareNumbers(a, b) {
    return a > b ? "first is bigger" : b > a ? "second is bigger" : "equal"
}
    console.log(compareNumbers(6 , 4))
    console.log(compareNumbers(6 , 7))
    console.log(compareNumbers(100, 100))


// 3

let calculatePrice = function(product, price, quantity = 1) {
    if (price <= 0) {
        return "Invalid price"
    }
    if (quantity <= 0) {
        return "Invalid quantity"
    }
    let total = price * quantity
    if (total >= 100) {
        total -= 10
    }
    return `Product: ${product}Total: ${total}`
};
console.log(calculatePrice("Laptop", 167, 3))
console.log(calculatePrice("Mouse", 25, 2))
console.log(calculatePrice("Keyboard", 20, 20))
console.log(calculatePrice("Monitor", 269, -9))