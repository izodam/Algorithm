const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const t = +input[0];

const dp = [0, 1, 2, 4]

for(let i = 0; i < t; i++){
    let n = +input[i+1];
    let s = dp.length;

    if (s < n+1){
        for(let j = s; j < n+1; j++){
            dp[j] = (dp[j-1]+dp[j-2]+dp[j-3]) % 1000000009
        }
    }

    console.log(dp[n]);
}
