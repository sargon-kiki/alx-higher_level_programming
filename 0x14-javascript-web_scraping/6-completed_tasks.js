#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const taskCom = {};
    todos.forEach((todo) => {
      if (todo.taskCom && taskCom[todo.userId] === undefined) {
        taskCom[todo.userId] = 1;
      } else if (todo.taskCom) {
        taskCom[todo.userId] += 1;
      }
    });
    console.log(taskCom);
  }
});
