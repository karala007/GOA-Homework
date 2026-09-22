//1
let age = prompt("შეიყვანე შენი ასაკი: ")
let ticketPrice = prompt("შეიყვანე ბილეთის საწყისი ფასი: ")

let price

if (age < 0 || ticketPrice < 0) {
    console.log("შეცდომა: მონაცემები უარყოფითია")
} else if (age < 7) {
    price = 0
} else if (age <= 17) {
    price = ticketPrice * 0.5
} else if (age <= 59) {
    price = ticketPrice
} else if (age >= 60) {
    price = ticketPrice * 0.7
}

if (age < 18 || age >= 60) {
    console.log("You have a discount")
}

console.log(`ბილეთის საბოლოო ფასი არის ${price}`)


//2
let username = "Goga"
let password = "Goa2026"
let age1 = 20

if (username === "" || password === "") {
    console.log("Fill in all fields")
} else if (username === "Goga" && password === "Goa2026") {
    console.log("Login successful")
} else if (username === "Goga" && password !== "Goa2026") {
    console.log("Incorrect password")
} else if (username !== "Goga") {
    console.log("Incorrect username")
}

if (age1 < 18) {
    console.log("Access denied")
}


//3
let price1 = 250
let age2 = 22
let isMember = true

let discount = 0

if (price1 < 0) {
    console.log("Invalid price")
} else if (isMember && price1 > 200) {
    discount = 25
} else if (isMember || age2 < 18) {
    discount = 10
} else if (age2 >= 60 && price1 > 100) {
    discount = 15
}

if (price1 >= 0) {
    let finalPrice = price1 - discount
    console.log(`საწყისი ფასი: ${price1}`)
    console.log(`ფასდაკლება: ${discount}`)
    console.log(`გადასახდელი თანხა: ${finalPrice}`)
}


//4
let number = Number(prompt("შეიყვანე რიცხვი: "))

if (number > 100) {
    console.log("Large positive number")
} else if (number > 0 && number < 100) {
    console.log("Small positive number")
} else if (number < 0 && number % 2 === 0) {
    console.log("Negative even number")
} else if (number < 0 && number % 2 !== 0) {
    console.log("Negative odd number")
} else if (number === 0) {
    console.log("Zero")
}

if (number >= 10 && number <= 20) {
    console.log("Special range")
}


//5
let name = "Goga"
let math = 85
let english = 90
let programming = 95

let average = (math + english + programming) / 3

if (math < 50 || english < 50 || programming < 50) {
    console.log("Failed")
} else if (math >= 90 && english >= 90 && programming >= 90) {
    console.log("Excellent student")
} else if (average >= 80 && math >= 70) {
    console.log("Very good student")
} else {
    console.log("Needs improvement")
}


//6
let age3 = Number(prompt("შეიყვანე ასაკი: "))
let height = Number(prompt("შეიყვანე სიმაღლე (სმ-ში): "))

if (age3 < 0 || height < 0) {
    console.log("Invalid data")
} else if (age3 >= 12 && height >= 140) {
    console.log("You can ride")
} else if (age3 < 12 || height < 140) {
    console.log("You cannot ride")
}

if (age3 >= 18 && height >= 180) {
    console.log("VIP access")
}


//7
let number2 = 45

if (number2 >= 10 && number2 <= 50) {
    console.log("Inside range")
} else if (number2 < 10 || number2 > 50) {
    console.log("Outside range")
}

if (number2 % 2 === 0 && number2 > 20) {
    console.log("Special even number")
} else if (number2 % 2 !== 0 && number2 < 30) {
    console.log("Special odd number")
}

if (number2 === 25 || number2 === 50) {
    console.log("Exact match")
}

//8
let score1 = Number(prompt("შეიყვანე პირველი გამოცდის ქულა: "))
let score2 = Number(prompt("შეიყვანე მეორე გამოცდის ქულა: "))
let score3 = Number(prompt("შეიყვანე მესამე გამოცდის ქულა: "))
let age4 = Number(prompt("შეიყვანე ასაკი: "))

let average1 = (score1 + score2 + score3) / 3

if (score1 < 0 || score1 > 100 || score2 < 0 || score2 > 100 || score3 < 0 || score3 > 100) {
    console.log("Invalid score")
} else if (score1 < 50 || score2 < 50 || score3 < 50) {
    console.log("Rejected")
} else if (score1 >= 90 && score2 >= 90 && score3 >= 90) {
    console.log("Scholarship candidate")
} else if (score1 >= 80 && score2 >= 80 && score3 >= 80 && age4 >= 18) {
    console.log("Accepted")
} else if (average1 >= 70 && (score1 < 80 || score2 < 80 || score3 < 80)) {
    console.log("Waitlisted")
} else {
    console.log("Not accepted")
}