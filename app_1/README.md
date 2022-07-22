# Chatbot with Flash and Chatterbot

In this example, I combine two tutorials: [Edureka](https://www.edureka.co/blog/how-to-make-a-chatbot-in-python/) and [Upgrad](https://www.upgrad.com/blog/how-to-make-chatbot-in-python/).

## Starting up
1. Open your local repository in Visual Studio Code
2. Create a folder named `app` 
3. Within the `app` folder, create a folder named `static` and another folder named `templates`

## Creating a user interface for our chatbot
In your `template` folder, create a file named `index.html`. This page will act as a user interface (UI) for us to talk to our chatbot. This UI takes
our input, sends it to our bot, and shows us the output (bot's response). 

In your `static` folder, create a file named `style.css`. This file will contain some CSS code to decorate our UI. In this example, the design is very
basic, but feel free to make customize it. 

**`index.html`**

We start by adding the necessary html tags to our template to create the shape of our page. 

```
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
</head>

<body>
    <h1>Flask Chatterbot Example</h1>
</body>

</html>
```

The `<head>` tag is used to include links and external libraries that we may need for our app to function. In our case, we link our style sheet `style.css`
so that every changes made to it will reflect on our UI. 

We also include an external library `ajax/jquery` which allows our app to run on a local server. 

The part that is visible to the user is all contained within the `<body>` tags. In this part, we added a title "Flask Chatterbot Example". 

Now, we need to create an interface so that our UI takes our input and sends it to our bot. To do that, we can create a `chatbox`: 

```
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
</head>

<body>
    <h1>Flask Chatterbot Example</h1>
    <div>
        <div id="chatbox">
            <p class="botText"><span>Hi! I'm a bot.</span></p>
        </div>
        <div id="userInput">
            <input id="textInput" type="text" name="msg" placeholder="Message">
            <input id="buttonInput" type="submit" value="Send">
        </div>
    </div>
</body>

</html>
```

Within the `<body>` tag, we add a `<div>` tag which is simply a container to display our UI. We give the second `<div>` a "chatbox" id which means
that this `<div>` is where we will be able to interact with our bot. Within the chatbox, we place a text that becomes our bot's first message when we
open our page. 

Next, we add another `<div>` that will allow us to send messages to our bot.

So far, our app looks like this: 

![Capture d’écran, le 2022-07-22 à 12 57 53](https://user-images.githubusercontent.com/17911957/180488086-1b6e144c-6e52-47a5-b298-410746dbb934.png)

Now, we want to be able to receive a response from our bot when we send it a message. 

To do so, we will add a `<script>` tag to our code in which we create a function `getBotResponse()`. We use the id previously created to tell our code
where to take the input, send it, and after this, receive a response. Right now, nothing happens since we have not yet created our bot. 


```
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
</head>

<body>
    <h1>Flask Chatterbot Example</h1>
    <div>
        <div id="chatbox">
            <p class="botText"><span>Hi! I'm a bot.</span></p>
        </div>
        <div id="userInput">
            <input id="textInput" type="text" name="msg" placeholder="Message">
            <input id="buttonInp
            ut" type="submit" value="Send">
        </div>
        <script>
            function getBotResponse() {
                var rawText = $("#textInput").val();
                var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
                $("#textInput").val("");
                $("#chatbox").append(userHtml);
                document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
                $.get("/get", { msg: rawText }).done(function (data) {
                    var botHtml = '<p class="botText"><span>' + data + '</span></p>';
                    $("#chatbox").append(botHtml);
                    document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
                });
            }
            $("#textInput").keypress(function (e) {
                if (e.which == 13) {
                    getBotResponse();
                }
            });
            $("#buttonInput").click(function () {
                getBotResponse();
            })
        </script>
    </div>
</body>

</html>
```

**`style.css`**
Using the id's and tags from our `index.html` code, we can change their style, colour, and position through CSS. The basic styling can be found in
[the css file](https://github.com/jaslatendresse/summer-chatbot/blob/main/app_1/static/style.css). Our app now looks like this:

<img width="695" alt="Capture d’écran, le 2022-07-22 à 13 09 27" src="https://user-images.githubusercontent.com/17911957/180489904-602379b9-f5f6-475e-b6d0-4e4f03533b36.png">

## Creating the chatbot
Right now, all we have is a UI, but nothing really happens yet. In the `app` folder, create a file named `app.py`. This file will allow us to create our bot and run our app locally.

**Prepare dependencies and import classes** 
We first install `flask` by running `pip3 install flask` in the terminal. 

To install `chatterbot`, run `pip3 install git+git://github.com/gunthercox/ChatterBot.git@master`. 

If the `chatterbot` installation fails, you can install it from the source: 
1. `git clone https://github.com/gunthercox/ChatterBot.git`
2. `pip3 install ./ChatterBot`

Once that's done, we can import the classes we need for our bot: 

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
```

**Initializing our app**

This will allow our app to run locally on port 8000: 

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
```

**Create and train the bot**

This particular chatbot is an instance of the `ChatBot` class. After creating a new `ChatterBot` instance, we can train it and improve its performance. 
We can train the bot on whatever knowledge we want such as maths, trivia, science, etc. Training ensures that the bot has enough knowledge to get started with specific responses to specific inputs: 

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

my_bot = ChatBot(name='MyBot', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

if __name__ == "__main__":
    app.run(port=8000, debug=True)
```

Here, the parameter `name` represents the name of our bot. Then, if you want to disable the bot's ability to learn after training, 
you can include the `read_only = True` command. Finally, `logic_adapters` denotes the list of adapters used to train our bot: `chatterbot.logic.MathematicalEvaluation` helps our bot solve math problems and the `chatterbot.logic.BestMatch` helps it choose the best match from the list of responses that we provide. 

Let's provide our bot with some responses: 

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

my_bot = ChatBot(name='MyBot', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok.',
              'glad to hear that.',
              'i\'m fine.',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.', 
              'what\'s your name?',
              'i\'m MyBot. ask me a math question please.']

math_talk_1 = ['pythagorean theorem', 'a squared plus b squared equals to c squared']
math_talk_2 = ['law of cosines', 'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

if __name__ == "__main__":
    app.run(port=8000, debug=True)
```

Then, to train our bot, we can use the `ListTrainer` and supply it with a list of strings:

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

my_bot = ChatBot(name='MyBot', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok.',
              'glad to hear that.',
              'i\'m fine.',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.', 
              'what\'s your name?',
              'i\'m MyBot. ask me a math question please.']

math_talk_1 = ['pythagorean theorem', 'a squared plus b squared equals to c squared']
math_talk_2 = ['law of cosines', 'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)
```

At this point, our bot is ready to communicate. However, there is one last step to get our app to run, and it's to tell our code how to display our UI in the browser: 

```
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

my_bot = ChatBot(name='MyBot', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok.',
              'glad to hear that.',
              'i\'m fine.',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.', 
              'what\'s your name?',
              'i\'m MyBot. ask me a math question please.']

math_talk_1 = ['pythagorean theorem', 'a squared plus b squared equals to c squared']
math_talk_2 = ['law of cosines', 'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))
 
if __name__ == "__main__":
    app.run(port=8000, debug=True)
```

Here, we tell our code to render the UI that we created in the `index.html` page when running the app. Then, we create a function to fetch the bot's response and display it on the screen. 

We can now run our chatbot with `python3 app/app.py`: 

<img width="635" alt="Capture d’écran, le 2022-07-22 à 16 54 33" src="https://user-images.githubusercontent.com/17911957/180567146-44deddab-6899-45b5-a7c8-c093597bd086.png">




