const x = (arr) => (Array.isArray(arr) && arr.reduce((a, i) => (a + i.id), 0)) || [];
export default x;
