Hi all,

the Homepage where you can read the whole story is here: https://4coloring.wordpress.com

## Example

This is an example of graph colored with the Python program:
<p>
  <a href="https://github.com/stefanutti/maps-coloring-python/blob/master/graphs_created_and_colored/Test-1996-Vertices-2994-Edges.png">
    <img src="https://github.com/stefanutti/maps-coloring-python/blob/master/graphs_created_and_colored/Test-1996-Vertices-2994-Edges-small.png">
  </a>
</p>

The graph has 1996 vertices and 2994 edges and, starting from the planar representation of it, it took about 20 seconds to be colored:
- https://4coloring.wordpress.com/2016/10/16/four-color-theorem-a-fast-algorithm/

The input .dot file used can be downloaded here: <a href="https://github.com/stefanutti/maps-coloring-python/blob/master/graphs_created_and_colored/Test-1996-Vertices-2994-Edges.dot">Test-1996-Vertices-2994-Edges.dot</a>
- From an .edgelist graph (<a href="https://networkx.github.io/documentation/networkx-1.9.1/reference/readwrite.edgelist.html">networkx</a>) I generated an embedding of the graph on the plane. I used the Sage function is_planar(set_embedding = True)) 
- Then, from the planar representation of the original graph I use my algorithm

Note: The .dot file can be used to test other algorithms.

Definition of "planar embedding":
- A combinatorial embedding of a graph is a clockwise ordering of the neighbors of each vertex. From this information one can define the faces of the embedding, which is what this method returns
  - Planar representation example:
    - graphs.TetrahedralGraph().faces()
      - [[(0, 1), (1, 2), (2, 0)], [(3, 2), (2, 1), (1, 3)], [(2, 3), (3, 0), (0, 2)], [(0, 3), (3, 1), (1, 0)]]

## YouTube videos

Some videos of the running Python and Java programs:
- https://www.youtube.com/user/mariostefanutti/videos

## Installation:
- For the installation (docker version) of the environment to run the python 4ct program, read next.

## Pre-configured docker container (skip all next steps up to "Run 4ct.py")
- https://hub.docker.com/r/stefanutti/ai/

## Prepare a docker machine (if not yet done)
- https://github.com/stefanutti/docker-utils

## Install - ubuntu docker container
- docker run -it --name ai-temp ubuntu:16.04 bash
- docker commit ai-temp stefanutti/ai:1.0 (commit the container to create a personal new image to work with)
- docker rm ai-temp
- docker run -it -p 8888:8888 -p 6006:6006 --name ai -e PASSWORD=ai -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/dri --device /dev/snd stefanutti/ai:1.0 bash

## Install - utilities
- apt-get update
- apt-get install vim
- apt-get install git
- apt-get upgrade

## Install - Tensorflow
- apt-get install python-pip python-dev
- pip install tensorflow
- pip install --upgrade pip

## Install - DQN
- Read the installation info from here: https://github.com/devsisters/DQN-tensorflow
  - mkdir /dqn
  - cd /dqn
  - git clone https://github.com/devsisters/DQN-tensorflow.git
  - pip install tqdm gym[all] --> ERROR
    - https://github.com/openai/gym/issues/218
      - apt-get install xvfb libav-tools xorg-dev libsdl2-dev swig cmake
  - execution of "python main.py --env_name=Breakout-v0 --is_train=True --display=False"
    - Error: GPU
      - Disable GPU in main.py
        - flags.DEFINE_boolean('use_gpu', False, 'Whether to use gpu or not')
    - Error: Memory
      - Change memory usage in config.py
    - Error: AttributeError: 'TimeLimit' object has no attribute 'ale'
      - pip install gym==0.7.0 (Note: downgrade)
    - Now the command runs OK
  - execution of "python main.py --env_name=Breakout-v0 --is_train=True --display=True"
    - Error: pyglet.canvas.xlib.NoSuchDisplayException: Cannot connect to "None"
      - Set these params to docker
        - "docker run ... -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/dri --device /dev/snd ..."
    - Error: Visualization problem - https://github.com/devsisters/DQN-tensorflow/issues/35
      - pip install atari-py==0.0.21
    - Now the command runs OK

## Install - Sage (sage download is about 1.3 GB compressed and more than 4 GB when uncompressed)
- Note: Sage is needed by the python project that needs sage to make the embedding of a graph
- Read the installation info from here: http://www.sagemath.org/
  - ^D (return to the root user of your machine)
  - adduser sage
  - mkdir /sage
  - chown sage:sage /sage
  - su - sage
  - cd /sage
  - tar xvf <sage file name>.tar in . (sage needs, at least for now, the libgfortran3 ... so install it first from root)
    - ^D return to root
    - apt-get update
    - apt-get install build-essential
    - apt-get upgrade
    - apt-get install libgfortran3
  - ^D (return to the root user of your machine)
  - ln -s /sage /usr/local/bin/sage
  - cd /sage
  - ./sage to test it

## Download personal repo
- adduser <your_name>
- su - <your_name>
- mkdir prj
- cd prj (/home/<your_name>/prj)
- git clone https://github.com/stefanutti/maps-coloring-python.git

## Run 4ct.py
- su - <your_name>
- source ./prj/maps-coloring-python/set_environment.sh
- cd prj
- cd maps-coloring-python
- sage 4ct.py --help
- sage 4ct.py -r 100 (Random graph: dual of a triangulation of N vertices)
- other parameters
  - -i <file .edgelist> (Load a .edgelist file - networkx)
  - -p <file .serialized> (Load a .serialized planar embedding of the graph)
  - -o <file name without extension> (Save a .edgelist file (networkx), plus a .dot file (networkx)

Bye
