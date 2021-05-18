export default (set, start) => (typeof start === 'string' && start.length !== 0 && typeof set === 'object' && [...set]
  .filter((item) => item && item.startsWith(start)).map((i) => i.slice(start.length)).join('-')) || '';
