//Fizzbuzz activity
// let userInput = parseInt(prompt("Pick a number:"));

// if (userInput % 3 === 0 && userInput % 5 === 0) {
//     alert(`${userInput} is a Fizzbull number`);
// } else if (userInput % 5 === 0){
//     alert(`${userInput} is a Buzz number`);
// } else if (userInput % 3 === 0) {
//     alert(`${userInput} is a Fizz number`);
// } else {
//     alert("The number is not divisible by 3 nor 5");
// }

// (userInput % 3 === 0 && userInput % 5 === 0)

// (userInput % 3 === 0)

//Logical Operators && = and          || = or
true && true; // = true
true && false; // = false
1 > 0 && 0 > 1 // = false (both values need to be true)
1 > 0 || 0 > 1 // = true (one of them needs to be true)

// let rain = prompt("Is it raining? (Yes/No)");
// rain = rain.toLowerCase();

// if (rain === "yes") {
//     let umbrella = prompt("Do you have an umbrella? (Yes/No)");
//     umbrella = umbrella.toLowerCase();
//     if (umbrella === "yes") {
//         alert("You can go outside!");
//     }
//     else {
//         alert("Please wait a while");
//     }
// } else {
//     alert("You can go outside!");
// }

let height = parseFloat(prompt("What is your height in meters?"));
let weight = parseInt(prompt("What is your weight in kilograms?"));
let bmi = weight/(height*height);
console.log(bmi);

if (bmi < 18.5){
    alert("You are underweight");
} else if (bmi>=18.5 && bmi < 25){
    alert("Your weight is normal");
} else if (bmi>= 25 && bmi < 30){
    alert("You are slighly overweight");
} else if (bmi>=30 && bmi < 35){
    alert("You are obese");
} else if (bmi>=35){
    alert("You are clinically obese");
} else {
    alert("Input the correct information");
}