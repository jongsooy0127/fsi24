console.log("It is running successfully");

//Creating variables in two different ways:
//let (variables can change)
let age = 20;
age++;

//const (variables do not change)
const PI = 3.14;

//var (outdated = do not use)
// var name = "Brian";
// console.log(name);

let expression = 'I watched a movie called "Inception"';
console.log(expression);

//String concatenation
//Adding two strings
let name = "Brian";
age = 28;
console.log(name +  age);

//Multiplication between two different variable type
console.log(name * age);

//String Methods

let message = 'hahaha';

message.toUpperCase(); // = HAHAHA
message.toLocaleLowerCase(); // = hahaha

let anotherMessage = '          lol       ';
anotherMessage.trim(); // = lol (no empty space)

//Length of string
//Attributes (does not require paranthesis unlike methods)
let firstName = 'Thomas';
console.log(firstName.length)

//Methods with arguments
let movie = 'Game of Thrones';
console.log(movie.indexOf('Game')); // output of 0 (first letter)
console.log(movie.indexOf('Thrones')); // output of 8 (starts at 9th letter)
console.log(movie.indexOf('Knight')); // output of -1 (doesn't exist)

//Replace method
let greeting = 'Hello, my name is Jennie';
console.log(greeting)
greeting = greeting.replace('Jennie', 'Jay'); // replace the string "Jennie" to "Jay"
console.log(greeting);

//Replace All method
greetings = "Hello, my name is Jennie. Jennie likes to study web development";
greetings = greetings.replaceAll("Jennie", "Jay"); // replace all "Jennie" with "Jay"
console.log(greetings);

//Slicing strings
let song = "Oppa Gangnam Style";
let word = song.slice(5,12);
console.log(word);

//Example
let example = "This country is Switzerland, and it is beautiful";
console.log(example.indexOf("Switzerland")); //Shows where the index of Switzerland starts
example = example.slice(16, 27); //Slices the word "Switzerland"
console.log(example); //outputs Switzerland 

//Other ways of using slice
//Slice with one argument
let language = "JavaScript";
console.log(language.slice(4)); //outputs Script (keeps the index)

//Slice with negative numbers
console.log(language.slice(-6)); //outputs Script (starts from -1 not 0)

//example
let play = "skateboard";
play = play.slice(-5); //removes "skate"
play = play.replace("o","e"); // replaces o with e
console.log(play); //prints beard

//String template literals
let userAge = 21;
let userName = "Johnny";
let userHobby = "playing basketball";
console.log(userName + " is " + userAge + " years old and he likes " + userHobby)
//there is a easier way to do this (backtick is above the tab key)
console.log(`${userName} is ${userAge} years old and he likes ${userHobby}`); //this is the easier way to do this
//${variableName} = when using variables in backtick

// userName = prompt("Enter your name");
// let productName = "apple";
// let productPrice = 2.50;
// let quantity = 3;
// console.log(`Hello ${userName}, the total price of ${quantity} ${productName}s is $${quantity * productPrice}`);

//Activity (ask user's age and name, and tell user how old they will be in 10 years)
let inputName = prompt("What is your name?");
let inputAge = prompt("How old are you?");
console.log(`Hello ${inputName}, you will be ${parseInt(inputAge) + 10} years old in 10 years`);

//null = intentional absence of data (username/password = user needs to input to define data)

console.log(Math.floor(Math.random() * 6) + 1);