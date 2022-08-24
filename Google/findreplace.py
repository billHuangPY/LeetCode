class Solution:
    def findReplaceString(self, s: str, indices, sources, targets) -> str:
        slist = [*s]
        for i, idx in enumerate(indices):
            source = "".join(slist[idx:idx+len(sources[i])])
            if not source == sources[i]:
                continue
            slist = slist[:idx] + [targets[i]] + \
                [""]*(len(sources[i])-1) + slist[idx+len(sources[i]):]
        return "".join(slist)