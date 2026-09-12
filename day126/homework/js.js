// 1
let productPrice = 120
let quantity = 3
let delivery = 15
const shopName = "Tech Store"

productPrice *= quantity
productPrice += delivery
console.log(`${shopName} order: ${productPrice} GEL`)
let orderCount = 1
orderCount++
console.log(typeof orderCount)

// 2

let score = 72
const studentName = "Goga"

score += 8
score *= 2
score -= 10
score /= 2
console.log(`${studentName}'s final score is: ${score}`)
console.log(typeof studentName)
console.log(typeof score)

// 3

let health = 100
let level = 1
let coins = 50
const player = "Warrior"
health -= 25
coins += 40
level++
coins *= 2
health /= 5
console.log(`${player}  Level: ${level}  Health: ${health}  Coins: ${coins}`)

// 4

let price = 80
  let quantity1 = 4
  let discount = 20
  const currency = "GEL"
  price *= quantity1
  price -= discount
  console.log("Total: " + price + " " + currency)
  console.log(`Total: ${price} ${currency}`)
  console.log(typeof price)
  console.log(typeof quantity1)
  console.log(typeof discount)
  console.log(typeof currency)

// 5

let counter = 10
counter++
console.log(counter)
counter++
console.log(counter)
counter += 5
console.log(counter)
counter--
console.log(counter)
counter *= 2
console.log(counter)
counter /= 4
console.log(counter)

// 6

const firstName = "Nika"
const lastName = "Beridze"
let age = 17
let city = "Tbilisi"
console.log(`My name is ${firstName} ${lastName}. I am ${age} years old and I live in ${city}.`)
age++
city = "Batumi"
console.log(`My name is ${firstName} ${lastName}. I am ${age} years old and I live in ${city}.`)

// 7

const accountOwner = "Ana"
let balance = 1000
balance += 500
balance -= 250
balance *= 2
balance -= 100
balance /= 2
console.log(`${accountOwner}'s current balance: ${balance} GEL`)
console.log(`Owner type: ${typeof accountOwner}`)
console.log(`Balance type: ${typeof balance}`)

// 8

const movie = "Avatar"
let ticketPrice = 25
let tickets = 4
let snacks = 30
ticketPrice *= tickets
ticketPrice += snacks
ticketPrice -= 10
tickets++
console.log(`Movie: ${movie} | Tickets: ${tickets} | Total: ${ticketPrice} GEL`)

// 9

let username = "Goga"
let age1 = 20
const isStudent = true
let salary = 1500
console.log(`Username: ${username}`)
console.log(`Age: ${age1}`)
console.log(`Student: ${isStudent}`)
console.log(`Salary: ${salary}`)
age1++
salary += 300
salary -= 100
salary *= 2
console.log(typeof username)
console.log(typeof age)
console.log(typeof isStudent)
console.log(typeof salary)

// 10

const name = "Luka"
  let age2 = 18
  let money = 500
  let items = 3
  const shop = "Game Store"
  money -= (3 * 50)
  money -= 70
  money += 200
  age2++;
  money -= 30
  console.log(`${name} Age: ${age2} Shop: ${shop}  Items: ${items}  Money: ${money} GEL`)
  console.log(`name: ${typeof name}`)
  console.log(`age: ${typeof age2}`)
  console.log(`money: ${typeof money}`)
  console.log(`items: ${typeof items}`)
  console.log(`shop: ${typeof shop}`)

//   11

const username1 = "Saba"
let age3 = 16
let balance1 = 250
let purchases = 2
const currency1 = "GEL"
const shopName1 = "Digital Shop"

purchases += 3
balance1 -= (3 * 40)
balance1 += 150
balance1 -= 25
age3++
balance1 *= 2

console.log(`User: ${username1}`)
console.log(`Age: ${age3}`)
console.log(`Purchases: ${purchases}`)
console.log(`Balance: ${balance1} ${currency1}`)
console.log(`Shop: ${shopName1}`)

console.log(typeof username1)
console.log(typeof age3)
console.log(typeof balance1)
console.log(typeof purchases)
console.log(typeof currency1)
console.log(typeof shopName1)