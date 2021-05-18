export default (m) => ((m instanceof Map) && (m.forEach((v, k) => ((v === 1)
    && m.set(k, 100)) || ((m instanceof Map) && (m.set(k, v)))))) || (function e() { throw new Error('Cannot process'); }());
