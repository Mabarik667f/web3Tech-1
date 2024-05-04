<script>
export default {
    name: "wave-input",
    props: {
        type: {
            type: String,
            default: 'text'
        },
        modelValue: {
            type: [String, Number],
            default: ''
        }
    }
}
</script>

<template>
    <input
    :type="type"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)">
</template>

<style scoped></style>