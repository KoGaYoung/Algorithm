const fs = require('fs'); 

// 테스트용
const input = fs.readFileSync('/Users/gayoungko/IdeaProjects/Algorithm/알고리즘/JS/example.txt').toString().split(' '); 

// 제출용
// const input = fs.readFileSync('/dev/stdin').toString().split(' '); 

const a = parseInt(input[0]); 
const b = parseInt(input[1]);

console.log(a+b);