export default (m) => m.forEach((v, k) => ((m instanceof Map) && (v === 1)
&& m.set(k, 100)) || ((m instanceof Map) && (m.set(k, v)))) || 'Cannot process';
