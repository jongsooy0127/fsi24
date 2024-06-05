let randomRoll = Math.random();

randomRoll = Math.floor(randomRoll * 6) + 1;
console.log(randomRoll);

let userInput = prompt("Enter a number between 1-6");

if (parseInt(userInput) === randomRoll) {
    console.log("You Win!");
    alert("You won the game!")
}

else {
    console.log("You Lost!");
    alert("You lost the game!")
}