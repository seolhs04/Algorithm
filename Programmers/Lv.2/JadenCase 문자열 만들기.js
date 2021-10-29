function solution(s) {
  s = s.toLowerCase();
  var answer = "" + s[0].toUpperCase();
  for (var i = 1; i < s.length; i++) {
    if (s[i - 1] === " ") {
      answer += s[i].toUpperCase();
    } else {
      answer += s[i];
    }
  }
  return answer;
}
