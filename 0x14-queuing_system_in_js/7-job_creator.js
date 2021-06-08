const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const push_notification_code_2 = kue.createQueue();
const createAndEnqueueJob = (jobData) => {
  const job = push_notification_code_2.create('push_notification_code_2', jobData).save((e) => !e && console.log(`Notification job created: ${job.id}`));
  job.on('complete', () => console.log(`Notification job ${job.id} completed`));
  job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
  job.on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
};
jobs.forEach(createAndEnqueueJob);
