const dx = [1, -1, 0, 0]
const dy = [0, 0, 1, -1]

function bfs(visited, board, x, y, color){
  const q = []
  q.push([x, y])
  visited[x][y] = 1

  while(q.length !== 0){
    const [x, y] = q.shift()

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i]
      const ny = y + dy[i]

      if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
        continue;
      }

      if (visited[nx][ny] === 0 && board[nx][ny] === color) {
        q.push([nx, ny])
        visited[nx][ny] = 1
      }
    }
  }
}

const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +inputData[0]

const board = []
const board_notNormal = []

for(let i = 0; i < n; i++){
  const row = inputData[i+1].trim().split("");
  board.push(row)
  const newRow = row.map((color) => color == "R" ? "G" : color)
  board_notNormal.push(newRow)
}

const visited_normal = Array.from(new Array(n), () => new Array(n).fill(0))
const visited_notNormal = Array.from({length: n}, () => Array(n).fill(0))

let res_normal = 0
let res_notNormal = 0


for (let row = 0; row < n; row++){
  for (let col = 0; col < n; col++){
    if (visited_normal[row][col] === 0) {
      bfs(visited_normal, board, row, col, board[row][col]);
      res_normal++;
    }
  }
}

for (let row = 0; row < n; row++){
  for (let col = 0; col < n; col++){
    if (visited_notNormal[row][col] === 0) {
      bfs(visited_notNormal, board_notNormal, row, col, board_notNormal[row][col]);
      res_notNormal ++;
    }
  }
}

console.log(res_normal, res_notNormal)
