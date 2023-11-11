
/**
 *  1. 0인 경우 맨 앞에 50 리턴
 *  2. -를 가진 음수인 경우 -뒤 5붙여서 리턴
 *  3. 양수인 경우 스트링으로 바꿔서 5보다 작은수가 나오면 추가
 */
 function solution(N) {
    const s = N.toString();

   // 1. 0인 경우
   if (N === 0) {
       return 50;
   }
   
   // 2. 음수인 경우
   else if (N < 0) {
       const foramtS = '-5' + s.split('-')[1];

       return parseInt(foramtS, 10);
   }

   // 3. 양수인 경우
   else {
       let max = 0;

       for (let i=0; i<= s.length; i++) {
           const newValue = parseInt(s.slice(0, i) + '5' + s.slice(i), 10);
  
           max = Math.max(max, newValue);
       }
       return max;
   }
}
