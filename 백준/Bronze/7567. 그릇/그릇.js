const fs = require('fs');
// const input = fs.readFileSync('example.txt').toString().split('');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('');

let bowl = input[0];
let res = 10;

for(let i = 1; i < input.length; i++){
    if (input[i] === '')    break;
    if(bowl === input[i]){
        res += 5;
    } else{
        res += 10;
        bowl = input[i];
    }
}
console.log(res);