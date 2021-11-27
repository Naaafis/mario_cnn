# PySuperTuxKart

The purpose of this repository is to hold the various files needed to train and test different models on a shared computing cluster. I am attempting to complete 4 Mario kart courses as fast as possible by applying a CNN and variety of training conditions. My current course of action is to test on the professor's controller vs. my own controller and see the difference in performance times. From there, I will design a CNN on both controllers and analyze the performance of the CNN. I will also tune the amount of images collected (vision data) to train the CNN. I will try to train the model on images collected from each individual track and observe the difference in performance when the model is only trained on those tracks vs. all the tracks.

Other things to try include adding and removing layers to test if any kind of overfitting is happening. I will potentially explore the option where:

"You could try building a neural network to predict whether there is something in the image ahead that is concerning (e.g., a turn) and pass that information into the controller to adjust your velocity. One possibility: try to predict whether the aim-point will change in the next few seconds."


# File Purposes:

hw_5 - The original NN trained without any experimentation. Base conditions for images collected from all the tracks. This is our control model

base_files - Used only to reset our project after each training session.

testing_files - Where I could try out the variety of strategies

image_collection - As the name suggests, this will be the files used to collect the images

cnn_extras - these files could be pasted into testing_files in order to get the testing_files ready for training
