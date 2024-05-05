<script>
import ProductReview from "./UI/ProductReview.vue";
export default {
    components: {
        ProductReview
    },
    props: {
        arr: {
            type: Array
        }
    }
}
</script>

<template>
    <div v-for="product in arr" :key="product.id">
        <ProductReview :request="product" @remove="$emit('remove', product)"></ProductReview>
    </div>
</template>

<style scoped>
</style>