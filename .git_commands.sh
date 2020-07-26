#!/bin/bash

function create(){
    source .env
    python create.py $1
    cd
    cd $PROJECT_FOLDER
    mkdir $1
    cd $1
    git init
    touch README.md
    git add .
    git commit -m "first commit"
    git remote add origin https://github.com/navneetsn18/$1.git
    git push -u origin master
    code .
    echo "Repo created on Github and System..."
}

function upload(){
    source .env
    python create.py $1
    cd
    cd $PROJECT_FOLDER
    cd $1
    git add .
    git commit -m "New Updates"
    git remote add origin https://github.com/navneetsn18/$1.git
    git push -u origin master
    code .
    echo "Repo created on Github and System..."
}

function remove(){
    python remove.py $1
    echo "Repo Deleted From Github.."
}
