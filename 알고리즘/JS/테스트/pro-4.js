function solution(n) {
    const doors = new Array(n).fill(false);  // 모든 문을 닫음
  
    for (let i = 1; i <= n; i++) {
      for (let j = i - 1; j < n; j += i) {
        doors[j] = !doors[j];
      }
    }
  
    const openDoors = doors.map((status, index) => (status ? index + 1 : 0)).filter(num => num !== 0);
    return openDoors.length;
  }
  
  //열려 있는 문의 개수
  console.log(solution(5));