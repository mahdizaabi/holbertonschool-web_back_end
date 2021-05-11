export default function getFullResponseFromAPI(success) {
  if (success) return new Promise((resolve) => resolve({ status: 200, body: 'Success' }));
  return new Promise((resolve, reject) => reject('The fake API is not working currently'));
}
