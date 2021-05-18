const x = (arr, city) => (Array.isArray(arr) && arr.filter((item) => item.location === city)) || [];
export default x;
