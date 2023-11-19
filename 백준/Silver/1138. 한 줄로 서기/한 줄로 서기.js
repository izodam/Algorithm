const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// '/dev/stdin'

const n = +input[0];

const res = Array.from({length: n}, () => 0)

for(let i = 1; i < n+1; i++){
    let t = +input[1].split(' ')[i-1];
    let cnt = 0;
    for(let j = 0; j < n; j++){
        if(cnt === t && res[j] === 0){
            res[j] = i;
            break;
        } else if(res[j] === 0){
            cnt ++;
        }
    }
}
console.log(res.join(' '));