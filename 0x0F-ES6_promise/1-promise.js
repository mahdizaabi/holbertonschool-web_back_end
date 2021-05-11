export default function getFullResponseFromAPI(success) {
  if (success) return new Promise((resolve) => resolve({ status: 200, body: 'success' }));
  return new Promise((reject) => reject('The fake API is not working currently'));
}
