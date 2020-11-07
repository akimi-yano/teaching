// Rotate
// Implement rotateArr(arr, shiftBy) that accepts array and offset. 
// Shift arr’s values to the right by that amount. ‘Wrap-around’ 
// any values that shift off array’s end to the other side, 
// so that no data is lost. Operate in-place: given ([1,2,3],1), 
// change the array to [3,1,2]. Don’t use built-in functions.

// Second: allow negative shiftBy (shift L, not R).

// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.

// Fourth: minimize the touches of each element.


function rotate(arr, count){
    // 2) while loop - condition is the shiftBy
    while (count>0){

    // 1) shit by 1 using for loop
        let temp = arr[arr.length-1]
        for (let i=arr.length-1; i>0; i--){
            arr[i] = arr[i-1];   
        }
        arr[0] = temp;
        
        count-=1;
    }
    return arr;
}

            //  0 1 2 3 4 
// original [1,2,3,4,5]
          // 5 1 2 3 4 
            //    temp = arr.length-1       
// 1 iteration shift by 1[5,1,2,3,4]
// 2nd  iteration shift by 1 [4,5,1,2,3]



arr = [1,2,3,4,5]
// console.log("before", arr)
shiftBy = 3
console.log(rotate(arr, shiftBy))
// console.log("after", arr)

