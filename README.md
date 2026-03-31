# Sourdough Planner

Example project description:
Sourdough Planner is a simple Flask web app that helps bakers plan a loaf from start to finish. It combines an ingredient calculator with a timeline generator so you can work backwards from your target finish time and organise each stage of the bake.

You can amend this description before uploading to GitHub.

## Features

- Calculate ingredient amounts for a target loaf size
- Adjust hydration, starter, and salt values in Advanced Mode
- Generate a baking timeline from a target loaf-ready time
- Customize starter activation, bulk fermentation, and cold fermentation timings
- Optionally include autolyse in the process
- Optionally include feeding the starter in the process
- Track progress through the generated timeline

## Screenshots

![Sourdough Planner on load](pictures/appOnLoad.png)

![Sourdough Planner with ingredient values populated](pictures/appPopulated.png)

![Sourdough Planner timeline view](pictures/appTimeline.png)

![Sourdough Planner extended timeline view](pictures/appTimeline2.png)

## Tech Stack

- Python
- Flask
- Jinja2
- Bootstrap 5
- Gunicorn

## Running Locally

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the Flask app.
4. Open the app in your browser.

Example commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The app runs locally on `http://127.0.0.1:5001`.

## Running With Docker

Build and run with:

```bash
docker build -t sourdough-planner .
docker run -p 8000:8000 sourdough-planner
```

Then open `http://127.0.0.1:8000`.

## Project Structure

```text
.
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
└── README.md
```

## How To Use

Example text to edit:

1. Enter your target loaf size in the Ingredient Calculator.
2. Click `Calculate` to generate ingredient amounts.
3. Choose your target loaf-ready time in the Timeline Generator.
4. Adjust fermentation timings if needed.
5. Toggle optional steps like autolyse or feeding the starter.
6. Generate the timeline and work through the bake.

## Roadmap

Example ideas to keep, remove, or rewrite:

- Add persistent saved recipes
- Add multiple loaf profiles
- Add printable or exportable timeline views
- Add mobile layout improvements
- Add unit or integration tests

## Contributing

Example text to amend:
Contributions, suggestions, and improvements are welcome. If you would like to contribute, feel free to fork the repository and open a pull request.

## License

Example text to amend:
Choose a license before publishing, such as MIT, Apache-2.0, or keep this section updated with your preferred terms.
