const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'log-aggregator-app',
  brokers: ['kafka1:9092']
});


const consumer = kafka.consumer({
  groupId: 'log-aggregator-group',
  allowAutoOffsetReset: true,
  autoOffsetReset: 'earliest'
});

async function consumeLogMessages() {
  await consumer.connect();
  await consumer.subscribe({
    topic: 'logs',
    fromBeginning: true
  });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      const logMessage = JSON.parse(message.value.toString());
      console.log(`Received log message: ${JSON.stringify(logMessage)}`);

      // send log message to log aggregation service
      // e.g. using http request or websocket
    }
  });
}

consumeLogMessages()
    .then(() => {
        console.log('Consuming log messages');
    })    
    .catch((error) => {
        console.error('Error consuming log messages', error);
    });