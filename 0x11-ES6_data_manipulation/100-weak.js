export const weakMap = new WeakMap();
export const queryAPI = (obj) => {
  if (!obj.protocol || !obj.name) {
    return;
  }
  weakMap.set(obj, (weakMap.get(obj) && (weakMap.get(obj)) + 1) || 0);
  if (weakMap.get(obj) >= 5) {
    throw Error('Endpoint load is high');
  }
};
