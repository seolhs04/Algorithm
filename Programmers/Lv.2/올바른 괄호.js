function solution(s) {
  var answer = s.split("").reduce((a, c) => {
    if (c === "(") a += 1;
    else a -= 1;
    return a < 0 ? -9999 : a;
  }, 0);

  return answer !== 0 ? false : true;
}
