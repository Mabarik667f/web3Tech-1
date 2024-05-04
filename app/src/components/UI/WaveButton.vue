<script>
export default {
    name: "wave-button",
    props: {
        type: {
            type: String,
            default: 'submit'
        },
        buttonText: {
            type: String,
            default: 'Подтвердить'
        }
    }
}
</script>

<template>
    <button :type="type" class="btn btn-primary"><slot>{{ buttonText }}</slot></button>
</template>

<style scoped></style>