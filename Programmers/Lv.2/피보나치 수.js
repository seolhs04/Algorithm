function solution(n) {
  var answer = makeArr(n);
  return answer;
}

function makeArr(length) {
  var arr = [0, 1];
  for (var i = 2; i <= length; i++) {
    arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567;
  }
  return arr[length];
}
