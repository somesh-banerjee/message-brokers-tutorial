const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'log-aggregator-app',
  brokers: ['kafka1:9092']
});

const producer = kafka.producer();

async function sendLogMessage(message) {
  await producer.connect();
  await producer.send({
    topic: 'logs',
    messages: [
      { value: JSON.stringify(message) }
    ]
  });
  await producer.disconnect();
}

setInterval(() => {
    sendLogMessage({
        message: 'This is a log message',
        timestamp: new Date().toISOString(),
        service: process.env.SERVICE_NAME
    });
}, 4000);

producer.connect().then(() => {
    console.log('Connected to Kafka');
}).catch((error) => {
    console.error('Error connecting to Kafka', error);
});