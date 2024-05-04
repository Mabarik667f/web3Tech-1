import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
export default function createProduct(formData) {
    const func = async () => {
        const config = await sdk.node.config();

        const fee = await config.minimumFee[104];
        const SEED = '';

        const keypair = await Keypair.fromExistingSeedPhrase(SEED);
        const publicKey = await keypair.publicKey();

        const tx = await TRANSACTIONS.CallContract.V2({
            contractId: CONTRACT_ID,
            fee: fee,
            senderPublicKey: public_key,
            contractVersion: contractVersion,
            params: [
                {
                    key: "product",
                    type: "string",
                    value: `{\"\"}`
                },
                {
                    key: "tx_type",
                    value: "create_product",
                    type: "string"
                }
            ]
        });

        const signedTx = await sdk.signer.getSignedTx(tx, SEED);
        const res = await sdk.broadcast(signedTx);
        console.log(res);
    }
}