import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const { body } = values[0];
      const { firstName } = values[1];
      const { lastName } = values[1];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup;

/* second working method
export default function handleProfileSignup() {
  uploadPhoto()
    .then((response1) => {
      createUser()
        .then((response2) => console.log(
          response1.body,
          response2.firstName,
          response2.lastName,
        ));
    }).catch(() => console.log('Signup system offline'));
}
*/
