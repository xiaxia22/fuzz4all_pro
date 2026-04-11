# Class HTMLEditorKit.ParserCallback

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.ParserCallback.html`

### Class Description

```java
public static class
HTMLEditorKit.ParserCallback

extends
Object
```

The result of parsing drives these callback methods.
The open and close actions should be balanced. The

flush

method will be the last method
called, to give the receiver a chance to flush any
pending data into the document.

Refer to DocumentParser, the default parser used, for further
information on the contents of the AttributeSets, the positions, and
other info.

**Direct Known Subclasses:** HTMLDocument.HTMLReader

---

### Field Details

#### public static final
Object
IMPLIED

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

**Since:**
- 1.3

---

### Constructor Details

#### public ParserCallback()

*No description found.*

---

### Method Details

#### public void flush()
throws
BadLocationException

The last method called on the reader. It allows
any pending changes to be flushed into the document.
Since this is currently loading synchronously, the entire
set of changes are pushed in at this point.

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document.

---

#### public void handleText​(char[] data,
int pos)

Called by the parser to indicate a block of text was
encountered.

**Parameters:**
- data

- a data
- pos

- a position

---

#### public void handleComment​(char[] data,
int pos)

Called by the parser to indicate a block of comment was
encountered.

**Parameters:**
- data

- a data
- pos

- a position

---

#### public void handleStartTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:**
- t

- an HTML tag
- a

- a set of attributes
- pos

- a position

---

#### public void handleEndTag​(
HTML.Tag
t,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:**
- t

- an HTML tag
- pos

- a position

---

#### public void handleSimpleTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:**
- t

- an HTML tag
- a

- a set of attributes
- pos

- a position

---

#### public void handleError​(
String
errorMsg,
int pos)

Callback from the parser. Route to the appropriate
handler for the error.

**Parameters:**
- errorMsg

- a error message
- pos

- a position

---

#### public void handleEndOfLineString​(
String
eol)

This is invoked after the stream has been parsed, but before

flush

.

eol

will be one of \n, \r
or \r\n, which ever is encountered the most in parsing the
stream.

**Parameters:**
- eol

- value of eol

**Since:**
- 1.3

---

### Additional Sections

#### Class HTMLEditorKit.ParserCallback

java.lang.Object

- javax.swing.text.html.HTMLEditorKit.ParserCallback

javax.swing.text.html.HTMLEditorKit.ParserCallback

**Direct Known Subclasses:** HTMLDocument.HTMLReader

**Enclosing class:** HTMLEditorKit

```java
public static class
HTMLEditorKit.ParserCallback

extends
Object
```

The result of parsing drives these callback methods.
The open and close actions should be balanced. The

flush

method will be the last method
called, to give the receiver a chance to flush any
pending data into the document.

Refer to DocumentParser, the default parser used, for further
information on the contents of the AttributeSets, the positions, and
other info.

**See Also:** DocumentParser

public static class

HTMLEditorKit.ParserCallback

extends

Object

The result of parsing drives these callback methods.
The open and close actions should be balanced. The

flush

method will be the last method
called, to give the receiver a chance to flush any
pending data into the document.

Refer to DocumentParser, the default parser used, for further
information on the contents of the AttributeSets, the positions, and
other info.

Refer to DocumentParser, the default parser used, for further
information on the contents of the AttributeSets, the positions, and
other info.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Object

IMPLIED

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ParserCallback

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

The last method called on the reader.

void

handleComment

​(char[] data,
int pos)

Called by the parser to indicate a block of comment was
encountered.

void

handleEndOfLineString

​(

String

eol)

This is invoked after the stream has been parsed, but before

flush

.

void

handleEndTag

​(

HTML.Tag

t,
int pos)

Callback from the parser.

void

handleError

​(

String

errorMsg,
int pos)

Callback from the parser.

void

handleSimpleTag

​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser.

void

handleStartTag

​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser.

void

handleText

​(char[] data,
int pos)

Called by the parser to indicate a block of text was
encountered.

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

static

Object

IMPLIED

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

---

#### Field Summary

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

Constructor Summary

Constructors

Constructor

Description

ParserCallback

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

The last method called on the reader.

void

handleComment

​(char[] data,
int pos)

Called by the parser to indicate a block of comment was
encountered.

void

handleEndOfLineString

​(

String

eol)

This is invoked after the stream has been parsed, but before

flush

.

void

handleEndTag

​(

HTML.Tag

t,
int pos)

Callback from the parser.

void

handleError

​(

String

errorMsg,
int pos)

Callback from the parser.

void

handleSimpleTag

​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser.

void

handleStartTag

​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser.

void

handleText

​(char[] data,
int pos)

Called by the parser to indicate a block of text was
encountered.

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

The last method called on the reader.

Called by the parser to indicate a block of comment was
encountered.

This is invoked after the stream has been parsed, but before

flush

.

Callback from the parser.

Called by the parser to indicate a block of text was
encountered.

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

- IMPLIED

```java
public static final
Object
IMPLIED
```

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

**Since:** 1.3

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ParserCallback

```java
public ParserCallback()
```

============ METHOD DETAIL ==========

- Method Detail

- flush

```java
public void flush()
throws
BadLocationException
```

The last method called on the reader. It allows
any pending changes to be flushed into the document.
Since this is currently loading synchronously, the entire
set of changes are pushed in at this point.

**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document.

- handleText

```java
public void handleText​(char[] data,
int pos)
```

Called by the parser to indicate a block of text was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

- handleComment

```java
public void handleComment​(char[] data,
int pos)
```

Called by the parser to indicate a block of comment was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

- handleStartTag

```java
public void handleStartTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

- handleEndTag

```java
public void handleEndTag​(
HTML.Tag
t,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** pos

- a position

- handleSimpleTag

```java
public void handleSimpleTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

- handleError

```java
public void handleError​(
String
errorMsg,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the error.

**Parameters:** errorMsg

- a error message
**Parameters:** pos

- a position

- handleEndOfLineString

```java
public void handleEndOfLineString​(
String
eol)
```

This is invoked after the stream has been parsed, but before

flush

.

eol

will be one of \n, \r
or \r\n, which ever is encountered the most in parsing the
stream.

**Parameters:** eol

- value of eol
**Since:** 1.3

Field Detail

- IMPLIED

```java
public static final
Object
IMPLIED
```

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

**Since:** 1.3

---

#### Field Detail

IMPLIED

```java
public static final
Object
IMPLIED
```

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

**Since:** 1.3

---

#### IMPLIED

public static final

Object

IMPLIED

This is passed as an attribute in the attributeset to indicate
the element is implied eg, the string '<>foo<\t>'
contains an implied html element and an implied body element.

Constructor Detail

- ParserCallback

```java
public ParserCallback()
```

---

#### Constructor Detail

ParserCallback

```java
public ParserCallback()
```

---

#### ParserCallback

public ParserCallback()

Method Detail

- flush

```java
public void flush()
throws
BadLocationException
```

The last method called on the reader. It allows
any pending changes to be flushed into the document.
Since this is currently loading synchronously, the entire
set of changes are pushed in at this point.

**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document.

- handleText

```java
public void handleText​(char[] data,
int pos)
```

Called by the parser to indicate a block of text was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

- handleComment

```java
public void handleComment​(char[] data,
int pos)
```

Called by the parser to indicate a block of comment was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

- handleStartTag

```java
public void handleStartTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

- handleEndTag

```java
public void handleEndTag​(
HTML.Tag
t,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** pos

- a position

- handleSimpleTag

```java
public void handleSimpleTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

- handleError

```java
public void handleError​(
String
errorMsg,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the error.

**Parameters:** errorMsg

- a error message
**Parameters:** pos

- a position

- handleEndOfLineString

```java
public void handleEndOfLineString​(
String
eol)
```

This is invoked after the stream has been parsed, but before

flush

.

eol

will be one of \n, \r
or \r\n, which ever is encountered the most in parsing the
stream.

**Parameters:** eol

- value of eol
**Since:** 1.3

---

#### Method Detail

flush

```java
public void flush()
throws
BadLocationException
```

The last method called on the reader. It allows
any pending changes to be flushed into the document.
Since this is currently loading synchronously, the entire
set of changes are pushed in at this point.

**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document.

---

#### flush

public void flush()
throws

BadLocationException

The last method called on the reader. It allows
any pending changes to be flushed into the document.
Since this is currently loading synchronously, the entire
set of changes are pushed in at this point.

handleText

```java
public void handleText​(char[] data,
int pos)
```

Called by the parser to indicate a block of text was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

---

#### handleText

public void handleText​(char[] data,
int pos)

Called by the parser to indicate a block of text was
encountered.

handleComment

```java
public void handleComment​(char[] data,
int pos)
```

Called by the parser to indicate a block of comment was
encountered.

**Parameters:** data

- a data
**Parameters:** pos

- a position

---

#### handleComment

public void handleComment​(char[] data,
int pos)

Called by the parser to indicate a block of comment was
encountered.

handleStartTag

```java
public void handleStartTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

---

#### handleStartTag

public void handleStartTag​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

handleEndTag

```java
public void handleEndTag​(
HTML.Tag
t,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** pos

- a position

---

#### handleEndTag

public void handleEndTag​(

HTML.Tag

t,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

handleSimpleTag

```java
public void handleSimpleTag​(
HTML.Tag
t,

MutableAttributeSet
a,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the tag.

**Parameters:** t

- an HTML tag
**Parameters:** a

- a set of attributes
**Parameters:** pos

- a position

---

#### handleSimpleTag

public void handleSimpleTag​(

HTML.Tag

t,

MutableAttributeSet

a,
int pos)

Callback from the parser. Route to the appropriate
handler for the tag.

handleError

```java
public void handleError​(
String
errorMsg,
int pos)
```

Callback from the parser. Route to the appropriate
handler for the error.

**Parameters:** errorMsg

- a error message
**Parameters:** pos

- a position

---

#### handleError

public void handleError​(

String

errorMsg,
int pos)

Callback from the parser. Route to the appropriate
handler for the error.

handleEndOfLineString

```java
public void handleEndOfLineString​(
String
eol)
```

This is invoked after the stream has been parsed, but before

flush

.

eol

will be one of \n, \r
or \r\n, which ever is encountered the most in parsing the
stream.

**Parameters:** eol

- value of eol
**Since:** 1.3

---

#### handleEndOfLineString

public void handleEndOfLineString​(

String

eol)

This is invoked after the stream has been parsed, but before

flush

.

eol

will be one of \n, \r
or \r\n, which ever is encountered the most in parsing the
stream.

---

