Add env vars then run command

```
docker exec -i CONTAINER_ID /bin/bash -c "export VAR1=VAL1 && export VAR2=VAL2 && your_cmd"
```