const fs = require("fs")
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +inputData[0].split(" ")[0]
const k = +inputData[0].split(" ")[1]

const words = []
const visited = Array(26).fill(false)
let res = 0
for (let i = 1; i <= n; i++) words.push(inputData[i].trim());

if (k < 5) return console.log(0)

const a = "a".charCodeAt()

visited["a".charCodeAt() - a] = true
visited["n".charCodeAt() - a] = true
visited["t".charCodeAt() - a] = true
visited["i".charCodeAt() - a] = true
visited["c".charCodeAt() - a] = true

function dfs(start, idx){
  if (idx === k-5) {
    let flag
    let cnt = 0;

    for (const word of words) {
      flag = true

      for (const ch of word){
        if (!visited[ch.charCodeAt() - a]){
          flag = false
          break;
        }
      }

      if (flag) cnt += 1
    }
    res = Math.max(res, cnt)
  }

  for (let i = start; i < 26; i++){
    if (visited[i]) continue
    visited[i] = true
    dfs(i+1, idx+1)
    visited[i] = false
  }
}

dfs(0, 0);
console.log(res);