#!/usr/bin/python
# 
# v2.0 fixed error with perl scripts; added applescript support
# v2.1 fixed error if no selection; now just inserts a comment marker in the text
# v2.2 Added commments and started added html support
#
# -- PB User Script Info --
# %%%{PBXName=Un/Commenter Python}%%%
# %%%{PBXInput=AllText}%%%
# %%%{PBXOutput=ReplaceSelection}%%%
# %%%{PBXKeyEquivalent=@/}%%%

import os, re, sys

def main():
    start = %%%{PBXSelectionStart}%%%
    finish = %%%{PBXSelectionEnd}%%%
#    sys.stderr.write("start: %s\nfinish: %s\n" % (start, finish))
    # stdin has AllText
    # need to get this even if no selection otherwise XCode quits!
    inputLines = sys.stdin.readlines()
    firstLine = inputLines[0]
    text = "".join(inputLines)
    selection = text[start:finish]
   
    # Commment styles
    # Applescript comment
    aComment = r'--'
    # Python and Perl comment
    pComment = r'#'
    # C comment
    cComment = r'//'
    # HTML comment: not implemented
    hOpenCommment = r'<!--'
    hCloseCommment = r'-->'
    commentString = cComment
    # test using filename suffix
    filename = r"%%%{PBXFilePath}%%%"
    fileNameRegex = re.compile(r".*(?P<suffix>py|pl|sh|applescript)$", re.VERBOSE | re.IGNORECASE)
    match = fileNameRegex.search(filename)
    if match:
        # will match shell to default
        suffix = match.group('suffix')
        if suffix == "py" or suffix == "pl":
            commentString = pComment
        elif suffix == "applescript":
            commentString = aComment
    else:
        # determine the type of file we have by looking for the #! line at the top
        # careful--it might already be commented out!
        # test first line
        allTextRegex = re.compile(r"""
         ^([#]|//)*                 # it may be commented out
         \s*.*                      # whitespace
         (?P<script>python|perl|sh) # look for shell
         .*                         # following characters
         """, re.VERBOSE) # | re.IGNORECASE)
        match = allTextRegex.search(firstLine)
        if match:
            script = match.group('script')
            if script == "python" or script == "perl":
                commentString = pComment

    lines = selection.splitlines()
    if lines:
        # add or remove comment markers depending on the state of the first line of the selection
        # if it is uncommented, comment all lines.  If it is commented, remove comment markers, if present
        commentRegex = re.compile(r"^[" + commentString + r"]+(?P<text>.*)$")
        commentStringPresent = commentRegex.match(lines[0])
        
        for i in range(len(lines)):
            line = lines[i]
            if commentStringPresent:
                # remove comment markers
                m = commentRegex.match(line)
                if m:
                    if commentStringPresent:
                        lines[i] = m.group('text')
                    else:
                        lines[i] = commentString + line
            else:
                # prefix with comment
                lines[i] = commentString + line
        replacement = os.linesep.join(lines)
    else:
        replacement = commentString
    output = "%s%s%s" % (r"%%%{PBXSelection}%%%", replacement, r"%%%{PBXSelection}%%%")
    if selection and (selection[-1] == os.linesep):
        output = output + os.linesep
    sys.stdout.write(output)

# main area
if __name__ == "__main__":
    main()
