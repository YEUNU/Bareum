import { ref } from 'vue';
import axios from 'axios';
import { useUserInfo } from './stores.js';

const checkLogin = async () => {
    const userInfo = useUserInfo();
    try {
      if (!userInfo.isLoggedIn) {
        return false;
      }

      const response = await axios.get('/api/account/session', {
        withCredentials: true,
      });

      if (response.status === 200) {
        return true;
      }
    } catch (err) {
      if (err.response.status === 302) {
        userInfo.$reset();
        window.alert('세션이 만료되었습니다. 다시 로그인 해주세요');
        return false;
      }
    }
};

export default checkLogin;

