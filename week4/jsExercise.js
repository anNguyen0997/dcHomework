    // Hello You! && Hello You! Part 2
        // write a function hello which given a name, says hello to the name
            // if no name is given, function will print "Hello, world!"

function sayHello(name) {
    if (name == undefined) {
        console.log(`Hello, world!`)
    } else {
    console.log(`Hello, ${name}`);
    }
}
// // sayHello()
// sayHello('An')

// -------------------------------------------------------------------------------------------------
    // Madlib
        // write a function, which is given a name and a subject
        // it will return(not print) a new string, (name)'s favorite subject in school (subject)

function favSubject(name, subj) {
    let newString = `${name}'s favorite subject in school is ${subj}`;
    return newString;
}
// console.log(favSubject('Donny', 'science'))

// -------------------------------------------------------------------------------------------------
    // Tip Calculator 
        // write a function tipAmount that is given the bill amount and the level of service
        // (one of good, fair, and poor) and returns the dollar amount for the tip

function tipAmount(bill, serviceLevel) {
    
    if (serviceLevel == 'good') {
        console.log(`Bill: ${bill} | service: ${serviceLevel}`)
        return bill * .20
    } else if (serviceLevel == 'fair') {
        console.log(`Bill: ${bill} | service: ${serviceLevel}`)
        return bill * .15
    } else if (serviceLevel == 'poor') {
        console.log(`Bill: ${bill} | service: ${serviceLevel}`)
        return bill * .10
    }
}
        // Part 2
            // write a function totalAmount that takes the same arguments as tipAmount
            // except it returns the total as the tip amount plus the bill amount

// function totalAmount(bill, serviceLevel) {
//     function tipAmount(bill, serviceLevel) {
//         return bill
//     }
// }

function splitAmount(bill, serviceLevel, numOfPeople) {
    if (serviceLevel == 'good') {
        let goodTip = bill * .20
        let total = bill + goodTip
        let split = total / numOfPeople
        console.log(`Bill: ${bill} | service: ${serviceLevel} | Amount after split: ${split}`)

    } else if (serviceLevel == 'fair') {
        let fairTip = bill * .15
        let total = bill + fairTip
        let split = total / numOfPeople
        console.log(`Bill: ${bill} | service: ${serviceLevel} | Amount after split: ${split}`)

    } else if (serviceLevel == 'poor') {
        let poorTip = bill * .15
        let total = bill + poorTip
        let split = total / numOfPeople
        console.log(`Bill: ${bill} | service: ${serviceLevel} | Amount after split: ${split}`)
    }

}

console.log(tipAmount(200, 'good'))
// console.log(totalAmount(200, 'good'))
console.log(splitAmount(200, 'good', 4))
// ---------------------------------------------------------------------------------------------





    