const x = (length, position, value) => {
  /*eslint-disable */
  (position > length - 1) && ((function n() { throw Error('Position outside range'); }()));
  const buffer = new Array(length);
  const view = new DataView(buffer, 0);
  view.setInt8(position, value);
  return view;
};

export default x;
