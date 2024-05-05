<script>
export default {
    props: {
        product: {
            type: Object,
            required: true
        }
    },
}
</script>

<template>
    <div>
        <h1>{{ product.title }}</h1>
        <span>{{ product.regions }}</span>
        <wave-button @click="$router.push('/createOrder')">Заказать</wave-button>
    </div>
</template>

<style scoped>

</style>