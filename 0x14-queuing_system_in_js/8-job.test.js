const kue = require('kue');
const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job');

const queue = kue.createQueue();

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

test('creates and enqueue jobs with valid data', () => {
  createPushNotificationsJobs([{ num: '14141414', message: '14_14_14_14' }], queue);
  expect(queue.testMode.jobs.length).to.equal(1);
  expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  expect(queue.testMode.jobs[0].data).to.eql({ num: '14141414', message: '14_14_14_14' });
});

test('throw an Error for invalid Data', () => {
  expect(() => {
    createPushNotificationsJobs('14_14', queue);
  }).to.throw('Jobs is not an array');
});
