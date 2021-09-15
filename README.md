# clashBlock

## Source List
* Adaway 
 LAST UPDATE 15-9-21
 
> https://adaway.org/hosts.txt


* oisd LAST 
  UPDATE 15-9-21

  Rules count = 90174
> https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/hosts_light.txt


## HOW TO

### Adaway

* rule provider
```yaml
rule-providers:
  clashBlock_Adaway:
    type: http
    behavior: classical
    path: "./rule_provider/clashBlock_adaway.yaml"
    url: https://raw.githubusercontent.com/zzzt27/clashBlock/main/adaway.yaml
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,clashBlock_Adaway,REJECT
```

### oisd_light

* rule provider
```yaml
rule-providers:
  clashBlock_oisd_l:
    type: http
    behavior: classical
    path: "./rule_provider/clashBlock_oisd_l.yaml"
    url: https://raw.githubusercontent.com/zzzt27/clashBlock/main/oisd_light.yaml
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,clashBlock_oisd_l,REJECT
```
