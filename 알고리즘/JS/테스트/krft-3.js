/**
 * 폼검사 함수 만들기
 * 
 * 사람 or 회사 하나만 선택
 * 
 * 1. 사람인 경우
 * firstname, lastname 비면 안됨, 공백은됨.
 * 이메일 @포함 문자숫자 /. (a-z, A-Z, 0-9, .) 1~64자
 * 
 * 2. 회사인 경우
 * 컴퍼니네임 필수
 * 전화번호는 대시와 공백으로 구분 6자리이상
 */
 function solution() {
  

    // 사람체크 한 경우
    if ($('#type_person').is(':checked')) {
        
        var firstName = $('#first_name').val().trim();
        var lastName = $('#last_name').val().trim();
        var email = $('#email').val().trim();

        // 이메일 정규식
        var emailReg = /^[a-zA-Z0-9.]*(\.?[a-zA-Z0-9.]){1,64}@[a-zA-Z0-9.]*(\.?[a-zA-Z0-9.])*$/;

        return firstName !== '' &&
        lastName !== '' &&
        emailReg.test(email)

    
        
    }
     
    
    // 회사 체크한 경우
    else if ($('#type_company').is(':checked')){
         var companyName = $('#company_name').val().trim();
         var companyPhone = $('#phone').val().trim();

        var phoneReg = /^\d[\d\s-{4,}\d]$/;

        return companyName !== '' &&
        phoneReg.test(companyPhone)
        
    }

    else {
        return false;
    }
}
