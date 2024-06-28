const fs = require("fs");

const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +inputData[0].split(" ")[0];
const m = +inputData[0].split(" ")[1];

const board = [];

for (let i = 0; i < n; i++) {
  const row = inputData[i + 1].split(" ").map((res) => +res);
  board.push(row);
}

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function bfs(x, y) {
  const q = [];
  q.push([x, y]);
  board[x][y] = 0;
  let cnt = 1;

  while (q.length !== 0) {
    const [x, y] = q.shift();

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
        continue;
      }

      if (board[nx][ny] === 1) {
        board[nx][ny] = 0;
        q.push([nx, ny]);
        cnt += 1;
      }
    }
  }
  return cnt;
}

const res = [];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1) {
      res.push(bfs(i, j));
    }
  }
}

if (res.length === 0) {
  console.log(0);
  console.log(0);
} else {
  console.log(res.length);
  console.log(Math.max(...res));
}
