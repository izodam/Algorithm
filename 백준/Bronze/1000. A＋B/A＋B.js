const fs = require("fs");

// string으로 받고 싶으면 .map 을 안쓰면 된다
// 여러 줄로 입력받을 때는 split안에 \n
// const inputData1 = fs
//   .readFileSync("/dev/stdin")
//   .toString()
//   .split(" ")
//   .map((value) => +value);
const inputData1 = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((value) => +value);

const [a, b] = inputData1;

console.log(a + b);
