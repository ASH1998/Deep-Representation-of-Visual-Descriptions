# Deep-Representation-of-Visual-Descriptions  
[![HitCount](http://hits.dwyl.io/ASH1998/Deep-Representation-of-Visual-Descriptions.svg)](http://hits.dwyl.io/ASH1998/Deep-Representation-of-Visual-Descriptions.svg)       [![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg?style=popout)](https://github.com/ASH1998/Deep-Representation-of-Visual-Descriptions/)  ![](https://img.shields.io/jenkins/s/https/jenkins.qa.ubuntu.com/view/Precise/view/All%20Precise/job/precise-desktop-amd64_default.svg)  
`The project is ongoing, so changes will be frequent!!`     
The aim of this project is about simplifying the concept of Attention mechanism in using it for generating images given some visual description for the images to be genrated.


## Why? [![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](https://ash1998.github.io/Deep-Representation-of-Visual-Descriptions/) 


## Documentation [![wiki](https://img.shields.io/badge/Wiki-GO-brightgreen.svg)](https://github.com/ASH1998/Deep-Representation-of-Visual-Descriptions/wiki)
## Dependencies ![](https://img.shields.io/depfu/depfu/example-ruby.svg)
1. Python 3.0
2. Pytorch
3. torchfile
4. nltk- ('punkt')
5. pandas
6. scikit-learn
7. python-dateutil
8. easydict
9. shutil
10. Matplotlib
11. Scikit-Image(skimage)

## Data Download
### Repo : [![](https://img.shields.io/badge/download%20repo:-273.93MiB-blue.svg)](https://github.com/ASH1998/Deep-Representation-of-Visual-Descriptions/archive/master.zip)

## Models :

Model Architecture  :

![](https://github.com/ASH1998/Deep-Representation-of-Visual-Descriptions/blob/master/project.png)
### Trained models:
### Eval models

## Using Jupyter

[View Notebook](code/Driver!!.ipynb). This notebook uses the data and pretrained models to take in sentences from the user and provide the outputs.
#### BIRD GENERATED IMAGES
![](jup3.png)

#### COCO GENERATED IMAGES
![](jup4.png)
## Current Outputs

##### `Text : flat screen television on top of an old tv console`  
![](models/coco_AttnGAN2/example_captions/0_s_11_g2.png)
![](models/coco_AttnGAN2/example_captions/0_s_11_a1.png)


##### `Text : a large red and white boat floating on top of a lake`  
![](models/coco_AttnGAN2/example_captions/0_s_3_g2.png)
![](models/coco_AttnGAN2/example_captions/0_s_3_a1.png)


##### `TEXT :this bird is red and white in color with a stubby beak and red eye rings`  
![](models/bird_AttnGAN2/next/0_s_3_g2.png)
![](models/bird_AttnGAN2/next/0_s_3_a1.png)

##### `Text : this bird is yellow with black on its head and has a very short beak`  
![](models/bird_AttnGAN2/next/0_s_0_g2.png)
![](models/bird_AttnGAN2/next/0_s_0_a1.png)


##### Caption Generation with Attention:    
![](output/coco_DAMSM_2018_10_10_04_42_55/Image/attention_maps0.png)


## Contributing :
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ASH1998/Deep-Representation-of-Visual-Descriptions/issues)

## Website :
[https://ash1998.github.io/Deep-Representation-of-Visual-Descriptions/](https://ash1998.github.io/Deep-Representation-of-Visual-Descriptions/)
