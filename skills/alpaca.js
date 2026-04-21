// skills/alpaca.js
// Example JavaScript skill to interact with the Alpaca brokerage API.

const Alpaca = require('alpaca-trade-api');

/**
 * Create an Alpaca client using API credentials from environment variables.
 * @returns {object} An Alpaca client instance.
 */
function getClient() {
  const keyId = process.env.ALPACA_KEY_ID;
  const secretKey = process.env.ALPACA_SECRET_KEY;
  const paper = process.env.PAPER_TRADING === 'true';
  return new Alpaca({ keyId, secretKey, paper });
}

/**
 * Fetch the account details.
 * @returns {Promise<object>} Account information.
 */
async function getAccount() {
  const alpaca = getClient();
  const account = await alpaca.getAccount();
  return account;
}

/**
 * Place a market order for a given symbol and quantity.
 * Prompts for confirmation if PAPER_TRADING is false.
 * @param {string} symbol The ticker symbol to trade (e.g., 'AAPL').
 * @param {number} qty The number of shares to buy or sell (use negative qty to sell).
 * @returns {Promise<object>} Order confirmation.
 */
async function placeOrder(symbol, qty) {
  const alpaca = getClient();
  const isPaper = process.env.PAPER_TRADING === 'true';

  if (!isPaper) {
    throw new Error('Live trading is not allowed in this skill. Use bot logic to confirm before placing live orders.');
  }

  const order = await alpaca.createOrder({
    symbol: symbol,
    qty: Math.abs(qty),
    side: qty > 0 ? 'buy' : 'sell',
    type: 'market',
    time_in_force: 'gtc',
  });

  return order;
}

module.exports = {
  getAccount,
  placeOrder,
};
