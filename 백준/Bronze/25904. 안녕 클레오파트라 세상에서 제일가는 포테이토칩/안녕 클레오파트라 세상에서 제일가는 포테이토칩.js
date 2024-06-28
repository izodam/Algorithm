fs = require("fs");

inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +inputData[0].split(" ")[0];
let x = +inputData[0].split(" ")[1];

const t = inputData[1].split(" ").map((res) => +res);
// console.log(t);

let idx = 0;

while (1) {
  if (t[idx] < x) {
    console.log(idx + 1);
    break;
  }
  idx += 1;
  idx = idx % n;

  x += 1;
}
