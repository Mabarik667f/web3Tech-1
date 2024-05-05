import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
import store from "@/store";
export default function reviewOrder(formData) {
    const reviewOrderTx = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = store.state.auth.seed;

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();

        const params = [{
                key: "order_id",
                type: "integer",
                value: formData.id
            },
            {
                type: 'integer',
                key: "total_price",
                value: parseInt(formData.totalPrice),
            },
            {
                type: 'string',
                key: "tx_type",
                value: "review_order"
            }]

        if (formData.newDate) {
            params.push({
                type: 'string',
                key: "new_date",
                value: formData.newDate
            })
        }

        if (formData.paymentTerm) {
            params.push({
                type: 'string',
                key: "payment_term",
                value: formData.paymentTerm
            })
        }

        if (formData.pre_payment) {
            params.push({
                type: 'bool',
                key: 'pre_payment',
                value: formData.prePayment
            })
        }
        const tx = TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: publicKey,
            contractVersion: contractVersion,
            params: params
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }

    return {reviewOrderTx}
}