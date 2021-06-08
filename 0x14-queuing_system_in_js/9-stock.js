import express from 'express';

import redis from 'redis';
import { listProducts } from './listProducts';

const { promisify } = require('util');

const getItemById = (itemId) => listProducts.filter((item) => item.itemId === JSON.parse(itemId));
const getInitialQuantity = (itemId) => listProducts.filter((item) => item.itemId === JSON.parse(itemId))[0].initialAvailableQuantity;
const reserveStockById = (itemId, stock) => client.set(`item.${itemId}`, stock);
const getCurrentReservedStockById = async (itemId) => await client.get(`item.${itemId}`);

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

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  !item[0] && res.send({ status: 'Product not found' }) && res.end();
  getCurrentReservedStockById(itemId).then((currentStock) => {
    item[0] && res.send(JSON.stringify({ ...item[0], currentQuantity: currentStock }));
  }).catch((e) => res.send({ status: 'Product not found' }));
});
app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  !item[0] && res.send({ status: 'Product not found' }) && res.end();
  item[0] && getCurrentReservedStockById(itemId).then((currentStock) => {
    if (currentStock === null && currentStock !== 0 || currentStock > 0) {
      if (currentStock > 0) reserveStockById(itemId, currentStock - 1);
      else reserveStockById(itemId, getInitialQuantity(itemId) - 1);
      res.send(JSON.stringify({ status: 'Reservation confirmed', itemId }));
    } else {
      res.send(JSON.stringify({ status: 'Not enough stock available', itemId }));
    }
  }).catch((e) => res.send({ status: 'Product not found' }));
});
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
