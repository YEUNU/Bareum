<template>
    <div>
        <p>{{ postId }}</p>

        <div v-for="comment in comments" :key="comment.commentId">
            <p>{{comment.commentDate}}</p>
            <p>{{comment.commentUserName}}</p>
            <p>{{comment.commentContent}}</p>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserInfo } from '../../stores';

export default {
    props: {
        postId: {
            type: String,
            required: true,
        }
    },
    setup(){
        const userInfo = useUserInfo();
        const comments = ref([]);

        async function fetchPostComment(postId){
            try {
                const response = await axios.get(`api/community/comments/${postId}`);
                comments.value = response.data.comments;
            } catch(err) {
                console.error("error",err);
            }
        }
        onMounted(() => {
            // fetchPostComment(postId);
        });
        return {
            fetchPostComment,
            comments,
        }
    }
};
</script>
