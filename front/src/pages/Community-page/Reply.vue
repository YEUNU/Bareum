<template>

        <div>
            <p>댓글 작성일 {{ comment.comment_date }}</p>
            <p>댓글 내용 {{ comment.comment_contents }}</p>
            <p>좋아요{{ comment.comment_like }}</p>
            <p>댓글 작성자 {{ comment.user.user_name }}</p>            
            <div v-if="comment.replies.length" class="replies">
                <div v-for="reply in comment.replies" :key="reply.comments_id">
                    <p>대댓글 작성일 {{ reply.comment_date }}</p>
                    <p>대댓글 내용 {{ reply.comment_contents }}</p>
                    <p>좋아요 {{ reply.comment_like }}</p>
                    <p>대댓글 작성자 {{ reply.user.user_name }}</p>
                </div>
            </div>
            <div>
            </div>
        </div>

    <CommuInput></CommuInput>
</template>
<script>
import {ref,onMounted} from 'vue'
import axios from 'axios';
import CommuInput from '../../components/CommuInput.vue';

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
        const comment = ref({});
        async function fetchDetailComment(commentId){
            try {
                const response = await axios.get(`/api/community/comments/reply/${commentId}`);
                comment.value = response.data
            } catch(err) {
                console.error("error",err);
            }
        };

        onMounted(() => {
            fetchDetailComment(props.commentsId)
        });

        return{
            comment,
            fetchDetailComment,
        }
    },
    components: { CommuInput }

}

</script>
<style>
    
</style>