<template>
    <div>
      <h1>Post Detail: {{ postId }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      postId: {
        type: Number,
        required: true,
      },
    },
  };
  </script>