const {We} = require('@wavesenterprise/sdk');
const {TRANSACTIONS} = require('@wavesenterprise/transactions-factory');
const {Keypair} = require("@wavesenterprise/signer");


// const SEED = 'copper venture beauty snake wear million champion enact humor visa prepare garment party rapid annual'
const NODE_URL = 'http://localhost:6862';
// const NODE_URL = '';
const sdk = new We(NODE_URL)

const contractVersion = 15;

// const call = process.argv[2];

const CONTRACT_ID = 'DsDga12xYn8WJjtEHqTN5ZRsMMsuBmwBX3B2Drzz7r8A'

// console.log("Call ", {call})

// async function addLiquidity() {
//     const config = await sdk.node.config()
//     const fee = config.minimumFee[103]

//     const keypair = await Keypair.fromExistingSeedPhrase(SEED);

//     const tx = TRANSACTIONS.CallContract.V5({
//         contractId: CONTRACT_ID,
//         params: [
//             {
//                 key: 'action',
//                 value: 'addLiquidity',
//                 type: 'string'
//             },
//         ],
//         senderPublicKey: await keypair.publicKey(),
//         fee: fee,
//         contractVersion: 2,
//         payments: [
//             {
//                 amount: 100000000
//             },
//             {
//                 assetId: "AmL1n9b8NJtPcMALhN2CScDadLMBg48kEwux6Jg9Ar7J",
//                 amount: 100000
//             }
//         ]
//     })

//     const signedTx = await sdk.signer.getSignedTx(tx, SEED);

//     const res = await sdk.broadcast(signedTx);

//     console.log(res)
// }

// async function swap() {
//     const config = await sdk.node.config()
//     const fee = config.minimumFee[104]

//     // const keypair = await Keypair.generate(16);
//     const keypair = await Keypair.fromExistingSeedPhrase(SEED);

//     const tx = TRANSACTIONS.CallContract.V2({
//         contractId: CONTRACT_ID,
//         params: [
//             {
//                 type: "string",
//                 key: "user",
//                 value: "{\"name\": \"boba\", \"last_name\": \"biba\", \"status\": \"false\", \"public_key\": \"3NjgyxwApvzyWDznH9f3cUAFmEXHT5z3E9D\"}"
//             },
//             {
//                 key: 'tx_type',
//                 value: "client_registry",
//                 type: 'string'
//             }
//         ],
//         senderPublicKey: await keypair.publicKey(),
//         fee: fee,
//         contractVersion: 13,
        
//     })

//     const signedTx = await sdk.signer.getSignedTx(tx, SEED);

//     const res = await sdk.broadcast(signedTx);

//     console.log(res)
// }

export {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion}
