<script>
import { ref } from 'vue';
import { useStore } from 'vuex';

export default {
    props: {
        request: {
            type: Object,
            required: true
        }
    },
    emits: ['remove'],
    setup(props, { emit }) {
        const formData = ref({
            key: props.request.role,
            id: props.request.id
        })

        const store = useStore();
        
        const reviewReg = async () => {
            await store.dispatch('reviewRegister', formData.value);
            emit('remove', formData.value);

        }
        return {reviewReg}
    }
}
</script>

<template>
    <div>
        <span>{{ request.second_name }}</span>
        <span>{{ request.first_name }}</span>
        <span>{{ request.last_name }}</span>
        <span>{{ request.role }}</span>
        <wave-button @click="reviewReg()">Одобрить</wave-button>
    </div>
</template>

<style scoped>
</style>