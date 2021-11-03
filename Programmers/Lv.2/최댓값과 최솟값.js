function solution(s) {
  var answer = "";
  var arr = s
    .split(" ")
    .map((a) => parseInt(a))
    .sort((a, b) => a - b);
  answer = arr[0] + " " + arr[arr.length - 1];
  return answer;
}
