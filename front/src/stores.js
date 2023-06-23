import axios from 'axios';
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
    isLoggedIn:false,
    memberId:null,
    loginId:"",
    name:"",
    profileImgUrl:"",
    birthDay:'',
    age:null,
    gender:null,
    nickName:"",
    weight:null,
    height:null,
  }),
  getters:{

    getIsLoggedIn(state){
      return this.isLoggedIn;
    },

  },
  actions:{
    userLogin(memberId,loginId,name,profileImgUrl){
      this.name = name;
      this.loginId = loginId;
      this.memberId = memberId;
      this.isLoggedIn = true;
      this.profileImgUrl = profileImgUrl
    },

    userAddInfo(birthDay,gender,nickName,weight,height){
      this.birthDay = birthDay;
      this.gender = gender;
      this.nickName = nickName;
      this.weight = weight;
      this.height = height;
    },

    userLogout() {
      this.isLoggedIn = false;
      this.isLoggedIn=false;
      this.userId="";
      this.name="";
      this.age=null;
      this.sex=null;
      axios.get("/api/account/logout")
      .then(()=>{
        window.alert("로그아웃 되었습니다.")
      })
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