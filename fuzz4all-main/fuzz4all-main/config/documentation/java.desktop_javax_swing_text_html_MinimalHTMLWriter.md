# Class MinimalHTMLWriter

**Source:** `java.desktop\javax\swing\text\html\MinimalHTMLWriter.html`

### Class Description

```java
public class
MinimalHTMLWriter

extends
AbstractWriter
```

MinimalHTMLWriter is a fallback writer used by the
HTMLEditorKit to write out HTML for a document that
is a not produced by the EditorKit.

The format for the document is:

```java
<html>
<head>
<style>
<!-- list of named styles
p.normal {
font-family: SansSerif;
margin-height: 0;
font-size: 14
}
-->
</style>
</head>
<body>
<p style=normal>

Bold, italic, and underline attributes
of the run are emitted as HTML tags.
The remaining attributes are emitted as
part of the style attribute of a <span> tag.
The syntax is similar to inline styles.

</p>
</body>
</html>
```

---

### Field Details

*No entries found.*

### Constructor Details

#### public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc)

Creates a new MinimalHTMLWriter.

**Parameters:**
- w

- Writer
- doc

- StyledDocument

---

#### public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc,
int pos,
int len)

Creates a new MinimalHTMLWriter.

**Parameters:**
- w

- Writer
- doc

- StyledDocument
- pos

- The location in the document to fetch the
content.
- len

- The amount to write out.

---

### Method Details

#### public void write()
throws
IOException
,

BadLocationException

Generates HTML output
from a StyledDocument.

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

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.
The attribute name and value are separated by a colon.
Each pair is separated by a semicolon.

**Overrides:**
- writeAttributes

in class

AbstractWriter

**Parameters:**
- attr

- an AttributeSet.

**Throws:**
- IOException

- on any I/O error

---

#### protected void text​(
Element
elem)
throws
IOException
,

BadLocationException

Writes out text.

**Overrides:**
- text

in class

AbstractWriter

**Parameters:**
- elem

- an Element.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void writeStartTag​(
String
tag)
throws
IOException

Writes out a start tag appropriately
indented. Also increments the indent level.

**Parameters:**
- tag

- a start tag

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeEndTag​(
String
endTag)
throws
IOException

Writes out an end tag appropriately
indented. Also decrements the indent level.

**Parameters:**
- endTag

- an end tag

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeHeader()
throws
IOException

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag. The content is surrounded by
valid HTML comment markers to ensure that the
document is viewable in applications/browsers
that do not support the tag.

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeStyles()
throws
IOException

Writes out all the named styles as the
content of the <style> tag.

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeBody()
throws
IOException
,

BadLocationException

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements. This method specially handles
leaf elements that are text.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if we are in an invalid
location within the document.

---

#### protected void writeEndParagraph()
throws
IOException

Emits an end tag for a <p>
tag. Before writing out the tag, this method ensures
that all other tags that have been opened are
appropriately closed off.

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeStartParagraph​(
Element
elem)
throws
IOException

Emits the start tag for a paragraph. If
the paragraph has a named style associated with it,
then this method also generates a class attribute for the
<p> tag and sets its value to be the name of the
style.

**Parameters:**
- elem

- an element

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeLeaf​(
Element
elem)
throws
IOException

Responsible for writing out other non-text leaf
elements.

**Parameters:**
- elem

- an element

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeImage​(
Element
elem)
throws
IOException

Responsible for handling Icon Elements;
deliberately unimplemented. How to implement this method is
an issue of policy. For example, if you're generating
an <img> tag, how should you
represent the src attribute (the location of the image)?
In certain cases it could be a URL, in others it could
be read from a stream.

**Parameters:**
- elem

- an element of type StyleConstants.IconElementName

**Throws:**
- IOException

- if I/O error occured.

---

#### protected void writeComponent​(
Element
elem)
throws
IOException

Responsible for handling Component Elements;
deliberately unimplemented.
How this method is implemented is a matter of policy.

**Parameters:**
- elem

- an element of type StyleConstants.ComponentElementName

**Throws:**
- IOException

- if I/O error occured.

---

#### protected boolean isText​(
Element
elem)

Returns true if the element is a text element.

**Parameters:**
- elem

- an element

**Returns:**
- true

if the element is a text element.

---

#### protected void writeContent​(
Element
elem,
boolean needsIndenting)
throws
IOException
,

BadLocationException

Writes out the attribute set
in an HTML-compliant manner.

**Parameters:**
- elem

- an element
- needsIndenting

- indention will be added if

needsIndenting

is

true

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void writeHTMLTags​(
AttributeSet
attr)
throws
IOException

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

**Parameters:**
- attr

- a set of attributes

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeNonHTMLAttributes​(
AttributeSet
attr)
throws
IOException

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way. Given that
attributes such as font family and font size have no direct
mapping to HTML tags, a <span> tag is generated and its
style attribute is set to contain the list of remaining
attributes just like inline styles.

**Parameters:**
- attr

- a set of attributes

**Throws:**
- IOException

- on any I/O error

---

#### protected boolean inFontTag()

Returns true if we are currently in a <font> tag.

**Returns:**
- true

if we are currently in a <font> tag.

---

#### protected void endFontTag()
throws
IOException

This is no longer used, instead <span> will be written out.

Writes out an end tag for the <font> tag.

**Throws:**
- IOException

- on any I/O error

---

#### protected void startFontTag​(
String
style)
throws
IOException

This is no longer used, instead <span> will be written out.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

**Parameters:**
- style

- a font style

**Throws:**
- IOException

- on any I/O error

---

### Additional Sections

#### Class MinimalHTMLWriter

java.lang.Object

- javax.swing.text.AbstractWriter
- - javax.swing.text.html.MinimalHTMLWriter

javax.swing.text.AbstractWriter

- javax.swing.text.html.MinimalHTMLWriter

javax.swing.text.html.MinimalHTMLWriter

```java
public class
MinimalHTMLWriter

extends
AbstractWriter
```

MinimalHTMLWriter is a fallback writer used by the
HTMLEditorKit to write out HTML for a document that
is a not produced by the EditorKit.

The format for the document is:

```java
<html>
<head>
<style>
<!-- list of named styles
p.normal {
font-family: SansSerif;
margin-height: 0;
font-size: 14
}
-->
</style>
</head>
<body>
<p style=normal>

Bold, italic, and underline attributes
of the run are emitted as HTML tags.
The remaining attributes are emitted as
part of the style attribute of a <span> tag.
The syntax is similar to inline styles.

</p>
</body>
</html>
```

public class

MinimalHTMLWriter

extends

AbstractWriter

MinimalHTMLWriter is a fallback writer used by the
HTMLEditorKit to write out HTML for a document that
is a not produced by the EditorKit.

The format for the document is:

```java
<html>
<head>
<style>
<!-- list of named styles
p.normal {
font-family: SansSerif;
margin-height: 0;
font-size: 14
}
-->
</style>
</head>
<body>
<p style=normal>

Bold, italic, and underline attributes
of the run are emitted as HTML tags.
The remaining attributes are emitted as
part of the style attribute of a <span> tag.
The syntax is similar to inline styles.

</p>
</body>
</html>
```

<html>
<head>
<style>
<!-- list of named styles
p.normal {
font-family: SansSerif;
margin-height: 0;
font-size: 14
}
-->
</style>
</head>
<body>
<p style=normal>

Bold, italic, and underline attributes
of the run are emitted as HTML tags.
The remaining attributes are emitted as
part of the style attribute of a <span> tag.
The syntax is similar to inline styles.

</p>
</body>
</html>

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

MinimalHTMLWriter

​(

Writer

w,

StyledDocument

doc)

Creates a new MinimalHTMLWriter.

MinimalHTMLWriter

​(

Writer

w,

StyledDocument

doc,
int pos,
int len)

Creates a new MinimalHTMLWriter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

endFontTag

()

This is no longer used, instead <span> will be written out.

protected boolean

inFontTag

()

Returns true if we are currently in a <font> tag.

protected boolean

isText

​(

Element

elem)

Returns true if the element is a text element.

protected void

startFontTag

​(

String

style)

This is no longer used, instead <span> will be written out.

protected void

text

​(

Element

elem)

Writes out text.

void

write

()

Generates HTML output
from a StyledDocument.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.

protected void

writeBody

()

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements.

protected void

writeComponent

​(

Element

elem)

Responsible for handling Component Elements;
deliberately unimplemented.

protected void

writeContent

​(

Element

elem,
boolean needsIndenting)

Writes out the attribute set
in an HTML-compliant manner.

protected void

writeEndParagraph

()

Emits an end tag for a <p>
tag.

protected void

writeEndTag

​(

String

endTag)

Writes out an end tag appropriately
indented.

protected void

writeHeader

()

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag.

protected void

writeHTMLTags

​(

AttributeSet

attr)

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

protected void

writeImage

​(

Element

elem)

Responsible for handling Icon Elements;
deliberately unimplemented.

protected void

writeLeaf

​(

Element

elem)

Responsible for writing out other non-text leaf
elements.

protected void

writeNonHTMLAttributes

​(

AttributeSet

attr)

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way.

protected void

writeStartParagraph

​(

Element

elem)

Emits the start tag for a paragraph.

protected void

writeStartTag

​(

String

tag)

Writes out a start tag appropriately
indented.

protected void

writeStyles

()

Writes out all the named styles as the
content of the <style> tag.

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

output

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

,

writeLineSeparator

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

MinimalHTMLWriter

​(

Writer

w,

StyledDocument

doc)

Creates a new MinimalHTMLWriter.

MinimalHTMLWriter

​(

Writer

w,

StyledDocument

doc,
int pos,
int len)

Creates a new MinimalHTMLWriter.

---

#### Constructor Summary

Creates a new MinimalHTMLWriter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

endFontTag

()

This is no longer used, instead <span> will be written out.

protected boolean

inFontTag

()

Returns true if we are currently in a <font> tag.

protected boolean

isText

​(

Element

elem)

Returns true if the element is a text element.

protected void

startFontTag

​(

String

style)

This is no longer used, instead <span> will be written out.

protected void

text

​(

Element

elem)

Writes out text.

void

write

()

Generates HTML output
from a StyledDocument.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.

protected void

writeBody

()

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements.

protected void

writeComponent

​(

Element

elem)

Responsible for handling Component Elements;
deliberately unimplemented.

protected void

writeContent

​(

Element

elem,
boolean needsIndenting)

Writes out the attribute set
in an HTML-compliant manner.

protected void

writeEndParagraph

()

Emits an end tag for a <p>
tag.

protected void

writeEndTag

​(

String

endTag)

Writes out an end tag appropriately
indented.

protected void

writeHeader

()

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag.

protected void

writeHTMLTags

​(

AttributeSet

attr)

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

protected void

writeImage

​(

Element

elem)

Responsible for handling Icon Elements;
deliberately unimplemented.

protected void

writeLeaf

​(

Element

elem)

Responsible for writing out other non-text leaf
elements.

protected void

writeNonHTMLAttributes

​(

AttributeSet

attr)

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way.

protected void

writeStartParagraph

​(

Element

elem)

Emits the start tag for a paragraph.

protected void

writeStartTag

​(

String

tag)

Writes out a start tag appropriately
indented.

protected void

writeStyles

()

Writes out all the named styles as the
content of the <style> tag.

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

output

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

,

writeLineSeparator

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

This is no longer used, instead <span> will be written out.

Returns true if we are currently in a <font> tag.

Returns true if the element is a text element.

Writes out text.

Generates HTML output
from a StyledDocument.

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements.

Responsible for handling Component Elements;
deliberately unimplemented.

Writes out the attribute set
in an HTML-compliant manner.

Emits an end tag for a <p>
tag.

Writes out an end tag appropriately
indented.

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag.

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

Responsible for handling Icon Elements;
deliberately unimplemented.

Responsible for writing out other non-text leaf
elements.

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way.

Emits the start tag for a paragraph.

Writes out a start tag appropriately
indented.

Writes out all the named styles as the
content of the <style> tag.

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

output

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

,

writeLineSeparator

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

- MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument

- MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc,
int pos,
int len)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

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

Generates HTML output
from a StyledDocument.

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

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.
The attribute name and value are separated by a colon.
Each pair is separated by a semicolon.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

- text

```java
protected void text​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out text.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeStartTag

```java
protected void writeStartTag​(
String
tag)
throws
IOException
```

Writes out a start tag appropriately
indented. Also increments the indent level.

**Parameters:** tag

- a start tag
**Throws:** IOException

- on any I/O error

- writeEndTag

```java
protected void writeEndTag​(
String
endTag)
throws
IOException
```

Writes out an end tag appropriately
indented. Also decrements the indent level.

**Parameters:** endTag

- an end tag
**Throws:** IOException

- on any I/O error

- writeHeader

```java
protected void writeHeader()
throws
IOException
```

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag. The content is surrounded by
valid HTML comment markers to ensure that the
document is viewable in applications/browsers
that do not support the tag.

**Throws:** IOException

- on any I/O error

- writeStyles

```java
protected void writeStyles()
throws
IOException
```

Writes out all the named styles as the
content of the <style> tag.

**Throws:** IOException

- on any I/O error

- writeBody

```java
protected void writeBody()
throws
IOException
,

BadLocationException
```

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements. This method specially handles
leaf elements that are text.

**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if we are in an invalid
location within the document.

- writeEndParagraph

```java
protected void writeEndParagraph()
throws
IOException
```

Emits an end tag for a <p>
tag. Before writing out the tag, this method ensures
that all other tags that have been opened are
appropriately closed off.

**Throws:** IOException

- on any I/O error

- writeStartParagraph

```java
protected void writeStartParagraph​(
Element
elem)
throws
IOException
```

Emits the start tag for a paragraph. If
the paragraph has a named style associated with it,
then this method also generates a class attribute for the
<p> tag and sets its value to be the name of the
style.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

- writeLeaf

```java
protected void writeLeaf​(
Element
elem)
throws
IOException
```

Responsible for writing out other non-text leaf
elements.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

- writeImage

```java
protected void writeImage​(
Element
elem)
throws
IOException
```

Responsible for handling Icon Elements;
deliberately unimplemented. How to implement this method is
an issue of policy. For example, if you're generating
an <img> tag, how should you
represent the src attribute (the location of the image)?
In certain cases it could be a URL, in others it could
be read from a stream.

**Parameters:** elem

- an element of type StyleConstants.IconElementName
**Throws:** IOException

- if I/O error occured.

- writeComponent

```java
protected void writeComponent​(
Element
elem)
throws
IOException
```

Responsible for handling Component Elements;
deliberately unimplemented.
How this method is implemented is a matter of policy.

**Parameters:** elem

- an element of type StyleConstants.ComponentElementName
**Throws:** IOException

- if I/O error occured.

- isText

```java
protected boolean isText​(
Element
elem)
```

Returns true if the element is a text element.

**Parameters:** elem

- an element
**Returns:** true

if the element is a text element.

- writeContent

```java
protected void writeContent​(
Element
elem,
boolean needsIndenting)
throws
IOException
,

BadLocationException
```

Writes out the attribute set
in an HTML-compliant manner.

**Parameters:** elem

- an element
**Parameters:** needsIndenting

- indention will be added if

needsIndenting

is

true
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeHTMLTags

```java
protected void writeHTMLTags​(
AttributeSet
attr)
throws
IOException
```

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- writeNonHTMLAttributes

```java
protected void writeNonHTMLAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way. Given that
attributes such as font family and font size have no direct
mapping to HTML tags, a <span> tag is generated and its
style attribute is set to contain the list of remaining
attributes just like inline styles.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- inFontTag

```java
protected boolean inFontTag()
```

Returns true if we are currently in a <font> tag.

**Returns:** true

if we are currently in a <font> tag.

- endFontTag

```java
protected void endFontTag()
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out an end tag for the <font> tag.

**Throws:** IOException

- on any I/O error

- startFontTag

```java
protected void startFontTag​(
String
style)
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

**Parameters:** style

- a font style
**Throws:** IOException

- on any I/O error

Constructor Detail

- MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument

- MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc,
int pos,
int len)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

---

#### Constructor Detail

MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument

---

#### MinimalHTMLWriter

public MinimalHTMLWriter​(

Writer

w,

StyledDocument

doc)

Creates a new MinimalHTMLWriter.

MinimalHTMLWriter

```java
public MinimalHTMLWriter​(
Writer
w,

StyledDocument
doc,
int pos,
int len)
```

Creates a new MinimalHTMLWriter.

**Parameters:** w

- Writer
**Parameters:** doc

- StyledDocument
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

---

#### MinimalHTMLWriter

public MinimalHTMLWriter​(

Writer

w,

StyledDocument

doc,
int pos,
int len)

Creates a new MinimalHTMLWriter.

Method Detail

- write

```java
public void write()
throws
IOException
,

BadLocationException
```

Generates HTML output
from a StyledDocument.

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

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.
The attribute name and value are separated by a colon.
Each pair is separated by a semicolon.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

- text

```java
protected void text​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out text.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeStartTag

```java
protected void writeStartTag​(
String
tag)
throws
IOException
```

Writes out a start tag appropriately
indented. Also increments the indent level.

**Parameters:** tag

- a start tag
**Throws:** IOException

- on any I/O error

- writeEndTag

```java
protected void writeEndTag​(
String
endTag)
throws
IOException
```

Writes out an end tag appropriately
indented. Also decrements the indent level.

**Parameters:** endTag

- an end tag
**Throws:** IOException

- on any I/O error

- writeHeader

```java
protected void writeHeader()
throws
IOException
```

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag. The content is surrounded by
valid HTML comment markers to ensure that the
document is viewable in applications/browsers
that do not support the tag.

**Throws:** IOException

- on any I/O error

- writeStyles

```java
protected void writeStyles()
throws
IOException
```

Writes out all the named styles as the
content of the <style> tag.

**Throws:** IOException

- on any I/O error

- writeBody

```java
protected void writeBody()
throws
IOException
,

BadLocationException
```

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements. This method specially handles
leaf elements that are text.

**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if we are in an invalid
location within the document.

- writeEndParagraph

```java
protected void writeEndParagraph()
throws
IOException
```

Emits an end tag for a <p>
tag. Before writing out the tag, this method ensures
that all other tags that have been opened are
appropriately closed off.

**Throws:** IOException

- on any I/O error

- writeStartParagraph

```java
protected void writeStartParagraph​(
Element
elem)
throws
IOException
```

Emits the start tag for a paragraph. If
the paragraph has a named style associated with it,
then this method also generates a class attribute for the
<p> tag and sets its value to be the name of the
style.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

- writeLeaf

```java
protected void writeLeaf​(
Element
elem)
throws
IOException
```

Responsible for writing out other non-text leaf
elements.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

- writeImage

```java
protected void writeImage​(
Element
elem)
throws
IOException
```

Responsible for handling Icon Elements;
deliberately unimplemented. How to implement this method is
an issue of policy. For example, if you're generating
an <img> tag, how should you
represent the src attribute (the location of the image)?
In certain cases it could be a URL, in others it could
be read from a stream.

**Parameters:** elem

- an element of type StyleConstants.IconElementName
**Throws:** IOException

- if I/O error occured.

- writeComponent

```java
protected void writeComponent​(
Element
elem)
throws
IOException
```

Responsible for handling Component Elements;
deliberately unimplemented.
How this method is implemented is a matter of policy.

**Parameters:** elem

- an element of type StyleConstants.ComponentElementName
**Throws:** IOException

- if I/O error occured.

- isText

```java
protected boolean isText​(
Element
elem)
```

Returns true if the element is a text element.

**Parameters:** elem

- an element
**Returns:** true

if the element is a text element.

- writeContent

```java
protected void writeContent​(
Element
elem,
boolean needsIndenting)
throws
IOException
,

BadLocationException
```

Writes out the attribute set
in an HTML-compliant manner.

**Parameters:** elem

- an element
**Parameters:** needsIndenting

- indention will be added if

needsIndenting

is

true
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- writeHTMLTags

```java
protected void writeHTMLTags​(
AttributeSet
attr)
throws
IOException
```

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- writeNonHTMLAttributes

```java
protected void writeNonHTMLAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way. Given that
attributes such as font family and font size have no direct
mapping to HTML tags, a <span> tag is generated and its
style attribute is set to contain the list of remaining
attributes just like inline styles.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

- inFontTag

```java
protected boolean inFontTag()
```

Returns true if we are currently in a <font> tag.

**Returns:** true

if we are currently in a <font> tag.

- endFontTag

```java
protected void endFontTag()
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out an end tag for the <font> tag.

**Throws:** IOException

- on any I/O error

- startFontTag

```java
protected void startFontTag​(
String
style)
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

**Parameters:** style

- a font style
**Throws:** IOException

- on any I/O error

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

Generates HTML output
from a StyledDocument.

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

Generates HTML output
from a StyledDocument.

writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.
The attribute name and value are separated by a colon.
Each pair is separated by a semicolon.

**Overrides:** writeAttributes

in class

AbstractWriter
**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

---

#### writeAttributes

protected void writeAttributes​(

AttributeSet

attr)
throws

IOException

Writes out all the attributes for the
following types:
StyleConstants.ParagraphConstants,
StyleConstants.CharacterConstants,
StyleConstants.FontConstants,
StyleConstants.ColorConstants.
The attribute name and value are separated by a colon.
Each pair is separated by a semicolon.

text

```java
protected void text​(
Element
elem)
throws
IOException
,

BadLocationException
```

Writes out text.

**Overrides:** text

in class

AbstractWriter
**Parameters:** elem

- an Element.
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

IOException

,

BadLocationException

Writes out text.

writeStartTag

```java
protected void writeStartTag​(
String
tag)
throws
IOException
```

Writes out a start tag appropriately
indented. Also increments the indent level.

**Parameters:** tag

- a start tag
**Throws:** IOException

- on any I/O error

---

#### writeStartTag

protected void writeStartTag​(

String

tag)
throws

IOException

Writes out a start tag appropriately
indented. Also increments the indent level.

writeEndTag

```java
protected void writeEndTag​(
String
endTag)
throws
IOException
```

Writes out an end tag appropriately
indented. Also decrements the indent level.

**Parameters:** endTag

- an end tag
**Throws:** IOException

- on any I/O error

---

#### writeEndTag

protected void writeEndTag​(

String

endTag)
throws

IOException

Writes out an end tag appropriately
indented. Also decrements the indent level.

writeHeader

```java
protected void writeHeader()
throws
IOException
```

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag. The content is surrounded by
valid HTML comment markers to ensure that the
document is viewable in applications/browsers
that do not support the tag.

**Throws:** IOException

- on any I/O error

---

#### writeHeader

protected void writeHeader()
throws

IOException

Writes out the <head> and <style>
tags, and then invokes writeStyles() to write
out all the named styles as the content of the
<style> tag. The content is surrounded by
valid HTML comment markers to ensure that the
document is viewable in applications/browsers
that do not support the tag.

writeStyles

```java
protected void writeStyles()
throws
IOException
```

Writes out all the named styles as the
content of the <style> tag.

**Throws:** IOException

- on any I/O error

---

#### writeStyles

protected void writeStyles()
throws

IOException

Writes out all the named styles as the
content of the <style> tag.

writeBody

```java
protected void writeBody()
throws
IOException
,

BadLocationException
```

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements. This method specially handles
leaf elements that are text.

**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if we are in an invalid
location within the document.

---

#### writeBody

protected void writeBody()
throws

IOException

,

BadLocationException

Iterates over the elements in the document
and processes elements based on whether they are
branch elements or leaf elements. This method specially handles
leaf elements that are text.

writeEndParagraph

```java
protected void writeEndParagraph()
throws
IOException
```

Emits an end tag for a <p>
tag. Before writing out the tag, this method ensures
that all other tags that have been opened are
appropriately closed off.

**Throws:** IOException

- on any I/O error

---

#### writeEndParagraph

protected void writeEndParagraph()
throws

IOException

Emits an end tag for a <p>
tag. Before writing out the tag, this method ensures
that all other tags that have been opened are
appropriately closed off.

writeStartParagraph

```java
protected void writeStartParagraph​(
Element
elem)
throws
IOException
```

Emits the start tag for a paragraph. If
the paragraph has a named style associated with it,
then this method also generates a class attribute for the
<p> tag and sets its value to be the name of the
style.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

---

#### writeStartParagraph

protected void writeStartParagraph​(

Element

elem)
throws

IOException

Emits the start tag for a paragraph. If
the paragraph has a named style associated with it,
then this method also generates a class attribute for the
<p> tag and sets its value to be the name of the
style.

writeLeaf

```java
protected void writeLeaf​(
Element
elem)
throws
IOException
```

Responsible for writing out other non-text leaf
elements.

**Parameters:** elem

- an element
**Throws:** IOException

- on any I/O error

---

#### writeLeaf

protected void writeLeaf​(

Element

elem)
throws

IOException

Responsible for writing out other non-text leaf
elements.

writeImage

```java
protected void writeImage​(
Element
elem)
throws
IOException
```

Responsible for handling Icon Elements;
deliberately unimplemented. How to implement this method is
an issue of policy. For example, if you're generating
an <img> tag, how should you
represent the src attribute (the location of the image)?
In certain cases it could be a URL, in others it could
be read from a stream.

**Parameters:** elem

- an element of type StyleConstants.IconElementName
**Throws:** IOException

- if I/O error occured.

---

#### writeImage

protected void writeImage​(

Element

elem)
throws

IOException

Responsible for handling Icon Elements;
deliberately unimplemented. How to implement this method is
an issue of policy. For example, if you're generating
an <img> tag, how should you
represent the src attribute (the location of the image)?
In certain cases it could be a URL, in others it could
be read from a stream.

writeComponent

```java
protected void writeComponent​(
Element
elem)
throws
IOException
```

Responsible for handling Component Elements;
deliberately unimplemented.
How this method is implemented is a matter of policy.

**Parameters:** elem

- an element of type StyleConstants.ComponentElementName
**Throws:** IOException

- if I/O error occured.

---

#### writeComponent

protected void writeComponent​(

Element

elem)
throws

IOException

Responsible for handling Component Elements;
deliberately unimplemented.
How this method is implemented is a matter of policy.

isText

```java
protected boolean isText​(
Element
elem)
```

Returns true if the element is a text element.

**Parameters:** elem

- an element
**Returns:** true

if the element is a text element.

---

#### isText

protected boolean isText​(

Element

elem)

Returns true if the element is a text element.

writeContent

```java
protected void writeContent​(
Element
elem,
boolean needsIndenting)
throws
IOException
,

BadLocationException
```

Writes out the attribute set
in an HTML-compliant manner.

**Parameters:** elem

- an element
**Parameters:** needsIndenting

- indention will be added if

needsIndenting

is

true
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### writeContent

protected void writeContent​(

Element

elem,
boolean needsIndenting)
throws

IOException

,

BadLocationException

Writes out the attribute set
in an HTML-compliant manner.

writeHTMLTags

```java
protected void writeHTMLTags​(
AttributeSet
attr)
throws
IOException
```

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

---

#### writeHTMLTags

protected void writeHTMLTags​(

AttributeSet

attr)
throws

IOException

Generates
bold <b>, italic <i>, and <u> tags for the
text based on its attribute settings.

writeNonHTMLAttributes

```java
protected void writeNonHTMLAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way. Given that
attributes such as font family and font size have no direct
mapping to HTML tags, a <span> tag is generated and its
style attribute is set to contain the list of remaining
attributes just like inline styles.

**Parameters:** attr

- a set of attributes
**Throws:** IOException

- on any I/O error

---

#### writeNonHTMLAttributes

protected void writeNonHTMLAttributes​(

AttributeSet

attr)
throws

IOException

Writes out the remaining
character-level attributes (attributes other than bold,
italic, and underline) in an HTML-compliant way. Given that
attributes such as font family and font size have no direct
mapping to HTML tags, a <span> tag is generated and its
style attribute is set to contain the list of remaining
attributes just like inline styles.

inFontTag

```java
protected boolean inFontTag()
```

Returns true if we are currently in a <font> tag.

**Returns:** true

if we are currently in a <font> tag.

---

#### inFontTag

protected boolean inFontTag()

Returns true if we are currently in a <font> tag.

endFontTag

```java
protected void endFontTag()
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out an end tag for the <font> tag.

**Throws:** IOException

- on any I/O error

---

#### endFontTag

protected void endFontTag()
throws

IOException

This is no longer used, instead <span> will be written out.

Writes out an end tag for the <font> tag.

Writes out an end tag for the <font> tag.

startFontTag

```java
protected void startFontTag​(
String
style)
throws
IOException
```

This is no longer used, instead <span> will be written out.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

**Parameters:** style

- a font style
**Throws:** IOException

- on any I/O error

---

#### startFontTag

protected void startFontTag​(

String

style)
throws

IOException

This is no longer used, instead <span> will be written out.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

Writes out a start tag for the <font> tag.
Because font tags cannot be nested,
this method closes out
any enclosing font tag before writing out a
new start tag.

---

