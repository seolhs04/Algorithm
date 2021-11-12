function solution(skill, skill_trees) {
  var answer = 0;
  skill = skill.split("");
  skill_trees = skill_trees.map((a) => a.split(""));
  for (var i = 0; i < skill_trees.length; i++) {
    skill_trees[i] = skill_trees[i].map((a) => {
      return skill.find((f) => f === a) ? skill.find((f) => f === a) : "";
    });
  }
  skill_trees = skill_trees.map((a) => a.join(""));
  var arr = [];
  for (var i = 1; i <= skill.length; i++) {
    arr.push(skill.slice(0, i).join(""));
  }
  for (var i = 0; i < skill_trees.length; i++) {
    if (skill_trees[i].length === 0) answer += 1;
    else {
      if (arr.find((a) => a === skill_trees[i])) answer += 1;
    }
  }
  return answer;
}
