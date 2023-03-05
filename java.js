/*write a function called add7 that takes one number and returns that number + 7 */

function add7(num) {
    console.log(num + 7);
}

add7(1); 


/* write a function called multiply that takes 2 numbers and treturns their product */
function multiply(a,b) {
    console.log(a * b);
}

multiply (3,4);


/* write a function called capitalize that takes a string and returns that string with only the first letter capitalized */

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

result = capitalize('sakshi');

console.log(result);


function lastletter(string) {
    return string.slice(5,6);
}

result = lastletter('sakshi')

console.log(result)



/* fizz buzz practice */


let answer = parseInt(prompt("Please enter the number you would like to Fizzbuzz up to:"))

for (let i = 1; i <= answer; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}