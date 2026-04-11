# Class DefaultStyledDocument

**Source:** `java.desktop\javax\swing\text\DefaultStyledDocument.html`

### Class Description

```java
public class
DefaultStyledDocument

extends
AbstractDocument

implements
StyledDocument
```

A document that can be marked up with character and paragraph
styles in a manner similar to the Rich Text Format. The element
structure for this document represents style crossings for
style runs. These style runs are mapped into a paragraph element
structure (which may reside in some other structure). The
style runs break at paragraph boundaries since logical styles are
assigned to paragraph boundaries.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Document

,

StyledDocument

---

### Field Details

#### public static final int BUFFER_SIZE_DEFAULT

The default size of the initial content buffer.

**See Also:**
- Constant Field Values

---

#### protected
DefaultStyledDocument.ElementBuffer
buffer

The element buffer.

---

### Constructor Details

#### public DefaultStyledDocument​(
AbstractDocument.Content
c,

StyleContext
styles)

Constructs a styled document.

**Parameters:**
- c

- the container for the content
- styles

- resources and style definitions which may
be shared across documents

---

#### public DefaultStyledDocument​(
StyleContext
styles)

Constructs a styled document with the default content
storage implementation and a shared set of styles.

**Parameters:**
- styles

- the styles

---

#### public DefaultStyledDocument()

Constructs a default styled document. This buffers
input content by a size of

BUFFER_SIZE_DEFAULT

and has a style context that is scoped by the lifetime
of the document and is not shared with other documents.

---

### Method Details

#### public
Element
getDefaultRootElement()

Gets the default root element.

**Specified by:**
- getDefaultRootElement

in interface

Document
- getDefaultRootElement

in class

AbstractDocument

**Returns:**
- the root

**See Also:**
- Document.getDefaultRootElement()

---

#### protected void create​(
DefaultStyledDocument.ElementSpec
[] data)

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method. If the
document contained any data it will first be removed.

**Parameters:**
- data

- the element data

---

#### protected void insert​(int offset,

DefaultStyledDocument.ElementSpec
[] data)
throws
BadLocationException

Inserts new elements in bulk. This is useful to allow
parsing with the document in an unlocked state and
prepare an element structure modification. This method
takes an array of tokens that describe how to update an
element structure so the time within a write lock can
be greatly reduced in an asynchronous update situation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Parameters:**
- offset

- the starting offset >= 0
- data

- the element data

**Throws:**
- BadLocationException

- for an invalid starting offset

---

#### public void removeElement​(
Element
elem)

Removes an element from this document.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

**Parameters:**
- elem

- the element to remove

**Throws:**
- NullPointerException

- if the element is

null
- IllegalArgumentException

- if the element could not be removed
- IllegalStateException

- if the element structure is invalid

**Since:**
- 1.7

---

#### public
Style
addStyle​(
String
nm,

Style
parent)

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Specified by:**
- addStyle

in interface

StyledDocument

**Parameters:**
- nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
- parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.

**Returns:**
- the style

---

#### public void removeStyle​(
String
nm)

Removes a named style previously added to the document.

**Specified by:**
- removeStyle

in interface

StyledDocument

**Parameters:**
- nm

- the name of the style to remove

---

#### public
Style
getStyle​(
String
nm)

Fetches a named style previously added.

**Specified by:**
- getStyle

in interface

StyledDocument

**Parameters:**
- nm

- the name of the style

**Returns:**
- the style

---

#### public
Enumeration
<?> getStyleNames()

Fetches the list of style names.

**Returns:**
- all the style names

---

#### public void setLogicalStyle​(int pos,

Style
s)

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- setLogicalStyle

in interface

StyledDocument

**Parameters:**
- pos

- the offset from the start of the document >= 0
- s

- the logical style to assign to the paragraph, null if none

---

#### public
Style
getLogicalStyle​(int p)

Fetches the logical style assigned to the paragraph
represented by the given position.

**Specified by:**
- getLogicalStyle

in interface

StyledDocument

**Parameters:**
- p

- the location to translate to a paragraph
and determine the logical style assigned >= 0. This
is an offset from the start of the document.

**Returns:**
- the style, null if none

---

#### public void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)

Sets attributes for some part of the document.
A write lock is held by this operation while changes
are being made, and a DocumentEvent is sent to the listeners
after the change has been successfully completed.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- setCharacterAttributes

in interface

StyledDocument

**Parameters:**
- offset

- the offset in the document >= 0
- length

- the length >= 0
- s

- the attributes
- replace

- true if the previous attributes should be replaced
before setting the new attributes

---

#### public void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)

Sets attributes for a paragraph.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- setParagraphAttributes

in interface

StyledDocument

**Parameters:**
- offset

- the offset into the paragraph >= 0
- length

- the number of characters affected >= 0
- s

- the attributes
- replace

- whether to replace existing attributes, or merge them

---

#### public
Element
getParagraphElement​(int pos)

Gets the paragraph element at the offset

pos

.
A paragraph consists of at least one child Element, which is usually
a leaf.

**Specified by:**
- getParagraphElement

in interface

StyledDocument
- getParagraphElement

in class

AbstractDocument

**Parameters:**
- pos

- the starting offset >= 0

**Returns:**
- the element

---

#### public
Element
getCharacterElement​(int pos)

Gets a character element based on a position.

**Specified by:**
- getCharacterElement

in interface

StyledDocument

**Parameters:**
- pos

- the position in the document >= 0

**Returns:**
- the element

---

#### protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. This implementation simply
parses the inserted content for line breaks and builds up a set
of instructions for the element buffer.

**Overrides:**
- insertUpdate

in class

AbstractDocument

**Parameters:**
- chng

- a description of the document change
- attr

- the attributes

---

#### protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)

Updates document structure as a result of text removal.

**Overrides:**
- removeUpdate

in class

AbstractDocument

**Parameters:**
- chng

- a description of the document change

---

#### protected
AbstractDocument.AbstractElement
createDefaultRoot()

Creates the root element to be used to represent the
default document structure.

**Returns:**
- the element base

---

#### public
Color
getForeground​(
AttributeSet
attr)

Gets the foreground color from an attribute set.

**Specified by:**
- getForeground

in interface

StyledDocument

**Parameters:**
- attr

- the attribute set

**Returns:**
- the color

---

#### public
Color
getBackground​(
AttributeSet
attr)

Gets the background color from an attribute set.

**Specified by:**
- getBackground

in interface

StyledDocument

**Parameters:**
- attr

- the attribute set

**Returns:**
- the color

---

#### public
Font
getFont​(
AttributeSet
attr)

Gets the font from an attribute set.

**Specified by:**
- getFont

in interface

StyledDocument

**Parameters:**
- attr

- the attribute set

**Returns:**
- the font

---

#### protected void styleChanged​(
Style
style)

Called when any of this document's styles have changed.
Subclasses may wish to be intelligent about what gets damaged.

**Parameters:**
- style

- The Style that has changed.

---

#### public void addDocumentListener​(
DocumentListener
listener)

Adds a document listener for notification of any changes.

**Specified by:**
- addDocumentListener

in interface

Document

**Overrides:**
- addDocumentListener

in class

AbstractDocument

**Parameters:**
- listener

- the listener

**See Also:**
- Document.addDocumentListener(javax.swing.event.DocumentListener)

---

#### public void removeDocumentListener​(
DocumentListener
listener)

Removes a document listener.

**Specified by:**
- removeDocumentListener

in interface

Document

**Overrides:**
- removeDocumentListener

in class

AbstractDocument

**Parameters:**
- listener

- the listener

**See Also:**
- Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

### Additional Sections

#### Class DefaultStyledDocument

java.lang.Object

- javax.swing.text.AbstractDocument
- - javax.swing.text.DefaultStyledDocument

javax.swing.text.AbstractDocument

- javax.swing.text.DefaultStyledDocument

javax.swing.text.DefaultStyledDocument

**All Implemented Interfaces:** Serializable

,

Document

,

StyledDocument

**Direct Known Subclasses:** HTMLDocument

```java
public class
DefaultStyledDocument

extends
AbstractDocument

implements
StyledDocument
```

A document that can be marked up with character and paragraph
styles in a manner similar to the Rich Text Format. The element
structure for this document represents style crossings for
style runs. These style runs are mapped into a paragraph element
structure (which may reside in some other structure). The
style runs break at paragraph boundaries since logical styles are
assigned to paragraph boundaries.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Document

,

AbstractDocument

,

Serialized Form

public class

DefaultStyledDocument

extends

AbstractDocument

implements

StyledDocument

A document that can be marked up with character and paragraph
styles in a manner similar to the Rich Text Format. The element
structure for this document represents style crossings for
style runs. These style runs are mapped into a paragraph element
structure (which may reside in some other structure). The
style runs break at paragraph boundaries since logical styles are
assigned to paragraph boundaries.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultStyledDocument.AttributeUndoableEdit

An UndoableEdit used to remember AttributeSet changes to an
Element.

class

DefaultStyledDocument.ElementBuffer

Class to manage changes to the element
hierarchy.

static class

DefaultStyledDocument.ElementSpec

Specification for building elements.

protected class

DefaultStyledDocument.SectionElement

Default root element for a document... maps out the
paragraphs/lines contained.

- Nested classes/interfaces declared in class javax.swing.text.

AbstractDocument

AbstractDocument.AbstractElement

,

AbstractDocument.AttributeContext

,

AbstractDocument.BranchElement

,

AbstractDocument.Content

,

AbstractDocument.DefaultDocumentEvent

,

AbstractDocument.ElementEdit

,

AbstractDocument.LeafElement

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

DefaultStyledDocument.ElementBuffer

buffer

The element buffer.

static int

BUFFER_SIZE_DEFAULT

The default size of the initial content buffer.

- Fields declared in class javax.swing.text.

AbstractDocument

BAD_LOCATION

,

BidiElementName

,

ContentElementName

,

ElementNameAttribute

,

listenerList

,

ParagraphElementName

,

SectionElementName

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultStyledDocument

()

Constructs a default styled document.

DefaultStyledDocument

​(

AbstractDocument.Content

c,

StyleContext

styles)

Constructs a styled document.

DefaultStyledDocument

​(

StyleContext

styles)

Constructs a styled document with the default content
storage implementation and a shared set of styles.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy.

protected void

create

​(

DefaultStyledDocument.ElementSpec

[] data)

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method.

protected

AbstractDocument.AbstractElement

createDefaultRoot

()

Creates the root element to be used to represent the
default document structure.

Color

getBackground

​(

AttributeSet

attr)

Gets the background color from an attribute set.

Element

getCharacterElement

​(int pos)

Gets a character element based on a position.

Element

getDefaultRootElement

()

Gets the default root element.

Font

getFont

​(

AttributeSet

attr)

Gets the font from an attribute set.

Color

getForeground

​(

AttributeSet

attr)

Gets the foreground color from an attribute set.

Style

getLogicalStyle

​(int p)

Fetches the logical style assigned to the paragraph
represented by the given position.

Element

getParagraphElement

​(int pos)

Gets the paragraph element at the offset

pos

.

Style

getStyle

​(

String

nm)

Fetches a named style previously added.

Enumeration

<?>

getStyleNames

()

Fetches the list of style names.

protected void

insert

​(int offset,

DefaultStyledDocument.ElementSpec

[] data)

Inserts new elements in bulk.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

void

removeDocumentListener

​(

DocumentListener

listener)

Removes a document listener.

void

removeElement

​(

Element

elem)

Removes an element from this document.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates document structure as a result of text removal.

void

setCharacterAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for some part of the document.

void

setLogicalStyle

​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position.

void

setParagraphAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for a paragraph.

protected void

styleChanged

​(

Style

style)

Called when any of this document's styles have changed.

- Methods declared in class javax.swing.text.

AbstractDocument

addUndoableEditListener

,

createBranchElement

,

createLeafElement

,

createPosition

,

dump

,

fireChangedUpdate

,

fireInsertUpdate

,

fireRemoveUpdate

,

fireUndoableEditUpdate

,

getAsynchronousLoadPriority

,

getAttributeContext

,

getBidiRootElement

,

getContent

,

getCurrentWriter

,

getDocumentFilter

,

getDocumentListeners

,

getDocumentProperties

,

getEndPosition

,

getLength

,

getListeners

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

getUndoableEditListeners

,

insertString

,

postRemoveUpdate

,

putProperty

,

readLock

,

readUnlock

,

remove

,

removeUndoableEditListener

,

render

,

replace

,

setAsynchronousLoadPriority

,

setDocumentFilter

,

setDocumentProperties

,

writeLock

,

writeUnlock

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

- Methods declared in interface javax.swing.text.

Document

addUndoableEditListener

,

createPosition

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeUndoableEditListener

,

render

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultStyledDocument.AttributeUndoableEdit

An UndoableEdit used to remember AttributeSet changes to an
Element.

class

DefaultStyledDocument.ElementBuffer

Class to manage changes to the element
hierarchy.

static class

DefaultStyledDocument.ElementSpec

Specification for building elements.

protected class

DefaultStyledDocument.SectionElement

Default root element for a document... maps out the
paragraphs/lines contained.

- Nested classes/interfaces declared in class javax.swing.text.

AbstractDocument

AbstractDocument.AbstractElement

,

AbstractDocument.AttributeContext

,

AbstractDocument.BranchElement

,

AbstractDocument.Content

,

AbstractDocument.DefaultDocumentEvent

,

AbstractDocument.ElementEdit

,

AbstractDocument.LeafElement

---

#### Nested Class Summary

An UndoableEdit used to remember AttributeSet changes to an
Element.

Class to manage changes to the element
hierarchy.

Specification for building elements.

Default root element for a document... maps out the
paragraphs/lines contained.

Nested classes/interfaces declared in class javax.swing.text.

AbstractDocument

AbstractDocument.AbstractElement

,

AbstractDocument.AttributeContext

,

AbstractDocument.BranchElement

,

AbstractDocument.Content

,

AbstractDocument.DefaultDocumentEvent

,

AbstractDocument.ElementEdit

,

AbstractDocument.LeafElement

---

#### Nested classes/interfaces declared in class javax.swing.text. AbstractDocument

Field Summary

Fields

Modifier and Type

Field

Description

protected

DefaultStyledDocument.ElementBuffer

buffer

The element buffer.

static int

BUFFER_SIZE_DEFAULT

The default size of the initial content buffer.

- Fields declared in class javax.swing.text.

AbstractDocument

BAD_LOCATION

,

BidiElementName

,

ContentElementName

,

ElementNameAttribute

,

listenerList

,

ParagraphElementName

,

SectionElementName

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Field Summary

The element buffer.

The default size of the initial content buffer.

Fields declared in class javax.swing.text.

AbstractDocument

BAD_LOCATION

,

BidiElementName

,

ContentElementName

,

ElementNameAttribute

,

listenerList

,

ParagraphElementName

,

SectionElementName

---

#### Fields declared in class javax.swing.text. AbstractDocument

Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Fields declared in interface javax.swing.text. Document

Constructor Summary

Constructors

Constructor

Description

DefaultStyledDocument

()

Constructs a default styled document.

DefaultStyledDocument

​(

AbstractDocument.Content

c,

StyleContext

styles)

Constructs a styled document.

DefaultStyledDocument

​(

StyleContext

styles)

Constructs a styled document with the default content
storage implementation and a shared set of styles.

---

#### Constructor Summary

Constructs a default styled document.

Constructs a styled document.

Constructs a styled document with the default content
storage implementation and a shared set of styles.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy.

protected void

create

​(

DefaultStyledDocument.ElementSpec

[] data)

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method.

protected

AbstractDocument.AbstractElement

createDefaultRoot

()

Creates the root element to be used to represent the
default document structure.

Color

getBackground

​(

AttributeSet

attr)

Gets the background color from an attribute set.

Element

getCharacterElement

​(int pos)

Gets a character element based on a position.

Element

getDefaultRootElement

()

Gets the default root element.

Font

getFont

​(

AttributeSet

attr)

Gets the font from an attribute set.

Color

getForeground

​(

AttributeSet

attr)

Gets the foreground color from an attribute set.

Style

getLogicalStyle

​(int p)

Fetches the logical style assigned to the paragraph
represented by the given position.

Element

getParagraphElement

​(int pos)

Gets the paragraph element at the offset

pos

.

Style

getStyle

​(

String

nm)

Fetches a named style previously added.

Enumeration

<?>

getStyleNames

()

Fetches the list of style names.

protected void

insert

​(int offset,

DefaultStyledDocument.ElementSpec

[] data)

Inserts new elements in bulk.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

void

removeDocumentListener

​(

DocumentListener

listener)

Removes a document listener.

void

removeElement

​(

Element

elem)

Removes an element from this document.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates document structure as a result of text removal.

void

setCharacterAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for some part of the document.

void

setLogicalStyle

​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position.

void

setParagraphAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for a paragraph.

protected void

styleChanged

​(

Style

style)

Called when any of this document's styles have changed.

- Methods declared in class javax.swing.text.

AbstractDocument

addUndoableEditListener

,

createBranchElement

,

createLeafElement

,

createPosition

,

dump

,

fireChangedUpdate

,

fireInsertUpdate

,

fireRemoveUpdate

,

fireUndoableEditUpdate

,

getAsynchronousLoadPriority

,

getAttributeContext

,

getBidiRootElement

,

getContent

,

getCurrentWriter

,

getDocumentFilter

,

getDocumentListeners

,

getDocumentProperties

,

getEndPosition

,

getLength

,

getListeners

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

getUndoableEditListeners

,

insertString

,

postRemoveUpdate

,

putProperty

,

readLock

,

readUnlock

,

remove

,

removeUndoableEditListener

,

render

,

replace

,

setAsynchronousLoadPriority

,

setDocumentFilter

,

setDocumentProperties

,

writeLock

,

writeUnlock

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

- Methods declared in interface javax.swing.text.

Document

addUndoableEditListener

,

createPosition

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeUndoableEditListener

,

render

---

#### Method Summary

Adds a document listener for notification of any changes.

Adds a new style into the logical style hierarchy.

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method.

Creates the root element to be used to represent the
default document structure.

Gets the background color from an attribute set.

Gets a character element based on a position.

Gets the default root element.

Gets the font from an attribute set.

Gets the foreground color from an attribute set.

Fetches the logical style assigned to the paragraph
represented by the given position.

Gets the paragraph element at the offset

pos

.

Fetches a named style previously added.

Fetches the list of style names.

Inserts new elements in bulk.

Updates document structure as a result of text insertion.

Removes a document listener.

Removes an element from this document.

Removes a named style previously added to the document.

Updates document structure as a result of text removal.

Sets attributes for some part of the document.

Sets the logical style to use for the paragraph at the
given position.

Sets attributes for a paragraph.

Called when any of this document's styles have changed.

Methods declared in class javax.swing.text.

AbstractDocument

addUndoableEditListener

,

createBranchElement

,

createLeafElement

,

createPosition

,

dump

,

fireChangedUpdate

,

fireInsertUpdate

,

fireRemoveUpdate

,

fireUndoableEditUpdate

,

getAsynchronousLoadPriority

,

getAttributeContext

,

getBidiRootElement

,

getContent

,

getCurrentWriter

,

getDocumentFilter

,

getDocumentListeners

,

getDocumentProperties

,

getEndPosition

,

getLength

,

getListeners

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

getUndoableEditListeners

,

insertString

,

postRemoveUpdate

,

putProperty

,

readLock

,

readUnlock

,

remove

,

removeUndoableEditListener

,

render

,

replace

,

setAsynchronousLoadPriority

,

setDocumentFilter

,

setDocumentProperties

,

writeLock

,

writeUnlock

---

#### Methods declared in class javax.swing.text. AbstractDocument

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

Methods declared in interface javax.swing.text.

Document

addUndoableEditListener

,

createPosition

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeUndoableEditListener

,

render

---

#### Methods declared in interface javax.swing.text. Document

============ FIELD DETAIL ===========

- Field Detail

- BUFFER_SIZE_DEFAULT

```java
public static final int BUFFER_SIZE_DEFAULT
```

The default size of the initial content buffer.

**See Also:** Constant Field Values

- buffer

```java
protected
DefaultStyledDocument.ElementBuffer
buffer
```

The element buffer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultStyledDocument

```java
public DefaultStyledDocument​(
AbstractDocument.Content
c,

StyleContext
styles)
```

Constructs a styled document.

**Parameters:** c

- the container for the content
**Parameters:** styles

- resources and style definitions which may
be shared across documents

- DefaultStyledDocument

```java
public DefaultStyledDocument​(
StyleContext
styles)
```

Constructs a styled document with the default content
storage implementation and a shared set of styles.

**Parameters:** styles

- the styles

- DefaultStyledDocument

```java
public DefaultStyledDocument()
```

Constructs a default styled document. This buffers
input content by a size of

BUFFER_SIZE_DEFAULT

and has a style context that is scoped by the lifetime
of the document and is not shared with other documents.

============ METHOD DETAIL ==========

- Method Detail

- getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element.

**Specified by:** getDefaultRootElement

in interface

Document
**Specified by:** getDefaultRootElement

in class

AbstractDocument
**Returns:** the root
**See Also:** Document.getDefaultRootElement()

- create

```java
protected void create​(
DefaultStyledDocument.ElementSpec
[] data)
```

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method. If the
document contained any data it will first be removed.

**Parameters:** data

- the element data

- insert

```java
protected void insert​(int offset,

DefaultStyledDocument.ElementSpec
[] data)
throws
BadLocationException
```

Inserts new elements in bulk. This is useful to allow
parsing with the document in an unlocked state and
prepare an element structure modification. This method
takes an array of tokens that describe how to update an
element structure so the time within a write lock can
be greatly reduced in an asynchronous update situation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Parameters:** offset

- the starting offset >= 0
**Parameters:** data

- the element data
**Throws:** BadLocationException

- for an invalid starting offset

- removeElement

```java
public void removeElement​(
Element
elem)
```

Removes an element from this document.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

**Parameters:** elem

- the element to remove
**Throws:** NullPointerException

- if the element is

null
**Throws:** IllegalArgumentException

- if the element could not be removed
**Throws:** IllegalStateException

- if the element structure is invalid
**Since:** 1.7

- addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Specified by:** addStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

- removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Specified by:** removeStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style to remove

- getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Specified by:** getStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style
**Returns:** the style

- getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the list of style names.

**Returns:** all the style names

- setLogicalStyle

```java
public void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setLogicalStyle

in interface

StyledDocument
**Parameters:** pos

- the offset from the start of the document >= 0
**Parameters:** s

- the logical style to assign to the paragraph, null if none

- getLogicalStyle

```java
public
Style
getLogicalStyle​(int p)
```

Fetches the logical style assigned to the paragraph
represented by the given position.

**Specified by:** getLogicalStyle

in interface

StyledDocument
**Parameters:** p

- the location to translate to a paragraph
and determine the logical style assigned >= 0. This
is an offset from the start of the document.
**Returns:** the style, null if none

- setCharacterAttributes

```java
public void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for some part of the document.
A write lock is held by this operation while changes
are being made, and a DocumentEvent is sent to the listeners
after the change has been successfully completed.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setCharacterAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset in the document >= 0
**Parameters:** length

- the length >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- true if the previous attributes should be replaced
before setting the new attributes

- setParagraphAttributes

```java
public void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for a paragraph.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setParagraphAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset into the paragraph >= 0
**Parameters:** length

- the number of characters affected >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- whether to replace existing attributes, or merge them

- getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Gets the paragraph element at the offset

pos

.
A paragraph consists of at least one child Element, which is usually
a leaf.

**Specified by:** getParagraphElement

in interface

StyledDocument
**Specified by:** getParagraphElement

in class

AbstractDocument
**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

- getCharacterElement

```java
public
Element
getCharacterElement​(int pos)
```

Gets a character element based on a position.

**Specified by:** getCharacterElement

in interface

StyledDocument
**Parameters:** pos

- the position in the document >= 0
**Returns:** the element

- insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. This implementation simply
parses the inserted content for line breaks and builds up a set
of instructions for the element buffer.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change
**Parameters:** attr

- the attributes

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates document structure as a result of text removal.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change

- createDefaultRoot

```java
protected
AbstractDocument.AbstractElement
createDefaultRoot()
```

Creates the root element to be used to represent the
default document structure.

**Returns:** the element base

- getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Gets the foreground color from an attribute set.

**Specified by:** getForeground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

- getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Gets the background color from an attribute set.

**Specified by:** getBackground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

- getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set.

**Specified by:** getFont

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the font

- styleChanged

```java
protected void styleChanged​(
Style
style)
```

Called when any of this document's styles have changed.
Subclasses may wish to be intelligent about what gets damaged.

**Parameters:** style

- The Style that has changed.

- addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Overrides:** addDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Overrides:** removeDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

Field Detail

- BUFFER_SIZE_DEFAULT

```java
public static final int BUFFER_SIZE_DEFAULT
```

The default size of the initial content buffer.

**See Also:** Constant Field Values

- buffer

```java
protected
DefaultStyledDocument.ElementBuffer
buffer
```

The element buffer.

---

#### Field Detail

BUFFER_SIZE_DEFAULT

```java
public static final int BUFFER_SIZE_DEFAULT
```

The default size of the initial content buffer.

**See Also:** Constant Field Values

---

#### BUFFER_SIZE_DEFAULT

public static final int BUFFER_SIZE_DEFAULT

The default size of the initial content buffer.

buffer

```java
protected
DefaultStyledDocument.ElementBuffer
buffer
```

The element buffer.

---

#### buffer

protected

DefaultStyledDocument.ElementBuffer

buffer

The element buffer.

Constructor Detail

- DefaultStyledDocument

```java
public DefaultStyledDocument​(
AbstractDocument.Content
c,

StyleContext
styles)
```

Constructs a styled document.

**Parameters:** c

- the container for the content
**Parameters:** styles

- resources and style definitions which may
be shared across documents

- DefaultStyledDocument

```java
public DefaultStyledDocument​(
StyleContext
styles)
```

Constructs a styled document with the default content
storage implementation and a shared set of styles.

**Parameters:** styles

- the styles

- DefaultStyledDocument

```java
public DefaultStyledDocument()
```

Constructs a default styled document. This buffers
input content by a size of

BUFFER_SIZE_DEFAULT

and has a style context that is scoped by the lifetime
of the document and is not shared with other documents.

---

#### Constructor Detail

DefaultStyledDocument

```java
public DefaultStyledDocument​(
AbstractDocument.Content
c,

StyleContext
styles)
```

Constructs a styled document.

**Parameters:** c

- the container for the content
**Parameters:** styles

- resources and style definitions which may
be shared across documents

---

#### DefaultStyledDocument

public DefaultStyledDocument​(

AbstractDocument.Content

c,

StyleContext

styles)

Constructs a styled document.

DefaultStyledDocument

```java
public DefaultStyledDocument​(
StyleContext
styles)
```

Constructs a styled document with the default content
storage implementation and a shared set of styles.

**Parameters:** styles

- the styles

---

#### DefaultStyledDocument

public DefaultStyledDocument​(

StyleContext

styles)

Constructs a styled document with the default content
storage implementation and a shared set of styles.

DefaultStyledDocument

```java
public DefaultStyledDocument()
```

Constructs a default styled document. This buffers
input content by a size of

BUFFER_SIZE_DEFAULT

and has a style context that is scoped by the lifetime
of the document and is not shared with other documents.

---

#### DefaultStyledDocument

public DefaultStyledDocument()

Constructs a default styled document. This buffers
input content by a size of

BUFFER_SIZE_DEFAULT

and has a style context that is scoped by the lifetime
of the document and is not shared with other documents.

Method Detail

- getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element.

**Specified by:** getDefaultRootElement

in interface

Document
**Specified by:** getDefaultRootElement

in class

AbstractDocument
**Returns:** the root
**See Also:** Document.getDefaultRootElement()

- create

```java
protected void create​(
DefaultStyledDocument.ElementSpec
[] data)
```

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method. If the
document contained any data it will first be removed.

**Parameters:** data

- the element data

- insert

```java
protected void insert​(int offset,

DefaultStyledDocument.ElementSpec
[] data)
throws
BadLocationException
```

Inserts new elements in bulk. This is useful to allow
parsing with the document in an unlocked state and
prepare an element structure modification. This method
takes an array of tokens that describe how to update an
element structure so the time within a write lock can
be greatly reduced in an asynchronous update situation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Parameters:** offset

- the starting offset >= 0
**Parameters:** data

- the element data
**Throws:** BadLocationException

- for an invalid starting offset

- removeElement

```java
public void removeElement​(
Element
elem)
```

Removes an element from this document.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

**Parameters:** elem

- the element to remove
**Throws:** NullPointerException

- if the element is

null
**Throws:** IllegalArgumentException

- if the element could not be removed
**Throws:** IllegalStateException

- if the element structure is invalid
**Since:** 1.7

- addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Specified by:** addStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

- removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Specified by:** removeStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style to remove

- getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Specified by:** getStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style
**Returns:** the style

- getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the list of style names.

**Returns:** all the style names

- setLogicalStyle

```java
public void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setLogicalStyle

in interface

StyledDocument
**Parameters:** pos

- the offset from the start of the document >= 0
**Parameters:** s

- the logical style to assign to the paragraph, null if none

- getLogicalStyle

```java
public
Style
getLogicalStyle​(int p)
```

Fetches the logical style assigned to the paragraph
represented by the given position.

**Specified by:** getLogicalStyle

in interface

StyledDocument
**Parameters:** p

- the location to translate to a paragraph
and determine the logical style assigned >= 0. This
is an offset from the start of the document.
**Returns:** the style, null if none

- setCharacterAttributes

```java
public void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for some part of the document.
A write lock is held by this operation while changes
are being made, and a DocumentEvent is sent to the listeners
after the change has been successfully completed.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setCharacterAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset in the document >= 0
**Parameters:** length

- the length >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- true if the previous attributes should be replaced
before setting the new attributes

- setParagraphAttributes

```java
public void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for a paragraph.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setParagraphAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset into the paragraph >= 0
**Parameters:** length

- the number of characters affected >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- whether to replace existing attributes, or merge them

- getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Gets the paragraph element at the offset

pos

.
A paragraph consists of at least one child Element, which is usually
a leaf.

**Specified by:** getParagraphElement

in interface

StyledDocument
**Specified by:** getParagraphElement

in class

AbstractDocument
**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

- getCharacterElement

```java
public
Element
getCharacterElement​(int pos)
```

Gets a character element based on a position.

**Specified by:** getCharacterElement

in interface

StyledDocument
**Parameters:** pos

- the position in the document >= 0
**Returns:** the element

- insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. This implementation simply
parses the inserted content for line breaks and builds up a set
of instructions for the element buffer.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change
**Parameters:** attr

- the attributes

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates document structure as a result of text removal.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change

- createDefaultRoot

```java
protected
AbstractDocument.AbstractElement
createDefaultRoot()
```

Creates the root element to be used to represent the
default document structure.

**Returns:** the element base

- getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Gets the foreground color from an attribute set.

**Specified by:** getForeground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

- getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Gets the background color from an attribute set.

**Specified by:** getBackground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

- getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set.

**Specified by:** getFont

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the font

- styleChanged

```java
protected void styleChanged​(
Style
style)
```

Called when any of this document's styles have changed.
Subclasses may wish to be intelligent about what gets damaged.

**Parameters:** style

- The Style that has changed.

- addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Overrides:** addDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Overrides:** removeDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### Method Detail

getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element.

**Specified by:** getDefaultRootElement

in interface

Document
**Specified by:** getDefaultRootElement

in class

AbstractDocument
**Returns:** the root
**See Also:** Document.getDefaultRootElement()

---

#### getDefaultRootElement

public

Element

getDefaultRootElement()

Gets the default root element.

create

```java
protected void create​(
DefaultStyledDocument.ElementSpec
[] data)
```

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method. If the
document contained any data it will first be removed.

**Parameters:** data

- the element data

---

#### create

protected void create​(

DefaultStyledDocument.ElementSpec

[] data)

Initialize the document to reflect the given element
structure (i.e. the structure reported by the

getDefaultRootElement

method. If the
document contained any data it will first be removed.

insert

```java
protected void insert​(int offset,

DefaultStyledDocument.ElementSpec
[] data)
throws
BadLocationException
```

Inserts new elements in bulk. This is useful to allow
parsing with the document in an unlocked state and
prepare an element structure modification. This method
takes an array of tokens that describe how to update an
element structure so the time within a write lock can
be greatly reduced in an asynchronous update situation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Parameters:** offset

- the starting offset >= 0
**Parameters:** data

- the element data
**Throws:** BadLocationException

- for an invalid starting offset

---

#### insert

protected void insert​(int offset,

DefaultStyledDocument.ElementSpec

[] data)
throws

BadLocationException

Inserts new elements in bulk. This is useful to allow
parsing with the document in an unlocked state and
prepare an element structure modification. This method
takes an array of tokens that describe how to update an
element structure so the time within a write lock can
be greatly reduced in an asynchronous update situation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

removeElement

```java
public void removeElement​(
Element
elem)
```

Removes an element from this document.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

**Parameters:** elem

- the element to remove
**Throws:** NullPointerException

- if the element is

null
**Throws:** IllegalArgumentException

- if the element could not be removed
**Throws:** IllegalStateException

- if the element structure is invalid
**Since:** 1.7

---

#### removeElement

public void removeElement​(

Element

elem)

Removes an element from this document.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

The element is removed from its parent element, as well as
the text in the range identified by the element. If the
element isn't associated with the document,

IllegalArgumentException

is thrown.

As empty branch elements are not allowed in the document, if the
element is the sole child, its parent element is removed as well,
recursively. This means that when replacing all the children of a
particular element, new children should be added

before

removing old children.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

Element removal results in two events being fired, the

DocumentEvent

for changes in element structure and

UndoableEditEvent

for changes in document content.

If the element contains end-of-content mark (the last

"\n"

character in document), this character is not removed;
instead, preceding leaf element is extended to cover the
character. If the last leaf already ends with

"\n",

it is
included in content removal.

If the element is

null,

NullPointerException

is
thrown. If the element structure would become invalid after the removal,
for example if the element is the document root element,

IllegalArgumentException

is thrown. If the current element structure is
invalid,

IllegalStateException

is thrown.

addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Specified by:** addStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

---

#### addStyle

public

Style

addStyle​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Specified by:** removeStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style to remove

---

#### removeStyle

public void removeStyle​(

String

nm)

Removes a named style previously added to the document.

getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Specified by:** getStyle

in interface

StyledDocument
**Parameters:** nm

- the name of the style
**Returns:** the style

---

#### getStyle

public

Style

getStyle​(

String

nm)

Fetches a named style previously added.

getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the list of style names.

**Returns:** all the style names

---

#### getStyleNames

public

Enumeration

<?> getStyleNames()

Fetches the list of style names.

setLogicalStyle

```java
public void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setLogicalStyle

in interface

StyledDocument
**Parameters:** pos

- the offset from the start of the document >= 0
**Parameters:** s

- the logical style to assign to the paragraph, null if none

---

#### setLogicalStyle

public void setLogicalStyle​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getLogicalStyle

```java
public
Style
getLogicalStyle​(int p)
```

Fetches the logical style assigned to the paragraph
represented by the given position.

**Specified by:** getLogicalStyle

in interface

StyledDocument
**Parameters:** p

- the location to translate to a paragraph
and determine the logical style assigned >= 0. This
is an offset from the start of the document.
**Returns:** the style, null if none

---

#### getLogicalStyle

public

Style

getLogicalStyle​(int p)

Fetches the logical style assigned to the paragraph
represented by the given position.

setCharacterAttributes

```java
public void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for some part of the document.
A write lock is held by this operation while changes
are being made, and a DocumentEvent is sent to the listeners
after the change has been successfully completed.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setCharacterAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset in the document >= 0
**Parameters:** length

- the length >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- true if the previous attributes should be replaced
before setting the new attributes

---

#### setCharacterAttributes

public void setCharacterAttributes​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for some part of the document.
A write lock is held by this operation while changes
are being made, and a DocumentEvent is sent to the listeners
after the change has been successfully completed.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

setParagraphAttributes

```java
public void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets attributes for a paragraph.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** setParagraphAttributes

in interface

StyledDocument
**Parameters:** offset

- the offset into the paragraph >= 0
**Parameters:** length

- the number of characters affected >= 0
**Parameters:** s

- the attributes
**Parameters:** replace

- whether to replace existing attributes, or merge them

---

#### setParagraphAttributes

public void setParagraphAttributes​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets attributes for a paragraph.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Gets the paragraph element at the offset

pos

.
A paragraph consists of at least one child Element, which is usually
a leaf.

**Specified by:** getParagraphElement

in interface

StyledDocument
**Specified by:** getParagraphElement

in class

AbstractDocument
**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

---

#### getParagraphElement

public

Element

getParagraphElement​(int pos)

Gets the paragraph element at the offset

pos

.
A paragraph consists of at least one child Element, which is usually
a leaf.

getCharacterElement

```java
public
Element
getCharacterElement​(int pos)
```

Gets a character element based on a position.

**Specified by:** getCharacterElement

in interface

StyledDocument
**Parameters:** pos

- the position in the document >= 0
**Returns:** the element

---

#### getCharacterElement

public

Element

getCharacterElement​(int pos)

Gets a character element based on a position.

insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. This implementation simply
parses the inserted content for line breaks and builds up a set
of instructions for the element buffer.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change
**Parameters:** attr

- the attributes

---

#### insertUpdate

protected void insertUpdate​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. This implementation simply
parses the inserted content for line breaks and builds up a set
of instructions for the element buffer.

removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates document structure as a result of text removal.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- a description of the document change

---

#### removeUpdate

protected void removeUpdate​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates document structure as a result of text removal.

createDefaultRoot

```java
protected
AbstractDocument.AbstractElement
createDefaultRoot()
```

Creates the root element to be used to represent the
default document structure.

**Returns:** the element base

---

#### createDefaultRoot

protected

AbstractDocument.AbstractElement

createDefaultRoot()

Creates the root element to be used to represent the
default document structure.

getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Gets the foreground color from an attribute set.

**Specified by:** getForeground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

---

#### getForeground

public

Color

getForeground​(

AttributeSet

attr)

Gets the foreground color from an attribute set.

getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Gets the background color from an attribute set.

**Specified by:** getBackground

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the color

---

#### getBackground

public

Color

getBackground​(

AttributeSet

attr)

Gets the background color from an attribute set.

getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set.

**Specified by:** getFont

in interface

StyledDocument
**Parameters:** attr

- the attribute set
**Returns:** the font

---

#### getFont

public

Font

getFont​(

AttributeSet

attr)

Gets the font from an attribute set.

styleChanged

```java
protected void styleChanged​(
Style
style)
```

Called when any of this document's styles have changed.
Subclasses may wish to be intelligent about what gets damaged.

**Parameters:** style

- The Style that has changed.

---

#### styleChanged

protected void styleChanged​(

Style

style)

Called when any of this document's styles have changed.
Subclasses may wish to be intelligent about what gets damaged.

addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Overrides:** addDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

---

#### addDocumentListener

public void addDocumentListener​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Overrides:** removeDocumentListener

in class

AbstractDocument
**Parameters:** listener

- the listener
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### removeDocumentListener

public void removeDocumentListener​(

DocumentListener

listener)

Removes a document listener.

---

