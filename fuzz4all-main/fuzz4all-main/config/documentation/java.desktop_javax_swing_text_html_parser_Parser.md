# Class Parser

**Source:** `java.desktop\javax\swing\text\html\parser\Parser.html`

### Class Description

```java
public class
Parser

extends
Object

implements
DTDConstants
```

A simple DTD-driven HTML parser. The parser reads an
HTML file from an InputStream and calls various methods
(which should be overridden in a subclass) when tags and
data are encountered.

Unfortunately there are many badly implemented HTML parsers
out there, and as a result there are many badly formatted
HTML files. This parser attempts to parse most HTML files.
This means that the implementation sometimes deviates from
the SGML specification in favor of HTML.

The parser treats \r and \r\n as \n. Newlines after starttags
and before end tags are ignored just as specified in the SGML/HTML
specification.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

**All Implemented Interfaces:** DTDConstants

---

### Field Details

#### protected
DTD
dtd

The dtd.

---

#### protected boolean strict

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility. If false, it will be lenient
with certain common classes of erroneous HTML constructs.
Strict or not, in either case an error will be recorded.

---

### Constructor Details

#### public Parser​(
DTD
dtd)

Creates parser with the specified

dtd

.

**Parameters:**
- dtd

- the dtd.

---

### Method Details

#### protected int getCurrentLine()

**Returns:**
- the line number of the line currently being parsed

---

#### protected
TagElement
makeTag​(
Element
elem,
boolean fictional)

Makes a TagElement.

**Parameters:**
- elem

- the element storing the tag definition
- fictional

- the value of the flag "

fictional

" to be set for the tag

**Returns:**
- the created

TagElement

---

#### protected
TagElement
makeTag​(
Element
elem)

Makes a TagElement.

**Parameters:**
- elem

- the element storing the tag definition

**Returns:**
- the created

TagElement

---

#### protected
SimpleAttributeSet
getAttributes()

Returns attributes for the current tag.

**Returns:**
- SimpleAttributeSet

containing the attributes

---

#### protected void flushAttributes()

Removes the current attributes.

---

#### protected void handleText​(char[] text)

Called when PCDATA is encountered.

**Parameters:**
- text

- the section text

---

#### protected void handleTitle​(char[] text)

Called when an HTML title tag is encountered.

**Parameters:**
- text

- the title text

---

#### protected void handleComment​(char[] text)

Called when an HTML comment is encountered.

**Parameters:**
- text

- the comment being handled

---

#### protected void handleEOFInComment()

Called when the content terminates without closing the HTML comment.

---

#### protected void handleEmptyTag​(
TagElement
tag)
throws
ChangedCharSetException

Called when an empty tag is encountered.

**Parameters:**
- tag

- the tag being handled

**Throws:**
- ChangedCharSetException

- if the document charset was changed

---

#### protected void handleStartTag​(
TagElement
tag)

Called when a start tag is encountered.

**Parameters:**
- tag

- the tag being handled

---

#### protected void handleEndTag​(
TagElement
tag)

Called when an end tag is encountered.

**Parameters:**
- tag

- the tag being handled

---

#### protected void handleError​(int ln,

String
msg)

An error has occurred.

**Parameters:**
- ln

- the number of line containing the error
- msg

- the error message

---

#### protected void error​(
String
err,

String
arg1,

String
arg2,

String
arg3)

Invokes the error handler.

**Parameters:**
- err

- the error type
- arg1

- the 1st error message argument
- arg2

- the 2nd error message argument
- arg3

- the 3rd error message argument

---

#### protected void error​(
String
err,

String
arg1,

String
arg2)

Invokes the error handler with the 3rd error message argument "?".

**Parameters:**
- err

- the error type
- arg1

- the 1st error message argument
- arg2

- the 2nd error message argument

---

#### protected void error​(
String
err,

String
arg1)

Invokes the error handler with the 2nd and 3rd error message argument "?".

**Parameters:**
- err

- the error type
- arg1

- the 1st error message argument

---

#### protected void error​(
String
err)

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

**Parameters:**
- err

- the error type

---

#### protected void startTag​(
TagElement
tag)
throws
ChangedCharSetException

Handle a start tag. The new tag is pushed
onto the tag stack. The attribute list is
checked for required attributes.

**Parameters:**
- tag

- the tag

**Throws:**
- ChangedCharSetException

- if the document charset was changed

---

#### protected void endTag​(boolean omitted)

Handle an end tag. The end tag is popped
from the tag stack.

**Parameters:**
- omitted

-

true

if the tag is no actually present in the
document, but is supposed by the parser

---

#### protected void markFirstTime​(
Element
elem)

Marks the first time a tag has been seen in a document

**Parameters:**
- elem

- the element represented by the tag

---

#### public
String
parseDTDMarkup()
throws
IOException

Parses the Document Type Declaration markup declaration.
Currently ignores it.

**Returns:**
- the string representation of the markup declaration

**Throws:**
- IOException

- if an I/O error occurs

---

#### protected boolean parseMarkupDeclarations​(
StringBuffer
strBuff)
throws
IOException

Parse markup declarations.
Currently only handles the Document Type Declaration markup.
Returns true if it is a markup declaration false otherwise.

**Parameters:**
- strBuff

- the markup declaration

**Returns:**
- true

if this is a valid markup declaration;
otherwise

false

**Throws:**
- IOException

- if an I/O error occurs

---

#### public void parse​(
Reader
in)
throws
IOException

Parse an HTML stream, given a DTD.

**Parameters:**
- in

- the reader to read the source from

**Throws:**
- IOException

- if an I/O error occurs

---

#### protected int getCurrentPos()

Returns the current position.

**Returns:**
- the current position

---

### Additional Sections

#### Class Parser

java.lang.Object

- javax.swing.text.html.parser.Parser

javax.swing.text.html.parser.Parser

**All Implemented Interfaces:** DTDConstants

**Direct Known Subclasses:** DocumentParser

```java
public class
Parser

extends
Object

implements
DTDConstants
```

A simple DTD-driven HTML parser. The parser reads an
HTML file from an InputStream and calls various methods
(which should be overridden in a subclass) when tags and
data are encountered.

Unfortunately there are many badly implemented HTML parsers
out there, and as a result there are many badly formatted
HTML files. This parser attempts to parse most HTML files.
This means that the implementation sometimes deviates from
the SGML specification in favor of HTML.

The parser treats \r and \r\n as \n. Newlines after starttags
and before end tags are ignored just as specified in the SGML/HTML
specification.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

**See Also:** DTD

,

TagElement

,

SimpleAttributeSet

public class

Parser

extends

Object

implements

DTDConstants

A simple DTD-driven HTML parser. The parser reads an
HTML file from an InputStream and calls various methods
(which should be overridden in a subclass) when tags and
data are encountered.

Unfortunately there are many badly implemented HTML parsers
out there, and as a result there are many badly formatted
HTML files. This parser attempts to parse most HTML files.
This means that the implementation sometimes deviates from
the SGML specification in favor of HTML.

The parser treats \r and \r\n as \n. Newlines after starttags
and before end tags are ignored just as specified in the SGML/HTML
specification.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

Unfortunately there are many badly implemented HTML parsers
out there, and as a result there are many badly formatted
HTML files. This parser attempts to parse most HTML files.
This means that the implementation sometimes deviates from
the SGML specification in favor of HTML.

The parser treats \r and \r\n as \n. Newlines after starttags
and before end tags are ignored just as specified in the SGML/HTML
specification.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

The parser treats \r and \r\n as \n. Newlines after starttags
and before end tags are ignored just as specified in the SGML/HTML
specification.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

The html spec does not specify how spaces are to be coalesced very well.
Specifically, the following scenarios are not discussed (note that a
space should be used here, but I am using &nbsp to force the space to
be displayed):

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

'<b>blah <i> <strike> foo' which can be treated as:
'<b>blah <i><strike>foo'

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

as well as:
'<p><a href="xx"> <em>Using</em></a></p>'
which appears to be treated as:
'<p><a href="xx"><em>Using</em></a></p>'

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

If

strict

is false, when a tag that breaks flow,
(

TagElement.breaksFlows

) or trailing whitespace is
encountered, all whitespace will be ignored until a non whitespace
character is encountered. This appears to give behavior closer to
the popular browsers.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

DTD

dtd

The dtd.

protected boolean

strict

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility.

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Parser

​(

DTD

dtd)

Creates parser with the specified

dtd

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

endTag

​(boolean omitted)

Handle an end tag.

protected void

error

​(

String

err)

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1)

Invokes the error handler with the 2nd and 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1,

String

arg2)

Invokes the error handler with the 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1,

String

arg2,

String

arg3)

Invokes the error handler.

protected void

flushAttributes

()

Removes the current attributes.

protected

SimpleAttributeSet

getAttributes

()

Returns attributes for the current tag.

protected int

getCurrentLine

()

protected int

getCurrentPos

()

Returns the current position.

protected void

handleComment

​(char[] text)

Called when an HTML comment is encountered.

protected void

handleEmptyTag

​(

TagElement

tag)

Called when an empty tag is encountered.

protected void

handleEndTag

​(

TagElement

tag)

Called when an end tag is encountered.

protected void

handleEOFInComment

()

Called when the content terminates without closing the HTML comment.

protected void

handleError

​(int ln,

String

msg)

An error has occurred.

protected void

handleStartTag

​(

TagElement

tag)

Called when a start tag is encountered.

protected void

handleText

​(char[] text)

Called when PCDATA is encountered.

protected void

handleTitle

​(char[] text)

Called when an HTML title tag is encountered.

protected

TagElement

makeTag

​(

Element

elem)

Makes a TagElement.

protected

TagElement

makeTag

​(

Element

elem,
boolean fictional)

Makes a TagElement.

protected void

markFirstTime

​(

Element

elem)

Marks the first time a tag has been seen in a document

void

parse

​(

Reader

in)

Parse an HTML stream, given a DTD.

String

parseDTDMarkup

()

Parses the Document Type Declaration markup declaration.

protected boolean

parseMarkupDeclarations

​(

StringBuffer

strBuff)

Parse markup declarations.

protected void

startTag

​(

TagElement

tag)

Handle a start tag.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected

DTD

dtd

The dtd.

protected boolean

strict

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility.

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Field Summary

The dtd.

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility.

Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Fields declared in interface javax.swing.text.html.parser. DTDConstants

Constructor Summary

Constructors

Constructor

Description

Parser

​(

DTD

dtd)

Creates parser with the specified

dtd

.

---

#### Constructor Summary

Creates parser with the specified

dtd

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

endTag

​(boolean omitted)

Handle an end tag.

protected void

error

​(

String

err)

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1)

Invokes the error handler with the 2nd and 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1,

String

arg2)

Invokes the error handler with the 3rd error message argument "?".

protected void

error

​(

String

err,

String

arg1,

String

arg2,

String

arg3)

Invokes the error handler.

protected void

flushAttributes

()

Removes the current attributes.

protected

SimpleAttributeSet

getAttributes

()

Returns attributes for the current tag.

protected int

getCurrentLine

()

protected int

getCurrentPos

()

Returns the current position.

protected void

handleComment

​(char[] text)

Called when an HTML comment is encountered.

protected void

handleEmptyTag

​(

TagElement

tag)

Called when an empty tag is encountered.

protected void

handleEndTag

​(

TagElement

tag)

Called when an end tag is encountered.

protected void

handleEOFInComment

()

Called when the content terminates without closing the HTML comment.

protected void

handleError

​(int ln,

String

msg)

An error has occurred.

protected void

handleStartTag

​(

TagElement

tag)

Called when a start tag is encountered.

protected void

handleText

​(char[] text)

Called when PCDATA is encountered.

protected void

handleTitle

​(char[] text)

Called when an HTML title tag is encountered.

protected

TagElement

makeTag

​(

Element

elem)

Makes a TagElement.

protected

TagElement

makeTag

​(

Element

elem,
boolean fictional)

Makes a TagElement.

protected void

markFirstTime

​(

Element

elem)

Marks the first time a tag has been seen in a document

void

parse

​(

Reader

in)

Parse an HTML stream, given a DTD.

String

parseDTDMarkup

()

Parses the Document Type Declaration markup declaration.

protected boolean

parseMarkupDeclarations

​(

StringBuffer

strBuff)

Parse markup declarations.

protected void

startTag

​(

TagElement

tag)

Handle a start tag.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Handle an end tag.

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

Invokes the error handler with the 2nd and 3rd error message argument "?".

Invokes the error handler with the 3rd error message argument "?".

Invokes the error handler.

Removes the current attributes.

Returns attributes for the current tag.

Returns the current position.

Called when an HTML comment is encountered.

Called when an empty tag is encountered.

Called when an end tag is encountered.

Called when the content terminates without closing the HTML comment.

An error has occurred.

Called when a start tag is encountered.

Called when PCDATA is encountered.

Called when an HTML title tag is encountered.

Makes a TagElement.

Marks the first time a tag has been seen in a document

Parse an HTML stream, given a DTD.

Parses the Document Type Declaration markup declaration.

Parse markup declarations.

Handle a start tag.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- dtd

```java
protected
DTD
dtd
```

The dtd.

- strict

```java
protected boolean strict
```

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility. If false, it will be lenient
with certain common classes of erroneous HTML constructs.
Strict or not, in either case an error will be recorded.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Parser

```java
public Parser​(
DTD
dtd)
```

Creates parser with the specified

dtd

.

**Parameters:** dtd

- the dtd.

============ METHOD DETAIL ==========

- Method Detail

- getCurrentLine

```java
protected int getCurrentLine()
```

**Returns:** the line number of the line currently being parsed

- makeTag

```java
protected
TagElement
makeTag​(
Element
elem,
boolean fictional)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Parameters:** fictional

- the value of the flag "

fictional

" to be set for the tag
**Returns:** the created

TagElement

- makeTag

```java
protected
TagElement
makeTag​(
Element
elem)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Returns:** the created

TagElement

- getAttributes

```java
protected
SimpleAttributeSet
getAttributes()
```

Returns attributes for the current tag.

**Returns:** SimpleAttributeSet

containing the attributes

- flushAttributes

```java
protected void flushAttributes()
```

Removes the current attributes.

- handleText

```java
protected void handleText​(char[] text)
```

Called when PCDATA is encountered.

**Parameters:** text

- the section text

- handleTitle

```java
protected void handleTitle​(char[] text)
```

Called when an HTML title tag is encountered.

**Parameters:** text

- the title text

- handleComment

```java
protected void handleComment​(char[] text)
```

Called when an HTML comment is encountered.

**Parameters:** text

- the comment being handled

- handleEOFInComment

```java
protected void handleEOFInComment()
```

Called when the content terminates without closing the HTML comment.

- handleEmptyTag

```java
protected void handleEmptyTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Called when an empty tag is encountered.

**Parameters:** tag

- the tag being handled
**Throws:** ChangedCharSetException

- if the document charset was changed

- handleStartTag

```java
protected void handleStartTag​(
TagElement
tag)
```

Called when a start tag is encountered.

**Parameters:** tag

- the tag being handled

- handleEndTag

```java
protected void handleEndTag​(
TagElement
tag)
```

Called when an end tag is encountered.

**Parameters:** tag

- the tag being handled

- handleError

```java
protected void handleError​(int ln,

String
msg)
```

An error has occurred.

**Parameters:** ln

- the number of line containing the error
**Parameters:** msg

- the error message

- error

```java
protected void error​(
String
err,

String
arg1,

String
arg2,

String
arg3)
```

Invokes the error handler.

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument
**Parameters:** arg3

- the 3rd error message argument

- error

```java
protected void error​(
String
err,

String
arg1,

String
arg2)
```

Invokes the error handler with the 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument

- error

```java
protected void error​(
String
err,

String
arg1)
```

Invokes the error handler with the 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument

- error

```java
protected void error​(
String
err)
```

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type

- startTag

```java
protected void startTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Handle a start tag. The new tag is pushed
onto the tag stack. The attribute list is
checked for required attributes.

**Parameters:** tag

- the tag
**Throws:** ChangedCharSetException

- if the document charset was changed

- endTag

```java
protected void endTag​(boolean omitted)
```

Handle an end tag. The end tag is popped
from the tag stack.

**Parameters:** omitted

-

true

if the tag is no actually present in the
document, but is supposed by the parser

- markFirstTime

```java
protected void markFirstTime​(
Element
elem)
```

Marks the first time a tag has been seen in a document

**Parameters:** elem

- the element represented by the tag

- parseDTDMarkup

```java
public
String
parseDTDMarkup()
throws
IOException
```

Parses the Document Type Declaration markup declaration.
Currently ignores it.

**Returns:** the string representation of the markup declaration
**Throws:** IOException

- if an I/O error occurs

- parseMarkupDeclarations

```java
protected boolean parseMarkupDeclarations​(
StringBuffer
strBuff)
throws
IOException
```

Parse markup declarations.
Currently only handles the Document Type Declaration markup.
Returns true if it is a markup declaration false otherwise.

**Parameters:** strBuff

- the markup declaration
**Returns:** true

if this is a valid markup declaration;
otherwise

false
**Throws:** IOException

- if an I/O error occurs

- parse

```java
public void parse​(
Reader
in)
throws
IOException
```

Parse an HTML stream, given a DTD.

**Parameters:** in

- the reader to read the source from
**Throws:** IOException

- if an I/O error occurs

- getCurrentPos

```java
protected int getCurrentPos()
```

Returns the current position.

**Returns:** the current position

Field Detail

- dtd

```java
protected
DTD
dtd
```

The dtd.

- strict

```java
protected boolean strict
```

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility. If false, it will be lenient
with certain common classes of erroneous HTML constructs.
Strict or not, in either case an error will be recorded.

---

#### Field Detail

dtd

```java
protected
DTD
dtd
```

The dtd.

---

#### dtd

protected

DTD

dtd

The dtd.

strict

```java
protected boolean strict
```

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility. If false, it will be lenient
with certain common classes of erroneous HTML constructs.
Strict or not, in either case an error will be recorded.

---

#### strict

protected boolean strict

This flag determines whether or not the Parser will be strict
in enforcing SGML compatibility. If false, it will be lenient
with certain common classes of erroneous HTML constructs.
Strict or not, in either case an error will be recorded.

Constructor Detail

- Parser

```java
public Parser​(
DTD
dtd)
```

Creates parser with the specified

dtd

.

**Parameters:** dtd

- the dtd.

---

#### Constructor Detail

Parser

```java
public Parser​(
DTD
dtd)
```

Creates parser with the specified

dtd

.

**Parameters:** dtd

- the dtd.

---

#### Parser

public Parser​(

DTD

dtd)

Creates parser with the specified

dtd

.

Method Detail

- getCurrentLine

```java
protected int getCurrentLine()
```

**Returns:** the line number of the line currently being parsed

- makeTag

```java
protected
TagElement
makeTag​(
Element
elem,
boolean fictional)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Parameters:** fictional

- the value of the flag "

fictional

" to be set for the tag
**Returns:** the created

TagElement

- makeTag

```java
protected
TagElement
makeTag​(
Element
elem)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Returns:** the created

TagElement

- getAttributes

```java
protected
SimpleAttributeSet
getAttributes()
```

Returns attributes for the current tag.

**Returns:** SimpleAttributeSet

containing the attributes

- flushAttributes

```java
protected void flushAttributes()
```

Removes the current attributes.

- handleText

```java
protected void handleText​(char[] text)
```

Called when PCDATA is encountered.

**Parameters:** text

- the section text

- handleTitle

```java
protected void handleTitle​(char[] text)
```

Called when an HTML title tag is encountered.

**Parameters:** text

- the title text

- handleComment

```java
protected void handleComment​(char[] text)
```

Called when an HTML comment is encountered.

**Parameters:** text

- the comment being handled

- handleEOFInComment

```java
protected void handleEOFInComment()
```

Called when the content terminates without closing the HTML comment.

- handleEmptyTag

```java
protected void handleEmptyTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Called when an empty tag is encountered.

**Parameters:** tag

- the tag being handled
**Throws:** ChangedCharSetException

- if the document charset was changed

- handleStartTag

```java
protected void handleStartTag​(
TagElement
tag)
```

Called when a start tag is encountered.

**Parameters:** tag

- the tag being handled

- handleEndTag

```java
protected void handleEndTag​(
TagElement
tag)
```

Called when an end tag is encountered.

**Parameters:** tag

- the tag being handled

- handleError

```java
protected void handleError​(int ln,

String
msg)
```

An error has occurred.

**Parameters:** ln

- the number of line containing the error
**Parameters:** msg

- the error message

- error

```java
protected void error​(
String
err,

String
arg1,

String
arg2,

String
arg3)
```

Invokes the error handler.

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument
**Parameters:** arg3

- the 3rd error message argument

- error

```java
protected void error​(
String
err,

String
arg1,

String
arg2)
```

Invokes the error handler with the 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument

- error

```java
protected void error​(
String
err,

String
arg1)
```

Invokes the error handler with the 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument

- error

```java
protected void error​(
String
err)
```

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type

- startTag

```java
protected void startTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Handle a start tag. The new tag is pushed
onto the tag stack. The attribute list is
checked for required attributes.

**Parameters:** tag

- the tag
**Throws:** ChangedCharSetException

- if the document charset was changed

- endTag

```java
protected void endTag​(boolean omitted)
```

Handle an end tag. The end tag is popped
from the tag stack.

**Parameters:** omitted

-

true

if the tag is no actually present in the
document, but is supposed by the parser

- markFirstTime

```java
protected void markFirstTime​(
Element
elem)
```

Marks the first time a tag has been seen in a document

**Parameters:** elem

- the element represented by the tag

- parseDTDMarkup

```java
public
String
parseDTDMarkup()
throws
IOException
```

Parses the Document Type Declaration markup declaration.
Currently ignores it.

**Returns:** the string representation of the markup declaration
**Throws:** IOException

- if an I/O error occurs

- parseMarkupDeclarations

```java
protected boolean parseMarkupDeclarations​(
StringBuffer
strBuff)
throws
IOException
```

Parse markup declarations.
Currently only handles the Document Type Declaration markup.
Returns true if it is a markup declaration false otherwise.

**Parameters:** strBuff

- the markup declaration
**Returns:** true

if this is a valid markup declaration;
otherwise

false
**Throws:** IOException

- if an I/O error occurs

- parse

```java
public void parse​(
Reader
in)
throws
IOException
```

Parse an HTML stream, given a DTD.

**Parameters:** in

- the reader to read the source from
**Throws:** IOException

- if an I/O error occurs

- getCurrentPos

```java
protected int getCurrentPos()
```

Returns the current position.

**Returns:** the current position

---

#### Method Detail

getCurrentLine

```java
protected int getCurrentLine()
```

**Returns:** the line number of the line currently being parsed

---

#### getCurrentLine

protected int getCurrentLine()

makeTag

```java
protected
TagElement
makeTag​(
Element
elem,
boolean fictional)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Parameters:** fictional

- the value of the flag "

fictional

" to be set for the tag
**Returns:** the created

TagElement

---

#### makeTag

protected

TagElement

makeTag​(

Element

elem,
boolean fictional)

Makes a TagElement.

makeTag

```java
protected
TagElement
makeTag​(
Element
elem)
```

Makes a TagElement.

**Parameters:** elem

- the element storing the tag definition
**Returns:** the created

TagElement

---

#### makeTag

protected

TagElement

makeTag​(

Element

elem)

Makes a TagElement.

getAttributes

```java
protected
SimpleAttributeSet
getAttributes()
```

Returns attributes for the current tag.

**Returns:** SimpleAttributeSet

containing the attributes

---

#### getAttributes

protected

SimpleAttributeSet

getAttributes()

Returns attributes for the current tag.

flushAttributes

```java
protected void flushAttributes()
```

Removes the current attributes.

---

#### flushAttributes

protected void flushAttributes()

Removes the current attributes.

handleText

```java
protected void handleText​(char[] text)
```

Called when PCDATA is encountered.

**Parameters:** text

- the section text

---

#### handleText

protected void handleText​(char[] text)

Called when PCDATA is encountered.

handleTitle

```java
protected void handleTitle​(char[] text)
```

Called when an HTML title tag is encountered.

**Parameters:** text

- the title text

---

#### handleTitle

protected void handleTitle​(char[] text)

Called when an HTML title tag is encountered.

handleComment

```java
protected void handleComment​(char[] text)
```

Called when an HTML comment is encountered.

**Parameters:** text

- the comment being handled

---

#### handleComment

protected void handleComment​(char[] text)

Called when an HTML comment is encountered.

handleEOFInComment

```java
protected void handleEOFInComment()
```

Called when the content terminates without closing the HTML comment.

---

#### handleEOFInComment

protected void handleEOFInComment()

Called when the content terminates without closing the HTML comment.

handleEmptyTag

```java
protected void handleEmptyTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Called when an empty tag is encountered.

**Parameters:** tag

- the tag being handled
**Throws:** ChangedCharSetException

- if the document charset was changed

---

#### handleEmptyTag

protected void handleEmptyTag​(

TagElement

tag)
throws

ChangedCharSetException

Called when an empty tag is encountered.

handleStartTag

```java
protected void handleStartTag​(
TagElement
tag)
```

Called when a start tag is encountered.

**Parameters:** tag

- the tag being handled

---

#### handleStartTag

protected void handleStartTag​(

TagElement

tag)

Called when a start tag is encountered.

handleEndTag

```java
protected void handleEndTag​(
TagElement
tag)
```

Called when an end tag is encountered.

**Parameters:** tag

- the tag being handled

---

#### handleEndTag

protected void handleEndTag​(

TagElement

tag)

Called when an end tag is encountered.

handleError

```java
protected void handleError​(int ln,

String
msg)
```

An error has occurred.

**Parameters:** ln

- the number of line containing the error
**Parameters:** msg

- the error message

---

#### handleError

protected void handleError​(int ln,

String

msg)

An error has occurred.

error

```java
protected void error​(
String
err,

String
arg1,

String
arg2,

String
arg3)
```

Invokes the error handler.

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument
**Parameters:** arg3

- the 3rd error message argument

---

#### error

protected void error​(

String

err,

String

arg1,

String

arg2,

String

arg3)

Invokes the error handler.

error

```java
protected void error​(
String
err,

String
arg1,

String
arg2)
```

Invokes the error handler with the 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument
**Parameters:** arg2

- the 2nd error message argument

---

#### error

protected void error​(

String

err,

String

arg1,

String

arg2)

Invokes the error handler with the 3rd error message argument "?".

error

```java
protected void error​(
String
err,

String
arg1)
```

Invokes the error handler with the 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type
**Parameters:** arg1

- the 1st error message argument

---

#### error

protected void error​(

String

err,

String

arg1)

Invokes the error handler with the 2nd and 3rd error message argument "?".

error

```java
protected void error​(
String
err)
```

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

**Parameters:** err

- the error type

---

#### error

protected void error​(

String

err)

Invokes the error handler with the 1st, 2nd and 3rd error message argument "?".

startTag

```java
protected void startTag​(
TagElement
tag)
throws
ChangedCharSetException
```

Handle a start tag. The new tag is pushed
onto the tag stack. The attribute list is
checked for required attributes.

**Parameters:** tag

- the tag
**Throws:** ChangedCharSetException

- if the document charset was changed

---

#### startTag

protected void startTag​(

TagElement

tag)
throws

ChangedCharSetException

Handle a start tag. The new tag is pushed
onto the tag stack. The attribute list is
checked for required attributes.

endTag

```java
protected void endTag​(boolean omitted)
```

Handle an end tag. The end tag is popped
from the tag stack.

**Parameters:** omitted

-

true

if the tag is no actually present in the
document, but is supposed by the parser

---

#### endTag

protected void endTag​(boolean omitted)

Handle an end tag. The end tag is popped
from the tag stack.

markFirstTime

```java
protected void markFirstTime​(
Element
elem)
```

Marks the first time a tag has been seen in a document

**Parameters:** elem

- the element represented by the tag

---

#### markFirstTime

protected void markFirstTime​(

Element

elem)

Marks the first time a tag has been seen in a document

parseDTDMarkup

```java
public
String
parseDTDMarkup()
throws
IOException
```

Parses the Document Type Declaration markup declaration.
Currently ignores it.

**Returns:** the string representation of the markup declaration
**Throws:** IOException

- if an I/O error occurs

---

#### parseDTDMarkup

public

String

parseDTDMarkup()
throws

IOException

Parses the Document Type Declaration markup declaration.
Currently ignores it.

parseMarkupDeclarations

```java
protected boolean parseMarkupDeclarations​(
StringBuffer
strBuff)
throws
IOException
```

Parse markup declarations.
Currently only handles the Document Type Declaration markup.
Returns true if it is a markup declaration false otherwise.

**Parameters:** strBuff

- the markup declaration
**Returns:** true

if this is a valid markup declaration;
otherwise

false
**Throws:** IOException

- if an I/O error occurs

---

#### parseMarkupDeclarations

protected boolean parseMarkupDeclarations​(

StringBuffer

strBuff)
throws

IOException

Parse markup declarations.
Currently only handles the Document Type Declaration markup.
Returns true if it is a markup declaration false otherwise.

parse

```java
public void parse​(
Reader
in)
throws
IOException
```

Parse an HTML stream, given a DTD.

**Parameters:** in

- the reader to read the source from
**Throws:** IOException

- if an I/O error occurs

---

#### parse

public void parse​(

Reader

in)
throws

IOException

Parse an HTML stream, given a DTD.

getCurrentPos

```java
protected int getCurrentPos()
```

Returns the current position.

**Returns:** the current position

---

#### getCurrentPos

protected int getCurrentPos()

Returns the current position.

---

