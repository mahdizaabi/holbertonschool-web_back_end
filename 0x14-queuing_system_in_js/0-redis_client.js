import redis from 'redis';


const client = redis.createClient();
client.on("Connect", function (error) {
    console.error('Redis client connected to the server');
});
client.on("error", function (error) {
    console.error('Redis client not connected to the server: ERROR_MESSAGE');
});

