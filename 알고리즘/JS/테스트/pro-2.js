function solution(n) {
    // 악수 가능한 방법의 수를 저장하는 배열을 생성하고 초기값을 설정합니다.
    let dp = [1, 2];
    
    // n이 1 또는 2일 경우, 초기값을 반환합니다.
    if (n === 1) return dp[0];
    if (n === 2) return dp[1];
    
    // n이 3부터 n까지 반복하면서 악수 가능한 방법의 수를 계산합니다.
    for (let i = 2; i < n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    // n명일 때의 악수 가능한 방법의 수를 반환합니다.
    return dp[n - 1];
}

console.log(solution(5));