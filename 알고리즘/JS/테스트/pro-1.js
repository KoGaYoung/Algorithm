/**
 * [[1, 3 6, 10, 15]
 *  [2, 5, 9, 14, 19]
 *  [4, 8, 13. 18, 21]
 *  [7, 12, 17, 20, 23]
 *  [11, 16, 20, 22, 24]
 * ]
 * 이런 유형의 배열을 r만큼 90도 회전했을 때 배열 리턴
 * @param {*} matrix 
 * @param {*} r 
 * @returns 
 */
function solution (matrix, r) {
    // 빈 배열 그대로 리턴
    if (matrix.length === 0) 
        return []
    
    let result = [];

    for(let i = 0; i < matrix[0].length; i++) {
        result.push([]); 
    }

    // 90도 돌렸을 때
    for(let j = 0; j < matrix[0].length; j++){
        for(let i = 0; i < matrix.length; i++){
            // matrix의 세로방향 요소들을 result의 가로방향 요소들로 import!
            result[j].push(matrix[i][j])
        } 

        result[j].reverse(); // 그리고 result의 요소들은 reverse
    }
    
    //4로 나누고 나머지가 0일때
    if(r % 4 === 0) { 
        return matrix;
    }
    // 나머지가 1일 때 위에서 구해놓은 result 바로 반환 
    else if(r === undefined || r % 4 === 1) {
        return result;
    }
    // 행렬의 각 요소를 reverse하고 행렬 전체도 한번 reverse
    else if(r % 4 === 2) { 
        for(let j=0; j<matrix.length; j++){
            matrix[j].reverse(); 
        }

        matrix.reverse();
        return matrix;
    }
    else {
        for(let j=0; j<result.length; j++){
            result[j].reverse();
        }
        result.reverse();
        return result;
    }
  };