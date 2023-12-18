/**
 * 1234567 -> 5 -> 5
 * 1234567891011 -> 10넘어가는 숫자는 2자리됨
 * 1~9 한 자리 숫자는 9개
 * 10~99까지 두 자리 숫자는 99-10+1 = 90개
 * 100~999까지 세 자리 숫자는 999-100+1 = 900개
 * 1000~9999 = 9000개
 * 
 * 일단 풀고 시간남으면 리펙토링
 * n = 1000000000 일때 타임아웃남
 * 
 * @param n number
 */
function solution(n) {
    let strNumber = '';
    let start = 1;

    for (let i=start; i< n + 1; i++) {
       strNumber += i.toString();
    }

    const strArray = strNumber.split('');

    return Number(strArray[n-1]);
}