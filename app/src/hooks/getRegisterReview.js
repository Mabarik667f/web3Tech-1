import {CONTRACT_ID, sdk} from "@/contractData";
import {ref, onMounted} from "vue";
export default function getRegisterReview() {
    const usersArray = ref([]);
    const makersArray = ref([]);
    const distributorsArray = ref([]);

    const getRequestsCount = async () => {
        let users = await sdk.contracts.getKey(CONTRACT_ID, 'users');
        let makers = await sdk.contracts.getKey(CONTRACT_ID, 'makers');
        let distributors = await sdk.contracts.getKey(CONTRACT_ID, 'distributors');
        users = JSON.parse(users.value);
        makers = JSON.parse(makers.value);
        distributors = JSON.parse(distributors.value);
        // console.log(users);
        return {users, makers, distributors}
    }

    const getRequests = async () => {
        const {users, makers, distributors} = await getRequestsCount();
        for (let i = 1; i <= users; i++) {
            let request = await sdk.contracts.getKey(CONTRACT_ID, `request_user_${i}`);
            let val = JSON.parse(request.value);
            if (!val['status']) {
                let user = await sdk.contracts.getKey(CONTRACT_ID, `request_user_${i}`);
                user = JSON.parse(user.value)
                user['id'] = i;
                usersArray.value.push(user);
            }
        }
        for (let i = 1; i <= makers; i++) {
            let request = await sdk.contracts.getKey(CONTRACT_ID, `request_maker_${i}`);
            let val = JSON.parse(request.value);
            if (!val['status']) {
                let maker = await sdk.contracts.getKey(CONTRACT_ID, `request_maker_${i}`);
                maker = JSON.parse(maker.value);
                maker['id'] = i;
                makersArray.value.push(maker);
            }
        }
        for (let i = 1; i <= distributors; i++) {
            let request = await sdk.contracts.getKey(CONTRACT_ID, `request_distributor_${i}`);
            let val = JSON.parse(request.value);
            if (!val['status']) {
                let distributor = await sdk.contracts.getKey(CONTRACT_ID, `request_distributor_${i}`);
                distributor = JSON.parse(distributor.value);
                distributor['id'] = i;
                distributorsArray.value.push(distributor);
            }
        }

    }

    onMounted(getRequests)
    return {usersArray, makersArray, distributorsArray}
}