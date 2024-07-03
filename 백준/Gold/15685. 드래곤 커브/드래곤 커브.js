const { group } = require("console");
const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// k세대 드래곤 커브는 k-1세대 드래곤 커브를 끝점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것
const n = +inputData[0];
const board = Array.from({ length: 101 }, () => Array(101).fill(0));

// x, y, d, g
// x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
// 0: x좌표가 증가하는 방향 (→) -> 90도 회전하면 1
// 1: y좌표가 감소하는 방향 (↑) -> 90도 회전하면 2
// 2: x좌표가 감소하는 방향 (←) -> 90도 회전하면 3
// 3: y좌표가 증가하는 방향 (↓) -> 90도 회전하면 0

const dx = [0, -1, 0, 1];
const dy = [1, 0, -1, 0];

for (let i = 0; i < n; i++) {
  let [y, x, d, g] = inputData[i + 1].split(" ").map(Number);
  board[x][y] = 1;

  // 커브 방향 저장
  const curve = [d];

  for (let j = 0; j < g; j++) {
    for (let k = curve.length - 1; k >= 0; k--) {
      curve.push((curve[k] + 1) % 4);
    }
  }

  // 보드판에 표시
  for (let j = 0; j < curve.length; j++) {
    x += dx[curve[j]];
    y += dy[curve[j]];

    if (x >= 0 && x <= 101 && y >= 0 && y <= 101) {
      board[x][y] = 1;
    }
  }
}

let res = 0;

for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 100; j++) {
    if (
      board[i][j] &&
      board[i + 1][j] &&
      board[i][j + 1] &&
      board[i + 1][j + 1]
    ) {
      res += 1;
    }
  }
}

console.log(res);