function solution(arr) {
  var answer = 최소공배수(arr[0], arr[1]);

  for (var i = 2; i < arr.length; i++) {
    answer = 최소공배수(answer, arr[i]);
  }
  return answer;
}

function 최대공약수(a, b) {
  if (b === 0) return a;
  return 최대공약수(b, a % b);
}
function 최소공배수(a, b) {
  return (a * b) / 최대공약수(a, b);
}
