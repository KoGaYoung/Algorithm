/**
 * n개의 문이 배열로 표현, 초기에 닫혀있음
 * 외부 루프(i)는 1부터 n까지 순회합니다.
 * 내부 루프(j)는 i-1부터 시작하여 n까지 i의 간격으로 증가합니다.
 * 내부 루프의 각 단계에서, 문의 상태가 뒤집힙니다 (닫혀 있으면 열리고, 열려 있으면 닫힘).
 * 최종적으로 열려 있는 문들의 개수를 반환합니다.
 * @param {*} n 
 * @returns 
 */
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