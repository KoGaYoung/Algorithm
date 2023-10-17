function solution(n, r, c) {
    if (n <= 0 || r <= 0 || c <= 0 || r > n || c > n) {
      return undefined; // 유효하지 않은 입력 처리
    }
  
    let num = 1;
    let row = 0;
    let col = 0;
    let direction = -1;
  
    while (num <= n * n) {
      if (row === r - 1 && col === c - 1) {
        return num;
      }
  
      if (direction === -1) {
        if (row > 0 && col < n - 1) {
          row--;
          col++;
        } else if (col < n - 1) {
          col++;
          direction = 1;
        } else {
          row++;
          direction = 1;
        }
      } else {
        if (col > 0 && row < n - 1) {
          col--;
          row++;
        } else if (row < n - 1) {
          row++;
          direction = -1;
        } else {
          col++;
          direction = -1;
        }
      }
  
      num++;
    }
  
    return undefined; // 해당 좌표를 찾지 못한 경우
  }