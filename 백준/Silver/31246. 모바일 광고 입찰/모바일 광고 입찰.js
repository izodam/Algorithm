const fs = require("fs");

const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +inputData[0].split(" ")[0];
const k = +inputData[0].split(" ")[1];

const dif = [];

for (let i = 1; i <= n; i++) {
  const a = +inputData[i].split(" ")[0];
  const b = +inputData[i].split(" ")[1];

  dif.push(b - a);
}

dif.sort(function (a, b) {
  return a - b;
});

// console.log(dif);

if (dif[k - 1] < 0) {
  console.log(0);
} else {
  console.log(dif[k - 1]);
}
