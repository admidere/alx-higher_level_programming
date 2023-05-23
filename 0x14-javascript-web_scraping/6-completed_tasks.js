#!/usr/bin/node

const request = require('request');

function countCompletedTasks (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to fetch task data. Status code: ${response.statusCode}`);
    } else {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach((task) => {
        if (task.completed) {
          const userId = task.userId;
          if (completedTasksByUser[userId]) {
            completedTasksByUser[userId]++;
          } else {
            completedTasksByUser[userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    }
  });
}

// Usage: node script.js <API_URL>
const apiUrl = process.argv[2];
countCompletedTasks(apiUrl);
