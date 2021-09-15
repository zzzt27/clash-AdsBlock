# clashBlock

## Source List

NAME | LINK | UPDATE | RULES COUNT
------------ | ------------- | ------------- | -------------
[Adaway](https://adaway.org/) | https://adaway.org/hosts.txt | **15-09-21** | -
[oisd](https://oisd.nl/) | https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/hosts_light.txt | **15-09-21** | 90174

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
