<script>
export default {
    name: "wave-form",
}
</script>

<template>
    <form method="post">
        <slot name="header"></slot>
        <slot name="fields"></slot>
        <slot name="button"></slot>
    </form>
</template>

<style scoped>
.default-form {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-content: center;
    justify-content: center;
    /* align-items: flex-start; */
    height: 85vh;
    max-width: 700px;
    margin: 10vh auto;
    box-shadow: 0 0 10px rgba(0, 68, 255, 0.5); 
    border-radius: 20px; 
    padding: 20px;
}

</style>