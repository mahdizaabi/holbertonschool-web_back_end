const calculateNumber = (type, a, b) => type === "SUM" ? Math.round(a) + Math.round(b) : type === "SUBTRACT" ? Math.round(a) - Math.round(b) : type === "DIVIDE" && Math.round(b) !== 0 ? Math.round(a) / Math.round(b) : "Error"


module.exports = calculateNumber;