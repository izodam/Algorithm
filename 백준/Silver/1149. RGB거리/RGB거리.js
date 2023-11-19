const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// '/dev/stdin'

const n = +input[0];
const cost = [];

for(let i = 0; i < n; i++){
    let [r,g,b] = input[i+1].split(' ').map(Number);
    cost.push([r,g,b]);
}

let res = 1000;

for(let i = 1; i < n; i++){
    cost[i][0] += Math.min(cost[i-1][1], cost[i-1][2]);
    cost[i][1] += Math.min(cost[i-1][0], cost[i-1][2]);
    cost[i][2] += Math.min(cost[i-1][0], cost[i-1][1]);
}
console.log(Math.min(cost[n-1][0],cost[n-1][1],cost[n-1][2]));