import redis from 'redis';
import express from 'express';

const { promisify } = require('util');
const kue = require('kue');

const client = redis.createClient();

const reserveSeat = (number) => client.set('avaialable_seats', number);
// eslint-disable-next-line no-return-await
const getCurrentAvailableSeats = async () => await client.get('avaialable_seats');

/* REDIS */
client.get = promisify(client.get).bind(client);
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/* set initial availbale seats   */
reserveSeat(3);
let reservationEnabled = true;

const app = express();
const port = 1245;

app.get('/available_seats', (req, res) => {
  // eslint-disable-next-line max-len
  getCurrentAvailableSeats().then((availabeSeat) => res.send(JSON.stringify({ numberOfAvailableSeats: availabeSeat })));
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }

  /* QUEUE */
  /* Create a Queue */
  const reserve_seat = kue.createQueue();
  /* enqueue a new Job in the queue reserve seat */
  const job = reserve_seat.create('reserve_seat').save((e) => !e && res.send({ status: 'Reservation in process' }) || res.send({ status: 'Reservation failed' }));
  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`));
  job.on('failed', (error) => console.log(`Seat reservation job ${job.id} failed: ${error}`));
});

app.get('/process', (req, res) => {
  const Queue = kue.createQueue();
  Queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (JSON.parse(currentAvailableSeats) <= 0) {
      done(new Error('Not enough seats available'));
      res.end();
      return;
    }
    if (JSON.parse(currentAvailableSeats) === 1) {
      reservationEnabled = false;
    }
    reserveSeat(currentAvailableSeats - 1);
    done();
  });
  res.send({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
