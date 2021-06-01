
import express from 'express';
const { promisify } = require("util");
import redis from 'redis';


const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];
const getItemById = (itemId) => listProducts.filter(item => item.itemId === JSON.parse(itemId));
const app = express();
const port = 1245;

const client = redis.createClient();
client.get = promisify(client.get).bind(client);
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

reserveStockById(1, 0);

const getCurrentReservedStockById = async (itemId) => await client.get(`item.${itemId}`);
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});
app.get('/list_products/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId)

  !item[0] && res.send({ "status": "Product not found" }) && res.end()
  getCurrentReservedStockById(itemId).then(currentStock => {

    item[0] && res.send(JSON.stringify({ ...item[0], currentQuantity: currentStock }))
  }).catch(e => res.send({ "status": "Product not found" }))

});
app.get('/reserve_product/:itemId', (req,res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId)
  !item[0] && res.send({ "status": "Product not found" }) && res.end();
  item[0] && getCurrentReservedStockById(itemId).then(currentStock => {
    (currentStock >= 1) && res.send(JSON.stringify({ "status": "Reservation confirmed", "itemId": itemId }))
    !(currentStock >= 1) && res.send(JSON.stringify({ "status": "Not enough stock available", "itemId": itemId }))
  }).catch(e => res.send({ "status": "Product not found" }))
})
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
