function solution(arr1, arr2) {
  var answer = [];

  for (var i = 0; i < arr1.length; i++) {
    var arr = [];
    for (var j = 0; j < arr2[0].length; j++) {
      var number = 0;
      for (var k = 0; k < arr2.length; k++) {
        number += arr1[i][k] * arr2[k][j];
      }
      arr.push(number);
    }
    answer.push(arr);
  }

  return answer;
}
