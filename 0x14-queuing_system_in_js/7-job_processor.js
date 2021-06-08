const kue = require('kue');

const Queue = kue.createQueue();
const blackList = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  blackList.includes(phoneNumber) && (() => { done(Error(`Phone number ${phoneNumber} is blacklisted`)); })();
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

Queue.process('push_notification_code_2', (job, done) => {
  if (!job) return done(new Error('invalid'));
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done();
});
