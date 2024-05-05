<script>
import OrderReview from "./UI/OrderReview.vue";
export default {
    components: {
        OrderReview
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
        <OrderReview :request="order" @remove="$emit('remove', order)"></OrderReview>
    </div>
</template>

<style scoped>
</style>