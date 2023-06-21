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
            <div v-if="post.post_image_urls && post.post_image_urls.length > 0">
              <div v-for="(url, index) in post.post_image_urls" :key="index">
                <img :src="url" :alt="'Image ' + (index + 1)" />
              </div>
            </div>
        </div>
        <div v-if="post.member_id == userInfo.memberId">
            <button>수정</button>
            <button>삭제</button>
        </div>
        <div>
            ------------------
        </div>
        <button @click="likePost">개추좀용 ㅎ</button>
        <span>{{ post.post_like }}</span>
        <div v-for="comment in comments" :key="comment.comments_id">
            <p>댓글 작성일 {{ comment.comment_date }}</p>
            <p>댓글 내용 {{ comment.comment_contents }}</p>
            <p>좋아요{{ comment.comment_like }}</p>
            <p>댓글 작성자 {{ comment.user.user_name }}</p>

            <div v-if="comment.user.member_id == userInfo.memberId">
                <button>수정</button>
                <button>삭제</button>
            </div>            
            <div v-if="comment.replies.length" class="replies">
                <div v-for="reply in comment.replies" :key="reply.comments_id">
                    <p>대댓글 작성일 {{ reply.comment_date }}</p>
                    <p>대댓글 내용 {{ reply.comment_contents }}</p>
                    <p>좋아요 {{ reply.comment_like }}</p>
                    <p>대댓글 작성자 {{ reply.user.user_name }}</p>
                    <div v-if="reply.user.member_id == userInfo.memberId">
                        <button>수정</button>
                        <button>삭제</button>
                    </div> 
                </div>
            </div>
            <router-link :to="{ name: 'postReplyPage', params: { postId: post.post_id, commentsId: comment.comments_id }}">
                    <p>답글 달기</p>
            </router-link>
        </div>
        
    </div>
    <CommuInput @submit="submitComment"></CommuInput>

</template>
  
<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserInfo } from '../../stores';
import Cookies from 'js-cookie';
import CommuInput from '../../components/CommuInput.vue';
import { computed } from 'vue';
export default {
    props: {
        postId: {
            type: String,
            required: true,
        }
    },
    setup(props) {
        const userInfo = useUserInfo();
        const comments = ref([]);
        const post = ref({});
        const commentInput = ref("");
        const csrf_token = Cookies.get("csrftoken");
        const replyInput = ref("");
        const userInfoComputed = computed(() => userInfo.value);
        const likePost = () => {
            if (post.value.member_id !== userInfoComputed.value.memberId) {
            axios
                .post(
                "/api/community/like_post",
                { post_id: post.value.post_id, member_id: userInfoComputed.value.memberId },
                {
                    headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrf_token,
                    },
                }
                )
                .then((response) => {
                if (response.data.success) {
                    post.value.post_like += 1;
                }
                })
                .catch((error) => {
                console.error(error);
                });
            } else {
            console.log("게시물 작성자는 좋아요를 누를 수 없습니다.");
            }
        }


        async function fetchPostDetail(postId) {
            try {
                const response = await axios.get(`/api/community/detail/${postId}`);
                post.value = response.data;
            }
            catch (err) {
                console.error("error", err);
            }
        }

        async function fetchPostComment(postId) {
            try {
                const response = await axios.get(`/api/community/comments/${postId}`);
                comments.value = response.data;
            }
            catch (err) {
                console.error("error", err);
            }
        }

        const submitComment = async (commentInput) => {
            try {
                const postId = post.value.post_id;
                await axios.post(`/api/community/comments/${postId}`, {
                  comment_contents: commentInput,
                  memberId: userInfo.memberId,
                }, {
                  headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrf_token,
                  },
                });
                await fetchPostComment(postId);
            } catch (error) {
                console.error(error);
            }
        };

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
            userInfo,
            likePost // likePost 함수를 반환하여 템플릿에서 사용할 수 있게합니다.
        };
    },
    components: { CommuInput }
};
</script>

