<template>
    <div>
        <div>
            <div>
            작성자 : {{ post.user_name }}
            </div>
            <div>
                작성일자 : {{ post.post_date }}
            </div>
        </div>
        <div>
            <div>
               제목: {{ post.post_title }}
            </div>
            <div>
               내용: {{ post.post_contents }}
            </div>

        </div>
        <div>
            ------------------
        </div>
        <div v-for="comment in comments" :key="comment.comments_id">
            <p>댓글 작성일 {{ comment.comment_date }}</p>
            <p>댓글 내용 {{ comment.comment_contents }}</p>
            <p>좋아요{{ comment.comment_like }}</p>
            <p>댓글 작성자 {{ comment.user.user_name }}</p>
            <button @click="showReplyForm = !showReplyForm; ">답글 작성</button>
            <div v-if="showReplyForm">
                <input type="text" v-model="replyInput"/>
                <button @click="submitReply(comment.comments_id)">확인</button>
            </div>
            <div v-if="comment.replies.length" class="replies">
                <div v-for="reply in comment.replies" :key="reply.comments_id">
                    <p>대댓글 작성일 {{ reply.comment_date }}</p>
                    <p>대댓글 내용 {{ reply.comment_contents }}</p>
                    <p>좋아요 {{ reply.comment_like }}</p>
                    <p>대댓글 작성자 {{ reply.user.user_name }}</p>
                    <button type="radio"></button>
                </div>
            </div>

        </div>
        <form @submit.prevent="submitComment">
            <label for="comment-input">댓글</label>
            <input type="text" id="comment-input" v-model="commentInput" required/>
            <button type="submit">작성</button>
        </form>
    </div>

</template>
  
<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserInfo } from '../../stores';
import Cookies from 'js-cookie';

export default {
    props: {
        postId: {
            type: String, 
            required: true,
        }
    },
    setup(props){
        const userInfo = useUserInfo();
        const comments = ref([]);
        const post = ref({});
        const commentInput = ref("");
        const csrf_token = Cookies.get('csrftoken');
        const showReplyForm = ref(false);
        const replyInput = ref("");

        async function fetchPostDetail(postId){
            try {
                const response = await axios.get(`/api/community/detail/${postId}`);
                post.value =  response.data
            } catch(err) {
                console.error("error",err);
            }
        }

        async function fetchPostComment(postId){
            try {
                const response = await axios.get(`/api/community/comments/${postId}`);
                comments.value = response.data
            } catch(err) {
                console.error("error",err);
            }
        }

        async function submitComment() {
         try {
           const postId = post.value.post_id;
           await axios.post(`/api/community/comments/${postId}`, {
             comment_contents: commentInput.value, memberId : userInfo.memberId
           },{
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
          }});
           commentInput.value = "";
           await fetchPostComment(postId);
         } catch (error) {
           console.error(error);
         }
    }   
        async function submitReply(parentCommentId) {
        try {
            const postId = post.value.post_id;
            await axios.post(`/api/community/comments/reply/${postId}`, {
                comment_contents: replyInput.value, 
                memberId: userInfo.memberId,
                parent: parentCommentId
            },{
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token
            }});
            replyInput.value = "";
            await fetchPostComment(postId);
        } catch (error) {
            console.error(error);
        }
    }

        
        onMounted(() => {
            fetchPostComment(props.postId);
            fetchPostDetail(props.postId);
        });
        return {
            fetchPostComment,
            comments,
            fetchPostDetail,
            post,
            submitComment,
            commentInput,
            showReplyForm,
            replyInput,
            submitReply            
        }
    }
};
</script>
