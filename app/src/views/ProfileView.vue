<script>
import RegisterReviewList from "@/components/RegisterReviewList.vue";
import ProductsReviewList from "@/components/ProductsReviewList.vue";
import OrdersReviewList from "@/components/OrdersReviewList.vue";
import UserOrdersReviewList from "@/components/UserOrdersReviewList.vue";

import getRegisterReview from "@/hooks/getRegisterReview";
import getReviewProducts from "@/hooks/getReviewProducts";
import getReviewOrders from "@/hooks/getReviewOrders";
import getUserReviewOrders from "@/hooks/getUserReviewOrders";

import { mapState } from "vuex";
export default {
    components: {
        RegisterReviewList,
        ProductsReviewList,
        OrdersReviewList,
        UserOrdersReviewList
    },
    computed: {
        ...mapState({
            role: state => state.auth.role
        })
    },
    setup() {
    
        const { usersArray, makersArray, distributorsArray } = getRegisterReview();

        const {reviewProducts} = getReviewProducts();

        const {reviewOrders} = getReviewOrders();

        const {userReviewOrders} = getUserReviewOrders();

        const removeUserRequest = (user) => {
            usersArray.value = usersArray.value.filter(u => u.id !== user.id);
        };
        const removeMakerRequest = (user) => {
            makersArray.value = makersArray.value.filter(u => u.id !== user.id);
        };
        const removeDistributorRequest = (user) => {
            distributorsArray.value = distributorsArray.value.filter(u => u.id !== user.id);
        };
        const removeProductRequest = (product) => {
            reviewProducts.value = reviewProducts.value.filter(p => p.id !== product.id);
        };

        const removeOrderRequest = (order) => {
            reviewOrders.value = reviewOrders.value.filter(o => o.id !== order.id);
        };

        const removeUserOrderRequest = (order) => {
            userReviewOrders.value = userReviewOrders.value.filter(o => o.id !== order.id);
        };


        return { usersArray,
            makersArray,
            distributorsArray,
            reviewProducts,
            reviewOrders,
            userReviewOrders,

            removeUserRequest, 
            removeMakerRequest,
            removeDistributorRequest,
            removeProductRequest,
            removeOrderRequest,
            removeUserOrderRequest };

    }
}
</script>

<template>
    <div class="profile">
        <wave-button @click="$router.push('/createProduct')">Создать товар</wave-button>
        <div>
            <h2>Профиль</h2>
        </div>
        <div v-if="role === 'operator'">
            <h2>Активация учетных записей</h2>
            <RegisterReviewList :arr="usersArray" @remove="removeUserRequest"></RegisterReviewList>
            <RegisterReviewList :arr="makersArray" @remove="removeMakerRequest"></RegisterReviewList>
            <RegisterReviewList :arr="distributorsArray" @remove="removeDistributorRequest"></RegisterReviewList>
        </div>
        <div v-if="role === 'operator'">
            <h2>Подтвердить создание товара</h2>
            <ProductsReviewList :arr="reviewProducts" @remove="removeProductRequest"></ProductsReviewList>
        </div>
        <div>
            <h2>Подтвердить создание заказа</h2>
            <OrdersReviewList :arr="reviewOrders" @remove="removeOrderRequest"></OrdersReviewList>
        </div>
        <div>
            <h2>Принять изменения в заказе</h2>
            <UserOrdersReviewList :arr="userReviewOrders" @remove="removeUserOrderRequest"></UserOrdersReviewList>
        </div>
    </div>
</template>

<style scoped>
.profile {
    margin-top: 20px;
}
</style>