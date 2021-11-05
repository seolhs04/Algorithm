function solution(n) {
  var answer = 0;
  var count = n
    .toString(2)
    .split("")
    .reduce((a, c) => (a += c === "1" ? 1 : 0), 0);
  while (answer === 0) {
    n += 1;
    answer =
      count ===
      n
        .toString(2)
        .split("")
        .reduce((a, c) => (a += c === "1" ? 1 : 0), 0)
        ? n
        : 0;
  }

  return answer;
}
