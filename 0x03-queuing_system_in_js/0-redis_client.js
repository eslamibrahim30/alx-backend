import { createClient } from 'redis';

function connectRedis() {
    const client = createClient()
        .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
    console.log('Redis client connected to the server');
}

connectRedis();
