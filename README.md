# sdc-driver-clone

## Installation (you need to have `pyenv` and `pipenv` in your global)
* In your ${project_root}, run `pipenv install --ignore-pipfile --dev` - Install all dependencies.


## Run the pretrained model
Start up [the Udacity self-driving simulator](https://github.com/udacity/self-driving-car-sim), choose a scene and press the Autonomous Mode button. Then, in ${project_root} run the model as follows (assume your h5 model file is `my_model.h5`):
```python
pipenv run python drive.py my_model.h5
```

## To train the model
You'll need the data folder which contains the training images. Then, in ${project_root} run
```python
pipenv run python model.py
```
This will generate a file `model-<epoch>.h5` whenever the performance in the epoch is better than the previous best.  For example, the first epoch will generate a file called `model-000.h5`.

## References
* The code in this repo is most from naokishibuya's work [https://github.com/naokishibuya/car-behavioral-cloning](https://github.com/naokishibuya/car-behavioral-cloning).
