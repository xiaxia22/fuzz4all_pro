# Class HTMLEditorKit

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.html`

### Class Description

```java
public class
HTMLEditorKit

extends
StyledEditorKit

implements
Accessible
```

The Swing JEditorPane text component supports different kinds
of content via a plug-in mechanism called an EditorKit. Because
HTML is a very popular format of content, some support is provided
by default. The default support is provided by this class, which
supports HTML version 3.2 (with some extensions), and is migrating
toward version 4.0.
The <applet> tag is not supported, but some support is provided
for the <object> tag.

There are several goals of the HTML EditorKit provided, that have
an effect upon the way that HTML is modeled. These
have influenced its design in a substantial way.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Accessible

---

### Field Details

#### public static final
String
DEFAULT_CSS

Default Cascading Style Sheet file that sets
up the tag views.

**See Also:**
- Constant Field Values

---

#### public static final
String
BOLD_ACTION

The bold action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
ITALIC_ACTION

The italic action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
PARA_INDENT_LEFT

The paragraph left indent action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
PARA_INDENT_RIGHT

The paragraph right indent action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
FONT_CHANGE_BIGGER

The font size increase to next value action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
FONT_CHANGE_SMALLER

The font size decrease to next value action identifier

**See Also:**
- Constant Field Values

---

#### public static final
String
COLOR_ACTION

The Color choice action identifier
The color is passed as an argument

**See Also:**
- Constant Field Values

---

#### public static final
String
LOGICAL_STYLE_ACTION

The logical style choice action identifier
The logical style is passed in as an argument

**See Also:**
- Constant Field Values

---

#### public static final
String
IMG_ALIGN_TOP

Align images at the top.

**See Also:**
- Constant Field Values

---

#### public static final
String
IMG_ALIGN_MIDDLE

Align images in the middle.

**See Also:**
- Constant Field Values

---

#### public static final
String
IMG_ALIGN_BOTTOM

Align images at the bottom.

**See Also:**
- Constant Field Values

---

#### public static final
String
IMG_BORDER

Align images at the border.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public HTMLEditorKit()

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

---

### Method Details

#### public
String
getContentType()

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/html

.

**Overrides:**
- getContentType

in class

DefaultEditorKit

**Returns:**
- the type

---

#### public
ViewFactory
getViewFactory()

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

**Overrides:**
- getViewFactory

in class

StyledEditorKit

**Returns:**
- the factory

---

#### public
Document
createDefaultDocument()

Create an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:**
- createDefaultDocument

in class

StyledEditorKit

**Returns:**
- the model

---

#### public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException

Inserts content from the given stream. If

doc

is
an instance of HTMLDocument, this will read
HTML 3.2 text. Inserting HTML into a non-empty document must be inside
the body Element, if you do not insert into the body an exception will
be thrown. When inserting into a non-empty document all tags outside
of the body (head, title) will be dropped.

**Overrides:**
- read

in class

DefaultEditorKit

**Parameters:**
- in

- the stream to read from
- doc

- the destination for the insertion
- pos

- the location in the document to place the
content

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document
- RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

---

#### public void insertHTML​(
HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
insertTag)
throws
BadLocationException
,

IOException

Inserts HTML into an existing document.

**Parameters:**
- doc

- the document to insert into
- offset

- the offset to insert HTML at
- popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
- html

- the HTML string
- pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
- insertTag

- the first tag to start inserting into document

**Throws:**
- BadLocationException

- if

offset

is invalid
- IOException

- on I/O error
- RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

---

#### public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:**
- write

in class

DefaultEditorKit

**Parameters:**
- out

- the stream to write to
- doc

- the source for the write
- pos

- the location in the document to fetch the
content
- len

- the amount to write out

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if

pos

represents an invalid
location within the document

---

#### public void install​(
JEditorPane
c)

Called when the kit is being installed into the
a JEditorPane.

**Overrides:**
- install

in class

StyledEditorKit

**Parameters:**
- c

- the JEditorPane

---

#### public void deinstall​(
JEditorPane
c)

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:**
- deinstall

in class

StyledEditorKit

**Parameters:**
- c

- the JEditorPane

---

#### public void setStyleSheet​(
StyleSheet
s)

Set the set of styles to be used to render the various
HTML elements. These styles are specified in terms of
CSS specifications. Each document produced by the kit
will have a copy of the sheet which it can add the
document specific styles to. By default, the StyleSheet
specified is shared by all HTMLEditorKit instances.
This should be reimplemented to provide a finer granularity
if desired.

**Parameters:**
- s

- a StyleSheet

---

#### public
StyleSheet
getStyleSheet()

Get the set of styles currently being used to render the
HTML elements. By default the resource specified by
DEFAULT_CSS gets loaded, and is shared by all HTMLEditorKit
instances.

**Returns:**
- the StyleSheet

---

#### public
Action
[] getActions()

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:**
- getActions

in class

StyledEditorKit

**Returns:**
- the command list

---

#### protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Overrides:**
- createInputAttributes

in class

StyledEditorKit

**Parameters:**
- element

- the element
- set

- the attributes

---

#### public
MutableAttributeSet
getInputAttributes()

Gets the input attributes used for the styled
editing actions.

**Overrides:**
- getInputAttributes

in class

StyledEditorKit

**Returns:**
- the attribute set

---

#### public void setDefaultCursor​(
Cursor
cursor)

Sets the default cursor.

**Parameters:**
- cursor

- a cursor

**Since:**
- 1.3

---

#### public
Cursor
getDefaultCursor()

Returns the default cursor.

**Returns:**
- the cursor

**Since:**
- 1.3

---

#### public void setLinkCursor​(
Cursor
cursor)

Sets the cursor to use over links.

**Parameters:**
- cursor

- a cursor

**Since:**
- 1.3

---

#### public
Cursor
getLinkCursor()

Returns the cursor to use over hyper links.

**Returns:**
- the cursor

**Since:**
- 1.3

---

#### public boolean isAutoFormSubmission()

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

**Returns:**
- true if html form submission is processed automatically,
false otherwise.

**See Also:**
- setAutoFormSubmission(boolean)

**Since:**
- 1.5

---

#### public void setAutoFormSubmission​(boolean isAuto)

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.
By default it is set to true.

**Parameters:**
- isAuto

- if

true

, html form submission is processed automatically.

**See Also:**
- isAutoFormSubmission()

,

FormSubmitEvent

**Since:**
- 1.5

---

#### public
Object
clone()

Creates a copy of the editor kit.

**Overrides:**
- clone

in class

StyledEditorKit

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### protected
HTMLEditorKit.Parser
getParser()

Fetch the parser to use for reading HTML streams.
This can be reimplemented to provide a different
parser. The default implementation is loaded dynamically
to avoid the overhead of loading the default parser if
it's not used. The default parser is the HotJava parser
using an HTML 3.2 DTD.

**Returns:**
- the parser

---

#### public
AccessibleContext
getAccessibleContext()

returns the AccessibleContext associated with this editor kit

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Returns:**
- the AccessibleContext associated with this editor kit

**Since:**
- 1.4

---

### Additional Sections

#### Class HTMLEditorKit

java.lang.Object

- javax.swing.text.EditorKit
- - javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit
- - javax.swing.text.html.HTMLEditorKit

javax.swing.text.EditorKit

- javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit
- - javax.swing.text.html.HTMLEditorKit

javax.swing.text.DefaultEditorKit

- javax.swing.text.StyledEditorKit
- - javax.swing.text.html.HTMLEditorKit

javax.swing.text.StyledEditorKit

- javax.swing.text.html.HTMLEditorKit

javax.swing.text.html.HTMLEditorKit

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Accessible

```java
public class
HTMLEditorKit

extends
StyledEditorKit

implements
Accessible
```

The Swing JEditorPane text component supports different kinds
of content via a plug-in mechanism called an EditorKit. Because
HTML is a very popular format of content, some support is provided
by default. The default support is provided by this class, which
supports HTML version 3.2 (with some extensions), and is migrating
toward version 4.0.
The <applet> tag is not supported, but some support is provided
for the <object> tag.

There are several goals of the HTML EditorKit provided, that have
an effect upon the way that HTML is modeled. These
have influenced its design in a substantial way.

**See Also:** Serialized Form

public class

HTMLEditorKit

extends

StyledEditorKit

implements

Accessible

The Swing JEditorPane text component supports different kinds
of content via a plug-in mechanism called an EditorKit. Because
HTML is a very popular format of content, some support is provided
by default. The default support is provided by this class, which
supports HTML version 3.2 (with some extensions), and is migrating
toward version 4.0.
The <applet> tag is not supported, but some support is provided
for the <object> tag.

There are several goals of the HTML EditorKit provided, that have
an effect upon the way that HTML is modeled. These
have influenced its design in a substantial way.

There are several goals of the HTML EditorKit provided, that have
an effect upon the way that HTML is modeled. These
have influenced its design in a substantial way.

The modeling of HTML is provided by the class

HTMLDocument

.
Its documentation describes the details of how the HTML is modeled.
The editing support leverages heavily off of the text package.

Extendable/Scalable

To maximize the usefulness of this kit, a great deal of effort
has gone into making it extendable. These are some of the
features.

- The parser is replaceable. The default parser is the Hot Java
parser which is DTD based. A different DTD can be used, or an
entirely different parser can be used. To change the parser,
reimplement the getParser method. The default parser is
dynamically loaded when first asked for, so the class files
will never be loaded if an alternative parser is used. The
default parser is in a separate package called parser below
this package.

The parser drives the ParserCallback, which is provided by
HTMLDocument. To change the callback, subclass HTMLDocument
and reimplement the createDefaultDocument method to return
document that produces a different reader. The reader controls
how the document is structured. Although the Document provides
HTML support by default, there is nothing preventing support of
non-HTML tags that result in alternative element structures.

The default view of the models are provided as a hierarchy of
View implementations, so one can easily customize how a particular
element is displayed or add capabilities for new kinds of elements
by providing new View implementations. The default set of views
are provided by the

HTMLFactory

class. This can
be easily changed by subclassing or replacing the HTMLFactory
and reimplementing the getViewFactory method to return the alternative
factory.

The View implementations work primarily off of CSS attributes,
which are kept in the views. This makes it possible to have
multiple views mapped over the same model that appear substantially
different. This can be especially useful for printing. For
most HTML attributes, the HTML attributes are converted to CSS
attributes for display. This helps make the View implementations
more general purpose

Asynchronous Loading

Larger documents involve a lot of parsing and take some time
to load. By default, this kit produces documents that will be
loaded asynchronously if loaded using

JEditorPane.setPage

.
This is controlled by a property on the document. The method

createDefaultDocument

can
be overriden to change this. The batching of work is done
by the

HTMLDocument.HTMLReader

class. The actual
work is done by the

DefaultStyledDocument

and

AbstractDocument

classes in the text package.

Customization from current LAF

HTML provides a well known set of features without exactly
specifying the display characteristics. Swing has a theme
mechanism for its look-and-feel implementations. It is desirable
for the look-and-feel to feed display characteristics into the
HTML views. An user with poor vision for example would want
high contrast and larger than typical fonts.

The support for this is provided by the

StyleSheet

class. The presentation of the HTML can be heavily influenced
by the setting of the StyleSheet property on the EditorKit.

Not lossy

An EditorKit has the ability to be read and save documents.
It is generally the most pleasing to users if there is no loss
of data between the two operation. The policy of the HTMLEditorKit
will be to store things not recognized or not necessarily visible
so they can be subsequently written out. The model of the HTML document
should therefore contain all information discovered while reading the
document. This is constrained in some ways by the need to support
editing (i.e. incorrect documents sometimes must be normalized).
The guiding principle is that information shouldn't be lost, but
some might be synthesized to produce a more correct model or it might
be rearranged.

The parser is replaceable. The default parser is the Hot Java
parser which is DTD based. A different DTD can be used, or an
entirely different parser can be used. To change the parser,
reimplement the getParser method. The default parser is
dynamically loaded when first asked for, so the class files
will never be loaded if an alternative parser is used. The
default parser is in a separate package called parser below
this package.

The parser drives the ParserCallback, which is provided by
HTMLDocument. To change the callback, subclass HTMLDocument
and reimplement the createDefaultDocument method to return
document that produces a different reader. The reader controls
how the document is structured. Although the Document provides
HTML support by default, there is nothing preventing support of
non-HTML tags that result in alternative element structures.

The default view of the models are provided as a hierarchy of
View implementations, so one can easily customize how a particular
element is displayed or add capabilities for new kinds of elements
by providing new View implementations. The default set of views
are provided by the

HTMLFactory

class. This can
be easily changed by subclassing or replacing the HTMLFactory
and reimplementing the getViewFactory method to return the alternative
factory.

The View implementations work primarily off of CSS attributes,
which are kept in the views. This makes it possible to have
multiple views mapped over the same model that appear substantially
different. This can be especially useful for printing. For
most HTML attributes, the HTML attributes are converted to CSS
attributes for display. This helps make the View implementations
more general purpose

The support for this is provided by the

StyleSheet

class. The presentation of the HTML can be heavily influenced
by the setting of the StyleSheet property on the EditorKit.

Not lossy

An EditorKit has the ability to be read and save documents.
It is generally the most pleasing to users if there is no loss
of data between the two operation. The policy of the HTMLEditorKit
will be to store things not recognized or not necessarily visible
so they can be subsequently written out. The model of the HTML document
should therefore contain all information discovered while reading the
document. This is constrained in some ways by the need to support
editing (i.e. incorrect documents sometimes must be normalized).
The guiding principle is that information shouldn't be lost, but
some might be synthesized to produce a more correct model or it might
be rearranged.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

HTMLEditorKit.HTMLFactory

A factory to build views for HTML.

static class

HTMLEditorKit.HTMLTextAction

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

static class

HTMLEditorKit.InsertHTMLTextAction

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document.

static class

HTMLEditorKit.LinkController

Class to watch the associated component and fire
hyperlink events on it when appropriate.

static class

HTMLEditorKit.Parser

Interface to be supported by the parser.

static class

HTMLEditorKit.ParserCallback

The result of parsing drives these callback methods.

- Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

BOLD_ACTION

The bold action identifier

static

String

COLOR_ACTION

The Color choice action identifier
The color is passed as an argument

static

String

DEFAULT_CSS

Default Cascading Style Sheet file that sets
up the tag views.

static

String

FONT_CHANGE_BIGGER

The font size increase to next value action identifier

static

String

FONT_CHANGE_SMALLER

The font size decrease to next value action identifier

static

String

IMG_ALIGN_BOTTOM

Align images at the bottom.

static

String

IMG_ALIGN_MIDDLE

Align images in the middle.

static

String

IMG_ALIGN_TOP

Align images at the top.

static

String

IMG_BORDER

Align images at the border.

static

String

ITALIC_ACTION

The italic action identifier

static

String

LOGICAL_STYLE_ACTION

The logical style choice action identifier
The logical style is passed in as an argument

static

String

PARA_INDENT_LEFT

The paragraph left indent action identifier

static

String

PARA_INDENT_RIGHT

The paragraph right indent action identifier

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HTMLEditorKit

()

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

Document

createDefaultDocument

()

Create an uninitialized text storage model
that is appropriate for this type of editor.

protected void

createInputAttributes

​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

AccessibleContext

getAccessibleContext

()

returns the AccessibleContext associated with this editor kit

Action

[]

getActions

()

Fetches the command list for the editor.

String

getContentType

()

Get the MIME type of the data that this
kit represents support for.

Cursor

getDefaultCursor

()

Returns the default cursor.

MutableAttributeSet

getInputAttributes

()

Gets the input attributes used for the styled
editing actions.

Cursor

getLinkCursor

()

Returns the cursor to use over hyper links.

protected

HTMLEditorKit.Parser

getParser

()

Fetch the parser to use for reading HTML streams.

StyleSheet

getStyleSheet

()

Get the set of styles currently being used to render the
HTML elements.

ViewFactory

getViewFactory

()

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

void

insertHTML

​(

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

insertTag)

Inserts HTML into an existing document.

void

install

​(

JEditorPane

c)

Called when the kit is being installed into the
a JEditorPane.

boolean

isAutoFormSubmission

()

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream.

void

setAutoFormSubmission

​(boolean isAuto)

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.

void

setDefaultCursor

​(

Cursor

cursor)

Sets the default cursor.

void

setLinkCursor

​(

Cursor

cursor)

Sets the cursor to use over links.

void

setStyleSheet

​(

StyleSheet

s)

Set the set of styles to be used to render the various
HTML elements.

void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

- Methods declared in class javax.swing.text.

StyledEditorKit

getCharacterAttributeRun

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

read

,

write

- Methods declared in class java.lang.

Object

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

Nested Classes

Modifier and Type

Class

Description

static class

HTMLEditorKit.HTMLFactory

A factory to build views for HTML.

static class

HTMLEditorKit.HTMLTextAction

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

static class

HTMLEditorKit.InsertHTMLTextAction

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document.

static class

HTMLEditorKit.LinkController

Class to watch the associated component and fire
hyperlink events on it when appropriate.

static class

HTMLEditorKit.Parser

Interface to be supported by the parser.

static class

HTMLEditorKit.ParserCallback

The result of parsing drives these callback methods.

- Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested Class Summary

A factory to build views for HTML.

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document.

Class to watch the associated component and fire
hyperlink events on it when appropriate.

Interface to be supported by the parser.

The result of parsing drives these callback methods.

Nested classes/interfaces declared in class javax.swing.text.

StyledEditorKit

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

---

#### Nested classes/interfaces declared in class javax.swing.text. StyledEditorKit

Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested classes/interfaces declared in class javax.swing.text. DefaultEditorKit

Field Summary

Fields

Modifier and Type

Field

Description

static

String

BOLD_ACTION

The bold action identifier

static

String

COLOR_ACTION

The Color choice action identifier
The color is passed as an argument

static

String

DEFAULT_CSS

Default Cascading Style Sheet file that sets
up the tag views.

static

String

FONT_CHANGE_BIGGER

The font size increase to next value action identifier

static

String

FONT_CHANGE_SMALLER

The font size decrease to next value action identifier

static

String

IMG_ALIGN_BOTTOM

Align images at the bottom.

static

String

IMG_ALIGN_MIDDLE

Align images in the middle.

static

String

IMG_ALIGN_TOP

Align images at the top.

static

String

IMG_BORDER

Align images at the border.

static

String

ITALIC_ACTION

The italic action identifier

static

String

LOGICAL_STYLE_ACTION

The logical style choice action identifier
The logical style is passed in as an argument

static

String

PARA_INDENT_LEFT

The paragraph left indent action identifier

static

String

PARA_INDENT_RIGHT

The paragraph right indent action identifier

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Field Summary

The bold action identifier

The Color choice action identifier
The color is passed as an argument

Default Cascading Style Sheet file that sets
up the tag views.

The font size increase to next value action identifier

The font size decrease to next value action identifier

Align images at the bottom.

Align images in the middle.

Align images at the top.

Align images at the border.

The italic action identifier

The logical style choice action identifier
The logical style is passed in as an argument

The paragraph left indent action identifier

The paragraph right indent action identifier

Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Fields declared in class javax.swing.text. DefaultEditorKit

Constructor Summary

Constructors

Constructor

Description

HTMLEditorKit

()

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

---

#### Constructor Summary

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

Document

createDefaultDocument

()

Create an uninitialized text storage model
that is appropriate for this type of editor.

protected void

createInputAttributes

​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

AccessibleContext

getAccessibleContext

()

returns the AccessibleContext associated with this editor kit

Action

[]

getActions

()

Fetches the command list for the editor.

String

getContentType

()

Get the MIME type of the data that this
kit represents support for.

Cursor

getDefaultCursor

()

Returns the default cursor.

MutableAttributeSet

getInputAttributes

()

Gets the input attributes used for the styled
editing actions.

Cursor

getLinkCursor

()

Returns the cursor to use over hyper links.

protected

HTMLEditorKit.Parser

getParser

()

Fetch the parser to use for reading HTML streams.

StyleSheet

getStyleSheet

()

Get the set of styles currently being used to render the
HTML elements.

ViewFactory

getViewFactory

()

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

void

insertHTML

​(

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

insertTag)

Inserts HTML into an existing document.

void

install

​(

JEditorPane

c)

Called when the kit is being installed into the
a JEditorPane.

boolean

isAutoFormSubmission

()

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream.

void

setAutoFormSubmission

​(boolean isAuto)

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.

void

setDefaultCursor

​(

Cursor

cursor)

Sets the default cursor.

void

setLinkCursor

​(

Cursor

cursor)

Sets the cursor to use over links.

void

setStyleSheet

​(

StyleSheet

s)

Set the set of styles to be used to render the various
HTML elements.

void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

- Methods declared in class javax.swing.text.

StyledEditorKit

getCharacterAttributeRun

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

read

,

write

- Methods declared in class java.lang.

Object

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

Creates a copy of the editor kit.

Create an uninitialized text storage model
that is appropriate for this type of editor.

Copies the key/values in

element

s AttributeSet into

set

.

Called when the kit is being removed from the
JEditorPane.

returns the AccessibleContext associated with this editor kit

Fetches the command list for the editor.

Get the MIME type of the data that this
kit represents support for.

Returns the default cursor.

Gets the input attributes used for the styled
editing actions.

Returns the cursor to use over hyper links.

Fetch the parser to use for reading HTML streams.

Get the set of styles currently being used to render the
HTML elements.

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

Inserts HTML into an existing document.

Called when the kit is being installed into the
a JEditorPane.

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

Inserts content from the given stream.

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.

Sets the default cursor.

Sets the cursor to use over links.

Set the set of styles to be used to render the various
HTML elements.

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

Methods declared in class javax.swing.text.

StyledEditorKit

getCharacterAttributeRun

---

#### Methods declared in class javax.swing.text. StyledEditorKit

Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

read

,

write

---

#### Methods declared in class javax.swing.text. DefaultEditorKit

Methods declared in class java.lang.

Object

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

- DEFAULT_CSS

```java
public static final
String
DEFAULT_CSS
```

Default Cascading Style Sheet file that sets
up the tag views.

**See Also:** Constant Field Values

- BOLD_ACTION

```java
public static final
String
BOLD_ACTION
```

The bold action identifier

**See Also:** Constant Field Values

- ITALIC_ACTION

```java
public static final
String
ITALIC_ACTION
```

The italic action identifier

**See Also:** Constant Field Values

- PARA_INDENT_LEFT

```java
public static final
String
PARA_INDENT_LEFT
```

The paragraph left indent action identifier

**See Also:** Constant Field Values

- PARA_INDENT_RIGHT

```java
public static final
String
PARA_INDENT_RIGHT
```

The paragraph right indent action identifier

**See Also:** Constant Field Values

- FONT_CHANGE_BIGGER

```java
public static final
String
FONT_CHANGE_BIGGER
```

The font size increase to next value action identifier

**See Also:** Constant Field Values

- FONT_CHANGE_SMALLER

```java
public static final
String
FONT_CHANGE_SMALLER
```

The font size decrease to next value action identifier

**See Also:** Constant Field Values

- COLOR_ACTION

```java
public static final
String
COLOR_ACTION
```

The Color choice action identifier
The color is passed as an argument

**See Also:** Constant Field Values

- LOGICAL_STYLE_ACTION

```java
public static final
String
LOGICAL_STYLE_ACTION
```

The logical style choice action identifier
The logical style is passed in as an argument

**See Also:** Constant Field Values

- IMG_ALIGN_TOP

```java
public static final
String
IMG_ALIGN_TOP
```

Align images at the top.

**See Also:** Constant Field Values

- IMG_ALIGN_MIDDLE

```java
public static final
String
IMG_ALIGN_MIDDLE
```

Align images in the middle.

**See Also:** Constant Field Values

- IMG_ALIGN_BOTTOM

```java
public static final
String
IMG_ALIGN_BOTTOM
```

Align images at the bottom.

**See Also:** Constant Field Values

- IMG_BORDER

```java
public static final
String
IMG_BORDER
```

Align images at the border.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HTMLEditorKit

```java
public HTMLEditorKit()
```

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

============ METHOD DETAIL ==========

- Method Detail

- getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/html

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

**Overrides:** getViewFactory

in class

StyledEditorKit
**Returns:** the factory

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Create an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

StyledEditorKit
**Returns:** the model

- read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream. If

doc

is
an instance of HTMLDocument, this will read
HTML 3.2 text. Inserting HTML into a non-empty document must be inside
the body Element, if you do not insert into the body an exception will
be thrown. When inserting into a non-empty document all tags outside
of the body (head, title) will be dropped.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- the stream to read from
**Parameters:** doc

- the destination for the insertion
**Parameters:** pos

- the location in the document to place the
content
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

- insertHTML

```java
public void insertHTML​(
HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
insertTag)
throws
BadLocationException
,

IOException
```

Inserts HTML into an existing document.

**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** html

- the HTML string
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** insertTag

- the first tag to start inserting into document
**Throws:** BadLocationException

- if

offset

is invalid
**Throws:** IOException

- on I/O error
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

- write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- the stream to write to
**Parameters:** doc

- the source for the write
**Parameters:** pos

- the location in the document to fetch the
content
**Parameters:** len

- the amount to write out
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if

pos

represents an invalid
location within the document

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

**Overrides:** install

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

- deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

- setStyleSheet

```java
public void setStyleSheet​(
StyleSheet
s)
```

Set the set of styles to be used to render the various
HTML elements. These styles are specified in terms of
CSS specifications. Each document produced by the kit
will have a copy of the sheet which it can add the
document specific styles to. By default, the StyleSheet
specified is shared by all HTMLEditorKit instances.
This should be reimplemented to provide a finer granularity
if desired.

**Parameters:** s

- a StyleSheet

- getStyleSheet

```java
public
StyleSheet
getStyleSheet()
```

Get the set of styles currently being used to render the
HTML elements. By default the resource specified by
DEFAULT_CSS gets loaded, and is shared by all HTMLEditorKit
instances.

**Returns:** the StyleSheet

- getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

StyledEditorKit
**Returns:** the command list

- createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Overrides:** createInputAttributes

in class

StyledEditorKit
**Parameters:** element

- the element
**Parameters:** set

- the attributes

- getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes used for the styled
editing actions.

**Overrides:** getInputAttributes

in class

StyledEditorKit
**Returns:** the attribute set

- setDefaultCursor

```java
public void setDefaultCursor​(
Cursor
cursor)
```

Sets the default cursor.

**Parameters:** cursor

- a cursor
**Since:** 1.3

- getDefaultCursor

```java
public
Cursor
getDefaultCursor()
```

Returns the default cursor.

**Returns:** the cursor
**Since:** 1.3

- setLinkCursor

```java
public void setLinkCursor​(
Cursor
cursor)
```

Sets the cursor to use over links.

**Parameters:** cursor

- a cursor
**Since:** 1.3

- getLinkCursor

```java
public
Cursor
getLinkCursor()
```

Returns the cursor to use over hyper links.

**Returns:** the cursor
**Since:** 1.3

- isAutoFormSubmission

```java
public boolean isAutoFormSubmission()
```

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

**Returns:** true if html form submission is processed automatically,
false otherwise.
**Since:** 1.5
**See Also:** setAutoFormSubmission(boolean)

- setAutoFormSubmission

```java
public void setAutoFormSubmission​(boolean isAuto)
```

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.
By default it is set to true.

**Parameters:** isAuto

- if

true

, html form submission is processed automatically.
**Since:** 1.5
**See Also:** isAutoFormSubmission()

,

FormSubmitEvent

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

StyledEditorKit
**Returns:** the copy
**See Also:** Cloneable

- getParser

```java
protected
HTMLEditorKit.Parser
getParser()
```

Fetch the parser to use for reading HTML streams.
This can be reimplemented to provide a different
parser. The default implementation is loaded dynamically
to avoid the overhead of loading the default parser if
it's not used. The default parser is the HotJava parser
using an HTML 3.2 DTD.

**Returns:** the parser

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

returns the AccessibleContext associated with this editor kit

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the AccessibleContext associated with this editor kit
**Since:** 1.4

Field Detail

- DEFAULT_CSS

```java
public static final
String
DEFAULT_CSS
```

Default Cascading Style Sheet file that sets
up the tag views.

**See Also:** Constant Field Values

- BOLD_ACTION

```java
public static final
String
BOLD_ACTION
```

The bold action identifier

**See Also:** Constant Field Values

- ITALIC_ACTION

```java
public static final
String
ITALIC_ACTION
```

The italic action identifier

**See Also:** Constant Field Values

- PARA_INDENT_LEFT

```java
public static final
String
PARA_INDENT_LEFT
```

The paragraph left indent action identifier

**See Also:** Constant Field Values

- PARA_INDENT_RIGHT

```java
public static final
String
PARA_INDENT_RIGHT
```

The paragraph right indent action identifier

**See Also:** Constant Field Values

- FONT_CHANGE_BIGGER

```java
public static final
String
FONT_CHANGE_BIGGER
```

The font size increase to next value action identifier

**See Also:** Constant Field Values

- FONT_CHANGE_SMALLER

```java
public static final
String
FONT_CHANGE_SMALLER
```

The font size decrease to next value action identifier

**See Also:** Constant Field Values

- COLOR_ACTION

```java
public static final
String
COLOR_ACTION
```

The Color choice action identifier
The color is passed as an argument

**See Also:** Constant Field Values

- LOGICAL_STYLE_ACTION

```java
public static final
String
LOGICAL_STYLE_ACTION
```

The logical style choice action identifier
The logical style is passed in as an argument

**See Also:** Constant Field Values

- IMG_ALIGN_TOP

```java
public static final
String
IMG_ALIGN_TOP
```

Align images at the top.

**See Also:** Constant Field Values

- IMG_ALIGN_MIDDLE

```java
public static final
String
IMG_ALIGN_MIDDLE
```

Align images in the middle.

**See Also:** Constant Field Values

- IMG_ALIGN_BOTTOM

```java
public static final
String
IMG_ALIGN_BOTTOM
```

Align images at the bottom.

**See Also:** Constant Field Values

- IMG_BORDER

```java
public static final
String
IMG_BORDER
```

Align images at the border.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_CSS

```java
public static final
String
DEFAULT_CSS
```

Default Cascading Style Sheet file that sets
up the tag views.

**See Also:** Constant Field Values

---

#### DEFAULT_CSS

public static final

String

DEFAULT_CSS

Default Cascading Style Sheet file that sets
up the tag views.

BOLD_ACTION

```java
public static final
String
BOLD_ACTION
```

The bold action identifier

**See Also:** Constant Field Values

---

#### BOLD_ACTION

public static final

String

BOLD_ACTION

The bold action identifier

ITALIC_ACTION

```java
public static final
String
ITALIC_ACTION
```

The italic action identifier

**See Also:** Constant Field Values

---

#### ITALIC_ACTION

public static final

String

ITALIC_ACTION

The italic action identifier

PARA_INDENT_LEFT

```java
public static final
String
PARA_INDENT_LEFT
```

The paragraph left indent action identifier

**See Also:** Constant Field Values

---

#### PARA_INDENT_LEFT

public static final

String

PARA_INDENT_LEFT

The paragraph left indent action identifier

PARA_INDENT_RIGHT

```java
public static final
String
PARA_INDENT_RIGHT
```

The paragraph right indent action identifier

**See Also:** Constant Field Values

---

#### PARA_INDENT_RIGHT

public static final

String

PARA_INDENT_RIGHT

The paragraph right indent action identifier

FONT_CHANGE_BIGGER

```java
public static final
String
FONT_CHANGE_BIGGER
```

The font size increase to next value action identifier

**See Also:** Constant Field Values

---

#### FONT_CHANGE_BIGGER

public static final

String

FONT_CHANGE_BIGGER

The font size increase to next value action identifier

FONT_CHANGE_SMALLER

```java
public static final
String
FONT_CHANGE_SMALLER
```

The font size decrease to next value action identifier

**See Also:** Constant Field Values

---

#### FONT_CHANGE_SMALLER

public static final

String

FONT_CHANGE_SMALLER

The font size decrease to next value action identifier

COLOR_ACTION

```java
public static final
String
COLOR_ACTION
```

The Color choice action identifier
The color is passed as an argument

**See Also:** Constant Field Values

---

#### COLOR_ACTION

public static final

String

COLOR_ACTION

The Color choice action identifier
The color is passed as an argument

LOGICAL_STYLE_ACTION

```java
public static final
String
LOGICAL_STYLE_ACTION
```

The logical style choice action identifier
The logical style is passed in as an argument

**See Also:** Constant Field Values

---

#### LOGICAL_STYLE_ACTION

public static final

String

LOGICAL_STYLE_ACTION

The logical style choice action identifier
The logical style is passed in as an argument

IMG_ALIGN_TOP

```java
public static final
String
IMG_ALIGN_TOP
```

Align images at the top.

**See Also:** Constant Field Values

---

#### IMG_ALIGN_TOP

public static final

String

IMG_ALIGN_TOP

Align images at the top.

IMG_ALIGN_MIDDLE

```java
public static final
String
IMG_ALIGN_MIDDLE
```

Align images in the middle.

**See Also:** Constant Field Values

---

#### IMG_ALIGN_MIDDLE

public static final

String

IMG_ALIGN_MIDDLE

Align images in the middle.

IMG_ALIGN_BOTTOM

```java
public static final
String
IMG_ALIGN_BOTTOM
```

Align images at the bottom.

**See Also:** Constant Field Values

---

#### IMG_ALIGN_BOTTOM

public static final

String

IMG_ALIGN_BOTTOM

Align images at the bottom.

IMG_BORDER

```java
public static final
String
IMG_BORDER
```

Align images at the border.

**See Also:** Constant Field Values

---

#### IMG_BORDER

public static final

String

IMG_BORDER

Align images at the border.

Constructor Detail

- HTMLEditorKit

```java
public HTMLEditorKit()
```

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

---

#### Constructor Detail

HTMLEditorKit

```java
public HTMLEditorKit()
```

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

---

#### HTMLEditorKit

public HTMLEditorKit()

Constructs an HTMLEditorKit, creates a StyleContext,
and loads the style sheet.

Method Detail

- getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/html

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

**Overrides:** getViewFactory

in class

StyledEditorKit
**Returns:** the factory

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Create an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

StyledEditorKit
**Returns:** the model

- read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream. If

doc

is
an instance of HTMLDocument, this will read
HTML 3.2 text. Inserting HTML into a non-empty document must be inside
the body Element, if you do not insert into the body an exception will
be thrown. When inserting into a non-empty document all tags outside
of the body (head, title) will be dropped.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- the stream to read from
**Parameters:** doc

- the destination for the insertion
**Parameters:** pos

- the location in the document to place the
content
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

- insertHTML

```java
public void insertHTML​(
HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
insertTag)
throws
BadLocationException
,

IOException
```

Inserts HTML into an existing document.

**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** html

- the HTML string
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** insertTag

- the first tag to start inserting into document
**Throws:** BadLocationException

- if

offset

is invalid
**Throws:** IOException

- on I/O error
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

- write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- the stream to write to
**Parameters:** doc

- the source for the write
**Parameters:** pos

- the location in the document to fetch the
content
**Parameters:** len

- the amount to write out
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if

pos

represents an invalid
location within the document

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

**Overrides:** install

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

- deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

- setStyleSheet

```java
public void setStyleSheet​(
StyleSheet
s)
```

Set the set of styles to be used to render the various
HTML elements. These styles are specified in terms of
CSS specifications. Each document produced by the kit
will have a copy of the sheet which it can add the
document specific styles to. By default, the StyleSheet
specified is shared by all HTMLEditorKit instances.
This should be reimplemented to provide a finer granularity
if desired.

**Parameters:** s

- a StyleSheet

- getStyleSheet

```java
public
StyleSheet
getStyleSheet()
```

Get the set of styles currently being used to render the
HTML elements. By default the resource specified by
DEFAULT_CSS gets loaded, and is shared by all HTMLEditorKit
instances.

**Returns:** the StyleSheet

- getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

StyledEditorKit
**Returns:** the command list

- createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Overrides:** createInputAttributes

in class

StyledEditorKit
**Parameters:** element

- the element
**Parameters:** set

- the attributes

- getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes used for the styled
editing actions.

**Overrides:** getInputAttributes

in class

StyledEditorKit
**Returns:** the attribute set

- setDefaultCursor

```java
public void setDefaultCursor​(
Cursor
cursor)
```

Sets the default cursor.

**Parameters:** cursor

- a cursor
**Since:** 1.3

- getDefaultCursor

```java
public
Cursor
getDefaultCursor()
```

Returns the default cursor.

**Returns:** the cursor
**Since:** 1.3

- setLinkCursor

```java
public void setLinkCursor​(
Cursor
cursor)
```

Sets the cursor to use over links.

**Parameters:** cursor

- a cursor
**Since:** 1.3

- getLinkCursor

```java
public
Cursor
getLinkCursor()
```

Returns the cursor to use over hyper links.

**Returns:** the cursor
**Since:** 1.3

- isAutoFormSubmission

```java
public boolean isAutoFormSubmission()
```

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

**Returns:** true if html form submission is processed automatically,
false otherwise.
**Since:** 1.5
**See Also:** setAutoFormSubmission(boolean)

- setAutoFormSubmission

```java
public void setAutoFormSubmission​(boolean isAuto)
```

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.
By default it is set to true.

**Parameters:** isAuto

- if

true

, html form submission is processed automatically.
**Since:** 1.5
**See Also:** isAutoFormSubmission()

,

FormSubmitEvent

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

StyledEditorKit
**Returns:** the copy
**See Also:** Cloneable

- getParser

```java
protected
HTMLEditorKit.Parser
getParser()
```

Fetch the parser to use for reading HTML streams.
This can be reimplemented to provide a different
parser. The default implementation is loaded dynamically
to avoid the overhead of loading the default parser if
it's not used. The default parser is the HotJava parser
using an HTML 3.2 DTD.

**Returns:** the parser

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

returns the AccessibleContext associated with this editor kit

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the AccessibleContext associated with this editor kit
**Since:** 1.4

---

#### Method Detail

getContentType

```java
public
String
getContentType()
```

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/html

.

**Overrides:** getContentType

in class

DefaultEditorKit
**Returns:** the type

---

#### getContentType

public

String

getContentType()

Get the MIME type of the data that this
kit represents support for. This kit supports
the type

text/html

.

getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

**Overrides:** getViewFactory

in class

StyledEditorKit
**Returns:** the factory

---

#### getViewFactory

public

ViewFactory

getViewFactory()

Fetch a factory that is suitable for producing
views of any models that are produced by this
kit.

createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Create an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

StyledEditorKit
**Returns:** the model

---

#### createDefaultDocument

public

Document

createDefaultDocument()

Create an uninitialized text storage model
that is appropriate for this type of editor.

read

```java
public void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream. If

doc

is
an instance of HTMLDocument, this will read
HTML 3.2 text. Inserting HTML into a non-empty document must be inside
the body Element, if you do not insert into the body an exception will
be thrown. When inserting into a non-empty document all tags outside
of the body (head, title) will be dropped.

**Overrides:** read

in class

DefaultEditorKit
**Parameters:** in

- the stream to read from
**Parameters:** doc

- the destination for the insertion
**Parameters:** pos

- the location in the document to place the
content
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

---

#### read

public void read​(

Reader

in,

Document

doc,
int pos)
throws

IOException

,

BadLocationException

Inserts content from the given stream. If

doc

is
an instance of HTMLDocument, this will read
HTML 3.2 text. Inserting HTML into a non-empty document must be inside
the body Element, if you do not insert into the body an exception will
be thrown. When inserting into a non-empty document all tags outside
of the body (head, title) will be dropped.

insertHTML

```java
public void insertHTML​(
HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
insertTag)
throws
BadLocationException
,

IOException
```

Inserts HTML into an existing document.

**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** html

- the HTML string
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** insertTag

- the first tag to start inserting into document
**Throws:** BadLocationException

- if

offset

is invalid
**Throws:** IOException

- on I/O error
**Throws:** RuntimeException

- (will eventually be a BadLocationException)
if pos is invalid

---

#### insertHTML

public void insertHTML​(

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

insertTag)
throws

BadLocationException

,

IOException

Inserts HTML into an existing document.

write

```java
public void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

**Overrides:** write

in class

DefaultEditorKit
**Parameters:** out

- the stream to write to
**Parameters:** doc

- the source for the write
**Parameters:** pos

- the location in the document to fetch the
content
**Parameters:** len

- the amount to write out
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if

pos

represents an invalid
location within the document

---

#### write

public void write​(

Writer

out,

Document

doc,
int pos,
int len)
throws

IOException

,

BadLocationException

Write content from a document to the given stream
in a format appropriate for this kind of content handler.

install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

**Overrides:** install

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

---

#### install

public void install​(

JEditorPane

c)

Called when the kit is being installed into the
a JEditorPane.

deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

StyledEditorKit
**Parameters:** c

- the JEditorPane

---

#### deinstall

public void deinstall​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

setStyleSheet

```java
public void setStyleSheet​(
StyleSheet
s)
```

Set the set of styles to be used to render the various
HTML elements. These styles are specified in terms of
CSS specifications. Each document produced by the kit
will have a copy of the sheet which it can add the
document specific styles to. By default, the StyleSheet
specified is shared by all HTMLEditorKit instances.
This should be reimplemented to provide a finer granularity
if desired.

**Parameters:** s

- a StyleSheet

---

#### setStyleSheet

public void setStyleSheet​(

StyleSheet

s)

Set the set of styles to be used to render the various
HTML elements. These styles are specified in terms of
CSS specifications. Each document produced by the kit
will have a copy of the sheet which it can add the
document specific styles to. By default, the StyleSheet
specified is shared by all HTMLEditorKit instances.
This should be reimplemented to provide a finer granularity
if desired.

getStyleSheet

```java
public
StyleSheet
getStyleSheet()
```

Get the set of styles currently being used to render the
HTML elements. By default the resource specified by
DEFAULT_CSS gets loaded, and is shared by all HTMLEditorKit
instances.

**Returns:** the StyleSheet

---

#### getStyleSheet

public

StyleSheet

getStyleSheet()

Get the set of styles currently being used to render the
HTML elements. By default the resource specified by
DEFAULT_CSS gets loaded, and is shared by all HTMLEditorKit
instances.

getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

StyledEditorKit
**Returns:** the command list

---

#### getActions

public

Action

[] getActions()

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Overrides:** createInputAttributes

in class

StyledEditorKit
**Parameters:** element

- the element
**Parameters:** set

- the attributes

---

#### createInputAttributes

protected void createInputAttributes​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

This is called anytime the caret moves over a different location.

getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes used for the styled
editing actions.

**Overrides:** getInputAttributes

in class

StyledEditorKit
**Returns:** the attribute set

---

#### getInputAttributes

public

MutableAttributeSet

getInputAttributes()

Gets the input attributes used for the styled
editing actions.

setDefaultCursor

```java
public void setDefaultCursor​(
Cursor
cursor)
```

Sets the default cursor.

**Parameters:** cursor

- a cursor
**Since:** 1.3

---

#### setDefaultCursor

public void setDefaultCursor​(

Cursor

cursor)

Sets the default cursor.

getDefaultCursor

```java
public
Cursor
getDefaultCursor()
```

Returns the default cursor.

**Returns:** the cursor
**Since:** 1.3

---

#### getDefaultCursor

public

Cursor

getDefaultCursor()

Returns the default cursor.

setLinkCursor

```java
public void setLinkCursor​(
Cursor
cursor)
```

Sets the cursor to use over links.

**Parameters:** cursor

- a cursor
**Since:** 1.3

---

#### setLinkCursor

public void setLinkCursor​(

Cursor

cursor)

Sets the cursor to use over links.

getLinkCursor

```java
public
Cursor
getLinkCursor()
```

Returns the cursor to use over hyper links.

**Returns:** the cursor
**Since:** 1.3

---

#### getLinkCursor

public

Cursor

getLinkCursor()

Returns the cursor to use over hyper links.

isAutoFormSubmission

```java
public boolean isAutoFormSubmission()
```

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

**Returns:** true if html form submission is processed automatically,
false otherwise.
**Since:** 1.5
**See Also:** setAutoFormSubmission(boolean)

---

#### isAutoFormSubmission

public boolean isAutoFormSubmission()

Indicates whether an html form submission is processed automatically
or only

FormSubmitEvent

is fired.

setAutoFormSubmission

```java
public void setAutoFormSubmission​(boolean isAuto)
```

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.
By default it is set to true.

**Parameters:** isAuto

- if

true

, html form submission is processed automatically.
**Since:** 1.5
**See Also:** isAutoFormSubmission()

,

FormSubmitEvent

---

#### setAutoFormSubmission

public void setAutoFormSubmission​(boolean isAuto)

Specifies if an html form submission is processed
automatically or only

FormSubmitEvent

is fired.
By default it is set to true.

clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

StyledEditorKit
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of the editor kit.

getParser

```java
protected
HTMLEditorKit.Parser
getParser()
```

Fetch the parser to use for reading HTML streams.
This can be reimplemented to provide a different
parser. The default implementation is loaded dynamically
to avoid the overhead of loading the default parser if
it's not used. The default parser is the HotJava parser
using an HTML 3.2 DTD.

**Returns:** the parser

---

#### getParser

protected

HTMLEditorKit.Parser

getParser()

Fetch the parser to use for reading HTML streams.
This can be reimplemented to provide a different
parser. The default implementation is loaded dynamically
to avoid the overhead of loading the default parser if
it's not used. The default parser is the HotJava parser
using an HTML 3.2 DTD.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

returns the AccessibleContext associated with this editor kit

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the AccessibleContext associated with this editor kit
**Since:** 1.4

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

returns the AccessibleContext associated with this editor kit

---

