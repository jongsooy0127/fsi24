// Roulette
// 1. At the beginning, the user has $1000
let userMoney = 1000;

while (true) {
  let guess = Number(prompt("Select a number between 1 to 36"));
  let betMoney = Number(
    prompt(`How much money are you willing to bet? (1-${userMoney})`)
  );
  let winNum = Math.floor(Math.random() * 37);

  console.log(winNum, guess);

  if (winNum === 0) {
    userMoney = userMoney - betMoney;
    alert(`The winning number was ${winNum}`);
    alert(`You have $${userMoney} left`);
    if (userMoney < 1) {
      alert("Game Over");
    }
    break;
  } else if (guess === winNum) {
    userMoney = userMoney - betMoney + betMoney * 36;
    alert(`The winning number was ${winNum}`);
    alert(`You have $${userMoney}`);
  } else if (guess % 2 === 0 && winNum % 2 === 0) {
    userMoney = userMoney - betMoney + betMoney * 2;
    alert(`The winning number was ${winNum}`);
    alert(`You have $${userMoney}`);
  } else if (guess % 2 === 1 && winNum % 2 === 1) {
    userMoney = userMoney - betMoney + betMoney * 2;
    alert(`The winning number was ${winNum}`);
    alert(`You have $${userMoney}`);
  } else if (guess < 1 || guess > 36 || betMoney > userMoney) {
    alert(`Please input a valid answer`);
  } else {
    userMoney = userMoney - betMoney;
    alert(`The winning number was ${winNum}`);
    alert(`You have $${userMoney} left`);
    
    if (userMoney < 1) {
      alert("Game Over");
      
      let restart = prompt("Would you like to start again? (Yes/No)");
      restart = restart.toLowerCase();
      
      if (restart === "yes") {
        userMoney = 1000;
      } else {
        alert("Goodbye");
        break;
      }
    }
  }
}
// Loop:
// 2. Prompt the user for a number to bet on (1 ~ 36)

// 3. Prompt the user for an amount of money to bet (1 ~ currentMoney)

// 4. The game generates a random number between 0 ~ 36 (0 means computer always wins)

// 5. Check IF winner:
//     a. Same number -> multiply bet * 36;
//     b. If both ODD or both EVEN -> multiply bet * 2
//     c. Otherwise we lose the bet

// 6. We add or subtract the money, as needed
//     a. If we run out of money, game is over.

// 7. Ask the player if they want to continue
