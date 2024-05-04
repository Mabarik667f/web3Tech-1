<script>
import { ref } from 'vue';
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

        return {formData}
    }
}
</script>

<template>
        <wave-form>
            <template v-slot:header>
                <h1>Создать Товар</h1>
            </template>
            <template v-slot:fields>
                <div>
                    <label>Название: </label>
                    <wave-input
                    v-model="formData.title">
                    </wave-input>
                </div>
                <div>
                    <label>Описание: </label>
                    <textarea
                    v-model="formData.describe">
                    </textarea>
                </div>
                <div>
                    <label>Регионы: </label>
                    <wave-select 
                    v-model="formData.regions"
                    :options="regionsOptions">
                    </wave-select>
                </div>
            </template>
            <template v-slot:button>
                
            </template>
        </wave-form>
</template>

<style scoped>

</style>