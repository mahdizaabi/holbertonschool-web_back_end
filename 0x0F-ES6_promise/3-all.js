import { uploadPhoto, createUser } from './utils';

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
