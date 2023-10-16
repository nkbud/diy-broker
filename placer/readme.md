# Placer

What information and behaviors are sufficient for placing orders?


## The minimum?


| variable     | example        |
|--------------|----------------|
| **ticker**   | AAPL, SPY, ... |

Let's explore the possibility of *that* being sufficient information.

Our Placer can fill in the remaining details by querying our current state + default values.

| Variable | Question                       | RESULT                     | non-default options, ignored       |
|----------|--------------------------------|----------------------------|------------------------------------|
| action   | account has existing position? | yes: exit. <br> no: enter. |                                    |
| position |                                | long                       | short                              |
| price    |                                | market                     | $(limit price)                     |
| amount   |                                | 100%                       | (available)%, $(dollars), (shares) |
| lifetime |                                | day                        | extended, indefinite               |

Resulting in 2 possible orders:
``` 
{
  "ticker": "SPY",
  "action": "enter" | "exit",
  "position": "long",
  "price": "market",
  "amount": "100%"  
}
```

Are these useful behaviors to support? 
- exiting 100% of a long position immediately at market value
- entering a long position at 100% of available cash immediately at market value

I think so. 

But these optional overrides seem to be worth the trouble:

## More?

Which complexities are we pursuing?

| Variable | Baseline Support               | Roadmap |
|----------|--------------------------------|---------|
| ticker   |                                |         |
| action   | account has existing position? |         |                               
| position |                                |         |
| price    |                                |         |
| amount   |                                |         |

And metrics. Keeping track of activity.

## Most?

Which complexities are not being pursued, yet or ever?
- other order types: stop, stop-limit, bracket
- crypto
- margin






