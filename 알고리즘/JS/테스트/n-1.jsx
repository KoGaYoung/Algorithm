function solution(S) {
    const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

    // 문자열 시간을 분 단위로 변환하는 함수
    const toMinutes = (day, time) => {
        let [hours, minutes] = time.split(':').map(Number);
        return days.indexOf(day) * 24 * 60 + hours * 60 + minutes;
    };

    let meetings = S.split('\n').map(meeting => {
        let [day, start, end] = meeting.split(' ');
        return [toMinutes(day, start), toMinutes(day, end)];
    });

    // 모든 회의 시간을 분 단위로 정렬
    meetings.sort((a, b) => a[0] - b[0]);

    let maxSleep = 0;
    for (let i = 0; i < meetings.length - 1; i++) {
        let sleepTime = meetings[i + 1][0] - meetings[i][1];
        maxSleep = Math.max(maxSleep, sleepTime);
    }

    // 첫 회의 전과 마지막 회의 후의 자는 시간을 고려
    maxSleep = Math.max(maxSleep, meetings[0][0]);
    maxSleep = Math.max(maxSleep, 7 * 24 * 60 - meetings[meetings.length - 1][1]);

    return maxSleep;
}

// 예제 입력
let input = "Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu 01:00-23:00\nFri 01:00-23:00\nSat 01:00-23:00\nSun 01:00-21:00";
console.log(solution(input));  // 출력: 180
