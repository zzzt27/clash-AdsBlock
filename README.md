# clashBlock

## Source List

NAME | UPDATE | RULES COUNT
------------ | ------------- | -------------
[oisd_small](https://small.oisd.nl/domainswild) | -- | --
[oisd_big](https://big.oisd.nl/domainswild) | -- | --
[oisd_nsfw🔞](https://nsfw.oisd.nl/domainswild) | -- | --

## HOW TO

### oisd_small

* rule provider
```yaml
rule-providers:
  oisd_light:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_light.txt"
    url: https://small.oisd.nl/domainswild
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_small,REJECT
```

### oisd_big

* rule provider
```yaml
rule-providers:
  oisd_big:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_big.txt"
    url: https://big.oisd.nl/domainswild
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_big,REJECT
```

### oisd_nsfw🔞

* rule provider
```yaml
rule-providers:
  oisd_nsfw🔞:
    type: http
    behavior: domain
    format: text
    path: "./rule_provider/oisd_nsfw.txt"
    url: https://nsfw.oisd.nl/domainswild
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,oisd_nsfw🔞,REJECT
```
