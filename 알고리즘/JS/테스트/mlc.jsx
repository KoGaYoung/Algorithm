function solution(numbers) {
  if (numbers.length <= 2) {
    return 0;
  }

  const first = numbers[0];
  const second = numbers.length && numbers[1];

  let count = 0;

  for (let i = 2; i < numbers.length; i++) {
    if (numbers[i] !== first && numbers[i] !== second) {
      count++;
    }
  }

  return count;
}