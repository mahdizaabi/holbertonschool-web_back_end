const createPushNotificationsJobs = require('./8-job');
const kue = require('kue')
const expect = require('chai').expect;
const queue = kue.createQueue();

afterEach(function () {
    queue.testMode.clear();
});

after(function () {
    queue.testMode.exit()
});

it('Creates and enqueue jobs with valid data', function () {
    createPushNotificationsJobs([{ num: '14141414', message: '14_14_14_14' }], queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({ num: '14141414', message: '14_14_14_14' });
});

it('throw an Error for invalid Data', () => {
    expect(() => {
        createPushNotificationsJobs('14_14', queue);
    }).to.throw('Jobs is not an array');
});