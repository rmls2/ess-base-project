<template>
    <div class="add-task">
        <button @click="addTask">Test Api Get</button>
    </div>

    <div class="add-task">
        <button @click="addTask2">Test Api Post</button>
    </div>

    <div class="add-task">
        <button @click="addTask3">Test Api Put</button>
    </div>

    <div class="add-task">
        <button @click="addTask4">Test Api Delete</button>
    </div>

    <div class="test-retorno"> {{ responseData }} </div>
    <div class="test-retorno"> {{ responseDataPost }} </div>
    <div class="test-retorno"> {{ responseDataPut }} </div>
    <div class="test-retorno"> {{ responseDataDelete }} </div>
    

</template>

<script lang="ts">
import { useApiService, PromotionModel, PromotionUpdateModel } from '../services/apiService';
import { ref } from 'vue';

export default {

    setup() {
        const { getPromotion, createPromotion, updatePromotion, deletePromotion } = useApiService();
        const responseData = ref<string>('');
        const responseDataPost = ref<string>('');
        const responseDataPut = ref<string>('');
        const responseDataDelete = ref<string>('');

        const addTask = async () => {
            const data = await getPromotion();
            responseData.value = data.data.newValue;
        }

        const addTask2 = async () => {
            const promotionData: PromotionModel = {
                user: "Pedro",
                adm_key: "879456",
                hotel: "noite estrelada",
                room_id: "womrjatajDEa1X0as0W7lVVa",
                reservationValue: 157,
                discountValue: 20
            };
            const data = await createPromotion(promotionData);
            responseDataPost.value = data.data.discountValue;
        }

        const addTask3 = async () => {
            const promotionDataUp: PromotionUpdateModel = {
                user: "Pedro",
                adm_key: "879456",
                room_id: "womrjatajDEa1X0as0W7lVVa",
                currentDiscountValue: 20,
                newDiscountValue: 25
            }
            const data = await updatePromotion(promotionDataUp);
            responseDataPut.value = data.data.newValue;
        }

        const addTask4 = async () => {
            const data = await deletePromotion();
            responseDataDelete.value = data.data.count;
        }

        return {
            responseData,
            responseDataPost,
            responseDataPut,
            responseDataDelete,
            addTask,
            addTask2,
            addTask3,
            addTask4
        };

    }

}
</script>

<style>
.add-task {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.test-retorno {
    color: #54ca7b;
}

button {
    padding: 12px 24px;
    font-size: 18px;
    border: none;
    border-radius: 6px;
    background-color: #54ca7b;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
</style>