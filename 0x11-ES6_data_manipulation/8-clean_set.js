export default (set, start) => (start !== '' && [...set]
  .filter((item) => start !== '' && item.includes(start))
  .map((i) => i.slice(start.length)).join('-')) || '';
