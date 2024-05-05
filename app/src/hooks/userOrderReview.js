import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
import store from "@/store";

export default function userOrderReview(order_id, accept) {
    const userOrderReviewTx = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = store.state.auth.seed;

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();
        const tx = TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: publicKey,
            contractVersion: contractVersion,
            params: [
                
                {
                    type: 'string',
                    key: "tx_type",
                    value: "user_order_review",
                },
                {
                    type: "boolean",
                    key: "accept",
                    value: accept,
                },
                {
                    type: "integer",
                    key: "order_id",
                    value: order_id
                }
            ]
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }

    return {userOrderReviewTx}
}