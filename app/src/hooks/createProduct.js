import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
import store from "@/store";
export default function createProduct(formData) {
    const func = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = store.state.auth.seed;

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();

        const value = JSON.stringify({
            title: formData.title,
            describe: formData.describe,
            regions: formData.regions
        });

        const tx = TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: publicKey,
            contractVersion: contractVersion,
            params: [
                {
                    key: "product",
                    type: "string",
                    value: value
                },
                {
                    type: 'string',
                    key: "tx_type",
                    value: "create_product",
                }
            ]
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }

    return {func}
}