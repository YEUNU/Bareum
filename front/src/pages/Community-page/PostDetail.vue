<template>
  <router-view :postId="postId" :commentsId="commentsId" />
</template>
<script>

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
  components:{}
}
</script>
<style >

    
</style>