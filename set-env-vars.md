Use `/etc/environment` file for setting the environment variables. Then add the following line inside the /etc/environment file.

```
ABC="123"
```

Now the ABC variable will be accessible from all the user sessions. To test the variable output first refresh the environment variable using command

```
source /etc/environment
```

and run `echo $ABC`.
