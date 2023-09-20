## The Convergence Protocol  (September 23)

### Procedures

First task is to dig something up that you think could be optimized. Once I can confirm that it's valid, we can move on to PR creation.

Go over contracts and check each variable initialization, functions, etc and see if any of those optimizable in terms of gas
compare it with what we are learning in the RareSkills Book of Gas Optimization

1. Announce that you found a new issue here in the chat. (Just one finding, even if you technically are already aware of more issues.)
2. Write a finding report about that finding.
3. Create a PR about it.
4. Have a review discussion with me via GitHub. (During this process, you can, of course, already look for more findings but
   *don't announce* them in the team chat just yet.)
5. Only once your PR is merged, then you are allowed to announce a new finding here in the chat and repeat the process.

Blocking you from taking credit for many findings in a very short amount of time

1. prevents you from "taking away" findings from other team members without much effort (i.e., writing the report) and
2. incentivises you to focus on report *quality* rather than *quantity*.

This will benefit you in the long run and also ensure that the team report's quality level doesn't fluctuate from finding to finding.

### Findings by Marco

- The "runs" parameter of the optimizer is set to 250 which is extremely considering that the current upper limit is 1000000. Low values of this parameter lead to cheaper deployment while large values prioritize runtime code-efficiency. There's of course a trade-off to be made, but at least the developers should consider playing around with this parameter. (It's likely that they haven't done that, yet.)
- Splitting a require statement that check a boolean AND (&&) expression into to separate require statements can save gas.
- Constants can be private to save gas during deployment.
- Version pragma should be specified precisely (not "floating" a la ^0.8.0, but rather 0.8.19). While this is more of a security finding, it's also gas relevant since 0.8.19 introduced some automatic gas optimizations.
- Preincrement (++i) is cheaper than postincrement (i++)
- There are numerous places in the codebase where storage variables aren't cached but where the same variable is read from contract storage multiple times within the same function. Reading from storage is very expensive, so whenever you read a variable from storage and you need it more than once during function execution, you should manually cache it and work with the cached value instead of reading from storage multiple times. Depending on how often this is done throughout the various contracts, this can save a ton of gas.

## Links

[Existing Tools](https://dreamlab.net/de/blog/post/smarts-contracts-security-tools-comparison-mythx-mythril-securify-v20-and-slither-1/)

[Repo for Convergence](https://github.com/Cvg-Finance/hats-audit)

