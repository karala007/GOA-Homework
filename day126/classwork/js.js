let name = prompt("name:")
let last = prompt("last:")
let age = prompt("age:")
let address = prompt("address:")

let sentence = `hello ${name} ${last} you are ${age}  and live ${address}. right?`

console.log(sentence)

let number = 691

if (number > 0) {
    console.log("positive")
} else if (number < 0) {
    console.log("negative")
} else {
    console.log("zero")
}