from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    timeline = []
    include_autolyse = True

    # Keep form state between submissions
    end_time_str = ''
    bulk_hours = 7.0
    cold_hours = 12.0

    if request.method == 'POST':
        end_time_str = request.form.get('end_time', end_time_str)
        bulk_hours = float(request.form.get('bulk', bulk_hours))
        cold_hours = float(request.form.get('cold', cold_hours))
        include_autolyse = request.form.get('autolyse') == 'on'

        end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')

        steps = [
            {
                "title": "Rest before slicing",
                "desc": " Remove from the oven if not already done so, Some say this step is the most difficult part... allowing the loaf to cool completely before slicing. This helps the crumb set properly and the bread to finish cooking inside as it cools. It is best to leave it for at least an hour to cool properly before slicing, but if you can wait longer than that it will be even better.",
                "mins": 60
            },
            {
                "title": "Bake uncovered",
                "desc": "After the 20 minutes remove the lid from the Dutch oven to allow the crust on the loaf to brown and crisp. This step usually lasts around 20-25 minutes but keep an eye on it. How you finish your loaf depends on two things, one the size and shape of your loaf and two how deep a golden brown you prefer on the crust. The guide here is to look for a deep golden brown colour but not burnt.",
                "mins": 25
            },
            {
                "title": "Bake covered",
                "desc": "Bake with the lid on to trap steam and allow the loaf to rise for 20 minutes.",
                "mins": 20
            },
            {
                "title": "Score + load into oven",
                "desc": "Remove the banneton from the fridge and the Dutch Oven from the oven. Turn the dough out of the banneton and onto some parchment paper or a silicon bread mat and place into the Dutch Oven. Score the top using a scoring lame or a sharp knife, the cut should be approx 1cm deep running the full length of the loaf. Place the lid back on the Dutch oven and place into the preheated oven.",
                "mins": 5
            },
            {
                "title": "Preheat oven",
                "desc": "Preheat your oven with your Dutch oven inside to 230°C / 450°F / gas mark 8.",
                "mins": 20
            },
            {
                "title": "Cold ferment",
                "desc": "Place the shaped dough into a banneton and place in the fridge to develop flavour slowly. This can be anywhere from 8-24 hours, the longer it goes the more flavour it will develop, but if you are short on time you can do a shorter cold ferment and still get good results. Again with this step if you baked sourdough previously you may have a certain amount of time in mind that works well for you, if so you can set the cold fermentation slider above to help guide the timings better.",
                "mins": cold_hours * 60
            },
            {
                "title": "Bench rest + shaping",
                "desc": "Once the bulk fermentation is complete, turn the dough out onto a lightly floured surface, gently shape it into a round or oval loaf, and let it rest for 20 minutes before shaping into a final shape using any method you like, two suggestions are the letter fold method or the burrito fold method to build up the surface tension of the dough.",
                "mins": 20
            },
            {
                "title": "Bulk fermentation",
                "desc": "For this step cover the bowl and let the dough rise at room temperature while it ferments, it will take anything from 3-8 hours. It just depends on how warm your kitchen is. If it fermented dough in your kitchen previously you may have a good idea how long this is likely to take and if so you can set the fermentation slider above to help guide the timings better. If not, a good rule of thumb is to look for the dough to have almost doubled in size and to have some bubbles on the surface and around the sides of the bowl. Before leaving it to ferment you can mark the side of the bowl with a piece of tape or a marker to help you see how much it has risen. The guide here should be on the rising of the dough, not the time, as the time can vary greatly depending on the temperature of your kitchen and the strength of your starter.",
                "mins": bulk_hours * 60
            },
            {
                "title": "Stretch & folds - 4th and final time (4 times in total)",
                "desc": "The fourth and final of the 4 sets of stretch and fold every 30 minutes to build strength. To do this gently lift one side of the dough, stretch it up and fold it over the top, then rotate the bowl a quarter turnand repeat until you've come full circle and done it 4 times.",
                "mins": 30
            },
            {
                "title": "Stretch & folds - 3rd time(4 times in total)",
                "desc": "The third of 4 sets of stretch and fold every 30 minutes to build strength. To do this gently lift one side of the dough, stretch it up and fold it over the top, then rotate the bowl a quarter turnand repeat until you've come full circle and done it 4 times.",
                "mins": 30
            },
            {
                "title": "Stretch & fold - 2nd time (4 times in total)",
                "desc": "The second of 4 sets of stretch and fold every 30 minutes to build strength. To do this gently lift one side of the dough, stretch it up and fold it over the top, then rotate the bowl a quarter turnand repeat until you've come full circle and done it 4 times.",
                "mins": 30
            },
            {
                "title": "Stretch & fold - 1st time (4 times in total)",
                "desc": "The first of 4 sets of stretch and fold every 30 minutes to build strength. To do this gently lift one side of the dough, stretch it up and fold it over the top, then rotate the bowl a quarter turnand repeat until you've come full circle and done it 4 times.",
                "mins": 30
            },
            {
                "title": "Add starter",
                "desc": "Mix the starter into the dough until fully incorporated and combined and allow it to rest for 30 minutes before beginning the stretch and folds.",
                "mins": 30
            }
        ]

        if include_autolyse:
            steps.append({
                "title": "Autolyse",
                "desc": "If you include this step it can help the flour and water start to combine and the gluten start to develop and give you a stronger dough. Mix just the flour and water together to form whats called by many as a shaggy dough, then let it rest for 30 minutes before adding starter in the next step.",
                "mins": 30
            })

        # ✅ IMPORTANT: define current BEFORE loop
        current = end_time

        for step in steps:
            start = current - timedelta(minutes=step["mins"])
            timeline.insert(0, {
                "title": step["title"],
                "desc": step["desc"],
                "start": start,
                "end": current
            })
            current = start

    return render_template(
        'index.html',
        timeline=timeline,
        include_autolyse=include_autolyse,
        end_time=end_time_str,
        bulk_hours=bulk_hours,
        cold_hours=cold_hours
    )

if __name__ == '__main__':
    # keep debug off in local run to avoid development warning and debugger exposure
    app.run(debug=False, port=5001)

# Production: use a WSGI server (gunicorn/uwsgi) instead of Flask dev server
# Example: gunicorn --bind 0.0.0.0:8000 app:app