let names = ["Brian", "Luke", "Isaac", "Paulo", "Laney", "Jay"];
names.push("Tobey");
for (let i=0; i<6; i++) {
    console.log(i);
    console.log(names[i]);
}

console.log(names[Math.floor((Math.random() * names.length))]);

// OR

let randomIndex = Math.floor(Math.random() * names.length);
console.log(names[randomIndex]);

//push = add to end of the array
//pop = removes from the end of array
//shift = removes from the start of the array
//unshift = add to the start of the array
//splice method - removes elements from an array
names.splice(2,1,"Toby"); //removes 1 element at index 2, and adds Toby (replaces "Issac" with "Toby")

//concat method = merges two or more arrays
let numbers = [1,2,3,4];
let moreNumbers = [5,6,7,8];
let allNumbers = numbers.concat(moreNumbers);
console.log(allNumbers);

//includes method = checks if an element is in an array (RETURNS TRUE OR FALSE)
console.log(allNumbers.includes(5)); //true
console.log(allNumbers.includes(11)); //false

//indexOf method = returns the index of an element
console.log(allNumbers.indexOf(5)); //returns 4

//join method = joins all elements of an array into a string
console.log(names.join(", ")) //output is a string

//reverse method = reverse the order of elements in an array
console.log(names.reverse()); //['Tobey', 'Jay', 'Laney', 'Paulo', 'Toby', 'Luke', 'Brian']

//slice method = extracts a section of an array
names = ["Brian", "Luke", "Isaac", "Paulo", "Laney", "Jay"]
console.log(names.slice(1,3));

//sort method = sorts the element of an array
console.log(names.sort());
console.log(allNumbers.sort());

//Activity
const vowel = ["a", "e", "i", "o", "u"];
const consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
let input = prompt("Enter a letter:");
input = input.toLowerCase();

if (true === vowel.includes(input)) {
    alert(`"${input}" is a vowel`)
} else if (true === consonant.includes(input)) {
    alert(`"${input}" is a consonant`)
} else {
    alert(`Please input 1 letter, and not a number!`);
}



