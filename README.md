# Ads Block by osid for clash

## Source List

### OISD
NAME | UPDATE | RULES COUNT
------------ | ------------- | -------------
[oisd_small](https://small.oisd.nl/domainswild) | **22-08-24** | 44182
[oisd_big](https://big.oisd.nl/domainswild) | **22-08-24** | 170137
[oisd_nsfw🔞](https://nsfw.oisd.nl/domainswild) | **22-08-24** | 378395


### ABPindo
NAME | UPDATE |
------------ | -------------
[ABPindo](https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/domain.txt) | **16-09-21** 

### [HAGEZI](https://github.com/hagezi/dns-blocklists)
| Version | Blocking<br>level | Blocking<br>type | UPDATE | RULES COUNT |
|:--------|:---------------|:--------------|:--------------|:--------------|
| :green_book:[Light](#light)| :green_book::green_book:| Relaxed | **16-09-21** | 90339
| :blue_book:[Normal](#normal)       | :blue_book::blue_book::blue_book:                                                           | Relaxed/Balanced    |
| :ledger:[Pro](#pro)                | :ledger::ledger::ledger::ledger:                                                            | Balanced            |
| :orange_book:[Pro++](#proplus)     | :orange_book::orange_book::orange_book::orange_book::orange_book::orange_book:              | Balanced/Aggressive |
| :closed_book:[Ultimate](#ultimate) | :closed_book::closed_book::closed_book::closed_book::closed_book::closed_book::closed_book: | Aggressive |

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

## Source

https://oisd.nl/

Source List
[oisd_small](https://small.oisd.nl/domainswild) 
[oisd_big](https://big.oisd.nl/domainswild)
[oisd_nsfw🔞](https://nsfw.oisd.nl/domainswild) 

