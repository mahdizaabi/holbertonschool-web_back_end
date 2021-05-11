import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const Prom1 = signUpUser(firstName, lastName);
  const Prom2 = uploadPhoto(fileName);
  return Promise.allSettled([Prom1, Prom2])
    .then((results) => results).catch((e) => console.log(e));
}
