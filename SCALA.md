# SCALA

## Setup IDE

### Install openjdk-8-jdk

add in your sources.list

```
sudo nano /etc/apt/sources.list
```

following repo: deb <http://ftp.us.debian.org/debian> sid main then:

```
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

### Install IntelliJ IDEA

[Download IntelliJ IDEA](https://www.jetbrains.com/idea/)

```
sudo tar xzf ideaIC-2018.3.2.tar.gz -C /opt
cd /opt/ideaIC-2018.3.2.tar.gz/bin
./idea.sh
```

### Setup SCALA project

[Follow these instructions](https://docs.scala-lang.org/getting-started/intellij-track/getting-started-with-scala-in-intellij.html)

### Install SBT

```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt
```

## Syntax
