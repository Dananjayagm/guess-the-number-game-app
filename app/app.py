from flask import Flask, request, render_template, session
import random


app = Flask(__name__)
app.secret_key = "random-number"

@app.route("/", methods=[ "Get", "POST"])
def index():
       if "number" not in session:
                   session["number"] = random.randint(1, 100)
                   session['tries'] = 0
                      
              msg = ""
              if request.method == "POST":
                  guess = request.form.get("guess")
                  try:
                      g = int(guess)
                  except (TypeError, ValueError):
                      message = " Please type a correct valid number"
                     return render_template("index.html", message=message, tries=session['tries'])

               session['tries'] += 1
               target = session['number']
               if g == target:
                   message = f"Correct!!! The number was{target}.you guessed the correct number in {session['tries']} tries"
     
              session.pop('number', None)
              session.pop('tries', None)
          elif g < target :
               message = "Too low. try agian!"
          else:
          message = "Too high, try again"

return __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=true)

