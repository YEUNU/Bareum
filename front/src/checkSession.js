import axios from "axios";

export default {
    methods: {
      checkSession() {
        try{
            const response = axios.get("/api/account/session",{
                withCredentials:true
            });

            if (response.status===200){
                return true
            }
        }catch(err){
            if(err.response.status ===302){
                return false
            }
        }
      },
    },
  };