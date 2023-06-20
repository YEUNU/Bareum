<template>
    <div>
       뒤로가기 홈 등등
    </div>
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
}
</script>
<style >

    
</style>