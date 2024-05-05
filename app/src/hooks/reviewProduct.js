import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
import store from "@/store";

export default function reviewProduct(formData) {
    const reviewProductTx = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = store.state.auth.seed;

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();
        console.log(formData);
        
        const tx = TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: publicKey,
            contractVersion: contractVersion,
            params: [
                {
                    key: "product",
                    type: "integer",
                    value: formData.id
                },
                {
                    key: "max_v",
                    type: "integer",
                    value: parseInt(formData.max_v)
                },
                {
                    key: "min_v",
                    type: "integer",
                    value: parseInt(formData.min_v)
                },
                {
                    type: 'string',
                    key: "tx_type",
                    value: "review_product",
                }
            ]
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }

    return {reviewProductTx};
}