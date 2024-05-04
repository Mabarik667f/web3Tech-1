import {TRANSACTIONS, Keypair, CONTRACT_ID, sdk, contractVersion} from "@/contractData";
export const authModule = {
    state: () => ({
        isAuth: false,
        role: '',
        seed: '',
        status: false,
        email: ''
    }),

    getters: {
        isAuth: state => state.isAuth,
        role: state => state.role,
        seed: state => state.seed,
        status: state => state.status,
        email: state => state.email
    },

    mutations: {
        setAuth(state, {isAuth, role, seed, status, email}) {
            state.isAuth = isAuth;
            state.role = role;
            state.seed = seed;
            state.status = status;
            state.email = email;
        }
    },

    actions: {
        async getStorage({commit}) {
            commit('setAuth', {isAuth: localStorage.getItem('isAuth') === 'true',
                               role: localStorage.getItem('role'),
                               seed: localStorage.getItem('seed'),
                               status: localStorage.getItem('status') === 'true',
                               email: localStorage.getItem('email')});
        },
        async setStorage({dispatch}, { isAuth, role, seed, status, email }) {
            localStorage.setItem('isAuth', isAuth);
            localStorage.setItem('role', role);
            localStorage.setItem('seed', seed);
            localStorage.setItem('status', status);
            localStorage.setItem('email', email);

            await dispatch('getStore');

        },
        async login({dispatch, commit}, formData) {
            try {
                const user = await sdk.contracts.getKey(CONTRACT_ID, formData.email);
                let data = JSON.parse(user);
                if (data.password === formData.password) {
                    commit('setAuth', {isAuth: true, role: data.role, seed: data.seed, status: data.status, email: formData.email});
                    dispatch('setStorage', {isAuth: true, role: data.role, seed: data.seed, status: data.status, email: formData.email});
                } else {
                    console.log('Пароль не верен!');
                }
            } catch (error) {
                console.log(error);
            }
        },
        async logout({dispatch, commit}) {
            dispatch('setStorage', {isAuth: false,  role: '', seed: '', status: false, email: ''});
            commit('setAuth', {isAuth: false, role: '', seed: '', status: false, email: ''});
        },
        async operatorRegistry({dispatch, commit}, formData) {
            const config = await sdk.node.config();

            const fee = config.minimumFee[104];

            const keypair = await Keypair.generate(16);

            const publicKey = await keypair.publicKey();
            const seed = keypair.phrase();

            const value = JSON.stringify({
                first_name: formData.firstName,
                second_name: formData.secondName,
                last_name: formData.lastName,
                email: formData.email,
                role: 'operator',
                seed: seed,
                public_key: publicKey,
                password: formData.password
            });
            
            const tx = TRANSACTIONS.CallContract.V2({
                contractId: CONTRACT_ID,
                fee: fee,
                contractVersion: contractVersion,
                senderPublicKey: publicKey,
                params: [
                    {
                        type: "string",
                        key: "user",
                        value: value
                        
                    },
                    {
                        key: 'tx_type',
                        value: "operator_registry",
                        type: 'string'
                    }
                ]
            });

            const signedTx = await sdk.signer.getSignedTx(tx, seed);

            const res = await sdk.broadcast(signedTx);

            console.log(res);

            await dispatch('setStorage', {isAuth: true,  role: 'operator', seed: seed, status: false, email: formData.email});

        },
        async clientRegistry({dispatch}, formData) {
            const config = await sdk.node.config();

            const fee = config.minimumFee[104];

            const keypair = await Keypair.generate(16);

            const publicKey = await keypair.publicKey();
            const seed = keypair.phrase();

            const value = JSON.stringify({
                first_name: formData.firstName,
                second_name: formData.secondName,
                last_name: formData.lastName,
                email: formData.email,
                role: 'user',
                seed: seed,
                public_key: publicKey,
                password: formData.password
            });

            const tx = TRANSACTIONS.CallContract.V2({
                contractId: CONTRACT_ID,
                fee: fee,
                contractVersion: contractVersion,
                senderPublicKey: publicKey,
                params: [
                    {
                        type: "string",
                        key: "user",
                        value: value
                    },
                    {
                        key: 'tx_type',
                        value: "client_registry",
                        type: 'string'
                    }
                ]
            });
            const signedTx = await sdk.signer.getSignedTx(tx, seed);

            const res = await sdk.broadcast(signedTx);

            console.log(res);

            await dispatch('setStorage', {isAuth: true,  role: 'client', seed: seed, status: false, email: formData.email});

        },

        async makerRegistry({dispatch}, formData) {
            const config = await sdk.node.config();

            const fee = config.minimumFee[104];

            const keypair = await Keypair.generate(16);

            const publicKey = await keypair.publicKey();
            const seed = keypair.phrase();

            const value = JSON.stringify({
                title: formData.title,
                describe: formData.describe,
                regions: formData.regions,
                first_name: formData.firstName,
                second_name: formData.secondName,
                last_name: formData.lastName,
                email: formData.email,
                status: false,
                role: 'maker',
                seed: seed,
                public_key: publicKey,
                password: formData.password})

            const tx = TRANSACTIONS.CallContract.V2({
                contractId: CONTRACT_ID,
                fee: fee,
                contractVersion: contractVersion,
                senderPublicKey: publicKey,
                params: [
                    {
                        type: "string",
                        key: "user",
                        value: value
                    },
                    {
                        key: 'tx_type',
                        value: "maker_registry",
                        type: 'string'
                    }
                ]
            });

            const signedTx = await sdk.signer.getSignedTx(tx, seed);

            const res = await sdk.broadcast(signedTx);

            console.log(res);

            await dispatch('setStorage', {isAuth: true,  role: 'maker', seed: seed, status: false, email: formData.email});
        },

        async distributorRegistry({dispatch}, formData) {
            const config = await sdk.node.config();

            const fee = config.minimumFee[104];

            const keypair = await Keypair.generate(16);

            const publicKey = await keypair.publicKey();
            const seed = keypair.phrase();

            const value = JSON.stringify({
                title: formData.title,
                regions: formData.regions,
                first_name: formData.firstName,
                second_name: formData.secondName,
                last_name: formData.lastName,
                email: formData.email,
                status: false,
                role: 'distributor',
                seed: seed,
                public_key: publicKey,
                password: formData.password})

            const tx = TRANSACTIONS.CallContract.V2({
                contractId: CONTRACT_ID,
                fee: fee,
                contractVersion: contractVersion,
                senderPublicKey: publicKey,
                params: [
                    {
                        type: "string",
                        key: "user",
                        value: value
                    },
                    {
                        key: 'tx_type',
                        value: "distributor_registry",
                        type: 'string'
                    }
                ]
            });

            const signedTx = await sdk.signer.getSignedTx(tx, seed);

            const res = await sdk.broadcast(signedTx);

            console.log(res);

            await dispatch('setStorage', {isAuth: true,  role: 'distributor', seed: seed, status: false, email: formData.email});
        },

        async reviewRegister(formData) {
            const config = await sdk.node.config();

            const fee = config.minimumFee[104];

            const keypair = await Keypair.generate(16);

            const publicKey = await keypair.publicKey();
            const seed = keypair.phrase();

            const tx = TRANSACTIONS.CallContract.V2({
                contractId: CONTRACT_ID,
                fee: fee,
                contractVersion: contractVersion,
                senderPublicKey: publicKey,
                params: [
                    {
                        type: "string",
                        key: `${formData.key}`,
                        value: `${formData.value}`
                    },
                    {
                        key: 'tx_type',
                        value: "review_register",
                        type: 'string'
                    }
                ]
            });

            const signedTx = await sdk.signer.getSignedTx(tx, seed);

            const res = await sdk.broadcast(signedTx);

            console.log(res);
        }
    }
}