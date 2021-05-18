export default (m) => m.forEach((v, k) => ((v === 1) && m.set(k, 100)) || m.set(k, v));
