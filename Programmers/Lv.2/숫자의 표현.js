function solution(n) {
  var answer = 1;
  for (var i = 2; i <= n; i++) {
    i % 2 !== 0 && n % i === 0 ? (answer += 1) : null;
  }
  return answer;
}
