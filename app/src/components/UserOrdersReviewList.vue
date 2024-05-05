<script>
import UserOrderReview from "./UI/UserOrderReview.vue";
export default {
    components: {
        UserOrderReview
    },
    props: {
        arr: {
            type: Array
        }
    }
}
</script>

<template>
    <div v-for="order in arr" :key="order.id">
        <UserOrderReview :request="order" @remove="$emit('remove', order)"></UserOrderReview>
    </div>
</template>

<style scoped>
</style>