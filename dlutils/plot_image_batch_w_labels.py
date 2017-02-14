"""
Module to plot a batch of images along w/ their corresponding label(s)/annotations and save the plot to disc.

Use cases:
Plot images along w/ their corresponding ground-truth label & model predicted label,
Plot images generated by a GAN along w/ any annotations used to generate these images,
Plot synthetic, generated, refined, and real images and see how they compare as training progresses in a GAN,
etc...
"""

import os

import matplotlib

matplotlib.use('Agg')  # b/c matplotlib is such a great piece of software ;) - needed to work on ubuntu
from matplotlib import pyplot as plt


def plot_batch(image_batch, figure_path, label_batch=None):
    """
    Plots a batch of images and their corresponding label(s)/annotations, saving the plot to disc.

    :param image_batch: Batch of images to be plotted.
    :param figure_path: Full path of the filename the plot will be saved as.
    :param label_batch: Batch of labels corresponding to `image_batch`.
       Labels will be displayed along w/ their corresponding image.
    """
    if label_batch:
        assert image_batch.shape[0] == label_batch.shape[0], 'Their must be a label for each image to be plotted.'

    batch_size = image_batch.shape[0]

    # plot images in rows and columns
    nb_rows = batch_size // 10 + 1  # each row will have 10 images, last row will have the rest of images in the batch
    nb_columns = 10

    _, ax = plt.subplots(nb_rows, nb_columns, sharex=True, sharey=True)

    for i in range(nb_rows):
        for j in range(nb_columns):
            try:
                ax[i][j].imshow(image_batch[i * nb_columns + j])
                ax[i][j].set_title(label_batch[i * nb_columns + j])
                ax[i][j].set_axis_off()
            except IndexError:
                break

    plt.savefig(os.path.join(figure_path), dpi=600)
    plt.close()
