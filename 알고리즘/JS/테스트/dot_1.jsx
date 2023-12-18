
/**
 * 1:1 식사이벤트 선호도조사
 * 서로 선호하는 관계가 몇 쌍인지
 * @param p Array<[number, number]>
 */
function solution(p) {
    let answer = 0;

    // 짝
    let prefer = new Map();
    
    // 짝 맞춰 저장
    for (let i = 0; i < p.length; i++) {
        const [a, b] = p[i];
        if (!prefer.has(a)) {
            prefer.set(a, new Set());
        }
        prefer.get(a).add(b);
    }

    // 맞는 짝 카운트
    for (let i = 0; i < p.length; i++) {
        const [a, b] = p[i];
       
        // 짝 찾았어요
        if (prefer.has(b) && prefer.get(b).has(a)) {
            answer ++;
            
            prefer.get(b).delete(a);
            prefer.get(a).delete(b);
        }
    }

    return answer;
}