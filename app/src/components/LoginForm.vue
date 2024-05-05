<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router';
export default {
    setup() {
        const formData = ref({
            email: '',
            password: ''
        })
        
        const store = useStore();

        const loginHook = async () => {
            const res = await store.dispatch('login', formData.value);
            if (res) {
                router.push('/profile');
            }
        }
        return {formData, loginHook}
    }
}
</script>

<template>
    <wave-form @submit.prevent="loginHook()" class="default-form">
        <template v-slot:header>
            <h1 class="form-header">Войти</h1>
        </template>
        <template v-slot:fields>
            <div class="form-group">
                <label :for="formData.email">Email</label>
                <wave-input
                :type="'email'"
                v-model="formData.email"
                :id="'email'"
                class="form-control"
                ></wave-input>
            </div>
            <div class="form-group">
                <label :for="formData.password">Пароль</label>
                <wave-input
                :type="'password'"
                v-model="formData.password"
                :id="'password'"
                class="form-control"
                ></wave-input>
            </div>
        </template>
        <template v-slot:button>
            <wave-button class="form-button">Войти</wave-button>
        </template>
    </wave-form>
</template>

<style>
.form-header{
    margin-bottom: 10px;
}
.form-button {
    margin-top: 10px;
}
</style>