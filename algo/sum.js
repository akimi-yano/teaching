function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    return sum;
}
var result1 = add(3,5);
var result2 = add(4,7);
console.log(result1);
console.log(result2);




// STEPS:
// 1 call add  function with argument 3 and 5 and assign the result to result1
//     print "Summing Numbers!"
//     print "num1 is: 3"
//     print "num2 is: 5"
//     sum of 3 and 5 is 8 and assign it to the variable called sum
//     return 8
//     result1 is now 8

// 2 call the add function with argument 4 and 7 and assign the result to result2
//     print "Summing Numbers!"
//     print "num1 is: 4"
//     print "num2 is: 7"
//     sum of 4 and 7 is 11 and assign it to the variable called sum
//     return 11
//     result2 is now 11

// 3 print 8 because result1 is 8 
// 4 print 11 because result2 is 11 

// That is why the output/ printed values are follwoing:
//     print "Summing Numbers!"
//     print "num1 is: 3"
//     print "num2 is: 5"
//     print "Summing Numbers!"
//     print "num1 is: 4"
//     print "num2 is: 7"
//     print 8
//     print 11
