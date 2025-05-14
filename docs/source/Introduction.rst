<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Simple Static Website</title>
    <style>
        body {
            font-family: sans-serif; /* Sets a common sans-serif font */
            line-height: 1.6; /* Adds spacing between lines of text */
            margin: 0; /* Removes default margin around the body */
            padding: 20px; /* Adds padding inside the body */
            background-color: #f4f4f4; /* Sets a light grey background color */
            color: #333; /* Sets a dark grey text color */
        }
        .container {
            max-width: 800px; /* Sets a maximum width for the content area */
            margin: auto; /* Centers the container horizontally */
            background: #fff; /* Sets a white background for the container */
            padding: 20px; /* Adds padding inside the container */
            border-radius: 8px; /* Rounds the corners of the container */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow */
        }
        h1 {
            color: #0056b3; /* Sets a blue color for the main heading */
        }
        p {
            margin-bottom: 15px; /* Adds space below paragraphs */
        }
        .footer {
            margin-top: 20px; /* Adds space above the footer */
            text-align: center; /* Centers the text in the footer */
            font-size: 0.9em; /* Makes the footer text slightly smaller */
            color: #666; /* Sets a medium grey color for the footer text */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Static Website!</h1>
        <p>This is a simple example of a static HTML page.</p>
        <p>Static websites are great for content that doesn't change often, like blogs, portfolios, or documentation.</p>
        <p>In AWS Cloud Quest, you can learn how to host a website like this using Amazon S3.</p>
        <div class="footer">
            &copy; 2025 My Simple Website
        </div>
    </div>
</body>
</html>
