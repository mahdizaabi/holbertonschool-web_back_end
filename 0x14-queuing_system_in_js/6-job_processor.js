const kue = require('kue');

/* crate a queue to get acess to Redis */
const Queue = kue.createQueue();
/*  */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

Queue.process('push_notification_code', (job, done) => {
  if (!job) return done(new Error('invalid'));
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
  return 0;
});
