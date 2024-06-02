<!-- app/templates/ask.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ask a Question</title>
</head>
<body>
    <h1>Ask a Question</h1>
    <form method="POST">
        <label for="question">Question:</label><br>
        <textarea id="question" name="question" rows="4" cols="50"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    {% if question %}
    <h2>Question:</h2>
    <p>{{ question }}</p>
    <h2>Answer:</h2>
    <p>{{ answer }}</p>
    {% endif %}
</body>
</html>

