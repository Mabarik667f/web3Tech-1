<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router';

export default {
    data() {
        return {
            labels: {
                firstName: 'Имя',
                secondName: 'Фамилия',
                lastName: 'Отчество',
                email: 'Email',
                password: 'Пароль'
            }
        }
    },
    setup() {
        const formData = ref({
            firstName: "",
            secondName: '',
            lastName: '',
            email: '',
            password: '',
        })

        const store = useStore();

        const clientRegistryHook = async () => {
            await store.dispatch('clientRegistry', formData.value);
            router.push('/profile');
        }

        return {formData, clientRegistryHook}
    }
}
</script>

<template>
    <div>
        <wave-form @submit.prevent=clientRegistryHook()>
            <template v-slot:header>
                <h1>Зарегистрироваться</h1>
            </template>
            <template v-slot:fields>
                <div v-for="(value, key) in formData" :key="key">
                <div v-if="key === 'password'" class="form-group">
                    <label :for="key">{{ labels[key] }}: </label>
                    <wave-input :id="key" class="form-control"
                    v-model="formData[key]"
                    :type="'password'"></wave-input>
                </div>
                <div v-else-if="key === 'email'" class="form-group">
                    <label :for="key">{{ labels[key] }}: </label>
                    <wave-input :id="key" class="form-control"
                    v-model="formData[key]"
                    :type="'email'"></wave-input>
                </div>
                <div v-else class="form-group">
                    <label :for="key">{{ labels[key] }}: </label>
                    <wave-input :id="key" class="form-control"
                    v-model="formData[key]"
                    ></wave-input>
                </div>
            </div>
            </template>
            <template v-slot:button>
                <wave-button></wave-button>
            </template>
        </wave-form>
    </div>
</template>

<style scoped>

</style>