import { createClient } from 'redis';

async function connectRedis() {
    const client = await createClient()
        .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
    console.log('Redis client connected to the server')
}

connectRedis();
