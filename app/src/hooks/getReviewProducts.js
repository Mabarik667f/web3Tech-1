import {CONTRACT_ID, sdk} from "@/contractData";
import {ref, onMounted} from "vue";
export default function getReviewProducts() {
    const reviewProducts = ref([]);
    const getProducts = async () => {
        const productsCount = await sdk.contracts.getKey(CONTRACT_ID, 'products');
        for (let i = 1; i <= JSON.parse(productsCount.value); i++) {
            let product = await sdk.contracts.getKey(CONTRACT_ID, `product_${i}`);
            product = JSON.parse(product.value);
            product['id'] = i;
            if (!("min_v" in product)) {
                reviewProducts.value.push(product);
            }
        }
    }

    onMounted(getProducts);
    return {reviewProducts};


}