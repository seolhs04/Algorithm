function solution(n) {
  let arr = n.toString().split("");
  let firstIdx = 0;
  let lastIdx = arr.length - 1;
  while (lastIdx - firstIdx > -1) {
    let temp = null;
    temp = arr[firstIdx];
    arr[firstIdx] = +arr[lastIdx];
    arr[lastIdx] = +temp;
    firstIdx += 1;
    lastIdx -= 1;
  }
  return arr;
}
