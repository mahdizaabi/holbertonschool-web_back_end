import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  let rejectedProm = {};
  const Prom1 = await signUpUser(firstName, lastName);
  const resolvedProm = { status: 'fulfilled', value: { ...Prom1 } };
  try {
    /*eslint-disable */
    let Prom2 = await uploadPhoto(fileName);
  } catch (e) {
    rejectedProm = { status: 'rejected', value: e.toString() };
  }
  return new Promise((resolve=>resolve([resolvedProm, rejectedProm])));
}
