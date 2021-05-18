export default (map) => {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }
  map.forEach((v, k) => (v === 1 ? map.set(k, 100) : map.set(k, v)));
  return map;
};
