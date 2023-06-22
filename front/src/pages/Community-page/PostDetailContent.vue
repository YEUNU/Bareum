<template>
    <div style="width:100%; height: 100%; margin-bottom: 20%;">
        <nav class="navbar fixed-top bg-white" style="position: fixed; width: 100%; top: 0; z-index: 10;">
                    <div class="container-fluid">
                    <router-link to="/community" class="navbar-brand" style="margin-left: 2vh;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                        </svg>
                    </router-link>
                    </div>
                    
        </nav>

        <div style="width: 100%; height: 100%; position: relative; top: 10vh;" >
        
            

            <div style="text-align: left; font-weight: bold; font-size: 35px;">
                {{ post.post_title }}
            </div>

                <div class="d-flex align-items-center" style="margin-top: 2%; border-bottom: 2px solid #eeeeee;">
                    <div class="flex-shrink-0">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                        alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                        style="width: 50px; margin-bottom: 10%;">
                    </div>
                            <div class="flex-grow-1 ms-3">
                                <div style="text-align: left; font-weight: bold;">
                                {{ post.user_name }}
                            </div>
                            
                            <div style="text-align: left; font-size: 12px; color: gray;">
                                {{ formatDate(post.post_date) }}
                            </div>
                            
                        </div>
                </div>

            <div>
                <div style="width: 100%; height: 100%; text-align: left; margin-top: 2%; padding-top: 2%; padding-bottom: 2%; border-bottom: 2px solid #eeeeee;">
                    <div class="flex-shrink-0">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                        alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                        style="width: 30%; height: 50%; margin-bottom: 10%;">
                    </div>
                    {{ post.post_contents }}
                
                </div>
            </div>
                <div v-if="post.post_image_urls && post.post_image_urls.length > 0">
                    <div v-for="(url, index) in post.post_image_urls" :key="index">
                        <img :src="`${url}`" :alt="'Image ' + (index + 1)" class="post-image"/>
                    </div>
                </div>

            <div v-if="post.member_id == userInfo.memberId" style="  padding-top: 2%; padding-bottom: 2%; border-bottom: 2px solid #eeeeee;">
                <button class="postbutton" style="margin-right: 50%;">수정</button>
                <button class="postbutton">삭제</button>
            </div>

            <div v-for="comment in comments" :key="comment.comments_id">
                <div class="card-body" style=" border-bottom: 2px solid #eeeeee;">
                <div class="d-flex align-items-center" style="margin-top: 2%;">
                    
                <div class="flex-shrink-0">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                    alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                    style="width: 50px; margin-bottom: 10%;">
                </div>

                <div class="flex-grow-1 ms-3">
                    <div class="d-flex flex-row align-items-center">
                        
                        <div class="col-8 col-sm-3" style="text-align: left; font-weight: bold;">
                                        {{ comment.user.user_name }}
                                </div>
                                
                            <div class="col-2 col-sm-3"><router-link :to="{ name: 'postReplyPage', params: { postId: post.post_id, commentsId: comment.comments_id }}">
                            <span>답글</span>
                    </router-link></div>
                    <div class="col-2 col-sm-3"><div style="text-align: left; font-size: 15px;">좋아요{{ comment.comment_like }}</div></div>
                    </div>
                    <div>
                        <div style="text-align: left; font-size: 12px; color: gray; width:100%">
                                    {{ formatDate(comment.comment_date) }}
                                </div>
                    </div>
                </div>

                </div>

                <div style="text-align: left; font-size: 15px;">댓글 내용 {{ comment.comment_contents }}</div>
                
                <div v-if="comment.user.member_id == userInfo.memberId" style="margin-top: 2%; margin-bottom: 5%;">
                        <button class="postbutton">수정</button>
                        <button class="postbutton">삭제</button>
                    </div>
                
            
                
                <div v-if="comment.replies.length" class="replies" style="width:100%; margin-left:5%;">
                    <div>
                        
                    <div v-for="reply in comment.replies" :key="reply.comments_id" style="width:100%;">
                        <div class="d-flex align-items-center" style="margin-top: 2%; width: 100%;">
                            
                            <div class="flex-shrink-0">
                                <div style="width: 5%; margin-left: -20%;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-return-right" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1.5 1.5A.5.5 0 0 0 1 2v4.8a2.5 2.5 0 0 0 2.5 2.5h9.793l-3.347 3.346a.5.5 0 0 0 .708.708l4.2-4.2a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 8.3H3.5A1.5 1.5 0 0 1 2 6.8V2a.5.5 0 0 0-.5-.5z"/>
</svg></div>
                                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                                alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                                style="width: 50px; margin-bottom: 10%;">
                            </div>

                            <div class="flex-grow-1 ms-3">
                                <div class="d-flex flex-row align-items-center">
                                    
                                    <div class="col-8 col-sm-3" style="text-align: left; font-weight: bold;">
                                                {{ reply.user.user_name }}
                                    </div>
                                            
                                    <div class="col-2 col-sm-3">
                                            <router-link :to="{ name: 'postReplyPage', params: { postId: post.post_id, commentsId: comment.comments_id }}">
                                                <span>답글</span>
                                            </router-link>
                                    </div>

                                    <div class="col-2 col-sm-3">
                                            <div style="text-align: left; font-size: 15px;">좋아요{{ reply.comment_like }}</div>
                                    </div>

                                </div>

                                <div>
                                    <div style="text-align: left; font-size: 12px; color: gray; width:100%">
                                                {{ formatDate(reply.comment_date) }}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div style="text-align: left; font-size: 15px;">대댓글 내용 {{ reply.comment_contents }}</div>

                                    <div v-if="reply.user.member_id == userInfo.memberId" style="margin-top: 2%; margin-bottom: 5%;">
                                        <button class="postbutton">수정</button>
                                        <button class="postbutton">삭제</button>
                                    </div> 
                    </div>
                </div>
            </div>
        </div>

                <router-link :to="{ name: 'postReplyPage', params: { postId: post.post_id, commentsId: comment.comments_id }}">
                        <p>답글 달기</p>
                </router-link>

        </div>

            
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

export default {

    props: {
        postId: {
            type: String,
            required: true,
        }
    },
    setup(props) {
        const comments = ref([]);
        const commentInput = ref("");
        const csrf_token = Cookies.get("csrftoken");
        const replyInput = ref("");
        const userInfo = useUserInfo();
        const post = ref({});
        
        const formatDate=(date)=>{
            const dateObj = new Date(date);
            const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}  ${dateObj.getHours()}:${dateObj.getMinutes()}`;
            return formattedDate;
        }


        const likePost = () => {
            if (post.value.member_id !== userInfo.memberId) {
                axios
                .post(
                    "/api/community/like_post",
                    { post_id: post.value.post_id, member_id: post.value.member_Id },
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
                const response = await axios.get(`/api/community/detail/${postId}`,{
                    
                    headers:{
                        withCredentials: false, 
                    }
                });
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
            likePost, // likePost 함수를 반환하여 템플릿에서 사용할 수 있게합니다.
            formatDate,

        };
    },
    components: { CommuInput }
};
</script>

<style>
.postbutton {
    background-color: #2dce89;
    border-radius: 5px;
    color:white;
}

.post-image {
    width: 100px ;
    height: 100px ;
}
</style>