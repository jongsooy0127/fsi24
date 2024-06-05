//4 important topics: Object Oriented Programming, Loops, Data Structures, Functions

// Credit Score Assignment:
// let creditScore = parseInt(prompt("Enter your credit score"));

// if (creditScore >= 300 && creditScore <= 579) {
//     alert(`${creditScore} is pretty shitty`);
// } else if ( creditScore >= 580 && creditScore <= 669) {
//     alert(`${creditScore} is fair`);
// } else if (creditScore >=670 && creditScore <= 739){
//     alert(`${creditScore} is good`);
// } else if (creditScore >= 740 && creditScore <=799){
//     alert(`${creditScore} is very good`);
// } else if (creditScore >= 800 && creditScore <= 850) {
//     alert(`${creditScore} is excellent`);
// } else {
//     alert("Enter a credit score between 300 to 850");
// }

//Swimming Pool Registration
//1st we have to ask whether they want to use our swimming pool or not
//if yes, how old is the user? -> 6-12: children ($5) / 13-19: teenager ($8) / 19-28: adults ($12)
//how many people are there?
//Do you have swimming suits? If not, you can use our swimming suits ($3)
//Do you want to take a picture of your vacation? ($3)
//Here in your bill

// let bill = 0;

// console.log("Welcome to Javascript Swimming Area!");
// let userInput = prompt(
//   "Would you like to use our swimming pool services? (Yes/No)"
// );
// userInput = userInput.toLowerCase();
// if (userInput === "yes") {
//   let age = Number(prompt("Thank you for using our service! How old are you?"));
//   if (age <= 12 && age >= 6) {
//     let members = Number(prompt("How many are in your group? (1-9)"));
//     bill += 5 * members;
//     let suit = prompt("Do you want to use our swimming suits? (Yes/No)");
//     suit = suit.toLowerCase();
//     if (suit === "yes") {
//       bill += 3;
//     }

//     let photos = prompt("Do you want to take a picture? (Yes/No)");
//     photos = photos.toLowerCase();
//     if (photos === "yes") {
//       bill += 3;
//     }

//     console.log(`Your total bill is $${bill}\nThank you for using our service`);
//   } else if (age <= 19 && age >= 13) {
//     let members = Number(prompt("How many are in your group? (1-9)"));
//     bill += 8 * members;
//     let suit = prompt("Do you want to use our swimming suits? (Yes/No)");
//     suit = suit.toLowerCase();
//     if (suit === "yes") {
//       bill += 3;
//     }

//     let photos = prompt("Do you want to take a picture? (Yes/No)");
//     photos = photos.toLowerCase();
//     if (photos === "yes") {
//       bill += 3;
//     }

//     console.log(`Your total bill is $${bill}\nThank you for using our service`);
//   } else if (age <= 28 && age >= 20) {
//     let members = Number(prompt("How many are in your group? (1-9)"));
//     bill += 12 * members;
//     let suit = prompt("Do you want to use our swimming suits? (Yes/No)");
//     suit = suit.toLowerCase();
//     if (suit === "yes") {
//       bill += 3;
//     }

//     let photos = prompt("Do you want to take a picture? (Yes/No)");
//     photos = photos.toLowerCase();
//     if (photos === "yes") {
//       bill += 3;
//     }

//     console.log(`Your total bill is $${bill}\nThank you for using our service`);
//   } else {
//     console.log(
//       "Sorry, our swimming pool is only available for people between the ages of 6 and 29"
//     );
//   }
// } else {
//   console.log("Thank you for considering our services");
// }

//Javascript Pizza Activity

let bill = 0;

let userInput = prompt("Would you like to order our pizza? (Y/N)");
userInput = userInput.toLowerCase();
if (userInput === "y") {
  let size = prompt("What size would you like to order? (S/M/L)");
  size = size.toLowerCase();
  if (size==="s"){
    bill += 15;
    let smPep = prompt("Do you want to add pepperoni? (Y/N)");
    smPep = smPep.toLowerCase();
    if (smPep === "y"){
        bill+=2
    }
    let cheese = prompt("Do you want to add extra cheese? (Y/N)");
    cheese = cheese.toLowerCase();
    if (cheese === "y") {
        bill+=1
    }
  }
  if (size==="m"){
    bill += 20;
    let pep = prompt("Do you want to add pepperoni? (Y/N)");
    pep = pep.toLowerCase();
    if (pep === "y"){
        bill+=3
    }
    let cheese = prompt("Do you want to add extra cheese? (Y/N)");
    cheese = cheese.toLowerCase();
    if (cheese === "y") {
        bill+=1
    }
  }
  if (size==="l"){
    bill += 25;
    let pep = prompt("Do you want to add pepperoni? (Y/N)");
    pep = pep.toLowerCase();
    if (pep === "y"){
        bill+=3
    }
    let cheese = prompt("Do you want to add extra cheese? (Y/N)");
    cheese = cheese.toLowerCase();
    if (cheese === "y") {
        bill+=1
    }
  }
  alert(`Thank you for your order.\n Your total is $${bill}`)

} else {
  console.log("Hope to see you again.");
}
