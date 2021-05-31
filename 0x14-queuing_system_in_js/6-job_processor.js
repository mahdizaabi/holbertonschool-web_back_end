const kue = require('kue')
const Queue = kue.createQueue();

Queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message)
    done();
})
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
