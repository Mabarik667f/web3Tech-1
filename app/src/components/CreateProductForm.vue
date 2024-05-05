<script>
import { ref } from 'vue';
import createProduct from '@/hooks/createProduct';
import router from '@/router';
export default {
    data() {
        return {
            regionsOptions: [
                {value: 'Московская область', name: 'Московская область'},
                {value: 'Калужская область', name: 'Калужская область'},
                {value: 'Орловская область', name: 'Орловская область'}
            ]
        }
    },
    setup() {
        const formData = ref({
            title: '',
            describe: '',
            regions: []
        })

        const createProductHook = async () => {
            const {func} = createProduct(formData.value);
            func()
            router.push('/profile')
        }
        return {formData, createProductHook}
    }
}
</script>

<template>
        <wave-form @submit.prevent="createProductHook()" class="default-form">
            <template v-slot:header>
                <h1 class="form-header">Создать Товар</h1>
            </template>
            <template v-slot:fields>
                <div class="form-group">
                    <label :for="'title'">Название: </label>
                    <wave-input
                    v-model="formData.title"
                    :id="'title'"
                    class="form-control">
                    </wave-input>
                </div>
                <div class="form-group">
                    <label :for="'describe'">Описание: </label>
                    <textarea
                    v-model="formData.describe"
                    :id="'describe'"
                    class="form-control">
                    </textarea>
                </div>
                <div class="from-group">
                    <label :for="'regions'">Регионы: </label>
                    <wave-select 
                    v-model="formData.regions"
                    :options="regionsOptions"
                    :id="'regions'"
                    class="form-control">
                    </wave-select>
                </div>
            </template>
            <template v-slot:button>
                <wave-button class="form-button"></wave-button>
            </template>
        </wave-form>
</template>

<style scoped>

</style>