<script>
import { ref } from 'vue';
import reviewProduct from "@/hooks/reviewProduct";
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
            id: props.request.id,
            min_v: 0,
            max_v: 0
        })

        
        const reviewProductHook = () => {
            const {reviewProductTx} = reviewProduct(formData.value);
            reviewProductTx();
            emit('remove', formData.value);

        }
        return {reviewProductHook, formData}
    }
}
</script>

<template>
    <div >
        <wave-form @submit.prevent="reviewProductHook()" id='product' class="default-form">
            <template v-slot:header>
                <h5>{{ request.title }}</h5>
            </template>
            <template v-slot:fields>
                <div class="form-group">
                    <label :for="'min_v'">Мин. Объем</label>
                    <wave-input
                    v-model="formData.min_v"
                    class="form-control"
                    :type="'number'"
                    :id="'min_v'"></wave-input>
                </div>
                <div>
                    <label :for="'max_v'">Макс. Объем</label>
                    <wave-input
                    v-model="formData.max_v"
                    class="form-control"
                    :type="'number'"
                    :id="'max_v'"></wave-input>
                </div>
            </template>
            <template v-slot:button>
                <wave-button class="form-button">Одобрить</wave-button>
            </template> 
        </wave-form>
    </div>
</template>

<style scoped>
#product {
    height: 10vh;
    display: flex;
    flex-direction: row;
}
</style>