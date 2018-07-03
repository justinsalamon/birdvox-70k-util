# CREATED: 6/11/18 6:57 PM by Justin Salamon <justin.salamon@nyu.edu>

import h5py
import os
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
import glob
import argparse


def unpack_bv70k_h5(bvfile, bit='float32'):

    # Create output dir
    dirname = os.path.dirname(bvfile)
    dirname = os.path.join(dirname,
                           os.path.basename(bvfile).replace('.hdf5', ''))
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    # load data
    f = h5py.File(bvfile, 'r')

    print('Unpacking audio file in {}...'.format(os.path.basename(bvfile)))

    # Split into audio files and save into the folder
    for k in tqdm((f['waveforms'].keys())):
        audio = np.array(f['waveforms'][k])

        # cast to desired bit format
        if bit == 'float32':
            audio = audio.astype('float32')
        elif bit == 'int32':
            audio = (audio * 2147483647).astype('int32')
        elif bit == 'int16':
            audio = (audio * 32767).astype('int16')
        else:
            print('Unsupported bitrate, aborting')
            break

        filename = os.path.join(dirname, k + '.wav')
        wavfile.write(filename, 24000, audio)

    print('Done.')


def unpack_bv70k_folder(dir, bit='float32'):

    # Find h5 files in the directory
    h5files = glob.glob(os.path.join(dir, 'BirdVox-70k*.hdf5'))

    print('Unpacking all BirdVox-70k files found in folder: {}'.format(
        os.path.basename(dir)))

    for f in h5files:
        unpack_bv70k_h5(f, bit=bit)

    print('Finished unpacking all files.')


def run(folder, bit):

    if not os.path.isdir(folder):
        print('The provided path does not point to a valid folder, aborting.')
        return

    if bit not in ['float32', 'int32', 'int16']:
        print('Unsupported bit format {}, aborting.'.format(bit))
        return

    unpack_bv70k_folder(folder, bit=bit)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=(
        'Given a path to a folder containing BirdVox-70k hdf5 files, unpack '
        'each file into a folder containing individual audio files for each '
        'clip.'
    ))
    parser.add_argument('folder')

    bit_help= ('Bit format for output WAV files. Supported values are: '
               'float32 (default), int32 and int16.')
    parser.add_argument('--bit', type=str, default='float32', help=bit_help)

    args = parser.parse_args()
    run(**vars(args))
