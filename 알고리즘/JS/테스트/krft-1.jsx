import React, {useState} from "react";

/**
 * 로그인 양식 만들기
 * 2 개의 입력 필드 : username, password
 * 각 입력은 value 속성을 업데이트
 * 제출버튼 onsubmit 클릭 시 핸들러 호출
 * 
 * id="username-input" type="text"
 * id=password-input, type="password"
 * id="login-button", disabled
 */
export default function LoginForm({ onSubmit }) {
    // 유저명
    const [username, setUsername] = useState('');

    // 비밀번호
    const [password, setPassword] = useState('');

    // 둘다 입력되면 true
    const vaildUser = username.length > 0 && password.length > 0;

    /**
     * submit 버튼 클릭이벤트
     */
    const handleSubmit = () => {
      // 한번 더 체크
      if (!vaildUser) {
        return;
      }
      onSubmit(username, password);
    }

    return (
        <div>
            <input
              id="username-input"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeHolder="enter username"
            />
            <input
              id="password-input"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeHolder="enter password"
            />
            <button
              id="login-button"
              disabled={!vaildUser}
              onClick={handleSubmit}
            >Submit
            </button>
        </div>
    );
}
