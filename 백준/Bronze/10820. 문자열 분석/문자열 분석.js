const fs = require('fs');
// const input = fs.readFileSync('example.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

for(let i = 0; i < input.length; i++){
    if(input[i] === '') break;
    let answer = [0, 0, 0, 0];

    for(let j = 0; j < input[i].length; j++){
        if(input[i][j] >= 'a' && input[i][j] <= 'z'){
            answer[0]++;
        } else if(input[i][j] >= 'A' && input[i][j] <= 'Z'){
            answer[1]++;
        } else if(input[i][j] >= '0' && input[i][j] <= '9'){
            answer[2]++;
        } else{
            answer[3]++;
        }
    }
    res = answer.join(' ')
    console.log(res)
}