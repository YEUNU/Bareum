<template>
    <div>
        <p>{{postId}}</p>
        <p>{{postDate}}</p>
        <p>{{postTitle}}</p>
        <p>{{postContent}}</p>
        <p>{{postLike}}</p>
        <p>{{postUserName}}</p>
    </div>
    <div v-for="comment in comments" :key="comment.commentId">
        <p>{{comment.commentDate}}</p>
        <p>{{comment.commentUserName}}</p>
        <p>{{comment.commentContent}}</p>
 
    </div>
  </template>
  
<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import { useUserInfo } from '../../stores';

    export default {
        props: {
            postId: {
            type: Number,
            required: true,
        },
    },
        setup(){
            const userInfo = useUserInfo();
            
            const postDate = ref("");
            const postTitle = ref("");
            const postContent = ref("");
            const postLike = ref("");
            const postUserName = ref("");
            const postUserId = ref(0);

            const comments = ref([]);

            async function fetchPostDetail(postId){
                try{
                    const response = await axios.get(`api/community/detail/${this.postId}`);
                    postDate.value = response.data.postDate;
                    postTitle.value = response.data.postTitle;
                    postContent.value = response.data.postContent;
                    postLike.value = response.data.postLike;
                    postUserName.value = response.data.postUser;
                    postUserId.value = postUserId.data.postUserId;
                }catch(err){
                    console.error("err",err);
                }
            }

            async function fetchPostComment(postId){
                try{
                    const response = await axios.get(`api/community/comments/${this.postId}`);
                    comments.value = response.data.comments;

                }catch(err){
                    console.error("error",err);
                }
            }
            onMounted(()=>{
                fetchPostDetail,
                fetchPostComment
            });
            return{
                fetchPostDetail,
                fetchPostComment,
                postDate,
                postTitle,
                postContent,
                postLike,
                postUserName,
                postUserId,
                postUserId,
                comments
            }
    }
  };
  </script>