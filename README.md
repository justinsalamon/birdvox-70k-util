# birdvox-70k-util
Tools for working with the [BirdVox-70k dataset](https://zenodo.org/record/1226427).



## Extracting the audio files from the BirdVox-70k HDF5 files

The [BirdVox-70k dataset](https://zenodo.org/record/1226427) (details below) is provided as six HDF5 files (e.g. `BirdVox-70k_unit01.hdf5`). While you can load the files into memory directly e.g. using Python's `h5py` module, for some users and applications it might be more convenient to have each audio clip as a separate wav file on disk.

You can use the `unpack_bv70k.py` script to extract the individual audio files from the BirdVox-70k HDF5 files:

1. Download all the .hdf5 files of the [BirdVox-70k dataset](https://zenodo.org/record/1226427) and place them in the same folder

2. If you don't have Python installed on your system, follow the instructions here: https://conda.io/docs/user-guide/install/index.html

3. Once Python is installed, install the dependencies using `pip` by running the following command from your (anaconda) terminal: `>pip install h5py numpy scipy tqdm`

4. Run the unpacking script as follows: `>python unpack_bv70k.py <path to folder containing hdf5 files>`

The script will create a folder for each hdf5 file and save all the audio files contained within it as individual wav files. Once unpacked, each filename of each audio clip will end with a number, either 0 or 1. Files ending with 1 contain a flight call, files ending with a 0 do not (i.e. they contain background noise and other confounding factors that are not flight calls).

## About BirdVox-70k

The BirdVox-70k dataset contains 70k half-second clips from 6 audio recordings in the BirdVox-full-night dataset, each about ten hours in duration. These recordings come from ROBIN autonomous recording units, placed near Ithaca, NY, USA during the fall 2015. They were captured on the night of September 23rd, 2015, by six different sensors, originally numbered 1, 2, 3, 5, 7, and 10.

Andrew Farnsworth used the Raven software to pinpoint every avian flight call in time and frequency. He found 35402 flight calls in total. He estimates that about 25 different species of passerines (thrushes, warblers, and sparrows) are present in this recording. Species are not labeled in BirdVox-70k, but it is possible to tell apart thrushes from warblers and sparrrows by looking at the center frequencies of their calls. The annotation process took 102 hours.

The dataset can be used, among other things, for the research,development and testing of bioacoustic classification models, including the reproduction of the results reported in [1].

For details on the hardware of ROBIN recording units, we refer the reader to [2].

[1] V. Lostanlen, J. Salamon, A. Farnsworth, S. Kelling, J. Bello. BirdVox-full-night: a dataset and benchmark for avian flight call detection. Proc. IEEE ICASSP, 2018.

[2] J. Salamon, J. P. Bello, A. Farnsworth, M. Robbins, S. Keen, H. Klinck, and S. Kelling. Towards the Automatic Classification of Avian Flight Calls for Bioacoustic Monitoring. PLoS One, 2016.

```
@inproceedings{lostanlen2018icassp,
  title = {BirdVox-full-night: a dataset and benchmark for avian flight call detection},
  author = {Lostanlen, Vincent and Salamon, Justin and Farnsworth, Andrew and Kelling, Steve and Bello, Juan Pablo},
  booktitle = {Proc. IEEE ICASSP},
  year = {2018},
  published = {IEEE},
  venue = {Calgary, Canada},
  month = {April},
}
```
