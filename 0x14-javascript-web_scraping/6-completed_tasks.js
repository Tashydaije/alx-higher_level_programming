#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const completedTasksByUsers = {};
  const tasks = JSON.parse(body);

  tasks.forEach(task => {
    const userId = task.userId;
    const completed = task.completed;

    if (completed && !completedTasksByUsers[userId]) {
      completedTasksByUsers[userId] = 0;
    }
    if (completed) {
      ++completedTasksByUsers[userId];
    }
  });
  console.log(completedTasksByUsers);
});
