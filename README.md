# clashBlock

## Source List
* Adaway
> https://adaway.org/hosts.txt
* oisd
> https://raw.githubusercontent.com/ookangzheng/dbl-oisd-nl/master/hosts_light.txt


## HOW TO

### Adaway

* rule provider
```yaml
rule-providers:
  Adaway:
    type: http
    behavior: classical
    path: "./rule_provider/Unbreak.yaml"
    url: https://raw.githubusercontent.com/DivineEngine/Profiles/master/Clash/RuleSet/Unbreak.yaml
    interval: 86400
```

* rules
```yaml
rules:
  - RULE-SET,Adaway,REJECT
```
