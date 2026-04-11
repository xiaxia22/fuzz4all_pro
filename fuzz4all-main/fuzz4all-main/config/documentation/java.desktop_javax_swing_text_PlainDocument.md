# Class PlainDocument

**Source:** `java.desktop\javax\swing\text\PlainDocument.html`

### Class Description

```java
public class
PlainDocument

extends
AbstractDocument
```

A plain document that maintains no character attributes. The
default element structure for this document is a map of the lines in
the text. The Element returned by getDefaultRootElement is
a map of the lines, and each child element represents a line.
This model does not maintain any character level attributes,
but each line can be tagged with an arbitrary set of attributes.
Line to offset, and offset to line translations can be quickly
performed using the default root element. The structure information
of the DocumentEvent's fired by edits will indicate the line
structure changes.

The default content storage management is performed by a
gapped buffer implementation (GapContent). It supports
editing reasonably large documents with good efficiency when
the edits are contiguous or clustered, as is typical.

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

---

### Field Details

#### public static final
String
tabSizeAttribute

Name of the attribute that specifies the tab
size for tabs contained in the content. The
type for the value is Integer.

**See Also:**
- Constant Field Values

---

#### public static final
String
lineLimitAttribute

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.
The type for the value is Integer.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public PlainDocument()

Constructs a plain text document. A default model using

GapContent

is constructed and set.

---

#### public PlainDocument​(
AbstractDocument.Content
c)

Constructs a plain text document. A default root element is created,
and the tab size set to 8.

**Parameters:**
- c

- the container for the content

---

### Method Details

#### public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- insertString

in interface

Document

**Overrides:**
- insertString

in class

AbstractDocument

**Parameters:**
- offs

- the starting offset >= 0
- str

- the string to insert; does nothing with null/empty strings
- a

- the attributes for the inserted content

**Throws:**
- BadLocationException

- the given insert position is not a valid
position within the document

**See Also:**
- Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

---

#### public
Element
getDefaultRootElement()

Gets the default root element for the document model.

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

#### protected
AbstractDocument.AbstractElement
createDefaultRoot()

Creates the root element to be used to represent the
default document structure.

**Returns:**
- the element base

---

#### public
Element
getParagraphElement​(int pos)

Get the paragraph element containing the given position. Since this
document only models lines, it returns the line instead.

**Specified by:**
- getParagraphElement

in class

AbstractDocument

**Parameters:**
- pos

- the starting offset >= 0

**Returns:**
- the element

---

#### protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. Since this document simply
maps out lines, we refresh the line map.

**Overrides:**
- insertUpdate

in class

AbstractDocument

**Parameters:**
- chng

- the change event describing the dit
- attr

- the set of attributes for the inserted text

---

#### protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)

Updates any document structure as a result of text removal.
This will happen within a write lock. Since the structure
represents a line map, this just checks to see if the
removal spans lines. If it does, the two lines outside
of the removal area are joined together.

**Overrides:**
- removeUpdate

in class

AbstractDocument

**Parameters:**
- chng

- the change event describing the edit

---

### Additional Sections

#### Class PlainDocument

java.lang.Object

- javax.swing.text.AbstractDocument
- - javax.swing.text.PlainDocument

javax.swing.text.AbstractDocument

- javax.swing.text.PlainDocument

javax.swing.text.PlainDocument

**All Implemented Interfaces:** Serializable

,

Document

```java
public class
PlainDocument

extends
AbstractDocument
```

A plain document that maintains no character attributes. The
default element structure for this document is a map of the lines in
the text. The Element returned by getDefaultRootElement is
a map of the lines, and each child element represents a line.
This model does not maintain any character level attributes,
but each line can be tagged with an arbitrary set of attributes.
Line to offset, and offset to line translations can be quickly
performed using the default root element. The structure information
of the DocumentEvent's fired by edits will indicate the line
structure changes.

The default content storage management is performed by a
gapped buffer implementation (GapContent). It supports
editing reasonably large documents with good efficiency when
the edits are contiguous or clustered, as is typical.

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

PlainDocument

extends

AbstractDocument

A plain document that maintains no character attributes. The
default element structure for this document is a map of the lines in
the text. The Element returned by getDefaultRootElement is
a map of the lines, and each child element represents a line.
This model does not maintain any character level attributes,
but each line can be tagged with an arbitrary set of attributes.
Line to offset, and offset to line translations can be quickly
performed using the default root element. The structure information
of the DocumentEvent's fired by edits will indicate the line
structure changes.

The default content storage management is performed by a
gapped buffer implementation (GapContent). It supports
editing reasonably large documents with good efficiency when
the edits are contiguous or clustered, as is typical.

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

The default content storage management is performed by a
gapped buffer implementation (GapContent). It supports
editing reasonably large documents with good efficiency when
the edits are contiguous or clustered, as is typical.

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

static

String

lineLimitAttribute

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.

static

String

tabSizeAttribute

Name of the attribute that specifies the tab
size for tabs contained in the content.

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

PlainDocument

()

Constructs a plain text document.

PlainDocument

​(

AbstractDocument.Content

c)

Constructs a plain text document.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AbstractDocument.AbstractElement

createDefaultRoot

()

Creates the root element to be used to represent the
default document structure.

Element

getDefaultRootElement

()

Gets the default root element for the document model.

Element

getParagraphElement

​(int pos)

Get the paragraph element containing the given position.

void

insertString

​(int offs,

String

str,

AttributeSet

a)

Inserts some content into the document.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

- Methods declared in class javax.swing.text.

AbstractDocument

addDocumentListener

,

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

removeDocumentListener

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

Nested Class Summary

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

static

String

lineLimitAttribute

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.

static

String

tabSizeAttribute

Name of the attribute that specifies the tab
size for tabs contained in the content.

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

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.

Name of the attribute that specifies the tab
size for tabs contained in the content.

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

PlainDocument

()

Constructs a plain text document.

PlainDocument

​(

AbstractDocument.Content

c)

Constructs a plain text document.

---

#### Constructor Summary

Constructs a plain text document.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AbstractDocument.AbstractElement

createDefaultRoot

()

Creates the root element to be used to represent the
default document structure.

Element

getDefaultRootElement

()

Gets the default root element for the document model.

Element

getParagraphElement

​(int pos)

Get the paragraph element containing the given position.

void

insertString

​(int offs,

String

str,

AttributeSet

a)

Inserts some content into the document.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

- Methods declared in class javax.swing.text.

AbstractDocument

addDocumentListener

,

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

removeDocumentListener

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

---

#### Method Summary

Creates the root element to be used to represent the
default document structure.

Gets the default root element for the document model.

Get the paragraph element containing the given position.

Inserts some content into the document.

Updates document structure as a result of text insertion.

Updates any document structure as a result of text removal.

Methods declared in class javax.swing.text.

AbstractDocument

addDocumentListener

,

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

removeDocumentListener

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

============ FIELD DETAIL ===========

- Field Detail

- tabSizeAttribute

```java
public static final
String
tabSizeAttribute
```

Name of the attribute that specifies the tab
size for tabs contained in the content. The
type for the value is Integer.

**See Also:** Constant Field Values

- lineLimitAttribute

```java
public static final
String
lineLimitAttribute
```

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.
The type for the value is Integer.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PlainDocument

```java
public PlainDocument()
```

Constructs a plain text document. A default model using

GapContent

is constructed and set.

- PlainDocument

```java
public PlainDocument​(
AbstractDocument.Content
c)
```

Constructs a plain text document. A default root element is created,
and the tab size set to 8.

**Parameters:** c

- the container for the content

============ METHOD DETAIL ==========

- Method Detail

- insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Overrides:** insertString

in class

AbstractDocument
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

- getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element for the document model.

**Specified by:** getDefaultRootElement

in interface

Document
**Specified by:** getDefaultRootElement

in class

AbstractDocument
**Returns:** the root
**See Also:** Document.getDefaultRootElement()

- createDefaultRoot

```java
protected
AbstractDocument.AbstractElement
createDefaultRoot()
```

Creates the root element to be used to represent the
default document structure.

**Returns:** the element base

- getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Since this
document only models lines, it returns the line instead.

**Specified by:** getParagraphElement

in class

AbstractDocument
**Parameters:** pos

- the starting offset >= 0
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
will happen within a write lock. Since this document simply
maps out lines, we refresh the line map.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the dit
**Parameters:** attr

- the set of attributes for the inserted text

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal.
This will happen within a write lock. Since the structure
represents a line map, this just checks to see if the
removal spans lines. If it does, the two lines outside
of the removal area are joined together.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the edit

Field Detail

- tabSizeAttribute

```java
public static final
String
tabSizeAttribute
```

Name of the attribute that specifies the tab
size for tabs contained in the content. The
type for the value is Integer.

**See Also:** Constant Field Values

- lineLimitAttribute

```java
public static final
String
lineLimitAttribute
```

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.
The type for the value is Integer.

**See Also:** Constant Field Values

---

#### Field Detail

tabSizeAttribute

```java
public static final
String
tabSizeAttribute
```

Name of the attribute that specifies the tab
size for tabs contained in the content. The
type for the value is Integer.

**See Also:** Constant Field Values

---

#### tabSizeAttribute

public static final

String

tabSizeAttribute

Name of the attribute that specifies the tab
size for tabs contained in the content. The
type for the value is Integer.

lineLimitAttribute

```java
public static final
String
lineLimitAttribute
```

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.
The type for the value is Integer.

**See Also:** Constant Field Values

---

#### lineLimitAttribute

public static final

String

lineLimitAttribute

Name of the attribute that specifies the maximum
length of a line, if there is a maximum length.
The type for the value is Integer.

Constructor Detail

- PlainDocument

```java
public PlainDocument()
```

Constructs a plain text document. A default model using

GapContent

is constructed and set.

- PlainDocument

```java
public PlainDocument​(
AbstractDocument.Content
c)
```

Constructs a plain text document. A default root element is created,
and the tab size set to 8.

**Parameters:** c

- the container for the content

---

#### Constructor Detail

PlainDocument

```java
public PlainDocument()
```

Constructs a plain text document. A default model using

GapContent

is constructed and set.

---

#### PlainDocument

public PlainDocument()

Constructs a plain text document. A default model using

GapContent

is constructed and set.

PlainDocument

```java
public PlainDocument​(
AbstractDocument.Content
c)
```

Constructs a plain text document. A default root element is created,
and the tab size set to 8.

**Parameters:** c

- the container for the content

---

#### PlainDocument

public PlainDocument​(

AbstractDocument.Content

c)

Constructs a plain text document. A default root element is created,
and the tab size set to 8.

Method Detail

- insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Overrides:** insertString

in class

AbstractDocument
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

- getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element for the document model.

**Specified by:** getDefaultRootElement

in interface

Document
**Specified by:** getDefaultRootElement

in class

AbstractDocument
**Returns:** the root
**See Also:** Document.getDefaultRootElement()

- createDefaultRoot

```java
protected
AbstractDocument.AbstractElement
createDefaultRoot()
```

Creates the root element to be used to represent the
default document structure.

**Returns:** the element base

- getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Since this
document only models lines, it returns the line instead.

**Specified by:** getParagraphElement

in class

AbstractDocument
**Parameters:** pos

- the starting offset >= 0
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
will happen within a write lock. Since this document simply
maps out lines, we refresh the line map.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the dit
**Parameters:** attr

- the set of attributes for the inserted text

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal.
This will happen within a write lock. Since the structure
represents a line map, this just checks to see if the
removal spans lines. If it does, the two lines outside
of the removal area are joined together.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the edit

---

#### Method Detail

insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Overrides:** insertString

in class

AbstractDocument
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

---

#### insertString

public void insertString​(int offs,

String

str,

AttributeSet

a)
throws

BadLocationException

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

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

getDefaultRootElement

```java
public
Element
getDefaultRootElement()
```

Gets the default root element for the document model.

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

Gets the default root element for the document model.

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

getParagraphElement

```java
public
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Since this
document only models lines, it returns the line instead.

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

Get the paragraph element containing the given position. Since this
document only models lines, it returns the line instead.

insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. Since this document simply
maps out lines, we refresh the line map.

**Overrides:** insertUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the dit
**Parameters:** attr

- the set of attributes for the inserted text

---

#### insertUpdate

protected void insertUpdate​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. Since this document simply
maps out lines, we refresh the line map.

removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal.
This will happen within a write lock. Since the structure
represents a line map, this just checks to see if the
removal spans lines. If it does, the two lines outside
of the removal area are joined together.

**Overrides:** removeUpdate

in class

AbstractDocument
**Parameters:** chng

- the change event describing the edit

---

#### removeUpdate

protected void removeUpdate​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.
This will happen within a write lock. Since the structure
represents a line map, this just checks to see if the
removal spans lines. If it does, the two lines outside
of the removal area are joined together.

---

