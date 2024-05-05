<script>
import userOrderReview from "@/hooks/userOrderReview";
export default {
    props: {
        request: {
            type: Object,
            required: true
        }
    },
    emits: ['remove'],
    setup(props, { emit }) {
        
        const userOrderReviewSuccess = async () => {
            const {userOrderReviewTx} = userOrderReview(props.request.id, true);
            await userOrderReviewTx();
            emit('remove', props.request);

        }

        const userOrderReviewCancel = async () => {
            const {userOrderReviewTx} = userOrderReview(props.request.id, false);
            await userOrderReviewTx();
            emit('remove', props.request);

        }

        return {userOrderReviewSuccess, userOrderReviewCancel}
    }
}
</script>

<template>
    <div class="user-order">
        <h5>Order {{ request.total_price }} {{ request.id }}</h5>
        <wave-button class="btn-danger" @click="userOrderReviewCancel()">Отклонить</wave-button>
        <wave-button class="btn-success" @click="userOrderReviewSuccess()">Одобрить</wave-button>
       
    </div>
</template>

<style scoped>
.user-order {
    box-shadow: 0 0 10px rgba(0, 68, 255, 0.5); 
    display: flex;
    flex-direction: row;
    max-width: 300px;
}
</style>