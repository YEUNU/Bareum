<template>
    <form @submit.prevent="onSubmitInternal" style="display: flex; justify-content: space-between; text-align: center; width:100%; padding: 10px;">

      <input type="text" id="comment-input" v-model="commentInput" required placeholder="댓글 작성"
        style="padding: 0.2em 0.5em; width: 70%; border-radius: 8px; background-color: white; color: #333; border: 1px solid rgba(235, 242, 233, 1); flex-grow: 1;" />

      <button type="submit" style="margin-left: 2vw; padding: 0.2em; background-color: #2dce89; border-radius: 5px; color:white;">작성</button>

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
  