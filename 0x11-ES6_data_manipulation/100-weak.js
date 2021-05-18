export const weakMap = new WeakMap();
export const queryAPI = (obj) => {
  if (!obj.protocol || !obj.name) {
    return;
  }
  let nbFetch = weakMap.get(obj) || 0;
  nbFetch += 1;
  weakMap.set(obj, nbFetch);
  if (weakMap.get(obj) >= 5) {
    throw Error('Endpoint load is high');
  }
};
