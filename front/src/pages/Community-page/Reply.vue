<template>
    <div v-if="comment.length > 0">
      <p>댓글 작성일 {{ comment[0].comment_date }}</p>
      <p>댓글 내용 {{ comment[0].comment_contents }}</p>
      <p>좋아요{{ comment[0].comment_like }}</p>
      <p>댓글 작성자 {{ comment[0].user.user_name }}</p>
      <div v-if="comment[0].replies.length" class="replies">
        <div v-for="reply in comment[0].replies" :key="reply.comments_id">
          <p>대댓글 작성일 {{ reply.comment_date }}</p>
          <p>대댓글 내용 {{ reply.comment_contents }}</p>
          <p>좋아요 {{ reply.comment_like }}</p>
          <p>대댓글 작성자 {{ reply.user.user_name }}</p>
        </div>
      </div>
      <div></div>
    </div>
    <CommuInput @submit="submitReplyComment"></CommuInput>
  </template>
<script>
import {ref,onMounted} from 'vue'
import axios from 'axios';
import CommuInput from '../../components/CommuInput.vue';
import { useUserInfo } from '../../stores';
import Cookies from 'js-cookie'

export default {
    props: { 
      postId: {
        type: String,
        required: true,
      },
      commentsId: {
        type: String,   
        required: true,
      },
    },
    setup(props){
        const csrf_token = Cookies.get("csrftoken");
        const userInfo = useUserInfo();
        const comment = ref([]);
        async function fetchDetailComment(commentId){
            try {
                const response = await axios.get(`/api/community/comments/reply/${commentId}`);
                comment.value = response.data
            } catch(err) {
                console.error("error",err);
            }
        };

        const submitReplyComment = async (commentInput) => {
          try {
            const commentId = props.commentsId;
            await axios.post(`/api/community/comments/reply/${commentId}`, {
              comment_contents: commentInput,
              memberId: userInfo.memberId,
              postId:props.postId
            }, {
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
              },
            });
            await fetchDetailComment(commentId);
          } catch (error) {
            console.error(error);
          }
        };

        onMounted(() => {
            fetchDetailComment(props.commentsId)
        });

        return{
            comment,
            fetchDetailComment,
            submitReplyComment
        }
    },
    components: { CommuInput }

}

</script>
<style>
    
</style>