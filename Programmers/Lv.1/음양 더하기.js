function solution(absolutes, signs) {
  return absolutes.reduce((a, c, i) => (a += c * (signs[i] ? 1 : -1)), 0);
}
