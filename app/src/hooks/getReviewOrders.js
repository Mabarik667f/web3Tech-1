import {CONTRACT_ID, sdk} from "@/contractData";
import {ref, onMounted} from "vue";
export default function getReviewOrders() {
    const reviewOrders = ref([]);
    const getOrders = async () => {
        const ordersCount = await sdk.contracts.getKey(CONTRACT_ID, 'orders');
        for (let i = 1; i <= JSON.parse(ordersCount.value); i++) {
            let order = await sdk.contracts.getKey(CONTRACT_ID, `order_${i}`);
            order = JSON.parse(order.value);
            order['id'] = i;
            if (!("total_price" in order)) {
                reviewOrders.value.push(order);
            }
        }
    }

    onMounted(getOrders);
    return {reviewOrders};
}