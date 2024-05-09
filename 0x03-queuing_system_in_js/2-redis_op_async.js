import { createClient } from 'redis';
const util = require('util');
const redis = require('redis');

function connectRedis() {
    const client = createClient()
        .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
    console.log('Redis client connected to the server');
    return client;
}

const client = connectRedis();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const get = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    await get(schoolName)
    .then(data => {
        console.log(data)
    })
    .catch(err => {
        console.log(err)
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');