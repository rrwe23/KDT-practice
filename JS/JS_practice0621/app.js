const age = parseInt(prompt("How old are you?"));

if (isNaN(age)) {
    console.log("Please write a number");

} else if(age < 18) {
    console.log("you are too young")
} else if(age >=18 && age <=50) {   // && = and, || = or
    console.log("OK")
 
} else if(age === 100){
    console.log("Wow;; ")
} s