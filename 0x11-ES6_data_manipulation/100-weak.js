export const weakMap = new WeakMap();
export const queryAPI = (obj) => {
  let nbFetch = weakMap.get(obj) || 0;
  nbFetch += 1;
  if (weakMap.get(obj) >= 5) {
    throw Error('Endpoint load is high');
  }
  weakMap.set(obj, nbFetch);
  return nbFetch;
};
