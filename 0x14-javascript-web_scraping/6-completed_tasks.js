#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const counts = todos.reduce((acc, todo) => {
      if (todo.completed) {
        acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(JSON.stringify(counts));
  }
});
