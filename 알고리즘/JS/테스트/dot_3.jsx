/**
 * join_date: 입사날짜
 * resign_date: 퇴사날짜
 * holidays: 공휴일 날짜
 * 
 * 입사날짜~퇴사날짜까지 공휴일 제외 실 근무일수 구하기
 * 
 * @param join_date string
 * @param resign_date string
 * @param holidays string[]
 */
function solution(join_date, resign_date, holidays) {
    // 실 근무일수
    var answer = 0;

    // 날짜 차이 구하기
    const startDate = new Date(join_date.substring(0, 10));
    const endDate = new Date(resign_date);

    // 날짜 증가 반복
    for (let i = startDate; i <= endDate; i.setDate(i.getDate() + 1)) {
        // 휴일 형식으로 바꾸기
        const month = (i.getMonth() + 1).toString().padStart(2, '0');
        const day = i.getDate().toString().padStart(2, '0');
        const formattedDate = `${month}/${day}`;

        const weekend = i.getDay();

        // 휴일(0, 6), 공휴일 아닌 경우에 실근무 +
        if (weekend !== 0 && weekend !== 6 && !holidays.includes(formattedDate)) {
            answer++;
        }
    }
    return answer;
}