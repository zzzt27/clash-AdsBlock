# AdBlock Rules for Mihomo

## Source List

### [OISD](https://oisd.nl/)
NAME | UPDATE | RULES COUNT |
------------ | ------------- | ------------- |
[oisd_small](#small) | **05-07-25** | 41897
[oisd_big](#big) | **05-07-25** | 196784
[oisd_nsfw🔞](#nsfw) | **05-07-25** | 418193
[oisd_nsfw_small🔞](#nsfw-small) | **05-07-25** | 20908


### [ABPindo](https://github.com/ABPindo/indonesianadblockrules)
NAME | UPDATE | RULES COUNT |
------------ | ------------- | ------------- |
[ABPindo](#indo) | **05-07-25** | 135

## HOW TO

### oisd_small <a name="small"></a>

* rule provider
```yaml
rule-providers:
  oisd_small:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_small.txt"
    url: https://raw.githubusercontent.com/zzzt27/clash-AdsBlock/main/oisd_small.txt
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_small,REJECT
```

### oisd_big <a name="big"></a>

* rule provider
```yaml
rule-providers:
  oisd_big:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_big.txt"
    url: https://raw.githubusercontent.com/zzzt27/clash-AdsBlock/main/oisd_big.txt
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_big,REJECT
```

### oisd_nsfw🔞 <a name="nsfw"></a>

* rule provider
```yaml
rule-providers:
  oisd_nsfw🔞:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_nsfw.txt"
    url: https://raw.githubusercontent.com/zzzt27/clash-AdsBlock/main/oisd_nsfw.txt
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_nsfw🔞,REJECT
```

### oisd_nsfw_small🔞 <a name="nsfw-small"></a>

* rule provider
```yaml
rule-providers:
  oisd_nsfw_small🔞:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_nsfw_small.txt"
    url: https://raw.githubusercontent.com/zzzt27/clash-AdsBlock/main/oisd_nsfw_small.txt
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_nsfw_small🔞,REJECT
```

### ABPindo <a name="indo"></a>

* rule provider
```yaml
rule-providers:
  ABPindo:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/ABPindo.txt"
    url: https://raw.githubusercontent.com/zzzt27/clash-AdsBlock/main/ABPindo.txt
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,ABPindo,REJECT
```
