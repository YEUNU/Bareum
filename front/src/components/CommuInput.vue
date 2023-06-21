<template>
    <form @submit.prevent="onSubmitInternal">
      <label for="comment-input">댓글</label>
      <input type="text" id="comment-input" v-model="commentInput" required />
      <button type="submit">작성</button>
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
  