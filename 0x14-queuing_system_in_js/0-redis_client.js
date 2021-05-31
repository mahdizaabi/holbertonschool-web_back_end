import redis from 'redis';

const client = redis.createClient();
client.on('connect', (error) => {
  console.error('Redis client connected to the server');
});
client.on('error', (error) => {
  console.error('Redis client not connected to the server: ERROR_MESSAGE');
});

console.log('ok');
