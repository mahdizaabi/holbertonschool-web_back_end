export default function uploadPhoto(filename) {
  const file = filename;
  return new Promise((resolve, reject) => {
    reject(new Error(`${file} cannot be processed`));
  });
}
