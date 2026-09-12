// 1
let num1 = 15;
let num2 = 4;

console.log  (num1 + num2)
console.log  (num1 - num2)
console.log  (num1 * num2)
console.log  (num1 / num2)
console.log  (num1 % num2)
console.log  (num1 ** num2)
// 2
const firstName = "davit";
const lastName = "karalashvili";
const address = "tbilisi";
const country = "saqartvelo";

let sentenceOutput = "my name is " + firstName + ", my surname is " + lastName + " and i live in " + country + " (მისამართი: " + address + ").";
console.log("my name is " + firstName + ", my surname is " + lastName + " and i live in " + country + address + ").");


// 3
let myName = "   davita   ";
console.log(myName.trim().toUpperCase());

// 4
let rawText = "   ravi rame   ";
let cleanedText = rawText.trim().toLowerCase();
console.log(cleanedText);

// 5
let text6 = "   Hello,   my name is davita.   ";
console.log(text6.trim().replace("Hello", "Hi"));

// 6
let message = "JavaScript is hard. JavaScript is interesting. I love JavaScript.";
console.log(message.replaceAll("JavaScript", "JS"));

// 7
let username = "   davitkaralashvili   ";
console.log(username.trim().slice(0, 5));

// 8
let text10 = "I like cats. Cats are cute. My cat is sleeping.";
console.log(text10.replaceAll("cats", "dogs").replaceAll("Cats", "Dogs").replaceAll("cat", "dog"))

// 9
let sentence = "JavaScript is one of the most popular programming languages";
console.log(sentence.slice(0, 25) + "...");

// 10
let code = "AB-12-CD-34";
console.log(code.replaceAll("-", "*").slice(0, -2) + "##");

// 11
let email = "   davit.karalashvili@gmail.com   ";
console.log(email.trim().slice(0, 18).replaceAll(".", "_"))

// 12
let input = "   Hello!!! My name is Goga!!! I love JS!!!   ";
console.log(input.trim().replaceAll("!!!", "!").slice(0, 20) + "...");

// 13
let phone = " +995-577-54-72-55 ";
let cleanPhone = phone.trim().replaceAll("-", "");
console.log(cleanPhone.slice(cleanPhone.length - 9))


