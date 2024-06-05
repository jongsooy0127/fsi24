// 1. Generate a random number between MIN and MAX
let MIN = 1;
let MAX = 100;
const answer = Math.ceil(Math.random() * MAX);
let tries = 5;

// Loop:
while (true) {
    // 2. PROMPT the user to guess the number between MIN and MAX
    // prompt("Guess a number between " + MIN + " and " + MAX);
    let guess = parseInt(prompt(`Guess a number between ${MIN} and ${MAX}`));

    // 3. IF user guess is too low
    //     a. ALERT the user that their guess is too low
    //     b. UPDATE the MIN value
    //     c. GO BACK to STEP 2
    if (guess < answer) {
        alert("Your guess is too low! Try again");
        MIN = guess;
    }

    // 4. IF user guess is too high
    //     a. ALERT the user that their guess is too high
    //     b. UPDATE the MAX value
    //     c. GO BACK to STEP 2
    else if (guess > answer) {
        alert("Your guess is too high! Try again");
        MAX = guess;
    }

    // 5. IF user guess is perfect!
    //     a. ALERT a win message.
    //     b. BREAK out of the loop.
    else if (guess === answer) {
        alert("You win!");
        break;
    }

    // 6. IF user guess is invalid
    //     a. ALERT a goodbye message.
    //     b. BREAK out of the loop.
    else {
        alert(`Your answer is not a number! Goodbye!`);
        break;
    }
}