import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
import store from "@/store";
export default function createOrder(formData) {
    const func = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = store.state.auth.seed;

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();

        let value = {};

        for (let key in formData) {
            const val = formData[key];
            if (val !== '' && val !== undefined && val !== null) {
                value[key] = val;
            }
        }
        
        value = JSON.stringify(value);
        const tx = TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: publicKey,
            contractVersion: contractVersion,
            params: [
                {
                    key: "order",
                    type: "string",
                    value: value
                },
                {
                    type: 'string',
                    key: "tx_type",
                    value: "create_order",
                }
            ]
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }

    return {func}
}