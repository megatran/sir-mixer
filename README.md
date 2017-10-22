# Sir-Mixer

One teammate recently turned 21 and the team jokingly suggested making a smart cocktail mixer to brighten up his mood. After some discussions regarding fun features with the hackathon sponsors and figuring out the neat business potential of a smart assistant which can mix all kind of drinks from well-known distilled beverages, family-friendly juices, to get-up-and-go energy refreshment, we decided to turn this idea into reality and also learn new technologies (e.g. Qualcomm board, Microsoft Azure and API, etc) along the way!

### Contributors:

Purav Shah, Shweta Oak, Nhan Tran, Alex

### Requirements
see requirements.txt
* Amazon Alexa
* Arduinos
* Qualcomm dragonboard
* Microsoft Azure
* Microsoft Cognitive services APIs


### How we built it:

During the the fun weekend doing the IoT project, we kept in mind that Sir Mixer could serve a wide array of consumers/users.

Tech savy people who enjoy smart assistant (e.g. Alexa) could ask Sir Mixer to make their desired cocktail.
People who come home with certain moods after a long day can be satisfied with personalized mixed drinks which can be automatically triggered when Sir Mixer recognize your facial expressions using the Microsoft Cognitive Services.
We wired all electronics and designed the hardware prototype from scratch (took 2 iterations).
We spent countless hours going over documentations of new technologies most of us have rarely used. We're so glad that the engineers and developer evangelist spent time and helped us over the weekend: from discussing how to build resilient server architecture, the possibilities of the API of emotion and speech recognition, to suggesting some cool ideas for our project, and many more!


### Challenges we ran into
The primary challenge was trying to understand the apis, learn new things and implement those as per the requirement of the app.

At the backend, a lot of the processing is done using Microsoft Azure's services. We tried multiple Microsoft Cognitive services like Face API, Emotion API to detect the face and emotion of the user. Microsoft Bing speech recognition api, Custom speech service, Sentiment analysis of text generated from the speech recognition to determine the mood of the user from speech input. For mapping the emotions to different drinks, we tried implementing the Recommendations API, we also went on to research about the Matchbox recommender system and read a part of the the book Microsoft Azure Machine Learning, to try to implement it. We didn't have much luck in integrating some of these in the final project, but we learned a lot about them and gained experience using them.

### Accomplishments that we're proud of
We built a fully functional IoT system that have smooth mechanism to mix and shake drinks, and is smart to personalize drinks based on user's facial expression and emotions.
What we learned
We learned various new technologies and successfully integrated some of them in our project. We have provided some feedback to the sponsors who were present at the hackathon about our experiences, improve small parts of their documentation regarding unknown errors, and suggested better working examples with clearer steps.


### What's next for Sir Mixer
We plan on enhancing Sir Mixer 1.5 with multi facial recognition feature and fast drink mixing ability. We plan on fully implementing the Matchbox Recommender system on Azure to provide even better personalizations.
