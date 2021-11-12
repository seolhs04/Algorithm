function solution(numbers) {
  var answer = "";

  numbers.sort((a, b) =>
    parseInt(`${a}${b}`) > parseInt(`${b}${a}`) ? -1 : 1
  );

  answer = parseInt(numbers.join("")) === 0 ? "0" : numbers.join("");

  return answer;
}
