// skills/slack.js
// Simple skill to post messages to a Slack channel using an incoming webhook.

const axios = require('axios');

/**
 * Send a message to Slack via incoming webhook.
 * @param {string} text The message text to send.
 * @returns {Promise<void>} A promise that resolves when the message is sent.
 */
async function sendSlackMessage(text) {
  const webhookUrl = process.env.SLACK_WEBHOOK_URL;
  if (!webhookUrl) {
    throw new Error('Slack webhook URL is not set. Please configure SLACK_WEBHOOK_URL in your .env file.');
  }

  const payload = { text };
  await axios.post(webhookUrl, payload);
}

module.exports = {
  sendSlackMessage,
};
