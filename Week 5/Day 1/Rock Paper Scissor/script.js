let outcomes = ["rock", "scissor", "paper"];
let bot = Math.floor(Math.random()*3);
let player = prompt("Please choose one of the following: Rock, Scissor, or Paper")
player = player.toLowerCase();

if (player === "rock" && outcomes[bot] === "scissor") {
    alert("Player Wins!");
} else if (player === "scissor" && outcomes[bot] === "paper") {
    alert("Player Wins!");
} else if (player === "paper" && outcomes[bot] === "rock") {
    alert("Player Wins!");
} else if (player === outcomes[bot]){
    alert("It is a draw!");
} else {
    alert("Bot Wins!")
}

console.log(outcomes[bot]);