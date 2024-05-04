<script>
export default {
    name: "wave-select",
    props: {
        modelValue: {
            type: Array,
            default: () => []
        },
        options: {
            type: Array,
            default: () => []
        }
    },
    methods: {
        updateSelection(event) {
            const selectedValues = Array.from(event.target.selectedOptions, option => option.value);
            this.$emit("update:modelValue", selectedValues);
        }
    }
}
</script>

<template>
    <select multiple :value="modelValue" @change="updateSelection">
        <option disabled value="">Выберите из списка: </option>
        <option
        v-for="option in options"
        :key="option.value"
        :value="option.value">
            {{ option.name }}
        </option>
    </select>
</template>

<style scoped></style>