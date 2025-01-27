import os
import cv2
import numpy as np
import tensorflow as tf


def load_frame(filename, height, width):
    image_decoded = cv2.imread(filename)
    image_decoded = cv2.cvtColor(image_decoded, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_decoded, (width, height))
    image_resized = image_resized.astype(dtype=np.float32)
    image_resized = (image_resized / 127.5) - 1.0
    return image_resized


def inverse_transform(images):
    return (images + 1.) / 2.


def multi_scale_crop_load_frame(filename, height, width, bbox):
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (width, height))
    image = image.astype(dtype=np.float32)
    image = (image / 127.5) - 1.0

    return image[bbox[0][0]: bbox[0][1], bbox[1][0]:bbox[1][1], :]


def log10(t):
    """
    Calculates the base-10 log of each element in t.

    @param t: The tensor from which to calculate the base-10 log.

    @return: A tensor with the base-10 log of each element in t.
    """

    numerator = tf.log(t)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def psnr_error(gen_frames, gt_frames):
    """
    Computes the Peak Signal to Noise Ratio error between the generated images and the ground
    truth images.

    @param gen_frames: A tensor of shape [batch_size, height, width, 3]. The frames generated by the
                       generator model.
    @param gt_frames: A tensor of shape [batch_size, height, width, 3]. The ground-truth frames for
                      each frame in gen_frames.

    @return: A scalar tensor. The mean Peak Signal to Noise Ratio error over each frame in the
             batch.
    """
    shape = tf.shape(gen_frames)
    num_pixels = tf.to_float(shape[1] * shape[2] * shape[3])
    # gt_frames = (gt_frames + 1.0) / 2.0
    # gen_frames = (gen_frames + 1.0) / 2.0
    square_diff = tf.square((gt_frames - gen_frames) / 2.0)

    batch_errors = 10 * log10(1 / ((1 / num_pixels) * tf.reduce_sum(square_diff, [1, 2, 3])))
    return tf.reduce_mean(batch_errors)


def diff_square_mask(gen_frames, gt_frames):
    square_diff = tf.square((gt_frames - gen_frames) / 2.0)
    return square_diff


def diff_gray_mask(gen_frames, gt_frames, min_value=-1, max_value=1):
    # normalize to [0, 1]
    delta = max_value - min_value
    gen_frames = (gen_frames - min_value) / delta
    gt_frames = (gt_frames - min_value) / delta

    gen_gray_frames = tf.image.rgb_to_grayscale(gen_frames)
    gt_gray_frames = tf.image.rgb_to_grayscale(gt_frames)

    diff = tf.abs(gen_gray_frames - gt_gray_frames)
    return diff


def load(saver, sess, ckpt_path):
    saver.restore(sess, ckpt_path)
    print("Restored model parameters from {}".format(ckpt_path))


def save(saver, sess, logdir, step):
    model_name = 'model.ckpt'
    checkpoint_path = os.path.join(logdir, model_name)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    saver.save(sess, checkpoint_path, global_step=step)
    print('The checkpoint has been created.')