# Class HTMLWriter

**Source:** `java.desktop\javax\swing\text\html\HTMLWriter.html`

### Class Description

```java
public class
HTMLWriter

extends
AbstractWriter
```

This is a writer for HTMLDocuments.

---

### Field Details

*No entries found.*

### Constructor Details

#### public HTMLWriter​(
Writer
w,

HTMLDocument
doc)

Creates a new HTMLWriter.

**Parameters:**
- w

- a Writer
- doc

- an HTMLDocument

---

#### public HTMLWriter​(
Writer
w,

HTMLDocument
doc,
int pos,
int len)

Creates a new HTMLWriter.

**Parameters:**
- w

- a Writer
- doc

- an HTMLDocument
- pos

- the document location from which to fetch the content
- len

- the amount to write out

---

### Method Details

#### public void write()
throws
IOException
,

BadLocationException

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

**Specified by:**
- write

in class

AbstractWriter

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void writeAttributes​(
AttributeSet
attr)
throws
IOException

Writes out the attribute set. Ignores all
attributes with a key of type HTML.Tag,
attributes with a key of type StyleConstants,
and attributes with a key of type
HTML.Attribute.ENDTAG.

**Overrides:**
- writeAttributes

in class

AbstractWriter

**Parameters:**
- attr

- an AttributeSet

**Throws:**
- IOException

- on any I/O error

---

#### protected void emptyTag​(
Element
elem)
throws
BadLocationException
,

IOException

Writes out all empty elements (all tags that have no
corresponding end tag).

**Parameters:**
- elem

- an Element

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected boolean isBlockTag​(
AttributeSet
attr)

Determines if the HTML.Tag associated with the
element is a block tag.

**Parameters:**
- attr

- an AttributeSet

**Returns:**
- true if tag is block tag, false otherwise.

---

#### protected void startTag​(
Element
elem)
throws
IOException
,

BadLocationException

Writes out a start tag for the element.
Ignores all synthesized elements.

**Parameters:**
- elem

- an Element

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void textAreaContent​(
AttributeSet
attr)
throws
BadLocationException
,

IOException

Writes out text that is contained in a TEXTAREA form
element.

**Parameters:**
- attr

- an AttributeSet

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void text​(
Element
elem)
throws
BadLocationException
,

IOException

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Overrides:**
- text

in class

AbstractWriter

**Parameters:**
- elem

- an Element

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void selectContent​(
AttributeSet
attr)
throws
IOException

Writes out the content of the SELECT form element.

**Parameters:**
- attr

- the AttributeSet associated with the form element

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeOption​(
Option
option)
throws
IOException

Writes out the content of the Option form element.

**Parameters:**
- option

- an Option

**Throws:**
- IOException

- on any I/O error

---

#### protected void endTag​(
Element
elem)
throws
IOException

Writes out an end tag for the element.

**Parameters:**
- elem

- an Element

**Throws:**
- IOException

- on any I/O error

---

#### protected void comment​(
Element
elem)
throws
BadLocationException
,

IOException

Writes out comments.

**Parameters:**
- elem

- an Element

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected boolean synthesizedElement​(
Element
elem)

Returns

true

if the element is a
synthesized element. Currently we are only testing
for the p-implied tag.

**Parameters:**
- elem

- an element

**Returns:**
- true

if the element is a synthesized element.

---

#### protected boolean matchNameAttribute​(
AttributeSet
attr,

HTML.Tag
tag)

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

**Parameters:**
- attr

- a set of attributes
- tag

- an HTML tag

**Returns:**
- true

if the StyleConstants.NameAttribute is equal to the tag that is passed in as a parameter.

---

#### protected void writeEmbeddedTags​(
AttributeSet
attr)
throws
IOException

Searches for embedded tags in the AttributeSet
and writes them out. It also stores these tags in a vector
so that when appropriate the corresponding end tags can be
written out.

**Parameters:**
- attr

- a set of attributes

**Throws:**
- IOException

- on any I/O error

---

#### protected void closeOutUnwantedEmbeddedTags​(
AttributeSet
attr)
throws
IOException

Searches the attribute set and for each tag
that is stored in the tag vector. If the tag is not found,
then the tag is removed from the vector and a corresponding
end tag is written out.

**Parameters:**
- attr

- a set of attributes

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeLineSeparator()
throws
IOException

Writes the line separator. This is overriden to make sure we don't
replace the newline content in case it is outside normal ascii.

**Overrides:**
- writeLineSeparator

in class

AbstractWriter

**Throws:**
- IOException

- on any I/O error

**Since:**
- 1.3

---

#### protected void output​(char[] chars,
int start,
int length)
throws
IOException

This method is overriden to map any character entities, such as
< to &lt;.

super.output

will be invoked to
write the content.

**Overrides:**
- output

in class

AbstractWriter

**Parameters:**
- chars

- characters to output
- start

- starting index
- length

- length of output

**Throws:**
- IOException

- on any I/O error

**Since:**
- 1.3

---

### Additional Sections

#### Class HTMLWriter

java.lang.Object

- javax.swing.text.AbstractWriter
- - javax.swing.text.html.HTMLWriter

javax.swing.text.AbstractWriter

- javax.swing.text.html.HTMLWriter

javax.swing.text.html.HTMLWriter

```java
public class
HTMLWriter

extends
AbstractWriter
```

This is a writer for HTMLDocuments.

public class

HTMLWriter

extends

AbstractWriter

This is a writer for HTMLDocuments.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

AbstractWriter

NEWLINE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HTMLWriter

​(

Writer

w,

HTMLDocument

doc)

Creates a new HTMLWriter.

HTMLWriter

​(

Writer

w,

HTMLDocument

doc,
int pos,
int len)

Creates a new HTMLWriter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

closeOutUnwantedEmbeddedTags

​(

AttributeSet

attr)

Searches the attribute set and for each tag
that is stored in the tag vector.

protected void

comment

​(

Element

elem)

Writes out comments.

protected void

emptyTag

​(

Element

elem)

Writes out all empty elements (all tags that have no
corresponding end tag).

protected void

endTag

​(

Element

elem)

Writes out an end tag for the element.

protected boolean

isBlockTag

​(

AttributeSet

attr)

Determines if the HTML.Tag associated with the
element is a block tag.

protected boolean

matchNameAttribute

​(

AttributeSet

attr,

HTML.Tag

tag)

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

protected void

output

​(char[] chars,
int start,
int length)

This method is overriden to map any character entities, such as
< to &lt;.

protected void

selectContent

​(

AttributeSet

attr)

Writes out the content of the SELECT form element.

protected void

startTag

​(

Element

elem)

Writes out a start tag for the element.

protected boolean

synthesizedElement

​(

Element

elem)

Returns

true

if the element is a
synthesized element.

protected void

text

​(

Element

elem)

Writes out text.

protected void

textAreaContent

​(

AttributeSet

attr)

Writes out text that is contained in a TEXTAREA form
element.

void

write

()

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out the attribute set.

protected void

writeEmbeddedTags

​(

AttributeSet

attr)

Searches for embedded tags in the AttributeSet
and writes them out.

protected void

writeLineSeparator

()

Writes the line separator.

protected void

writeOption

​(

Option

option)

Writes out the content of the Option form element.

- Methods declared in class javax.swing.text.

AbstractWriter

decrIndent

,

getCanWrapLines

,

getCurrentLineLength

,

getDocument

,

getElementIterator

,

getEndOffset

,

getIndentLevel

,

getIndentSpace

,

getLineLength

,

getLineSeparator

,

getStartOffset

,

getText

,

getWriter

,

incrIndent

,

indent

,

inRange

,

isLineEmpty

,

setCanWrapLines

,

setCurrentLineLength

,

setIndentSpace

,

setLineLength

,

setLineSeparator

,

write

,

write

,

write

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

- Fields declared in class javax.swing.text.

AbstractWriter

NEWLINE

---

#### Field Summary

Fields declared in class javax.swing.text.

AbstractWriter

NEWLINE

---

#### Fields declared in class javax.swing.text. AbstractWriter

Constructor Summary

Constructors

Constructor

Description

HTMLWriter

​(

Writer

w,

HTMLDocument

doc)

Creates a new HTMLWriter.

HTMLWriter

​(

Writer

w,

HTMLDocument

doc,
int pos,
int len)

Creates a new HTMLWriter.

---

#### Constructor Summary

Creates a new HTMLWriter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

closeOutUnwantedEmbeddedTags

​(

AttributeSet

attr)

Searches the attribute set and for each tag
that is stored in the tag vector.

protected void

comment

​(

Element

elem)

Writes out comments.

protected void

emptyTag

​(

Element

elem)

Writes out all empty elements (all tags that have no
corresponding end tag).

protected void

endTag

​(

Element

elem)

Writes out an end tag for the element.

protected boolean

isBlockTag

​(

AttributeSet

attr)

Determines if the HTML.Tag associated with the
element is a block tag.

protected boolean

matchNameAttribute

​(

AttributeSet

attr,

HTML.Tag

tag)

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

protected void

output

​(char[] chars,
int start,
int length)

This method is overriden to map any character entities, such as
< to &lt;.

protected void

selectContent

​(

AttributeSet

attr)

Writes out the content of the SELECT form element.

protected void

startTag

​(

Element

elem)

Writes out a start tag for the element.

protected boolean

synthesizedElement

​(

Element

elem)

Returns

true

if the element is a
synthesized element.

protected void

text

​(

Element

elem)

Writes out text.

protected void

textAreaContent

​(

AttributeSet

attr)

Writes out text that is contained in a TEXTAREA form
element.

void

write

()

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out the attribute set.

protected void

writeEmbeddedTags

​(

AttributeSet

attr)

Searches for embedded tags in the AttributeSet
and writes them out.

protected void

writeLineSeparator

()

Writes the line separator.

protected void

writeOption

​(

Option

option)

Writes out the content of the Option form element.

- Methods declared in class javax.swing.text.

AbstractWriter

decrIndent

,

getCanWrapLines

,

getCurrentLineLength

,

getDocument

,

getElementIterator

,

getEndOffset

,

getIndentLevel

,

getIndentSpace

,

getLineLength

,

getLineSeparator

,

getStartOffset

,

getText

,

getWriter

,

incrIndent

,

indent

,

inRange

,

isLineEmpty

,

setCanWrapLines

,

setCurrentLineLength

,

setIndentSpace

,

setLineLength

,

setLineSeparator

,

write

,

write

,

write

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

Searches the attribute set and for each tag
that is stored in the tag vector.

Writes out comments.

Writes out all empty elements (all tags that have no
corresponding end tag).

Writes out an end tag for the element.

Determines if the HTML.Tag associated with the
element is a block tag.

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

This method is overriden to map any character entities, such as
< to &lt;.

Writes out the content of the SELECT form element.

Writes out a start tag for the element.

Returns

true

if the element is a
synthesized element.

Writes out text.

Writes out text that is contained in a TEXTAREA form
element.

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

Writes out the attribute set.

Searches for embedded tags in the AttributeSet
and writes them out.

Writes the line separator.

Writes out the content of the Option form element.

Methods declared in class javax.swing.text.

AbstractWriter

decrIndent

,

getCanWrapLines

,

getCurrentLineLength

,

getDocument

,

getElementIterator

,

getEndOffset

,

getIndentLevel

,

getIndentSpace

,

getLineLength

,

getLineSeparator

,

getStartOffset

,

getText

,

getWriter

,

incrIndent

,

indent

,

inRange

,

isLineEmpty

,

setCanWrapLines

,

setCurrentLineLength

,

setIndentSpace

,

setLineLength

,

setLineSeparator

,

write

,

write

,

write

---

#### Methods declared in class javax.swing.text. AbstractWriter

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument

- HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc,
int pos,
int len)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument
**Parameters:** pos

- the document location from which to fetch the content
**Parameters:** len

- the amount to write out

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write()
throws
IOException
,

BadLocationException
```

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

**Specified by:** write

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the attribute set. Ignores all
attributes with a key of type HTML.Tag,
attributes with a key of type StyleConstants,
and attributes with a key of type
HTML.Attribute.ENDTAG.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error

- emptyTag

```java
protected void emptyTag​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out all empty elements (all tags that have no
corresponding end tag).

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- isBlockTag

```java
protected boolean isBlockTag​(
AttributeSet
attr)
```

Determines if the HTML.Tag associated with the
element is a block tag.

**Parameters:** attr

- an AttributeSet
**Returns:** true if tag is block tag, false otherwise.

- startTag

```java
protected void startTag​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out a start tag for the element.
Ignores all synthesized elements.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- textAreaContent

```java
protected void textAreaContent​(
AttributeSet
attr)
throws
BadLocationException
,

IOException
```

Writes out text that is contained in a TEXTAREA form
element.

**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- selectContent

```java
protected void selectContent​(
AttributeSet
attr)
throws
IOException
```

Writes out the content of the SELECT form element.

**Parameters:** attr

- the AttributeSet associated with the form element
**Throws:** IOException

- on any I/O error

- writeOption

```java
protected void writeOption​(
Option
option)
throws
IOException
```

Writes out the content of the Option form element.

**Parameters:** option

- an Option
**Throws:** IOException

- on any I/O error

- endTag

```java
protected void endTag​(
Element
elem)
throws
IOException
```

Writes out an end tag for the element.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error

- comment

```java
protected void comment​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out comments.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- synthesizedElement

```java
protected boolean synthesizedElement​(
Element
elem)
```

Returns

true

if the element is a
synthesized element. Currently we are only testing
for the p-implied tag.

**Parameters:** elem

- an element
**Returns:** true

if the element is a synthesized element.

- matchNameAttribute

```java
protected boolean matchNameAttribute​(
AttributeSet
attr,

HTML.Tag
tag)
```

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

**Parameters:** attr

- a set of attributes
**Parameters:** tag

- an HTML tag
**Returns:** true

if the StyleConstants.NameAttribute is equal to the tag that is passed in as a parameter.

- writeEmbeddedTags

```java
protected void writeEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches for embedded tags in the AttributeSet
and writes them out. It also stores these tags in a vector
so that when appropriate the corresponding end tags can be
written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- closeOutUnwantedEmbeddedTags

```java
protected void closeOutUnwantedEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches the attribute set and for each tag
that is stored in the tag vector. If the tag is not found,
then the tag is removed from the vector and a corresponding
end tag is written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This is overriden to make sure we don't
replace the newline content in case it is outside normal ascii.

**Overrides:** writeLineSeparator

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Since:** 1.3

- output

```java
protected void output​(char[] chars,
int start,
int length)
throws
IOException
```

This method is overriden to map any character entities, such as
< to &lt;.

super.output

will be invoked to
write the content.

**Overrides:** output

in class

AbstractWriter
**Parameters:** chars

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

Constructor Detail

- HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument

- HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc,
int pos,
int len)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument
**Parameters:** pos

- the document location from which to fetch the content
**Parameters:** len

- the amount to write out

---

#### Constructor Detail

HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument

---

#### HTMLWriter

public HTMLWriter​(

Writer

w,

HTMLDocument

doc)

Creates a new HTMLWriter.

HTMLWriter

```java
public HTMLWriter​(
Writer
w,

HTMLDocument
doc,
int pos,
int len)
```

Creates a new HTMLWriter.

**Parameters:** w

- a Writer
**Parameters:** doc

- an HTMLDocument
**Parameters:** pos

- the document location from which to fetch the content
**Parameters:** len

- the amount to write out

---

#### HTMLWriter

public HTMLWriter​(

Writer

w,

HTMLDocument

doc,
int pos,
int len)

Creates a new HTMLWriter.

Method Detail

- write

```java
public void write()
throws
IOException
,

BadLocationException
```

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

**Specified by:** write

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the attribute set. Ignores all
attributes with a key of type HTML.Tag,
attributes with a key of type StyleConstants,
and attributes with a key of type
HTML.Attribute.ENDTAG.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error

- emptyTag

```java
protected void emptyTag​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out all empty elements (all tags that have no
corresponding end tag).

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- isBlockTag

```java
protected boolean isBlockTag​(
AttributeSet
attr)
```

Determines if the HTML.Tag associated with the
element is a block tag.

**Parameters:** attr

- an AttributeSet
**Returns:** true if tag is block tag, false otherwise.

- startTag

```java
protected void startTag​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out a start tag for the element.
Ignores all synthesized elements.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- textAreaContent

```java
protected void textAreaContent​(
AttributeSet
attr)
throws
BadLocationException
,

IOException
```

Writes out text that is contained in a TEXTAREA form
element.

**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- selectContent

```java
protected void selectContent​(
AttributeSet
attr)
throws
IOException
```

Writes out the content of the SELECT form element.

**Parameters:** attr

- the AttributeSet associated with the form element
**Throws:** IOException

- on any I/O error

- writeOption

```java
protected void writeOption​(
Option
option)
throws
IOException
```

Writes out the content of the Option form element.

**Parameters:** option

- an Option
**Throws:** IOException

- on any I/O error

- endTag

```java
protected void endTag​(
Element
elem)
throws
IOException
```

Writes out an end tag for the element.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error

- comment

```java
protected void comment​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out comments.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- synthesizedElement

```java
protected boolean synthesizedElement​(
Element
elem)
```

Returns

true

if the element is a
synthesized element. Currently we are only testing
for the p-implied tag.

**Parameters:** elem

- an element
**Returns:** true

if the element is a synthesized element.

- matchNameAttribute

```java
protected boolean matchNameAttribute​(
AttributeSet
attr,

HTML.Tag
tag)
```

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

**Parameters:** attr

- a set of attributes
**Parameters:** tag

- an HTML tag
**Returns:** true

if the StyleConstants.NameAttribute is equal to the tag that is passed in as a parameter.

- writeEmbeddedTags

```java
protected void writeEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches for embedded tags in the AttributeSet
and writes them out. It also stores these tags in a vector
so that when appropriate the corresponding end tags can be
written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- closeOutUnwantedEmbeddedTags

```java
protected void closeOutUnwantedEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches the attribute set and for each tag
that is stored in the tag vector. If the tag is not found,
then the tag is removed from the vector and a corresponding
end tag is written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This is overriden to make sure we don't
replace the newline content in case it is outside normal ascii.

**Overrides:** writeLineSeparator

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Since:** 1.3

- output

```java
protected void output​(char[] chars,
int start,
int length)
throws
IOException
```

This method is overriden to map any character entities, such as
< to &lt;.

super.output

will be invoked to
write the content.

**Overrides:** output

in class

AbstractWriter
**Parameters:** chars

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### Method Detail

write

```java
public void write()
throws
IOException
,

BadLocationException
```

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

**Specified by:** write

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### write

public void write()
throws

IOException

,

BadLocationException

Iterates over the
Element tree and controls the writing out of
all the tags and its attributes.

writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the attribute set. Ignores all
attributes with a key of type HTML.Tag,
attributes with a key of type StyleConstants,
and attributes with a key of type
HTML.Attribute.ENDTAG.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error

---

#### writeAttributes

protected void writeAttributes​(

AttributeSet

attr)
throws

IOException

Writes out the attribute set. Ignores all
attributes with a key of type HTML.Tag,
attributes with a key of type StyleConstants,
and attributes with a key of type
HTML.Attribute.ENDTAG.

emptyTag

```java
protected void emptyTag​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out all empty elements (all tags that have no
corresponding end tag).

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### emptyTag

protected void emptyTag​(

Element

elem)
throws

BadLocationException

,

IOException

Writes out all empty elements (all tags that have no
corresponding end tag).

isBlockTag

```java
protected boolean isBlockTag​(
AttributeSet
attr)
```

Determines if the HTML.Tag associated with the
element is a block tag.

**Parameters:** attr

- an AttributeSet
**Returns:** true if tag is block tag, false otherwise.

---

#### isBlockTag

protected boolean isBlockTag​(

AttributeSet

attr)

Determines if the HTML.Tag associated with the
element is a block tag.

startTag

```java
protected void startTag​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out a start tag for the element.
Ignores all synthesized elements.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### startTag

protected void startTag​(

Element

elem)
throws

IOException

,

BadLocationException

Writes out a start tag for the element.
Ignores all synthesized elements.

textAreaContent

```java
protected void textAreaContent​(
AttributeSet
attr)
throws
BadLocationException
,

IOException
```

Writes out text that is contained in a TEXTAREA form
element.

**Parameters:** attr

- an AttributeSet
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### textAreaContent

protected void textAreaContent​(

AttributeSet

attr)
throws

BadLocationException

,

IOException

Writes out text that is contained in a TEXTAREA form
element.

text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### text

protected void text​(

Element

elem)
throws

BadLocationException

,

IOException

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

selectContent

```java
protected void selectContent​(
AttributeSet
attr)
throws
IOException
```

Writes out the content of the SELECT form element.

**Parameters:** attr

- the AttributeSet associated with the form element
**Throws:** IOException

- on any I/O error

---

#### selectContent

protected void selectContent​(

AttributeSet

attr)
throws

IOException

Writes out the content of the SELECT form element.

writeOption

```java
protected void writeOption​(
Option
option)
throws
IOException
```

Writes out the content of the Option form element.

**Parameters:** option

- an Option
**Throws:** IOException

- on any I/O error

---

#### writeOption

protected void writeOption​(

Option

option)
throws

IOException

Writes out the content of the Option form element.

endTag

```java
protected void endTag​(
Element
elem)
throws
IOException
```

Writes out an end tag for the element.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error

---

#### endTag

protected void endTag​(

Element

elem)
throws

IOException

Writes out an end tag for the element.

comment

```java
protected void comment​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out comments.

**Parameters:** elem

- an Element
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### comment

protected void comment​(

Element

elem)
throws

BadLocationException

,

IOException

Writes out comments.

synthesizedElement

```java
protected boolean synthesizedElement​(
Element
elem)
```

Returns

true

if the element is a
synthesized element. Currently we are only testing
for the p-implied tag.

**Parameters:** elem

- an element
**Returns:** true

if the element is a synthesized element.

---

#### synthesizedElement

protected boolean synthesizedElement​(

Element

elem)

Returns

true

if the element is a
synthesized element. Currently we are only testing
for the p-implied tag.

matchNameAttribute

```java
protected boolean matchNameAttribute​(
AttributeSet
attr,

HTML.Tag
tag)
```

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

**Parameters:** attr

- a set of attributes
**Parameters:** tag

- an HTML tag
**Returns:** true

if the StyleConstants.NameAttribute is equal to the tag that is passed in as a parameter.

---

#### matchNameAttribute

protected boolean matchNameAttribute​(

AttributeSet

attr,

HTML.Tag

tag)

Returns true if the StyleConstants.NameAttribute is
equal to the tag that is passed in as a parameter.

writeEmbeddedTags

```java
protected void writeEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches for embedded tags in the AttributeSet
and writes them out. It also stores these tags in a vector
so that when appropriate the corresponding end tags can be
written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

---

#### writeEmbeddedTags

protected void writeEmbeddedTags​(

AttributeSet

attr)
throws

IOException

Searches for embedded tags in the AttributeSet
and writes them out. It also stores these tags in a vector
so that when appropriate the corresponding end tags can be
written out.

closeOutUnwantedEmbeddedTags

```java
protected void closeOutUnwantedEmbeddedTags​(
AttributeSet
attr)
throws
IOException
```

Searches the attribute set and for each tag
that is stored in the tag vector. If the tag is not found,
then the tag is removed from the vector and a corresponding
end tag is written out.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

---

#### closeOutUnwantedEmbeddedTags

protected void closeOutUnwantedEmbeddedTags​(

AttributeSet

attr)
throws

IOException

Searches the attribute set and for each tag
that is stored in the tag vector. If the tag is not found,
then the tag is removed from the vector and a corresponding
end tag is written out.

writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This is overriden to make sure we don't
replace the newline content in case it is outside normal ascii.

**Overrides:** writeLineSeparator

in class

AbstractWriter
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### writeLineSeparator

protected void writeLineSeparator()
throws

IOException

Writes the line separator. This is overriden to make sure we don't
replace the newline content in case it is outside normal ascii.

output

```java
protected void output​(char[] chars,
int start,
int length)
throws
IOException
```

This method is overriden to map any character entities, such as
< to &lt;.

super.output

will be invoked to
write the content.

**Overrides:** output

in class

AbstractWriter
**Parameters:** chars

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### output

protected void output​(char[] chars,
int start,
int length)
throws

IOException

This method is overriden to map any character entities, such as
< to &lt;.

super.output

will be invoked to
write the content.

---

