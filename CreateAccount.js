const StellarSdk = require('stellar-sdk');

const server = new StellarSdk.Server('http://127.0.0.1:8000', {allowHttp: true});

const passpharase = 'Standalone Network ; Februry 2017'

const MasterKey = StellarSdk.Keypair.master(passpharase)
const MasterSecret = MasterKey.secret();
const MasterPublicKey = MasterKey.publicKey();

console.log('Master account', MasterSecret, MasterPublicKey);


const pair1 = StellarSdk.Keypair.random(passpharase);
const pair2 = StellarSdk.Keypair.random(passpharase);
const pair3 = StellarSdk.Keypair.random(passpharase);

var SecreteKey1  = pair1.secret();
var PublicKey1  = pair1.publicKey();
console.log('Account1', SecreteKey1, PublicKey1);

var SecreteKey2  = pair2.secret();
var PublicKey2  = pair2.publicKey();
console.log('Account2', SecreteKey2, PublicKey2);

var SecreteKey3  = pair3.secret();
var PublicKey3  = pair3.publicKey();
console.log('Account3', SecreteKey3, PublicKey3);

(async function main() {

    const account = await server.loadAccount(MasterPublicKey);
    const fee = await server.fetchBaseFee();
})