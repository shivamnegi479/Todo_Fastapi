<h1>
Todo Fastapi
</h1>
<p>It is a simple application that allows users to manage their tasks or to-do items. It provides basic functionality such as creating new tasks, viewing existing tasks, and deleting tasks.</p>

<h5>Backend (FastAPI):</h5>
    <ul>
        <li>FastAPI is used as the web framework to handle HTTP requests and responses.
            </li>
        <li>It defines various endpoints to handle CRUD (Create, Read, Update, Delete) operations for the Todo items.</li>
        <li>Endpoints are configured to interact with a MongoDB database for data storage and retrieval.</li>
        <li>The backend performs operations like creating new tasks, fetching all tasks, and deleting tasks from the database.</li>
    </ul>
 <h5>Database (MongoDB):</h5>
    <ul>
        <li>MongoDB is used as the database to store the Todo items.
            
        <li>Each Todo item is represented as a document in a collection.</li>
        <li>
            The documents contain fields such as ID, title, description, and status (completed or not).</li>

        </li>
    </ul>
  <h5>Frontend (Jinja templates, JavaScript, CSS):</h5>
    <ul>
        <li>Jinja templates are used to generate dynamic HTML pages with placeholders for data from the backend.</li>
        <li>HTML templates are rendered by the server and sent to the client.</li>
        <li>JavaScript is used to handle user interactions and perform actions like submitting forms</li>
        <li>CSS stylesheets are used to define the visual appearance and layout of the web pages.</li>
    </ul>
