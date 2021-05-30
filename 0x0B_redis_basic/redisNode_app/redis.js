const redis = require('redis');
const { promisify } = require("util");






class redisClient {
    
    constructor() {
        this.client = redis.createClient();
        this.client.on("error", function (error) {
            console.error(error);
        });
        this.client.on('connect', function () {
            console.log('Redis Server Connected...');
        });
    }

    addedItemsToMap(key, items) {
        this.client.hmset(key, items);

    }

    getItemFromHash(key, field) {
        const getAsync = promisify(this.client.hget).bind(this.client);
        const result = getAsync(key, field);
        return result;
    }

    getAllItemsFromHash(key) {
        const getAsync = promisify(this.client.hgetall).bind(this.client);
        return getAsync(key, field);
    }
    addItemToList(listName, item) {
        this.client.rpush(listName, item);
    }
    getList(listName) {
        const getAsync = promisify(this.client.lrange).bind(this.client);
        const result = getAsync(listName, 0, -1);
        return result
    }
    removeItemFromList(listName, count, item){
        const getAsync = promisify(this.client.lrem).bind(this.client);
        const result = getAsync(listName, count, item);
        return result;

    }
}

module.exports = redisClient;