function solution(files) {
  var answer = [];
  files = files.reduce((a, c) => {
    return a.concat([format(c)]);
  }, []);
  files.sort((a, b) => {
    if (a[0].toLowerCase() > b[0].toLowerCase()) return 1;
    else if (a[0].toLowerCase() < b[0].toLowerCase()) return -1;
    else {
      if (parseInt(a[1]) > parseInt(b[1])) return 1;
      else if (parseInt(a[1]) < parseInt(b[1])) return -1;
      else return 0;
    }
  });
  files = files.reduce((a, c) => {
    return a.concat([c.join("")]);
  }, []);

  answer = files;

  return answer;
}
function format(fileName) {
  let arr = ["", "", ""];
  fileName = fileName.split("");

  while (fileName.length > 0) {
    if (isNaN(parseInt(fileName[0]))) {
      arr[0] += fileName.splice(0, 1);
    } else break;
  }
  while (fileName.length > 0) {
    if (!isNaN(parseInt(fileName[0]))) {
      arr[1] += fileName.splice(0, 1);
    } else break;
  }
  arr[2] = fileName.join("");
  return arr;
}
