import { onMounted } from 'vue';
import Cookies from 'js-cookie';

export default {
  install(app) {
    app.mixin({
      setup() {
        onMounted(() => {
          const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
          if (csrfToken) {
            Cookies.set('csrftoken', csrfToken);
          }
        });
      },
    });
  },
};
