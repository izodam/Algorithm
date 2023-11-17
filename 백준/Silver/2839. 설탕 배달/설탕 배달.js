const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let n = Number(input);
let res = 0;

while(n > 0){
    if(n % 5 === 0){
        n -= 5;
    } else{
        n -= 3;
    }
    res ++;
}

console.log(n === 0 ? res : -1);