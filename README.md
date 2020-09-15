### Metis Final Project

# Vinyasa Krama: AI-Generated Yoga Classes

### Anterra Kennedy

## Goal

This repository comprises my work on an application I'm creating, which creates safe, completely unique, and compelling AI-generated yoga classes, custom-built around a user's desired 'peak pose' (the hardest pose they want to get to, in the middle of the class), which can be taken at the click of a button. Especially given COVID-19, it will benefit people stuck at home greatly to have new yoga classes to take any time.

The application has options to be used both by yoga teachers, to create and print sequences to teach in their classes, thereby saving them time and improving the safety of their offerings, as well as by general yoga practitioners, who will be able to practice along with the animated front end of the application.

### Background

The rise in popularity of yoga in the United States has turned it into an \$18 billion a year industry, and yet it remains an industry without any kind of official licensure or credentialing system. The introduction of yoga to the West and its subsequent commercialization has created a culture of consumption surrounding yoga; offered so plentifully and consumed so rapidly that it is often not sat with or reflected upon, teachers in meeting that demand have to come up with so many new classes each week that they aren’t practicing those sequences on their own. Consequently, classes may not always have safe, efficient or well-rounded sequencing.

That lack of safety is compounded upon by COVID-19, which has ushered in the age of at-home work outs. Now that students cannot go to their favorite teachers and studios, they need options for classes at home. The current option is basically to take a gamble on a random youtube video by anyone.

As a lifelong practitioner of yoga, I hope that my app can serve as an injection of authenticity and informed, safe sequencing into the Western yoga community, and offer such unique, safe and custom classes to the community. Can data science replicate the firmly grounded and informed felt sense of a good yoga sequence that the likes of T. Krishnamacharya, the father of modern yoga, originally taught? The phrase "Vinyasa Krama" — the origin of the now popular ‘Vinyasa’ yoga — means a correctly organized sequence which progresses wisely. This ‘correct’ sequencing should include physical and biomechanical considerations for safety of the joints, necessary countermovements to each pose practiced, the energetic effect of the chosen asanas, and the overall arc and flow of the class. I want to use machine learing and neural networks to offer such authentic and well-rounded sequences to modern yoga teachers and practitioners.

## Methodologies:

Use a bi-directional LSTM neural network to generate yoga classes.

- Webscraped 50,000 yoga classes by real teachers all over the world.
- Utilize NLP pre-processing techniques of tokenization to isolate each pose and industry knowledge to reduce thousands of pose variations down to base poses and a few key variations.
- Used Word2Vec to create pose embeddings which captured pose similarities.
- Used transfer learning to initialize the neural network with weights from the Word2Vec model.
- Trained a 3-hidden layer bi-directional LSTM on the yoga classes. A bi-directional LSTM was an ideal choice, since it provides context in both directions from any input text, such that I could generate half the class in the backwards direction, of what should precede peak pose.
- Generated yoga classes from the middle (user's peak pose) out in both directions.
- Allowed the class to keep generating until naturally converging upon yoga class entry and exit poses of 'easy pose' and 'corpse pose', rather than defining a set length.
- Utilized the Unity Game Engine to create a 3D environment and person to demonstrate each pose in the generated class. Animated a demo class as a prototype.
- Created a flask app!

## Results & Strengths:

After generating and observing many example sequences, I saw the following strengths across a majority of the classes generated, and of the app as a whole:

- Only customizable yoga app (not yet) on the market, where a class is generated to a user's specification. Will allow yoga practioners to gradually work up to harder poses.
- Only app which will create unique classes for teachers to go offer in their classes, saving them time, and improving the safety of their offerings.
- Definitely captures the intended arc of a yoga class
- Good at repeating poses when they are imbalanced (one sided)
- Creates classes with an overall length and difficulty level that correlates to the difficulty of the chosen peak pose
- Fairly good at including the right preparatory poses to warm up the key muscle groups of the peak pose

## Future Work:

Before this app is ready to take to the market, it will need the following improvements:

- Dynamic rendering of Unity interface -- I will be rendering the below example class for users to follow along with as a proof of concept using the Unity game engine. The eventual intention is that the class created live and custom for the user via the neural network will be dynamically animated for them to take.
- Improved consistency of output. There's too much variability right now with it sometimes giving less good sequences with really random poses showing up in orders they shouldn't.
- More pose variations -- include all variations, instead of only base poses and a few key variations.
- Embedding information of muscle groups -- I'd love to be able to include this for additional safety, rather than just the context of poses showing up around other poses.

I am excited to continue work on this application and eventually bring it to market.

## Deliverables:

- [Vinyasa Krama App](https://github.com/anterra/vinyasa-krama/tree/master/application)
- [Modeling](https://github.com/anterra/vinyasa-krama/blob/master/modeling.ipynb)
- [Data Collection](https://github.com/anterra/vinyasa-krama/tree/master/data%20%26%20data%20collection)
- [Presentation Slides](https://github.com/anterra/vinyasa-krama/blob/master/Vinyasa%20Krama.pdf)
- Recording of Presentation

## Project Team:

- [Anterra Kennedy](https://linkedin.com/in/anterrakennedy)

## Technologies Used (Anticipated):

- Bi-Directional LSTM
- Tensorflow/Keras
- Unity
- Jupyter Notebook
- Python
- Pandas
- NLP
- Flask
- HTML/CSS

## Skills Demonstrated

- Neural Networks
- Unsupvised Machine Learning
- Web Scraping
- Word Embeddings
