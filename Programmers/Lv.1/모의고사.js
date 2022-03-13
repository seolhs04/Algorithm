function solution(answers) {
  var answer = [];
  var one_sol = [1, 2, 3, 4, 5];
  var two_sol = [2, 1, 2, 3, 2, 4, 2, 5];
  var three_sol = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  var one = 0;
  var two = 0;
  var three = 0;

  for (var i = 0; i < answers.length; i++) {
    if (answers[i] === one_sol[i % 5]) one += 1;
    if (answers[i] === two_sol[i % 8]) two += 1;
    if (answers[i] === three_sol[i % 10]) three += 1;
  }

  var max = Math.max(one, two, three);
  if (max === one) answer.push(1);
  if (max === two) answer.push(2);
  if (max === three) answer.push(3);

  return answer;
}
