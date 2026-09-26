// 1
function greet(name) {
  console.log(`Hello, ${name}`)
}

greet("Goga")
greet("dato")
greet("Nino")


// 2
function sum(a, b) {
  console.log(a + b)
}

sum(5, 10)
sum(15, 25)
sum(-3, 8)


// 3
function showInfo(name, age, city) {
  console.log(`My name is ${name}, I am ${age} years old and I live in ${city}.`)
}

showInfo("Goga", 20, "Tbilisi")
showInfo("Luka", 25, "Batumi")
showInfo("Mariam", 18, "Kutaisi")

// 4
function square(number) {
  console.log(number * number)
}

square(4)
square(7)
square(10)

// 5
function showProduct(name, price, category) {
  console.log(`Product: ${name}\nPrice: ${price}\nCategory: ${category}`)
}

showProduct("Laptop", 1500, "Electronics")
showProduct("Phone", 800, "Electronics")

// 6
function checkAge(age) {
  if (age >= 18) {
    console.log("You are an adult.")
  } else {
    console.log("You are a minor.")
  }
}

checkAge(20)
checkAge(15)
checkAge(18)

// 7
function checkNumber(number) {
  if (number > 0) {
    console.log("Positive")
  } else if (number < 0) {
    console.log("Negative")
  } else {
    console.log("Zero")
  }
}

checkNumber(10)
checkNumber(-5)
checkNumber(0)

// 8
function calculate(a, b, operator) {
  if (operator === "+") {
    console.log(a + b)
  } else if (operator === "-") {
    console.log(a - b)
  } else if (operator === "*") {
    console.log(a * b)
  } else if (operator === "/") {
    console.log(a / b)
  } else {
    console.log("Invalid operator")
  }
}

calculate(10, 5, "+")
calculate(10, 5, "-")
calculate(10, 5, "*")
calculate(10, 5, "/")


// 9
function checkProduct(name, price, budget) {
  if (budget >= price) {
    console.log(`You can buy ${name}.`)
  } else {
    console.log(`You cannot buy ${name}.`)
  }
}

checkProduct("Phone", 800, 1000)
checkProduct("Laptop", 2000, 1000)

// 10
function getGrade(name, score) {
  let grade

  if (score >= 90 && score <= 100) {
    grade = "A"
  } else if (score >= 80 && score <= 89) {
    grade = "B"
  } else if (score >= 70 && score <= 79) {
    grade = "C"
  } else if (score >= 60 && score <= 69) {
    grade = "D"
  } else if (score >= 0 && score <= 59) {
    grade = "F"
  } else {
    console.log("Invalid score")
    return;
  }

  console.log(`${name} got grade ${grade}.`)
}

getGrade("Nika", 87)
getGrade("Goga", 95)
getGrade("Luka", 62)