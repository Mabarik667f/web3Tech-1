const {We} = require('@wavesenterprise/sdk');
const {TRANSACTIONS} = require('@wavesenterprise/transactions-factory');
const {Keypair} = require("@wavesenterprise/signer");


const NODE_URL = 'http://localhost:6862';
const sdk = new We(NODE_URL)

const contractVersion = 5;

const CONTRACT_ID = 'HEUoh8rjazbGDZGMgAveJrcVhsMmaidF3Toj2cSgmPZ1'

export {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion}
