const fs = require('fs');
// const input = fs.readFileSync('example.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = input[0].split(' ')[0];
const m = input[0].split(' ')[1];

const basket = Array.from({length: n}, () => 0);

for(let x = 1; x <= m; x++){
    let i = +input[x].split(' ')[0];
    let j = +input[x].split(' ')[1];
    let k = +input[x].split(' ')[2];

    for(let y = i-1; y < j; y++){
        basket[y] = k;
    }
}

console.log(basket.join(' '));