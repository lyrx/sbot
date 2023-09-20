from fileutils import findpaths

paths = findpaths('/Users/alex/git/Web3Academy/hats-audit/contracts', '.sol')

for path in paths:
    print(path)
