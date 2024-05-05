<script>
import RegisterReviewRequest from "./UI/RegisterReviewRequest.vue";
export default {
    components: {
        RegisterReviewRequest
    },
    props: {
        arr: {
            type: Array
        }
    }
}
</script>

<template>
    <div v-for="user in arr" :key="user.id">
        <RegisterReviewRequest :request="user" @remove="$emit('remove', user)"></RegisterReviewRequest>
    </div>
</template>

<style scoped>
</style>