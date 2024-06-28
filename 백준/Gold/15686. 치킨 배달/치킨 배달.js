const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 도시의 치킨 거리는 모든 집의 치킨 거리의 합
const n = +inputData[0].split(" ")[0];
const m = +inputData[0].split(" ")[1];

const board = [];
const home = [];
const chicken = [];

let res = Infinity;

for (let i = 0; i < n; i++) {
  const row = inputData[i + 1].split(" ").map((value) => +value);
  for (let j = 0; j < n; j++) {
    if (row[j] === 1) {
      home.push([i, j]);
    } else if (row[j] === 2) {
      chicken.push([i, j]);
    }
  }
  board.push(row);
}

function cal_road(left_chicken) {
  let cityChickenLength = 0;
  for (let i = 0; i < home.length; i++) {
    let houseChickenLength = Infinity;
    for (let j = 0; j < left_chicken.length; j++) {
      houseChickenLength = Math.min(
        houseChickenLength,
        Math.abs(home[i][0] - left_chicken[j][0]) +
          Math.abs(home[i][1] - left_chicken[j][1])
      );
    }
    cityChickenLength += houseChickenLength;
  }
  return cityChickenLength;
}

function dfs(depth, idx, left_chicken) {
  if (depth === m) {
    res = Math.min(res, cal_road(left_chicken));
    return;
  }

  if (idx === chicken.length) {
    return;
  }



  left_chicken.push(chicken[idx]);
  dfs(depth + 1, idx + 1, left_chicken);
  left_chicken.pop();

  dfs(depth, idx + 1, left_chicken);
}

dfs(0, 0, []);

console.log(res);
