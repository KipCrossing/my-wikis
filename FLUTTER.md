# Flutter

### Getting started

Install dependencies:

```
sudo apt install curl
```

Get flutter:

```
git clone https://github.com/flutter/flutter.git -b master
echo '#Add Flutter to PATH' >> $HOME/.bashrc
echo 'export PATH="$PATH:'$(pwd)'/flutter/bin"' >> $HOME/.bashrc
source $HOME/.bashrc
echo "Check the flutter is in path"
echo $PATH
flutter precache
echo "Check your dependencies:"
flutter doctor
```

Download and install [Android Studio](https://developer.android.com/studio) and install the Flutter plugin:

Run `flutter doctor` again to check dependencies.

#### For web dev:

```
flutter channel beta
flutter upgrade
flutter config --enable-web
```

Make sure you have Chrome installed

```
flutter devices
```

And Run `flutter run -d chrome` in the project dir.
