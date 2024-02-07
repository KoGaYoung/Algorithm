/**
 * 명령어 입력 || 입덱스 입력
 */
function solution(commands) {
  // 명령어 종류 별 카운트
  let countCp = 0;
  let countLs = 0;
  let countMv = 0;

  // 실행할 명령어 배열
  let excutionCommandLine = [];

  commands.forEach((c) => {
    // 인덱스 명령어
    if (c.startsWith("!")) {
      const index = Number(c.replace("!", "")) - 1;
      c = excutionCommandLine[index];
    }

    // 명렁어
    switch (c) {
      case "cp":
        countCp++;
        break;
      case "ls":
        countLs++;
        break;
      case "mv":
        countMv++;
        break;
      default:
        break;
    }
    excutionCommandLine.push(c);
  });

  return [countCp, countLs, countMv];
}
