<template>
    <CommuTopNavBar/>
    <router-view :postId="postId" :commentsId="commentsId" />
</template>
<script>
import CommuTopNavBar from '../../components/Navbar/CommuTopNavBar.vue';
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
  components:{CommuTopNavBar}
}
</script>
<style >

    
</style>