///1
let greet = () => {
    return "zdarova"
}
console.log(greet())


//2
let greet1 = name => {
    return "Hello " + name
}
console.log(greet1("bondo"))
console.log(greet1("dzia"))
console.log(greet1("goga"))

// 3
let shemowmeba = (password, email) => {
    return (password === "123" && email === "gegimagaria@gmail.com") ? "login success" : "error"
}
console.log(shemowmeba("123", "gegimagaria@gmail.com"))
console.log(shemowmeba("568", "gegimagaria@gmail.com"))
console.log(shemowmeba("123", "rame sxva emaili"))

//1
const erti = (a, b) => a * b;

console.log(erti(5, 4));
console.log(erti(7, 3));
console.log(erti(-2, 8));

//2
function grdzeli(a, b) {
  return a * b;
}

console.log(grdzeli(5, 4));
console.log(grdzeli(10, 10));