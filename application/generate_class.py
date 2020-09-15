import numpy as np


def generate_class(model, tokenizer, word_embedding, peak_pose, stop_word, max_length):

    # generate seed text
    seed_text = [peak_pose, word_embedding.most_similar(peak_pose, topn=10)[np.random.choice(
        range(10))][0], word_embedding.most_similar(peak_pose, topn=10)[np.random.choice(range(10))][0]]
    in_text = seed_text

    # create yoga class, explicitly including user's desired peak pose
    yoga_class = list()
    yoga_class.append(peak_pose.lower())

    # generate sequence
    while True:
        encoded = tokenizer.texts_to_sequences([in_text])

        # select next pose integer based on models probability distribution
        prediction_output = model.predict(encoded)
        yhat = np.random.choice(
            len(prediction_output[0]), p=prediction_output[0])

        # find pose in dictionary
        out_word = ""
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break

        # append pose to current class, and update input text
        # add 'repeat other side' text on duplicate poses
        # converge to start and stop poses
        if out_word != "":
            in_text.append(out_word)
            if out_word == yoga_class[-1]:
                if stop_word == "easy pose":
                    yoga_class[-1] += ", repeat other side"
                    yoga_class.append(out_word)
                if stop_word == "corpse pose":
                    out_word += ", repeat other side"
                    yoga_class.append(out_word)
            else:
                yoga_class.append(out_word)
        if out_word == stop_word:
            break

        # if sequence gets too long without converging to ending, start over and try again.
        if len(yoga_class) == max_length:
            in_text = seed_text
            yoga_class = [peak_pose.lower()]

    yoga_class = [i.title() for i in yoga_class]
    return yoga_class
