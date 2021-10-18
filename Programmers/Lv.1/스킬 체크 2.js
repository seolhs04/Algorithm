function solution(n) {
  var answer = parseInt(
    parseInt(n.toString(3).split("").reverse().join(""), 3).toString(10)
  );

  return answer;
}
