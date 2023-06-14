export const loginWithKakao = () => {
    return new Promise((resolve, reject) => {
      // 카카오 초기화
      if (!window.Kakao.isInitialized()) {
        window.Kakao.init("11766fc41d5a6f91c459162e6c7ed4d8");
      }
  
      // 이전에 카톡 연결해지가 필요한 경우 호출하세요.
      // window.Kakao.Auth.logout();
  
      window.Kakao.Auth.login({
        scope: "profile_nickname,profile_image,gender,age_range,account_email",
        success: (authObj) => {
          resolve(authObj);
        },
        fail: (error) => {
          reject(error);
        },
      });
    });
  };
  