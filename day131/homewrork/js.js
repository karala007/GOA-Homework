// 1
let greet = (name) => `Hello, ${name}!`

console.log(greet("Nika"))
console.log(greet("Gegi"))

// 3
let calculateSalary = (salary, bonus) => bonus > 500 ? salary + salary * 0.1 : salary

console.log(calculateSalary(2000, 600))
console.log(calculateSalary(2000, 400))

// 4
let getAgeCategory = (age) => age >= 60 ? "Senior" : age >= 18 ? "Adult" : age >= 13 ? "Teenager" : "Child"

console.log(getAgeCategory(15))
console.log(getAgeCategory(25))
console.log(getAgeCategory(70))

// 5
let checkExam = (score, maxScore) => (score / maxScore) * 100 >= 90 ? "Excellent" : (score / maxScore) * 100 >= 75 ? "Very Good" : (score / maxScore) * 100 >= 60 ? "Passed" : "Failed"

console.log(checkExam(45, 50))
console.log(checkExam(32, 50))
console.log(checkExam(20, 50))

// 6
let withdraw = (balance, amount) => amount <= 0 ? "Invalid amount" : amount > balance ? "Not enough money" : balance - amount

console.log(withdraw(1000, 300))
console.log(withdraw(1000, 1500))
console.log(withdraw(1000, 0))

// 7
let checkPassword = (password) => password.length < 8 ? "Too short" : "Valid password"

console.log(checkPassword("hello"))
console.log(checkPassword("javascript"))

// 8
let getOrderPrice = (price, quantity, delivery) => price * quantity + (delivery === "express" ? 15 : 5)

console.log(getOrderPrice(100, 3, "standard"))
console.log(getOrderPrice(100, 3, "express"))

// 9
let calculateFinalPrice = (price, quantity, discount, isMember) => (price * quantity * (1 - discount / 100)) * (isMember ? 0.9 : 1)

console.log(calculateFinalPrice(100, 3, 20, true))
console.log(calculateFinalPrice(100, 3, 20, false))

// 10
let roundNumber = (number) => Math.round(number)

console.log(roundNumber(5.4))
console.log(roundNumber(5.6))

// 11
let floorNumber = (number) => Math.floor(number)

console.log(floorNumber(5.9))
console.log(floorNumber(8.2))
console.log(floorNumber(12.99))

// 12
let ceilNumber = (number) => Math.ceil(number)

console.log(ceilNumber(5.1))
console.log(ceilNumber(8.2))
console.log(ceilNumber(12.01))