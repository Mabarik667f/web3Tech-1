<script>
import {ref} from "vue";
import createOrder from "@/hooks/createOrder";
import router from "@/router";
export default {
    setup() {
        const formData = ref({
            volume: '',
            date: '',
            country: '',
            region: '',
            address: '',
            pre_payment: false
            
        })

        const createOrderHook = async () => {
            const {func} = createOrder(formData.value);
            await func();
            router.push('/profile');
        }

        const togglePrePayment = (event) => {
            formData.value.pre_payment = event.target.checked;
        };

        return { formData, createOrderHook, togglePrePayment };
    }
}
</script>

<template>
    <div>
        <wave-form class="default-form" @submit.prevent="createOrderHook()">
            <template v-slot:header>
                <h1 class="form-header">Создать Заказ</h1>
            </template>
            <template v-slot:fields>
                <div class="form-group">
                    <label :for="'volume'">Объем заказа</label>
                    <wave-input
                    v-model="formData.volume"
                    :id="'volume'"
                    :type="'number'"
                    class="form-control"></wave-input>
                </div>
                <div class="form-group">
                    <label :for="'date'">Дата доставки</label>
                    <wave-input
                    v-model="formData.date"
                    :id="'date'"
                    :type="'date'"
                    class="form-control"></wave-input>
                </div>
                <div class="form-group">
                    <label :for="'country'">Страна (необязательно)</label>
                    <wave-input
                    v-model="formData.country"
                    :id="'country'"
                    class="form-control"></wave-input>
                </div>
                <div class="form-group">
                    <label :for="'region'">Регион (необязательно)</label>
                    <wave-input
                    v-model="formData.region"
                    :id="'region'"
                    class="form-control"></wave-input>
                </div>
                <div class="form-group">
                    <label :for="'address'">Адрес (необязательно)</label>
                    <wave-input
                    v-model="formData.address"
                    :id="'address'"
                    class="form-control"></wave-input>
                </div>
                <div class="form-сheck">
                    <label :for="'pre_payment'">Предоплата</label>
                    <input
                    type="checkbox"
                    :id="'pre_payment'"
                    class="form-check-input"
                    :checked="formData.pre_payment"
                    @change="togglePrePayment"
                    />

                </div>
            </template>
            <template v-slot:button>
                <wave-button class="form-button">Создать</wave-button>
            </template>
        </wave-form>
    </div>
</template>

<style scoped>

</style>