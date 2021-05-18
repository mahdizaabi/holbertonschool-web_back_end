export default (arr, city) => (Array.isArray(arr) && arr.filter((item) => item.location === city)) || [];
