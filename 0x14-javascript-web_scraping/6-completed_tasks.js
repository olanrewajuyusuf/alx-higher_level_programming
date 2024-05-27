#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
	  } else {
	    completed[todo.userId]++;
	  }
	}
      });

      const res = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;
      console.log(Object.keys(completed).length > 2 ? res : completed);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
