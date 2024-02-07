/**
 * 멘션 수 구하기
 */
function solution(members, events) {
  // 멤버 별 멘션 수 초기화
  let mentionCount = new Map();
  members.forEach((id) => mentionCount.set(id, 0));

  // 오프라인 카운트
  let offLineCount = new Map();

  // 이벤트 발생
  events.forEach((e) => {
    let [type, timeStamp, message] = e;
    const time = Number(timeStamp);

    // 동작 확장 측면에서 swich문으로 작성
    switch (type) {
      // 오프라인상태
      case "OFFLINE":
        offLineCount.set(message, time + 60);
        break;

      case "MESSAGE":
        // 중복방지용 멘션
        let mentioned = new set();

        // 모든 유저 멘션 시
        if (message.includes("ALL")) {
          members.forEach((id) => mentioned.add(id));
        }

        message.split(" ").forEach((m) => {
          if (m.startsWith("id")) {
            mentioned.add(m); // 각각 저장
          } else if (m === "HERE") {
            members.forEach((id) => {
              if (!offLineCount.has(id) || offLineCount.get(id) <= timeStamp) {
                mentioned.add(id);
              }
            });
          }
        });

        mentioned.forEach((id) => {
          if (mentionCount.has(id)) {
            mentionCount.set(id, mentionCount.get(id) + 1);
          }
        });
        break;

      default:
        break;
    }
  });

  console.log(mentionCount);
}
