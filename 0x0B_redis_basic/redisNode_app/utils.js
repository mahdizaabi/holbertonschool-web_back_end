client.lrange('task1', 0, -1, function (err, reply) {
    const listx = reply.map((item) => {
        return (
`<div>
<form action="/delete" method="post">
        <input type="checkbox" name="task" value=${item} id="task">
        <label for="task"> ${item}</label>
        <input type="submit" value="Submit">
    </form>
</div>`)
    })
    res.end(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>Task Manager</h3>
    <form action="/addNewTask" method="post">
        <input type="text" name="task" id="task">
        <input type="submit" value="Submit">
        <label for="task"> add new task</label>
    </form>
    ${listx}
</body>
</html>`)
});