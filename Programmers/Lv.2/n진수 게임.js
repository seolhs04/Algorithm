function solution(n, t, m, p) {
  var answer = "";

  return 진법(n, t, m, p);
}

function 진법(n, t, m, p) {
  var result = "";
  for (var i = 0; i < t * m; i++) {
    result += i.toString(n).toUpperCase();
    if (result.length > t * m) break;
  }
  var arr = [];
  result = result.split("");
  for (var i = 0; i <= t * m; i++) {
    arr.push(result.splice(0, m));
  }
  var str = "";
  for (var i = 0; i < arr.length; i++) {
    str += arr[i][p - 1];
    if (str.length === t) break;
  }
  return str;
}
