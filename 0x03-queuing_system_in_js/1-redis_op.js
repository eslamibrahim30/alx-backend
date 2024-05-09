import { createClient } from 'redis';
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

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, data) => {
        if (err) {
            console.error(err);
        } else {
            console.log(data);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');