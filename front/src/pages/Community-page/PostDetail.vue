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
        <div v-for="comment in comments" :key="comment.commentId">
            <p>{{comment.commentDate}}</p>
            <p>{{comment.commentUserName}}</p>
            <p>{{comment.commentContent}}</p>
        </div>
        <form>
            <label>댓글</label>
            <input required/>
            <button type="submit"></button>
        </form>
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
    setup(props){
        const userInfo = useUserInfo();
        const comments = ref([]);
        const post = ref({});
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
                const jsonData = JSON.parse(response.data);
                const fieldsData = jsonData.map(item => item.fields);
            } catch(err) {
                console.error("error",err);
            }
        }
        onMounted(() => {
            // fetchPostComment(postId);
            fetchPostDetail(props.postId)
        });
        return {
            fetchPostComment,
            comments,
            fetchPostDetail,
            post,
        }
    }
};
</script>
