<script>
import { ref } from 'vue';
import reviewOrder from "@/hooks/reviewOrder";
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
            prePayment: props.request.pre_payment,
            totalPrice: '',
            paymentTerm: '',
            newDate: '',
        })
        
        
        const reviewOrderHook = () => {
            const {reviewOrderTx} = reviewOrder(formData.value);
            reviewOrderTx();
            emit('remove', formData.value);

        }
        return {reviewOrderHook, formData}
    }
}
</script>

<template>
    <div >
        <wave-form @submit.prevent="reviewOrderHook()" id='order' class="default-form">
            <template v-slot:header>
                <h5>Order {{ request.volume }} {{ request.date }} {{ request.id }} </h5>
            </template>
            <template v-slot:fields>
                <div class="form-group">
                    <label :for="'totalPrice'">Итоговая цена</label>
                    <wave-input
                    v-model="formData.totalPrice"
                    class="form-control"
                    :type="'number'"
                    :id="'totalPrice'"></wave-input>
                </div>
                <div>
                    <label :for="'paymentTerm'">Условия оплаты (необязательно)</label>
                    <wave-input
                    v-model="formData.paymentTerm"
                    class="form-control"
                    :type="'number'"
                    :id="'paymentTerm'"></wave-input>
                </div>
                <div>
                    <label :for="'newDate'">Новая дата (необязательно)</label>
                    <wave-input
                    v-model="formData.newDate"
                    class="form-control"
                    :type="'date'"
                    :id="'newDate'"></wave-input>
                </div>
            </template>
            <template v-slot:button>
                <wave-button class="form-button">Одобрить</wave-button>
            </template> 
        </wave-form>
    </div>
</template>

<style scoped>
#order {
    height: 20vh;
    display: flex;
    flex-direction: column;
}
</style>