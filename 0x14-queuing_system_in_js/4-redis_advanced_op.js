const { promisify } = require('util');
import redis from 'redis';
const client = redis.createClient();
client.on("connect", function (error) {
    console.error('Redis client connected to the server');
});
client.on("error", function (error) {
    console.error(`Redis client not connected to the server: ${error}`);
});

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);
client.hgetall('HolbertonSchools', (e, v) => console.log(v));
