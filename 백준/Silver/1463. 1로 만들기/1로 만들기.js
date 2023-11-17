const fs = require('fs');
// const input = fs.readFileSync('example.txt').toString().trim();
const input = fs.readFileSync('/dev/stdin').toString().trim();

n = +input;

let dp = [0, 0, 1];

for(let i = 3; i < n+1; i++){
    if(i%2 === 0 && i%3 === 0){
        dp[i] = Math.min(dp[i/3]+1, dp[i/2]+1, dp[i-1]+1);
    } else if(i%3 === 0){
        dp[i] = Math.min(dp[i/3]+1, dp[i-1]+1);
    } else if(i%2 === 0){
        dp[i] = Math.min(dp[i/2]+1, dp[i-1]+1);
    } else{
        dp[i] = dp[i-1]+1;
    }
}

console.log(dp[n]);