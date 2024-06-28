const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 보드판은 n*h로 생겼고, m개의 가로선이 주어져 있음
const [n, m, h] = inputData[0].split(" ").map(Number);

const board = Array.from({ length: h }, () => Array(n).fill(0));

for (let i = 0; i < m; i++) {
  const [a, b] = inputData[i + 1].split(" ").map(Number);
  board[a - 1][b - 1] = 1;
}

const valiable = [];
let res = 0;
let check = 0;
const now = [];

for (let i = 0; i < h; i++) {
  for (let j = 0; j < n - 1; j++) {
    if (board[i][j] === 0) {
      valiable.push([i, j]);
    }
  }
}

// 내려가는 것을 구현하는 함수
function lad() {
  for (let i = 0; i < n; i++) {
    // i 세로선을 시작으로 내려가기 !!!@!@
    nowRow = i;
    for (let nowCol = 0; nowCol < h; nowCol++) {
      if (board[nowCol][nowRow] === 1) {
        nowRow += 1;
      }
      // 왼쪽 확인
      else if (nowRow > 0 && board[nowCol][nowRow - 1] === 1) {
        nowRow -= 1;
      }
    }
    // i의 결과가 i가 아님 -> 답이 될 수 없음
    if (nowRow !== i) {
      return false;
    }
  }
  return true;
}

// 가로선 그려주는 함수
function draw(now) {
  for (let i = 0; i < now.length; i++) {
    board[now[i][0]][now[i][1]] = 1;
  }
  if (lad()) {
    check = 1;
    return true;
  }

  for (let i = 0; i < now.length; i++) {
    board[now[i][0]][now[i][1]] = 0;
  }
  return false;
}

function dfs(depth, res, idx) {
  // if (check) {
  //   return;
  // }
  if (depth === res) {
    draw(now);
    return;
  }
  for (let i = idx; i < valiable.length; i++) {
    now.push(valiable[i]);
    dfs(depth + 1, res, i + 1);
    now.pop();
  }
}

while (res < 4) {
  dfs(0, res, 0);
  if (check) {
    console.log(res);
    break;
  }
  res += 1;
}

if (!check) {
  console.log(-1);
}
