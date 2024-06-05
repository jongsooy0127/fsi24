//Object Literals

const studentData = {
    name: "Toby Green",
    age: 25,
    nationality: "American",
    subjects: ["Math", "Science", "English"],
    address: {
        street: "123 Main Street",
        city: "New York",
        state: "NY",
    },
};

//Printing the typeOf  the object
console.log(typeof studentData); //result is object

//First way to access the object property
console.log(studentData.name); //result is "Toby Green"

//Second way to access the object property
console.log(studentData["name"]);

//Printing New York
console.log(studentData.address.city)
console.log(studentData["address"]["city"]);
console.log(studentData.subjects[2]) //prints Science

//Printing the object keys
console.log(Object.keys(studentData));

//Printing the object values
console.log(Object.values(studentData));

const userData = {
    fName: "Naruto",
    lName: "Uzumaki",
    siblings: 0,
    friends: ["Sakura", "Sasuke"],
    teacher: ["Kakashi Hatake", "Jiraya", "Iruka Umino"],
    address: {
        street: "4 Chome-2-8 Shibakoen",
        district: "Minato City",
        city: "Tokyo",
        country: "Japan",
    },
}

//Adding new key and value
studentData["marriage"] = true; 
studentData.age = 26;
console.log(studentData);

//customer 

// const customer = {
//     name: prompt("What is your name?"),
//     age: prompt("How old are you?"),
//     country: prompt("What country are you from?"),
//     address: {
//         street: prompt("What street do you live on?"),
//         city: prompt("What city do you live in?"),
//         zipCode: prompt("What is your zip code?"),
//     }
// };

//Storing multiple objects in an array
const students = [
    {
        name: "Toby",
        age: 21,
        subjects: ["Math", "Science", "English"],
    },
    {
        name: "Alice",
        age: 23,
        subjects: ["History", "Chemistry", "English"],
    },
    {
        name: "Linda",
        age: 19,
        subjects: ["Literature", "Marketing", "Accounting"]
    },
];

for (let i = 0; i < 5; i++){
    console.log("Hello World!");
};

// let sum = 0;
// for (let i = 1; i <= 10; i++) {
//     sum += i;
//     console.log(sum);
// }

const fizzBuzz = [];
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum++
    if (sum % 3 === 0 && sum % 5 === 0){
        fizzBuzz.push("fizzbuzz")
    } else if (sum % 3 === 0) {
        fizzBuzz.push("fizz");
    } else if (sum % 5 === 0) {
        fizzBuzz.push("buzz");
    } else {
        fizzBuzz.push(sum);
    }
};