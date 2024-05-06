<script>
import ProductCard from '@/components/UI/ProductCard.vue';
import getSellers from "@/hooks/getSellers";
export default {
    components: {
        ProductCard
    },

    setup() {
        const {reviewProducts} = getSellers();
        return {reviewProducts}
    }
}
</script>

<template>
    <div>
        <div v-for="product in reviewProducts" :key="product.id">
            <ProductCard :product="product"></ProductCard>
        </div>
    </div>
</template>

<style scoped>

</style>