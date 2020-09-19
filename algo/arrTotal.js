
function sum(arr) {
    var total = 0;
    for(var i = 0; i < arr.length; i++ ) {
        total += arr[i]
    }
   console.log(total)
}
sum([2,4,5])

function total(arr){
    var count = 0;
    for(var i=0;i<arr.length;i++){
        count +=arr[i]
    }
    return count
}
console.log(total([2,4,5]))