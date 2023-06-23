<template>
    <form @submit.prevent="onSubmitInternal" style="text-align: center; width:100%;">
      <input type="text" id="comment-input" v-model="commentInput" required placeholder="댓글 작성"
        style=" width: 70%; margin-top: 10%; border-radius: 8px; border:1px solid #eeeeee;" />
      <button type="submit" style="margin-left: 5%; background-color: #2dce89; border-radius: 5px; color:white;">작성</button>
    </form>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    props: {
      onSubmit: {
        type: Function,
        required: true,
      },
    },
    setup(props) {
      const commentInput = ref('');
  
      const onSubmitInternal = () => {
        props.onSubmit(commentInput.value);
        commentInput.value = '';
      };
  
      return { commentInput, onSubmitInternal };
    },
  };
  </script>
  