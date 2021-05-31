const kue = require('kue');
/* JobData coming from the request  */
const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
}
/* Queue creation*/
const push_notification_code = kue.createQueue();

/* Enqueuing a new job  */
const job = push_notification_code.create('push_notification_code', jobData).save((e) => !e && console.log(`Notification job created: ${job.id}`))
job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'))

