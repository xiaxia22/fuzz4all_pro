# Interface Document

**Source:** `java.desktop\javax\swing\text\Document.html`

### Class Description

```java
public interface
Document
```

The

Document

is a container for text that serves
as the model for swing text components. The goal for this
interface is to scale from very simple needs (a plain text textfield)
to complex needs (an HTML or XML document, for example).

Content

At the simplest level, text can be
modeled as a linear sequence of characters. To support
internationalization, the Swing text model uses

unicode

characters.
The sequence of characters displayed in a text component is
generally referred to as the component's

content

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

**All Known Subinterfaces:** StyledDocument

---

### Field Details

#### static final
String
StreamDescriptionProperty

The property name for the description of the stream
used to initialize the document. This should be used
if the document was initialized from a stream and
anything is known about the stream.

**See Also:**
- Constant Field Values

---

#### static final
String
TitleProperty

The property name for the title of the document, if
there is one.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getLength()

Returns number of characters of content currently
in the document.

**Returns:**
- number of characters >= 0

---

#### void addDocumentListener​(
DocumentListener
listener)

Registers the given observer to begin receiving notifications
when changes are made to the document.

**Parameters:**
- listener

- the observer to register

**See Also:**
- removeDocumentListener(javax.swing.event.DocumentListener)

---

#### void removeDocumentListener​(
DocumentListener
listener)

Unregisters the given observer from the notification list
so it will no longer receive change updates.

**Parameters:**
- listener

- the observer to register

**See Also:**
- addDocumentListener(javax.swing.event.DocumentListener)

---

#### void addUndoableEditListener​(
UndoableEditListener
listener)

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

**Parameters:**
- listener

- the observer to register

**See Also:**
- UndoableEditEvent

---

#### void removeUndoableEditListener​(
UndoableEditListener
listener)

Unregisters the given observer from the notification list
so it will no longer receive updates.

**Parameters:**
- listener

- the observer to register

**See Also:**
- UndoableEditEvent

---

#### Object
getProperty​(
Object
key)

Gets the properties associated with the document.

**Parameters:**
- key

- a non-

null

property key

**Returns:**
- the properties

**See Also:**
- putProperty(Object, Object)

---

#### void putProperty​(
Object
key,

Object
value)

Associates a property with the document. Two standard
property keys provided are:

StreamDescriptionProperty

and

TitleProperty

.
Other properties, such as author, may also be defined.

**Parameters:**
- key

- the non-

null

property key
- value

- the property value

**See Also:**
- getProperty(Object)

---

#### void remove​(int offs,
int len)
throws
BadLocationException

Removes a portion of the content of the document.
This will cause a DocumentEvent of type
DocumentEvent.EventType.REMOVE to be sent to the
registered DocumentListeners, unless an exception
is thrown. The notification will be sent to the
listeners by calling the removeUpdate method on the
DocumentListeners.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:**
- offs

- the offset from the beginning >= 0
- len

- the number of characters to remove >= 0

**Throws:**
- BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

**See Also:**
- DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

---

#### void insertString​(int offset,

String
str,

AttributeSet
a)
throws
BadLocationException

Inserts a string of content. This will cause a DocumentEvent
of type DocumentEvent.EventType.INSERT to be sent to the
registered DocumentListers, unless an exception is thrown.
The DocumentEvent will be delivered by calling the
insertUpdate method on the DocumentListener.
The offset and length of the generated DocumentEvent
will indicate what change was actually made to the Document.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:**
- offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
- str

- the string to insert
- a

- the attributes to associate with the inserted
content. This may be null if there are no attributes.

**Throws:**
- BadLocationException

- the given insert position is not a valid
position within the document

**See Also:**
- DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

---

#### String
getText​(int offset,
int length)
throws
BadLocationException

Fetches the text contained within the given portion
of the document.

**Parameters:**
- offset

- the offset into the document representing the desired
start of the text >= 0
- length

- the length of the desired string >= 0

**Returns:**
- the text, in a String of length >= 0

**Throws:**
- BadLocationException

- some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

**Parameters:**
- offset

- the offset into the document representing the desired
start of the text >= 0
- length

- the length of the desired string >= 0
- txt

- the Segment object to return the text in

**Throws:**
- BadLocationException

- Some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### Position
getStartPosition()

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Returns:**
- the position

---

#### Position
getEndPosition()

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Returns:**
- the position

---

#### Position
createPosition​(int offs)
throws
BadLocationException

This method allows an application to mark a place in
a sequence of character content. This mark can then be
used to tracks change as insertions and removals are made
in the content. The policy is that insertions always
occur prior to the current position (the most common case)
unless the insertion location is zero, in which case the
insertion is forced to a position that follows the
original position.

**Parameters:**
- offs

- the offset from the start of the document >= 0

**Returns:**
- the position

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### Element
[] getRootElements()

Returns all of the root elements that are defined.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

- Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

**Returns:**
- the root element

---

#### Element
getDefaultRootElement()

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

**Returns:**
- the root element

---

#### void render​(
Runnable
r)

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

**Parameters:**
- r

- a

Runnable

used to render the model

---

### Additional Sections

#### Interface Document

**All Known Subinterfaces:** StyledDocument

**All Known Implementing Classes:** AbstractDocument

,

DefaultStyledDocument

,

HTMLDocument

,

PlainDocument

```java
public interface
Document
```

The

Document

is a container for text that serves
as the model for swing text components. The goal for this
interface is to scale from very simple needs (a plain text textfield)
to complex needs (an HTML or XML document, for example).

Content

At the simplest level, text can be
modeled as a linear sequence of characters. To support
internationalization, the Swing text model uses

unicode

characters.
The sequence of characters displayed in a text component is
generally referred to as the component's

content

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

,

Element

,

Position

,

AttributeSet

public interface

Document

The

Document

is a container for text that serves
as the model for swing text components. The goal for this
interface is to scale from very simple needs (a plain text textfield)
to complex needs (an HTML or XML document, for example).

Content

At the simplest level, text can be
modeled as a linear sequence of characters. To support
internationalization, the Swing text model uses

unicode

characters.
The sequence of characters displayed in a text component is
generally referred to as the component's

content

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Content

At the simplest level, text can be
modeled as a linear sequence of characters. To support
internationalization, the Swing text model uses

unicode

characters.
The sequence of characters displayed in a text component is
generally referred to as the component's

content

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

At the simplest level, text can be
modeled as a linear sequence of characters. To support
internationalization, the Swing text model uses

unicode

characters.
The sequence of characters displayed in a text component is
generally referred to as the component's

content

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

To refer to locations within the sequence, the coordinates
used are the location between two characters. As the diagram
below shows, a location in a text document can be referred to
as a position, or an offset. This position is zero-based.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

In the example, if the content of a document is the
sequence "The quick brown fox," as shown in the preceding diagram,
the location just before the word "The" is 0, and the location after
the word "The" and before the whitespace that follows it is 3.
The entire sequence of characters in the sequence "The" is called a

range

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

The following methods give access to the character data
that makes up the content.

- getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

getLength()

getText(int, int)

getText(int, int, javax.swing.text.Segment)

Structure

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Text is rarely represented simply as featureless content. Rather,
text typically has some sort of structure associated with it.
Exactly what structure is modeled is up to a particular Document
implementation. It might be as simple as no structure (i.e. a
simple text field), or it might be something like diagram below.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

The unit of structure (i.e. a node of the tree) is referred to
by the

Element

interface. Each Element
can be tagged with a set of attributes. These attributes
(name/value pairs) are defined by the

AttributeSet

interface.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

The following methods give access to the document structure.

- getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

getDefaultRootElement()

getRootElements()

Mutations

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

All documents need to be able to add and remove simple text.
Typically, text is inserted and removed via gestures from
a keyboard or a mouse. What effect the insertion or removal
has upon the document structure is entirely up to the
implementation of the document.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

The following methods are related to mutation of the
document content:

- insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

insertString(int, java.lang.String, javax.swing.text.AttributeSet)

remove(int, int)

createPosition(int)

Notification

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Mutations to the

Document

must be communicated to
interested observers. The notification of change follows the event model
guidelines that are specified for JavaBeans. In the JavaBeans
event model, once an event notification is dispatched, all listeners
must be notified before any further mutations occur to the source
of the event. Further, order of delivery is not guaranteed.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Notification is provided as two separate events,

DocumentEvent

, and

UndoableEditEvent

.
If a mutation is made to a

Document

through its api,
a

DocumentEvent

will be sent to all of the registered

DocumentListeners

. If the

Document

implementation supports undo/redo capabilities, an

UndoableEditEvent

will be sent
to all of the registered

UndoableEditListener

s.
If an undoable edit is undone, a

DocumentEvent

should be
fired from the Document to indicate it has changed again.
In this case however, there should be no

UndoableEditEvent

generated since that edit is actually the source of the change
rather than a mutation to the

Document

made through its
api.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Referring to the above diagram, suppose that the component shown
on the left mutates the document object represented by the blue
rectangle. The document responds by dispatching a DocumentEvent to
both component views and sends an UndoableEditEvent to the listening
logic, which maintains a history buffer.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Now suppose that the component shown on the right mutates the same
document. Again, the document dispatches a DocumentEvent to both
component views and sends an UndoableEditEvent to the listening logic
that is maintaining the history buffer.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

If the history buffer is then rolled back (i.e. the last UndoableEdit
undone), a DocumentEvent is sent to both views, causing both of them to
reflect the undone mutation to the document (that is, the
removal of the right component's mutation). If the history buffer again
rolls back another change, another DocumentEvent is sent to both views,
causing them to reflect the undone mutation to the document -- that is,
the removal of the left component's mutation.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

The methods related to observing mutations to the document are:

- addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

addDocumentListener(DocumentListener)

removeDocumentListener(DocumentListener)

addUndoableEditListener(UndoableEditListener)

removeUndoableEditListener(UndoableEditListener)

Properties

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

Document implementations will generally have some set of properties
associated with them at runtime. Two well known properties are the

StreamDescriptionProperty

,
which can be used to describe where the

Document

came from,
and the

TitleProperty

, which can be used to
name the

Document

. The methods related to the properties are:

- getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

getProperty(java.lang.Object)

putProperty(java.lang.Object, java.lang.Object)

For more information on the

Document

class, see

The Swing Connection

and most particularly the article,

The Element Interface

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

StreamDescriptionProperty

The property name for the description of the stream
used to initialize the document.

static

String

TitleProperty

The property name for the title of the document, if
there is one.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Registers the given observer to begin receiving notifications
when changes are made to the document.

void

addUndoableEditListener

​(

UndoableEditListener

listener)

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

Position

createPosition

​(int offs)

This method allows an application to mark a place in
a sequence of character content.

Element

getDefaultRootElement

()

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

Position

getEndPosition

()

Returns a position that represents the end of the document.

int

getLength

()

Returns number of characters of content currently
in the document.

Object

getProperty

​(

Object

key)

Gets the properties associated with the document.

Element

[]

getRootElements

()

Returns all of the root elements that are defined.

Position

getStartPosition

()

Returns a position that represents the start of the document.

String

getText

​(int offset,
int length)

Fetches the text contained within the given portion
of the document.

void

getText

​(int offset,
int length,

Segment

txt)

Fetches the text contained within the given portion
of the document.

void

insertString

​(int offset,

String

str,

AttributeSet

a)

Inserts a string of content.

void

putProperty

​(

Object

key,

Object

value)

Associates a property with the document.

void

remove

​(int offs,
int len)

Removes a portion of the content of the document.

void

removeDocumentListener

​(

DocumentListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive change updates.

void

removeUndoableEditListener

​(

UndoableEditListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive updates.

void

render

​(

Runnable

r)

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

StreamDescriptionProperty

The property name for the description of the stream
used to initialize the document.

static

String

TitleProperty

The property name for the title of the document, if
there is one.

---

#### Field Summary

The property name for the description of the stream
used to initialize the document.

The property name for the title of the document, if
there is one.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Registers the given observer to begin receiving notifications
when changes are made to the document.

void

addUndoableEditListener

​(

UndoableEditListener

listener)

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

Position

createPosition

​(int offs)

This method allows an application to mark a place in
a sequence of character content.

Element

getDefaultRootElement

()

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

Position

getEndPosition

()

Returns a position that represents the end of the document.

int

getLength

()

Returns number of characters of content currently
in the document.

Object

getProperty

​(

Object

key)

Gets the properties associated with the document.

Element

[]

getRootElements

()

Returns all of the root elements that are defined.

Position

getStartPosition

()

Returns a position that represents the start of the document.

String

getText

​(int offset,
int length)

Fetches the text contained within the given portion
of the document.

void

getText

​(int offset,
int length,

Segment

txt)

Fetches the text contained within the given portion
of the document.

void

insertString

​(int offset,

String

str,

AttributeSet

a)

Inserts a string of content.

void

putProperty

​(

Object

key,

Object

value)

Associates a property with the document.

void

remove

​(int offs,
int len)

Removes a portion of the content of the document.

void

removeDocumentListener

​(

DocumentListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive change updates.

void

removeUndoableEditListener

​(

UndoableEditListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive updates.

void

render

​(

Runnable

r)

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.

---

#### Method Summary

Registers the given observer to begin receiving notifications
when changes are made to the document.

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

This method allows an application to mark a place in
a sequence of character content.

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

Returns a position that represents the end of the document.

Returns number of characters of content currently
in the document.

Gets the properties associated with the document.

Returns all of the root elements that are defined.

Returns a position that represents the start of the document.

Fetches the text contained within the given portion
of the document.

Inserts a string of content.

Associates a property with the document.

Removes a portion of the content of the document.

Unregisters the given observer from the notification list
so it will no longer receive change updates.

Unregisters the given observer from the notification list
so it will no longer receive updates.

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.

============ FIELD DETAIL ===========

- Field Detail

- StreamDescriptionProperty

```java
static final
String
StreamDescriptionProperty
```

The property name for the description of the stream
used to initialize the document. This should be used
if the document was initialized from a stream and
anything is known about the stream.

**See Also:** Constant Field Values

- TitleProperty

```java
static final
String
TitleProperty
```

The property name for the title of the document, if
there is one.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

Returns number of characters of content currently
in the document.

**Returns:** number of characters >= 0

- addDocumentListener

```java
void addDocumentListener​(
DocumentListener
listener)
```

Registers the given observer to begin receiving notifications
when changes are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** removeDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
void removeDocumentListener​(
DocumentListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive change updates.

**Parameters:** listener

- the observer to register
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

- addUndoableEditListener

```java
void addUndoableEditListener​(
UndoableEditListener
listener)
```

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

- removeUndoableEditListener

```java
void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive updates.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

- getProperty

```java
Object
getProperty​(
Object
key)
```

Gets the properties associated with the document.

**Parameters:** key

- a non-

null

property key
**Returns:** the properties
**See Also:** putProperty(Object, Object)

- putProperty

```java
void putProperty​(
Object
key,

Object
value)
```

Associates a property with the document. Two standard
property keys provided are:

StreamDescriptionProperty

and

TitleProperty

.
Other properties, such as author, may also be defined.

**Parameters:** key

- the non-

null

property key
**Parameters:** value

- the property value
**See Also:** getProperty(Object)

- remove

```java
void remove​(int offs,
int len)
throws
BadLocationException
```

Removes a portion of the content of the document.
This will cause a DocumentEvent of type
DocumentEvent.EventType.REMOVE to be sent to the
registered DocumentListeners, unless an exception
is thrown. The notification will be sent to the
listeners by calling the removeUpdate method on the
DocumentListeners.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offs

- the offset from the beginning >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

- insertString

```java
void insertString​(int offset,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts a string of content. This will cause a DocumentEvent
of type DocumentEvent.EventType.INSERT to be sent to the
registered DocumentListers, unless an exception is thrown.
The DocumentEvent will be delivered by calling the
insertUpdate method on the DocumentListener.
The offset and length of the generated DocumentEvent
will indicate what change was actually made to the Document.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
**Parameters:** str

- the string to insert
**Parameters:** a

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

- getText

```java
String
getText​(int offset,
int length)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Returns:** the text, in a String of length >= 0
**Throws:** BadLocationException

- some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- getText

```java
void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Parameters:** txt

- the Segment object to return the text in
**Throws:** BadLocationException

- Some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- getStartPosition

```java
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Returns:** the position

- getEndPosition

```java
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Returns:** the position

- createPosition

```java
Position
createPosition​(int offs)
throws
BadLocationException
```

This method allows an application to mark a place in
a sequence of character content. This mark can then be
used to tracks change as insertions and removals are made
in the content. The policy is that insertions always
occur prior to the current position (the most common case)
unless the insertion location is zero, in which case the
insertion is forced to a position that follows the
original position.

**Parameters:** offs

- the offset from the start of the document >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- getRootElements

```java
Element
[] getRootElements()
```

Returns all of the root elements that are defined.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

- Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

**Returns:** the root element

- getDefaultRootElement

```java
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

**Returns:** the root element

- render

```java
void render​(
Runnable
r)
```

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

**Parameters:** r

- a

Runnable

used to render the model

Field Detail

- StreamDescriptionProperty

```java
static final
String
StreamDescriptionProperty
```

The property name for the description of the stream
used to initialize the document. This should be used
if the document was initialized from a stream and
anything is known about the stream.

**See Also:** Constant Field Values

- TitleProperty

```java
static final
String
TitleProperty
```

The property name for the title of the document, if
there is one.

**See Also:** Constant Field Values

---

#### Field Detail

StreamDescriptionProperty

```java
static final
String
StreamDescriptionProperty
```

The property name for the description of the stream
used to initialize the document. This should be used
if the document was initialized from a stream and
anything is known about the stream.

**See Also:** Constant Field Values

---

#### StreamDescriptionProperty

static final

String

StreamDescriptionProperty

The property name for the description of the stream
used to initialize the document. This should be used
if the document was initialized from a stream and
anything is known about the stream.

TitleProperty

```java
static final
String
TitleProperty
```

The property name for the title of the document, if
there is one.

**See Also:** Constant Field Values

---

#### TitleProperty

static final

String

TitleProperty

The property name for the title of the document, if
there is one.

Method Detail

- getLength

```java
int getLength()
```

Returns number of characters of content currently
in the document.

**Returns:** number of characters >= 0

- addDocumentListener

```java
void addDocumentListener​(
DocumentListener
listener)
```

Registers the given observer to begin receiving notifications
when changes are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** removeDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
void removeDocumentListener​(
DocumentListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive change updates.

**Parameters:** listener

- the observer to register
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

- addUndoableEditListener

```java
void addUndoableEditListener​(
UndoableEditListener
listener)
```

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

- removeUndoableEditListener

```java
void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive updates.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

- getProperty

```java
Object
getProperty​(
Object
key)
```

Gets the properties associated with the document.

**Parameters:** key

- a non-

null

property key
**Returns:** the properties
**See Also:** putProperty(Object, Object)

- putProperty

```java
void putProperty​(
Object
key,

Object
value)
```

Associates a property with the document. Two standard
property keys provided are:

StreamDescriptionProperty

and

TitleProperty

.
Other properties, such as author, may also be defined.

**Parameters:** key

- the non-

null

property key
**Parameters:** value

- the property value
**See Also:** getProperty(Object)

- remove

```java
void remove​(int offs,
int len)
throws
BadLocationException
```

Removes a portion of the content of the document.
This will cause a DocumentEvent of type
DocumentEvent.EventType.REMOVE to be sent to the
registered DocumentListeners, unless an exception
is thrown. The notification will be sent to the
listeners by calling the removeUpdate method on the
DocumentListeners.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offs

- the offset from the beginning >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

- insertString

```java
void insertString​(int offset,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts a string of content. This will cause a DocumentEvent
of type DocumentEvent.EventType.INSERT to be sent to the
registered DocumentListers, unless an exception is thrown.
The DocumentEvent will be delivered by calling the
insertUpdate method on the DocumentListener.
The offset and length of the generated DocumentEvent
will indicate what change was actually made to the Document.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
**Parameters:** str

- the string to insert
**Parameters:** a

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

- getText

```java
String
getText​(int offset,
int length)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Returns:** the text, in a String of length >= 0
**Throws:** BadLocationException

- some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- getText

```java
void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Parameters:** txt

- the Segment object to return the text in
**Throws:** BadLocationException

- Some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- getStartPosition

```java
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Returns:** the position

- getEndPosition

```java
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Returns:** the position

- createPosition

```java
Position
createPosition​(int offs)
throws
BadLocationException
```

This method allows an application to mark a place in
a sequence of character content. This mark can then be
used to tracks change as insertions and removals are made
in the content. The policy is that insertions always
occur prior to the current position (the most common case)
unless the insertion location is zero, in which case the
insertion is forced to a position that follows the
original position.

**Parameters:** offs

- the offset from the start of the document >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- getRootElements

```java
Element
[] getRootElements()
```

Returns all of the root elements that are defined.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

- Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

**Returns:** the root element

- getDefaultRootElement

```java
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

**Returns:** the root element

- render

```java
void render​(
Runnable
r)
```

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

**Parameters:** r

- a

Runnable

used to render the model

---

#### Method Detail

getLength

```java
int getLength()
```

Returns number of characters of content currently
in the document.

**Returns:** number of characters >= 0

---

#### getLength

int getLength()

Returns number of characters of content currently
in the document.

addDocumentListener

```java
void addDocumentListener​(
DocumentListener
listener)
```

Registers the given observer to begin receiving notifications
when changes are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** removeDocumentListener(javax.swing.event.DocumentListener)

---

#### addDocumentListener

void addDocumentListener​(

DocumentListener

listener)

Registers the given observer to begin receiving notifications
when changes are made to the document.

removeDocumentListener

```java
void removeDocumentListener​(
DocumentListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive change updates.

**Parameters:** listener

- the observer to register
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

---

#### removeDocumentListener

void removeDocumentListener​(

DocumentListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive change updates.

addUndoableEditListener

```java
void addUndoableEditListener​(
UndoableEditListener
listener)
```

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

---

#### addUndoableEditListener

void addUndoableEditListener​(

UndoableEditListener

listener)

Registers the given observer to begin receiving notifications
when undoable edits are made to the document.

removeUndoableEditListener

```java
void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Unregisters the given observer from the notification list
so it will no longer receive updates.

**Parameters:** listener

- the observer to register
**See Also:** UndoableEditEvent

---

#### removeUndoableEditListener

void removeUndoableEditListener​(

UndoableEditListener

listener)

Unregisters the given observer from the notification list
so it will no longer receive updates.

getProperty

```java
Object
getProperty​(
Object
key)
```

Gets the properties associated with the document.

**Parameters:** key

- a non-

null

property key
**Returns:** the properties
**See Also:** putProperty(Object, Object)

---

#### getProperty

Object

getProperty​(

Object

key)

Gets the properties associated with the document.

putProperty

```java
void putProperty​(
Object
key,

Object
value)
```

Associates a property with the document. Two standard
property keys provided are:

StreamDescriptionProperty

and

TitleProperty

.
Other properties, such as author, may also be defined.

**Parameters:** key

- the non-

null

property key
**Parameters:** value

- the property value
**See Also:** getProperty(Object)

---

#### putProperty

void putProperty​(

Object

key,

Object

value)

Associates a property with the document. Two standard
property keys provided are:

StreamDescriptionProperty

and

TitleProperty

.
Other properties, such as author, may also be defined.

remove

```java
void remove​(int offs,
int len)
throws
BadLocationException
```

Removes a portion of the content of the document.
This will cause a DocumentEvent of type
DocumentEvent.EventType.REMOVE to be sent to the
registered DocumentListeners, unless an exception
is thrown. The notification will be sent to the
listeners by calling the removeUpdate method on the
DocumentListeners.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offs

- the offset from the beginning >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

---

#### remove

void remove​(int offs,
int len)
throws

BadLocationException

Removes a portion of the content of the document.
This will cause a DocumentEvent of type
DocumentEvent.EventType.REMOVE to be sent to the
registered DocumentListeners, unless an exception
is thrown. The notification will be sent to the
listeners by calling the removeUpdate method on the
DocumentListeners.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

To ensure reasonable behavior in the face
of concurrency, the event is dispatched after the
mutation has occurred. This means that by the time a
notification of removal is dispatched, the document
has already been updated and any marks created by

createPosition

have already changed.
For a removal, the end of the removal range is collapsed
down to the start of the range, and any marks in the removal
range are collapsed down to the start of the range.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

If the Document structure changed as result of the removal,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to a
remove.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

insertString

```java
void insertString​(int offset,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts a string of content. This will cause a DocumentEvent
of type DocumentEvent.EventType.INSERT to be sent to the
registered DocumentListers, unless an exception is thrown.
The DocumentEvent will be delivered by calling the
insertUpdate method on the DocumentListener.
The offset and length of the generated DocumentEvent
will indicate what change was actually made to the Document.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
**Parameters:** str

- the string to insert
**Parameters:** a

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** DocumentEvent

,

DocumentListener

,

UndoableEditEvent

,

UndoableEditListener

---

#### insertString

void insertString​(int offset,

String

str,

AttributeSet

a)
throws

BadLocationException

Inserts a string of content. This will cause a DocumentEvent
of type DocumentEvent.EventType.INSERT to be sent to the
registered DocumentListers, unless an exception is thrown.
The DocumentEvent will be delivered by calling the
insertUpdate method on the DocumentListener.
The offset and length of the generated DocumentEvent
will indicate what change was actually made to the Document.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

If the Document structure changed as result of the insertion,
the details of what Elements were inserted and removed in
response to the change will also be contained in the generated
DocumentEvent. It is up to the implementation of a Document
to decide how the structure should change in response to an
insertion.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

If the Document supports undo/redo, an UndoableEditEvent will
also be generated.

getText

```java
String
getText​(int offset,
int length)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Returns:** the text, in a String of length >= 0
**Throws:** BadLocationException

- some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### getText

String

getText​(int offset,
int length)
throws

BadLocationException

Fetches the text contained within the given portion
of the document.

getText

```java
void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

**Parameters:** offset

- the offset into the document representing the desired
start of the text >= 0
**Parameters:** length

- the length of the desired string >= 0
**Parameters:** txt

- the Segment object to return the text in
**Throws:** BadLocationException

- Some portion of the given range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### getText

void getText​(int offset,
int length,

Segment

txt)
throws

BadLocationException

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}
```

int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do someting with text
nleft -= text.count;
offs += text.count;
}

getStartPosition

```java
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Returns:** the position

---

#### getStartPosition

Position

getStartPosition()

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

getEndPosition

```java
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Returns:** the position

---

#### getEndPosition

Position

getEndPosition()

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

createPosition

```java
Position
createPosition​(int offs)
throws
BadLocationException
```

This method allows an application to mark a place in
a sequence of character content. This mark can then be
used to tracks change as insertions and removals are made
in the content. The policy is that insertions always
occur prior to the current position (the most common case)
unless the insertion location is zero, in which case the
insertion is forced to a position that follows the
original position.

**Parameters:** offs

- the offset from the start of the document >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### createPosition

Position

createPosition​(int offs)
throws

BadLocationException

This method allows an application to mark a place in
a sequence of character content. This mark can then be
used to tracks change as insertions and removals are made
in the content. The policy is that insertions always
occur prior to the current position (the most common case)
unless the insertion location is zero, in which case the
insertion is forced to a position that follows the
original position.

getRootElements

```java
Element
[] getRootElements()
```

Returns all of the root elements that are defined.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

- Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

**Returns:** the root element

---

#### getRootElements

Element

[] getRootElements()

Returns all of the root elements that are defined.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

- Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

Typically there will be only one document structure, but the interface
supports building an arbitrary number of structural projections over the
text data. The document can have multiple root elements to support
multiple document structures. Some examples might be:

Text direction.

Lexical token streams.

Parse trees.

Conversions to formats other than the native format.

Modification specifications.

Annotations.

getDefaultRootElement

```java
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

**Returns:** the root element

---

#### getDefaultRootElement

Element

getDefaultRootElement()

Returns the root element that views should be based upon,
unless some other mechanism for assigning views to element
structures is provided.

render

```java
void render​(
Runnable
r)
```

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

**Parameters:** r

- a

Runnable

used to render the model

---

#### render

void render​(

Runnable

r)

Allows the model to be safely rendered in the presence
of concurrency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

---

