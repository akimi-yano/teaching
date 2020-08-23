class Node{
    constructor(value){
        this.data = value;
        this.next = null;
    }
}
var n1 = new Node(10);
var n2 = new Node(9);

n1.next = n2;
console.log(n1.next.data)