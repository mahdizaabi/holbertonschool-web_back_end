import redis from 'redis';

const { promisify } = require('util');

const client = redis.createClient();
client.on('connect', (error) => {
  console.error('Redis client connected to the server');
});
client.on('error', (error) => {
  console.error('Redis client not connected to the server: ERROR_MESSAGE');
});
client.get = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print);
const displaySchoolValue = async (schoolName) => console.log(`${await client.get(schoolName)}`);
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
