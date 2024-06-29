const fs = require("fs");
let [n, l] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let num = 1; // 양의 정수이기 때문에 0이 아닌 1부터 시작합니다
let cnt = 0; // 라벨을 붙인 개수

while (true) {
  if (!num.toString().includes(l)) {
    // 해당 숫자를 사용할 수 있으면
    cnt++; // 라벨을 붙입니다
    if (cnt === n) {
      // N개의 원소를 다 라벨링했다면
      console.log(num); // 마지막 값을 출력하고
      break; // 반복문을 그만둡니다
    }
    num++; // 반복문이 끝나지 않았다면 다음 숫자로 넘어갑니다
  } else {
    // l이 포함되어 해당 숫자를 사용할 수 없다면
    num++; // 다음 숫자로 넘어갑니다
  }
}
