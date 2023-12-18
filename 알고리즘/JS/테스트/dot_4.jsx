/**
 * 라운드로빈(순차방식) -> 걸리는 시간 리턴
 */
function roundRobin (numServer, logs) {
    const servers = new Array(numServer).fill(new Date());
    let currentServer = 0;

    // console.log(servers);
    for (let log of logs) {
        // 파싱
        const splitLog = log.split(' ');
        const requestTime = new Date(`${new Date().toISOString().substring(0, 10)}T${splitLog[0]}Z`);
        const processTime = splitLog[1];

        let startTime = new Date(Math.max(servers[currentServer].getTime(), requestTime.getTime()));
        servers[currentServer] = new Date(startTime.getTime() + processTime * 1000);

        // 다음 서버로 이동
        currentServer = (currentServer + 1) % numServer;
    }
    // console.log(servers);
    return Math.max(...servers.map(s => s.getTime())) - new Date(0).getTime();
}

/**
 * 2.리스트커넥션(최소접속방식) -> 걸리는 시간 리턴
 */
function leastConnection (numServer, logs) {
    const servers = new Array(numServer).fill(new Date());

    for (let log of logs) {
        // 파싱
        const splitLog = log.split(' ');
        const requestTime = new Date(`${new Date().toISOString().substring(0, 10)}T${splitLog[0]}Z`);
        const processTime = splitLog[1];

        // 가장 빨리 처리가 끝나는 서버 찾기
        let minFinishTime = Math.min(...servers.map(s => s.getTime()));
        let nextServer = servers.findIndex(s => s.getTime() === minFinishTime);

        let startTime = new Date(Math.max(servers[nextServer].getTime(), requestTime.getTime()));
        servers[nextServer] = new Date(startTime.getTime() + processTime * 1000);
    }
    return Math.max(...servers.map(s => s.getTime())) - new Date(0).getTime();
}

/**
 * 1.라운드로빈(순차방식) - 요청을 서버에 순차적 분배
 * 2.리스트커넥션(최소접속방식) - 요청을 커넥션 가장 적은 서버로 분배
 * 
 * 어떤 방식이 얼마나 빠른지 리턴
 * 
 * @param numServer number 서버 대수
 * @param logs string[] 요청시간 처리시간 로그
 * 
 * @return [1|2, number]
 */
function solution(numServer, logs) {
    const roundTime = roundRobin(numServer, logs);
    const leastTime = leastConnection(numServer, logs)

    // 숫자가 크면 느려요
    if (roundTime < leastTime) {
        return [1, leastTime - roundTime]
    }
    else if (roundTime > leastTime) {
        return [2, roundTime - leastTime]
    }
    // 같은 경우
    else {
        return [0,0]
    }
}