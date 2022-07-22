# Chatbot with Flash and Chatterbot

In this example, I combine two tutorials: [Edureka](https://www.edureka.co/blog/how-to-make-a-chatbot-in-python/) and [Upgrad](https://www.upgrad.com/blog/how-to-make-chatbot-in-python/).

## Starting up
1. Open your local repository in Visual Studio Code
2. Create a folder named `app` 
3. Within the `app` folder, create a folder named `static` and another folder named `templates`

## Installing dependencies
Within your repository open in Visual Studio Code, open the built-in terminal window and install the following dependencies:
* `pip3 install flask` 
* `pip3 install chatterbot`

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



