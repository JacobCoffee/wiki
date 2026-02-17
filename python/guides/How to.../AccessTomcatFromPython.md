# How to.../AccessTomcatFromPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

How to store the variables, \"HSstatsValue\[i\]\" below?? The syntax is wrong, what is the actual syntax to store the variable or value???

                for i in range(countTill):
                    #print "cntTrack=", cntTrack
                    s1 = re.compile(r"\d+").findall(lines[cntTrack+i+1])
                    #print "s1=", s1
                    #print "lines[cntTrack+i+1]=", cntTrack+i+1
                    #oPutFile.write(stats[i])
                    #print stats[i],
                    #oPutFile.write('\t')
                    if len(s1) == 1:
                        #print s1[0]+ '\n'
                        HSstatsValue[i]=s1[0]
                        #print "HSstatsValue[i]=", HSstatsValue[i]
                        oPutFile.write(s1[0])
                        oPutFile.write('\t')
                    elif len(s1) > 1:
                        for x in range(len(s1)):
                            zum = zum + int(s1[x])
                            HSstatsValue[i]=s1[0]

                        oPutFile.write(str(zum))
                        #print zum
                        #oPutFile.write('\t')
                        oPutFile.write('\t')
                    zum = 0
