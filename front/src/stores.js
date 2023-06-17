import { defineStore } from 'pinia';


//예시코드임 나중에 수정
// store를 여러개 만들어도됨
export const useStore = defineStore('app', {
  state() {
    return {
      count: 0,
      name: 'John',
      isLoggedIn: false,
    };
  },
  getter:{
    getCount(state){
        return state.count
    }
  },
  actions: {
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    },
    updateName(newName) {
      this.name = newName;
    },
    login() {
      this.isLoggedIn = true;
    },
    logout() {
      this.isLoggedIn = false;
    },
  },
});



//현재 로그인한 유저의 정보
export const useUserInfo = defineStore('userInfo',{
  state : ()=>({
    isLoggedIn:true,
    userId:"",
    name:"",
    age:null,
    sex:null,
  }),
  getters:{
    getIsLoggedIn(state){
      return this.isLoggedIn
    },
    getUserInfo(state){
      return state.userId, state.name, state.age, state.sex
    }
  },
  actions:{
    userLogin(userId,name){
      this.name = name;
      this.userId = userId;
      this.isLoggedIn = true;
    },
    userLogout() {
      this.isLoggedIn = false;
      this.isLoggedIn=false;
      this.userId="";
      this.name="";
      this.age=null;
      this.sex=null;
    },
  }
})

export const userNutraceuticals = defineStore('nutraceuticals',{
  state:()=>({
    name:"",
  }),
  getters:{

  },
  actions:{
    
  }
})