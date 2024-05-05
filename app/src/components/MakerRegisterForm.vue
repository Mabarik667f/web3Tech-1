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
                password: 'Пароль',
                title: 'Производитель',
                describe: 'Описание',
                regions: 'Регионы'
            },
            regionsOptions: [
                {value: 'Московская область', name: 'Московская область'},
                {value: 'Калужская область', name: 'Калужская область'},
                {value: 'Орловская область', name: 'Орловская область'}
            ]
        }
    },
    setup() {
        const formData = ref({
            firstName: "",
            secondName: '',
            lastName: '',
            email: '',
            password: '',
            title: '',
            describe: '',
            regions: []
        })

        const store = useStore();

        const makerRegistryHook = async () => {
            await store.dispatch('makerRegistry', formData.value);
            router.push('/profile');
        }

        return {formData, makerRegistryHook}
    }
}
</script>


<template>
        <wave-form @submit.prevent="makerRegistryHook()" class="default-form">
            <template v-slot:header>
                <h1>Зарегистрироваться</h1>
            </template>
            <template v-slot:fields>
                <div v-for="(value, key) in formData" :key="key">
                <div v-if="key === 'describe'" class="form-group">   
                    <label :for="key">{{ labels[key] }}: </label>
                    <textarea :id="key" class="form-control"
                    v-model="formData[key]">
                    </textarea>
                </div> 
                <div v-else-if="key === 'regions'" class="form-group">
                    <label :for="key">{{ labels[key] }} </label>
                    <wave-select :id="key" class="form-control"
                    v-model="formData.regions"
                    :options="regionsOptions"
                    ></wave-select>
                </div>
                <div v-else-if="key === 'password'" class="form-group">
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
</template>

<style scoped>

</style>