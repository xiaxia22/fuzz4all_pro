# Class DefaultTreeCellEditor

**Source:** `java.desktop\javax\swing\tree\DefaultTreeCellEditor.html`

### Class Description

```java
public class
DefaultTreeCellEditor

extends
Object

implements
ActionListener
,
TreeCellEditor
,
TreeSelectionListener
```

A

TreeCellEditor

. You need to supply an
instance of

DefaultTreeCellRenderer

so that the icons can be obtained. You can optionally supply
a

TreeCellEditor

that will be layed out according
to the icon in the

DefaultTreeCellRenderer

.
If you do not supply a

TreeCellEditor

,
a

TextField

will be used. Editing is started
on a triple mouse click, or after a click, pause, click and
a delay of 1200 milliseconds.

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

**All Implemented Interfaces:** ActionListener

,

EventListener

,

CellEditor

,

TreeSelectionListener

,

TreeCellEditor

---

### Field Details

#### protected
TreeCellEditor
realEditor

Editor handling the editing.

---

#### protected
DefaultTreeCellRenderer
renderer

Renderer, used to get border and offsets from.

---

#### protected
Container
editingContainer

Editing container, will contain the

editorComponent

.

---

#### protected transient
Component
editingComponent

Component used in editing, obtained from the

editingContainer

.

---

#### protected boolean canEdit

As of Java 2 platform v1.4 this field should no longer be used. If
you wish to provide similar behavior you should directly override

isCellEditable

.

---

#### protected transient int offset

Used in editing. Indicates x position to place

editingComponent

.

---

#### protected transient
JTree
tree

JTree

instance listening too.

---

#### protected transient
TreePath
lastPath

Last path that was selected.

---

#### protected transient
Timer
timer

Used before starting the editing session.

---

#### protected transient int lastRow

Row that was last passed into

getTreeCellEditorComponent

.

---

#### protected
Color
borderSelectionColor

True if the border selection color should be drawn.

---

#### protected transient
Icon
editingIcon

Icon to use when editing.

---

#### protected
Font
font

Font to paint with,

null

indicates
font of renderer is to be used.

---

### Constructor Details

#### public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer)

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor. (Use this constructor for normal editing.)

**Parameters:**
- tree

- a

JTree

object
- renderer

- a

DefaultTreeCellRenderer

object

---

#### public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer,

TreeCellEditor
editor)

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor. (Use this constructor
for specialized editing.)

**Parameters:**
- tree

- a

JTree

object
- renderer

- a

DefaultTreeCellRenderer

object
- editor

- a

TreeCellEditor

object

---

### Method Details

#### public void setBorderSelectionColor​(
Color
newColor)

Sets the color to use for the border.

**Parameters:**
- newColor

- the new border color

---

#### public
Color
getBorderSelectionColor()

Returns the color the border is drawn.

**Returns:**
- the border selection color

---

#### public void setFont​(
Font
font)

Sets the font to edit with.

null

indicates
the renderers font should be used. This will NOT
override any font you have set in the editor
the receiver was instantiated with. If

null

for an editor was passed in a default editor will be
created that will pick up this font.

**Parameters:**
- font

- the editing

Font

**See Also:**
- getFont()

---

#### public
Font
getFont()

Gets the font used for editing.

**Returns:**
- the editing

Font

**See Also:**
- setFont(java.awt.Font)

---

#### public
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Configures the editor. Passed onto the

realEditor

.

**Specified by:**
- getTreeCellEditorComponent

in interface

TreeCellEditor

**Parameters:**
- tree

- the JTree that is asking the editor to edit;
this parameter can be null
- value

- the value of the cell to be edited
- isSelected

- true if the cell is to be rendered with
selection highlighting
- expanded

- true if the node is expanded
- leaf

- true if the node is a leaf node
- row

- the row index of the node being edited

**Returns:**
- the component for editing

---

#### public
Object
getCellEditorValue()

Returns the value currently being edited.

**Specified by:**
- getCellEditorValue

in interface

CellEditor

**Returns:**
- the value currently being edited

---

#### public boolean isCellEditable​(
EventObject
event)

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

**Specified by:**
- isCellEditable

in interface

CellEditor

**Parameters:**
- event

- the event the editor should use to consider
whether to begin editing or not

**Returns:**
- true if editing can be started

**See Also:**
- CellEditor.shouldSelectCell(java.util.EventObject)

---

#### public boolean shouldSelectCell​(
EventObject
event)

Messages the

realEditor

for the return value.

**Specified by:**
- shouldSelectCell

in interface

CellEditor

**Parameters:**
- event

- the event the editor should use to start
editing

**Returns:**
- true if the editor would like the editing cell to be selected;
otherwise returns false

**See Also:**
- CellEditor.isCellEditable(java.util.EventObject)

---

#### public boolean stopCellEditing()

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

**Specified by:**
- stopCellEditing

in interface

CellEditor

**Returns:**
- true if editing was stopped; false otherwise

---

#### public void cancelCellEditing()

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

**Specified by:**
- cancelCellEditing

in interface

CellEditor

---

#### public void addCellEditorListener​(
CellEditorListener
l)

Adds the

CellEditorListener

.

**Specified by:**
- addCellEditorListener

in interface

CellEditor

**Parameters:**
- l

- the listener to be added

---

#### public void removeCellEditorListener​(
CellEditorListener
l)

Removes the previously added

CellEditorListener

.

**Specified by:**
- removeCellEditorListener

in interface

CellEditor

**Parameters:**
- l

- the listener to be removed

---

#### public
CellEditorListener
[] getCellEditorListeners()

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

**Returns:**
- all of the

CellEditorListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void valueChanged​(
TreeSelectionEvent
e)

Resets

lastPath

.

**Specified by:**
- valueChanged

in interface

TreeSelectionListener

**Parameters:**
- e

- the event that characterizes the change.

---

#### public void actionPerformed​(
ActionEvent
e)

Messaged when the timer fires, this will start the editing
session.

**Specified by:**
- actionPerformed

in interface

ActionListener

**Parameters:**
- e

- the event to be processed

---

#### protected void setTree​(
JTree
newTree)

Sets the tree currently editing for. This is needed to add
a selection listener.

**Parameters:**
- newTree

- the new tree to be edited

---

#### protected boolean shouldStartEditingTimer​(
EventObject
event)

Returns true if

event

is a

MouseEvent

and the click count is 1.

**Parameters:**
- event

- the event being studied

**Returns:**
- whether

event

should starts the editing timer

---

#### protected void startEditingTimer()

Starts the editing timer.

---

#### protected boolean canEditImmediately​(
EventObject
event)

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

**Parameters:**
- event

- the event being studied

**Returns:**
- whether editing can be started for the given

event

---

#### protected boolean inHitRegion​(int x,
int y)

Returns true if the passed in location is a valid mouse location
to start editing from. This is implemented to return false if

x

is <= the width of the icon and icon gap displayed
by the renderer. In other words this returns true if the user
clicks over the text part displayed by the renderer, and false
otherwise.

**Parameters:**
- x

- the x-coordinate of the point
- y

- the y-coordinate of the point

**Returns:**
- true if the passed in location is a valid mouse location

---

#### protected void determineOffset​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Determine the offset.

**Parameters:**
- tree

- a

JTree

object
- value

- a value
- isSelected

- selection status
- expanded

- expansion status
- leaf

- leaf status
- row

- current row

---

#### protected void prepareForEditing()

Invoked just before editing is to start. Will add the

editingComponent

to the

editingContainer

.

---

#### protected
Container
createContainer()

Creates the container to manage placement of

editingComponent

.

**Returns:**
- new Container object

---

#### protected
TreeCellEditor
createTreeCellEditor()

This is invoked if a

TreeCellEditor

is not supplied in the constructor.
It returns a

TextField

editor.

**Returns:**
- a new

TextField

editor

---

### Additional Sections

#### Class DefaultTreeCellEditor

java.lang.Object

- javax.swing.tree.DefaultTreeCellEditor

javax.swing.tree.DefaultTreeCellEditor

**All Implemented Interfaces:** ActionListener

,

EventListener

,

CellEditor

,

TreeSelectionListener

,

TreeCellEditor

```java
public class
DefaultTreeCellEditor

extends
Object

implements
ActionListener
,
TreeCellEditor
,
TreeSelectionListener
```

A

TreeCellEditor

. You need to supply an
instance of

DefaultTreeCellRenderer

so that the icons can be obtained. You can optionally supply
a

TreeCellEditor

that will be layed out according
to the icon in the

DefaultTreeCellRenderer

.
If you do not supply a

TreeCellEditor

,
a

TextField

will be used. Editing is started
on a triple mouse click, or after a click, pause, click and
a delay of 1200 milliseconds.

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

**See Also:** JTree

public class

DefaultTreeCellEditor

extends

Object

implements

ActionListener

,

TreeCellEditor

,

TreeSelectionListener

A

TreeCellEditor

. You need to supply an
instance of

DefaultTreeCellRenderer

so that the icons can be obtained. You can optionally supply
a

TreeCellEditor

that will be layed out according
to the icon in the

DefaultTreeCellRenderer

.
If you do not supply a

TreeCellEditor

,
a

TextField

will be used. Editing is started
on a triple mouse click, or after a click, pause, click and
a delay of 1200 milliseconds.

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

class

DefaultTreeCellEditor.DefaultTextField

TextField

used when no editor is supplied.

class

DefaultTreeCellEditor.EditorContainer

Container responsible for placing the

editingComponent

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

borderSelectionColor

True if the border selection color should be drawn.

protected boolean

canEdit

As of Java 2 platform v1.4 this field should no longer be used.

protected

Component

editingComponent

Component used in editing, obtained from the

editingContainer

.

protected

Container

editingContainer

Editing container, will contain the

editorComponent

.

protected

Icon

editingIcon

Icon to use when editing.

protected

Font

font

Font to paint with,

null

indicates
font of renderer is to be used.

protected

TreePath

lastPath

Last path that was selected.

protected int

lastRow

Row that was last passed into

getTreeCellEditorComponent

.

protected int

offset

Used in editing.

protected

TreeCellEditor

realEditor

Editor handling the editing.

protected

DefaultTreeCellRenderer

renderer

Renderer, used to get border and offsets from.

protected

Timer

timer

Used before starting the editing session.

protected

JTree

tree

JTree

instance listening too.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultTreeCellEditor

​(

JTree

tree,

DefaultTreeCellRenderer

renderer)

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor.

DefaultTreeCellEditor

​(

JTree

tree,

DefaultTreeCellRenderer

renderer,

TreeCellEditor

editor)

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Messaged when the timer fires, this will start the editing
session.

void

addCellEditorListener

​(

CellEditorListener

l)

Adds the

CellEditorListener

.

void

cancelCellEditing

()

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

protected boolean

canEditImmediately

​(

EventObject

event)

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

protected

Container

createContainer

()

Creates the container to manage placement of

editingComponent

.

protected

TreeCellEditor

createTreeCellEditor

()

This is invoked if a

TreeCellEditor

is not supplied in the constructor.

protected void

determineOffset

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Determine the offset.

Color

getBorderSelectionColor

()

Returns the color the border is drawn.

CellEditorListener

[]

getCellEditorListeners

()

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

Object

getCellEditorValue

()

Returns the value currently being edited.

Font

getFont

()

Gets the font used for editing.

Component

getTreeCellEditorComponent

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Configures the editor.

protected boolean

inHitRegion

​(int x,
int y)

Returns true if the passed in location is a valid mouse location
to start editing from.

boolean

isCellEditable

​(

EventObject

event)

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

protected void

prepareForEditing

()

Invoked just before editing is to start.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes the previously added

CellEditorListener

.

void

setBorderSelectionColor

​(

Color

newColor)

Sets the color to use for the border.

void

setFont

​(

Font

font)

Sets the font to edit with.

protected void

setTree

​(

JTree

newTree)

Sets the tree currently editing for.

boolean

shouldSelectCell

​(

EventObject

event)

Messages the

realEditor

for the return value.

protected boolean

shouldStartEditingTimer

​(

EventObject

event)

Returns true if

event

is a

MouseEvent

and the click count is 1.

protected void

startEditingTimer

()

Starts the editing timer.

boolean

stopCellEditing

()

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

void

valueChanged

​(

TreeSelectionEvent

e)

Resets

lastPath

.

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

Nested Classes

Modifier and Type

Class

Description

class

DefaultTreeCellEditor.DefaultTextField

TextField

used when no editor is supplied.

class

DefaultTreeCellEditor.EditorContainer

Container responsible for placing the

editingComponent

.

---

#### Nested Class Summary

TextField

used when no editor is supplied.

Container responsible for placing the

editingComponent

.

Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

borderSelectionColor

True if the border selection color should be drawn.

protected boolean

canEdit

As of Java 2 platform v1.4 this field should no longer be used.

protected

Component

editingComponent

Component used in editing, obtained from the

editingContainer

.

protected

Container

editingContainer

Editing container, will contain the

editorComponent

.

protected

Icon

editingIcon

Icon to use when editing.

protected

Font

font

Font to paint with,

null

indicates
font of renderer is to be used.

protected

TreePath

lastPath

Last path that was selected.

protected int

lastRow

Row that was last passed into

getTreeCellEditorComponent

.

protected int

offset

Used in editing.

protected

TreeCellEditor

realEditor

Editor handling the editing.

protected

DefaultTreeCellRenderer

renderer

Renderer, used to get border and offsets from.

protected

Timer

timer

Used before starting the editing session.

protected

JTree

tree

JTree

instance listening too.

---

#### Field Summary

True if the border selection color should be drawn.

As of Java 2 platform v1.4 this field should no longer be used.

Component used in editing, obtained from the

editingContainer

.

Editing container, will contain the

editorComponent

.

Icon to use when editing.

Font to paint with,

null

indicates
font of renderer is to be used.

Last path that was selected.

Row that was last passed into

getTreeCellEditorComponent

.

Used in editing.

Editor handling the editing.

Renderer, used to get border and offsets from.

Used before starting the editing session.

JTree

instance listening too.

Constructor Summary

Constructors

Constructor

Description

DefaultTreeCellEditor

​(

JTree

tree,

DefaultTreeCellRenderer

renderer)

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor.

DefaultTreeCellEditor

​(

JTree

tree,

DefaultTreeCellRenderer

renderer,

TreeCellEditor

editor)

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor.

---

#### Constructor Summary

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor.

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Messaged when the timer fires, this will start the editing
session.

void

addCellEditorListener

​(

CellEditorListener

l)

Adds the

CellEditorListener

.

void

cancelCellEditing

()

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

protected boolean

canEditImmediately

​(

EventObject

event)

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

protected

Container

createContainer

()

Creates the container to manage placement of

editingComponent

.

protected

TreeCellEditor

createTreeCellEditor

()

This is invoked if a

TreeCellEditor

is not supplied in the constructor.

protected void

determineOffset

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Determine the offset.

Color

getBorderSelectionColor

()

Returns the color the border is drawn.

CellEditorListener

[]

getCellEditorListeners

()

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

Object

getCellEditorValue

()

Returns the value currently being edited.

Font

getFont

()

Gets the font used for editing.

Component

getTreeCellEditorComponent

​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Configures the editor.

protected boolean

inHitRegion

​(int x,
int y)

Returns true if the passed in location is a valid mouse location
to start editing from.

boolean

isCellEditable

​(

EventObject

event)

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

protected void

prepareForEditing

()

Invoked just before editing is to start.

void

removeCellEditorListener

​(

CellEditorListener

l)

Removes the previously added

CellEditorListener

.

void

setBorderSelectionColor

​(

Color

newColor)

Sets the color to use for the border.

void

setFont

​(

Font

font)

Sets the font to edit with.

protected void

setTree

​(

JTree

newTree)

Sets the tree currently editing for.

boolean

shouldSelectCell

​(

EventObject

event)

Messages the

realEditor

for the return value.

protected boolean

shouldStartEditingTimer

​(

EventObject

event)

Returns true if

event

is a

MouseEvent

and the click count is 1.

protected void

startEditingTimer

()

Starts the editing timer.

boolean

stopCellEditing

()

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

void

valueChanged

​(

TreeSelectionEvent

e)

Resets

lastPath

.

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

Messaged when the timer fires, this will start the editing
session.

Adds the

CellEditorListener

.

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

Creates the container to manage placement of

editingComponent

.

This is invoked if a

TreeCellEditor

is not supplied in the constructor.

Determine the offset.

Returns the color the border is drawn.

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

Returns the value currently being edited.

Gets the font used for editing.

Configures the editor.

Returns true if the passed in location is a valid mouse location
to start editing from.

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

Invoked just before editing is to start.

Removes the previously added

CellEditorListener

.

Sets the color to use for the border.

Sets the font to edit with.

Sets the tree currently editing for.

Messages the

realEditor

for the return value.

Returns true if

event

is a

MouseEvent

and the click count is 1.

Starts the editing timer.

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

Resets

lastPath

.

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

- realEditor

```java
protected
TreeCellEditor
realEditor
```

Editor handling the editing.

- renderer

```java
protected
DefaultTreeCellRenderer
renderer
```

Renderer, used to get border and offsets from.

- editingContainer

```java
protected
Container
editingContainer
```

Editing container, will contain the

editorComponent

.

- editingComponent

```java
protected transient
Component
editingComponent
```

Component used in editing, obtained from the

editingContainer

.

- canEdit

```java
protected boolean canEdit
```

As of Java 2 platform v1.4 this field should no longer be used. If
you wish to provide similar behavior you should directly override

isCellEditable

.

- offset

```java
protected transient int offset
```

Used in editing. Indicates x position to place

editingComponent

.

- tree

```java
protected transient
JTree
tree
```

JTree

instance listening too.

- lastPath

```java
protected transient
TreePath
lastPath
```

Last path that was selected.

- timer

```java
protected transient
Timer
timer
```

Used before starting the editing session.

- lastRow

```java
protected transient int lastRow
```

Row that was last passed into

getTreeCellEditorComponent

.

- borderSelectionColor

```java
protected
Color
borderSelectionColor
```

True if the border selection color should be drawn.

- editingIcon

```java
protected transient
Icon
editingIcon
```

Icon to use when editing.

- font

```java
protected
Font
font
```

Font to paint with,

null

indicates
font of renderer is to be used.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer)
```

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor. (Use this constructor for normal editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object

- DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer,

TreeCellEditor
editor)
```

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor. (Use this constructor
for specialized editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object
**Parameters:** editor

- a

TreeCellEditor

object

============ METHOD DETAIL ==========

- Method Detail

- setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- the new border color

- getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the border selection color

- setFont

```java
public void setFont​(
Font
font)
```

Sets the font to edit with.

null

indicates
the renderers font should be used. This will NOT
override any font you have set in the editor
the receiver was instantiated with. If

null

for an editor was passed in a default editor will be
created that will pick up this font.

**Parameters:** font

- the editing

Font
**See Also:** getFont()

- getFont

```java
public
Font
getFont()
```

Gets the font used for editing.

**Returns:** the editing

Font
**See Also:** setFont(java.awt.Font)

- getTreeCellEditorComponent

```java
public
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Configures the editor. Passed onto the

realEditor

.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

- getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Returns the value currently being edited.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value currently being edited

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
event)
```

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** event

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
event)
```

Messages the

realEditor

for the return value.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** event

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true if editing was stopped; false otherwise

- cancelCellEditing

```java
public void cancelCellEditing()
```

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

**Specified by:** cancelCellEditing

in interface

CellEditor

- addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds the

CellEditorListener

.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be added

- removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes the previously added

CellEditorListener

.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

- getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- valueChanged

```java
public void valueChanged​(
TreeSelectionEvent
e)
```

Resets

lastPath

.

**Specified by:** valueChanged

in interface

TreeSelectionListener
**Parameters:** e

- the event that characterizes the change.

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Messaged when the timer fires, this will start the editing
session.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

- setTree

```java
protected void setTree​(
JTree
newTree)
```

Sets the tree currently editing for. This is needed to add
a selection listener.

**Parameters:** newTree

- the new tree to be edited

- shouldStartEditingTimer

```java
protected boolean shouldStartEditingTimer​(
EventObject
event)
```

Returns true if

event

is a

MouseEvent

and the click count is 1.

**Parameters:** event

- the event being studied
**Returns:** whether

event

should starts the editing timer

- startEditingTimer

```java
protected void startEditingTimer()
```

Starts the editing timer.

- canEditImmediately

```java
protected boolean canEditImmediately​(
EventObject
event)
```

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

**Parameters:** event

- the event being studied
**Returns:** whether editing can be started for the given

event

- inHitRegion

```java
protected boolean inHitRegion​(int x,
int y)
```

Returns true if the passed in location is a valid mouse location
to start editing from. This is implemented to return false if

x

is <= the width of the icon and icon gap displayed
by the renderer. In other words this returns true if the user
clicks over the text part displayed by the renderer, and false
otherwise.

**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Returns:** true if the passed in location is a valid mouse location

- determineOffset

```java
protected void determineOffset​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Determine the offset.

**Parameters:** tree

- a

JTree

object
**Parameters:** value

- a value
**Parameters:** isSelected

- selection status
**Parameters:** expanded

- expansion status
**Parameters:** leaf

- leaf status
**Parameters:** row

- current row

- prepareForEditing

```java
protected void prepareForEditing()
```

Invoked just before editing is to start. Will add the

editingComponent

to the

editingContainer

.

- createContainer

```java
protected
Container
createContainer()
```

Creates the container to manage placement of

editingComponent

.

**Returns:** new Container object

- createTreeCellEditor

```java
protected
TreeCellEditor
createTreeCellEditor()
```

This is invoked if a

TreeCellEditor

is not supplied in the constructor.
It returns a

TextField

editor.

**Returns:** a new

TextField

editor

Field Detail

- realEditor

```java
protected
TreeCellEditor
realEditor
```

Editor handling the editing.

- renderer

```java
protected
DefaultTreeCellRenderer
renderer
```

Renderer, used to get border and offsets from.

- editingContainer

```java
protected
Container
editingContainer
```

Editing container, will contain the

editorComponent

.

- editingComponent

```java
protected transient
Component
editingComponent
```

Component used in editing, obtained from the

editingContainer

.

- canEdit

```java
protected boolean canEdit
```

As of Java 2 platform v1.4 this field should no longer be used. If
you wish to provide similar behavior you should directly override

isCellEditable

.

- offset

```java
protected transient int offset
```

Used in editing. Indicates x position to place

editingComponent

.

- tree

```java
protected transient
JTree
tree
```

JTree

instance listening too.

- lastPath

```java
protected transient
TreePath
lastPath
```

Last path that was selected.

- timer

```java
protected transient
Timer
timer
```

Used before starting the editing session.

- lastRow

```java
protected transient int lastRow
```

Row that was last passed into

getTreeCellEditorComponent

.

- borderSelectionColor

```java
protected
Color
borderSelectionColor
```

True if the border selection color should be drawn.

- editingIcon

```java
protected transient
Icon
editingIcon
```

Icon to use when editing.

- font

```java
protected
Font
font
```

Font to paint with,

null

indicates
font of renderer is to be used.

---

#### Field Detail

realEditor

```java
protected
TreeCellEditor
realEditor
```

Editor handling the editing.

---

#### realEditor

protected

TreeCellEditor

realEditor

Editor handling the editing.

renderer

```java
protected
DefaultTreeCellRenderer
renderer
```

Renderer, used to get border and offsets from.

---

#### renderer

protected

DefaultTreeCellRenderer

renderer

Renderer, used to get border and offsets from.

editingContainer

```java
protected
Container
editingContainer
```

Editing container, will contain the

editorComponent

.

---

#### editingContainer

protected

Container

editingContainer

Editing container, will contain the

editorComponent

.

editingComponent

```java
protected transient
Component
editingComponent
```

Component used in editing, obtained from the

editingContainer

.

---

#### editingComponent

protected transient

Component

editingComponent

Component used in editing, obtained from the

editingContainer

.

canEdit

```java
protected boolean canEdit
```

As of Java 2 platform v1.4 this field should no longer be used. If
you wish to provide similar behavior you should directly override

isCellEditable

.

---

#### canEdit

protected boolean canEdit

As of Java 2 platform v1.4 this field should no longer be used. If
you wish to provide similar behavior you should directly override

isCellEditable

.

offset

```java
protected transient int offset
```

Used in editing. Indicates x position to place

editingComponent

.

---

#### offset

protected transient int offset

Used in editing. Indicates x position to place

editingComponent

.

tree

```java
protected transient
JTree
tree
```

JTree

instance listening too.

---

#### tree

protected transient

JTree

tree

JTree

instance listening too.

lastPath

```java
protected transient
TreePath
lastPath
```

Last path that was selected.

---

#### lastPath

protected transient

TreePath

lastPath

Last path that was selected.

timer

```java
protected transient
Timer
timer
```

Used before starting the editing session.

---

#### timer

protected transient

Timer

timer

Used before starting the editing session.

lastRow

```java
protected transient int lastRow
```

Row that was last passed into

getTreeCellEditorComponent

.

---

#### lastRow

protected transient int lastRow

Row that was last passed into

getTreeCellEditorComponent

.

borderSelectionColor

```java
protected
Color
borderSelectionColor
```

True if the border selection color should be drawn.

---

#### borderSelectionColor

protected

Color

borderSelectionColor

True if the border selection color should be drawn.

editingIcon

```java
protected transient
Icon
editingIcon
```

Icon to use when editing.

---

#### editingIcon

protected transient

Icon

editingIcon

Icon to use when editing.

font

```java
protected
Font
font
```

Font to paint with,

null

indicates
font of renderer is to be used.

---

#### font

protected

Font

font

Font to paint with,

null

indicates
font of renderer is to be used.

Constructor Detail

- DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer)
```

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor. (Use this constructor for normal editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object

- DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer,

TreeCellEditor
editor)
```

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor. (Use this constructor
for specialized editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object
**Parameters:** editor

- a

TreeCellEditor

object

---

#### Constructor Detail

DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer)
```

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor. (Use this constructor for normal editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object

---

#### DefaultTreeCellEditor

public DefaultTreeCellEditor​(

JTree

tree,

DefaultTreeCellRenderer

renderer)

Constructs a

DefaultTreeCellEditor

object for a JTree using the specified renderer and
a default editor. (Use this constructor for normal editing.)

DefaultTreeCellEditor

```java
public DefaultTreeCellEditor​(
JTree
tree,

DefaultTreeCellRenderer
renderer,

TreeCellEditor
editor)
```

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor. (Use this constructor
for specialized editing.)

**Parameters:** tree

- a

JTree

object
**Parameters:** renderer

- a

DefaultTreeCellRenderer

object
**Parameters:** editor

- a

TreeCellEditor

object

---

#### DefaultTreeCellEditor

public DefaultTreeCellEditor​(

JTree

tree,

DefaultTreeCellRenderer

renderer,

TreeCellEditor

editor)

Constructs a

DefaultTreeCellEditor

object for a

JTree

using the
specified renderer and the specified editor. (Use this constructor
for specialized editing.)

Method Detail

- setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- the new border color

- getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the border selection color

- setFont

```java
public void setFont​(
Font
font)
```

Sets the font to edit with.

null

indicates
the renderers font should be used. This will NOT
override any font you have set in the editor
the receiver was instantiated with. If

null

for an editor was passed in a default editor will be
created that will pick up this font.

**Parameters:** font

- the editing

Font
**See Also:** getFont()

- getFont

```java
public
Font
getFont()
```

Gets the font used for editing.

**Returns:** the editing

Font
**See Also:** setFont(java.awt.Font)

- getTreeCellEditorComponent

```java
public
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Configures the editor. Passed onto the

realEditor

.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

- getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Returns the value currently being edited.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value currently being edited

- isCellEditable

```java
public boolean isCellEditable​(
EventObject
event)
```

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** event

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

- shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
event)
```

Messages the

realEditor

for the return value.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** event

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

- stopCellEditing

```java
public boolean stopCellEditing()
```

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true if editing was stopped; false otherwise

- cancelCellEditing

```java
public void cancelCellEditing()
```

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

**Specified by:** cancelCellEditing

in interface

CellEditor

- addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds the

CellEditorListener

.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be added

- removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes the previously added

CellEditorListener

.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

- getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- valueChanged

```java
public void valueChanged​(
TreeSelectionEvent
e)
```

Resets

lastPath

.

**Specified by:** valueChanged

in interface

TreeSelectionListener
**Parameters:** e

- the event that characterizes the change.

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Messaged when the timer fires, this will start the editing
session.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

- setTree

```java
protected void setTree​(
JTree
newTree)
```

Sets the tree currently editing for. This is needed to add
a selection listener.

**Parameters:** newTree

- the new tree to be edited

- shouldStartEditingTimer

```java
protected boolean shouldStartEditingTimer​(
EventObject
event)
```

Returns true if

event

is a

MouseEvent

and the click count is 1.

**Parameters:** event

- the event being studied
**Returns:** whether

event

should starts the editing timer

- startEditingTimer

```java
protected void startEditingTimer()
```

Starts the editing timer.

- canEditImmediately

```java
protected boolean canEditImmediately​(
EventObject
event)
```

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

**Parameters:** event

- the event being studied
**Returns:** whether editing can be started for the given

event

- inHitRegion

```java
protected boolean inHitRegion​(int x,
int y)
```

Returns true if the passed in location is a valid mouse location
to start editing from. This is implemented to return false if

x

is <= the width of the icon and icon gap displayed
by the renderer. In other words this returns true if the user
clicks over the text part displayed by the renderer, and false
otherwise.

**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Returns:** true if the passed in location is a valid mouse location

- determineOffset

```java
protected void determineOffset​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Determine the offset.

**Parameters:** tree

- a

JTree

object
**Parameters:** value

- a value
**Parameters:** isSelected

- selection status
**Parameters:** expanded

- expansion status
**Parameters:** leaf

- leaf status
**Parameters:** row

- current row

- prepareForEditing

```java
protected void prepareForEditing()
```

Invoked just before editing is to start. Will add the

editingComponent

to the

editingContainer

.

- createContainer

```java
protected
Container
createContainer()
```

Creates the container to manage placement of

editingComponent

.

**Returns:** new Container object

- createTreeCellEditor

```java
protected
TreeCellEditor
createTreeCellEditor()
```

This is invoked if a

TreeCellEditor

is not supplied in the constructor.
It returns a

TextField

editor.

**Returns:** a new

TextField

editor

---

#### Method Detail

setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- the new border color

---

#### setBorderSelectionColor

public void setBorderSelectionColor​(

Color

newColor)

Sets the color to use for the border.

getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the border selection color

---

#### getBorderSelectionColor

public

Color

getBorderSelectionColor()

Returns the color the border is drawn.

setFont

```java
public void setFont​(
Font
font)
```

Sets the font to edit with.

null

indicates
the renderers font should be used. This will NOT
override any font you have set in the editor
the receiver was instantiated with. If

null

for an editor was passed in a default editor will be
created that will pick up this font.

**Parameters:** font

- the editing

Font
**See Also:** getFont()

---

#### setFont

public void setFont​(

Font

font)

Sets the font to edit with.

null

indicates
the renderers font should be used. This will NOT
override any font you have set in the editor
the receiver was instantiated with. If

null

for an editor was passed in a default editor will be
created that will pick up this font.

getFont

```java
public
Font
getFont()
```

Gets the font used for editing.

**Returns:** the editing

Font
**See Also:** setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Gets the font used for editing.

getTreeCellEditorComponent

```java
public
Component
getTreeCellEditorComponent​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Configures the editor. Passed onto the

realEditor

.

**Specified by:** getTreeCellEditorComponent

in interface

TreeCellEditor
**Parameters:** tree

- the JTree that is asking the editor to edit;
this parameter can be null
**Parameters:** value

- the value of the cell to be edited
**Parameters:** isSelected

- true if the cell is to be rendered with
selection highlighting
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- the row index of the node being edited
**Returns:** the component for editing

---

#### getTreeCellEditorComponent

public

Component

getTreeCellEditorComponent​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Configures the editor. Passed onto the

realEditor

.

getCellEditorValue

```java
public
Object
getCellEditorValue()
```

Returns the value currently being edited.

**Specified by:** getCellEditorValue

in interface

CellEditor
**Returns:** the value currently being edited

---

#### getCellEditorValue

public

Object

getCellEditorValue()

Returns the value currently being edited.

isCellEditable

```java
public boolean isCellEditable​(
EventObject
event)
```

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

**Specified by:** isCellEditable

in interface

CellEditor
**Parameters:** event

- the event the editor should use to consider
whether to begin editing or not
**Returns:** true if editing can be started
**See Also:** CellEditor.shouldSelectCell(java.util.EventObject)

---

#### isCellEditable

public boolean isCellEditable​(

EventObject

event)

If the

realEditor

returns true to this
message,

prepareForEditing

is messaged and true is returned.

shouldSelectCell

```java
public boolean shouldSelectCell​(
EventObject
event)
```

Messages the

realEditor

for the return value.

**Specified by:** shouldSelectCell

in interface

CellEditor
**Parameters:** event

- the event the editor should use to start
editing
**Returns:** true if the editor would like the editing cell to be selected;
otherwise returns false
**See Also:** CellEditor.isCellEditable(java.util.EventObject)

---

#### shouldSelectCell

public boolean shouldSelectCell​(

EventObject

event)

Messages the

realEditor

for the return value.

stopCellEditing

```java
public boolean stopCellEditing()
```

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

**Specified by:** stopCellEditing

in interface

CellEditor
**Returns:** true if editing was stopped; false otherwise

---

#### stopCellEditing

public boolean stopCellEditing()

If the

realEditor

will allow editing to stop,
the

realEditor

is removed and true is returned,
otherwise false is returned.

cancelCellEditing

```java
public void cancelCellEditing()
```

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

**Specified by:** cancelCellEditing

in interface

CellEditor

---

#### cancelCellEditing

public void cancelCellEditing()

Messages

cancelCellEditing

to the

realEditor

and removes it from this instance.

addCellEditorListener

```java
public void addCellEditorListener​(
CellEditorListener
l)
```

Adds the

CellEditorListener

.

**Specified by:** addCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be added

---

#### addCellEditorListener

public void addCellEditorListener​(

CellEditorListener

l)

Adds the

CellEditorListener

.

removeCellEditorListener

```java
public void removeCellEditorListener​(
CellEditorListener
l)
```

Removes the previously added

CellEditorListener

.

**Specified by:** removeCellEditorListener

in interface

CellEditor
**Parameters:** l

- the listener to be removed

---

#### removeCellEditorListener

public void removeCellEditorListener​(

CellEditorListener

l)

Removes the previously added

CellEditorListener

.

getCellEditorListeners

```java
public
CellEditorListener
[] getCellEditorListeners()
```

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

**Returns:** all of the

CellEditorListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getCellEditorListeners

public

CellEditorListener

[] getCellEditorListeners()

Returns an array of all the

CellEditorListener

s added
to this DefaultTreeCellEditor with addCellEditorListener().

valueChanged

```java
public void valueChanged​(
TreeSelectionEvent
e)
```

Resets

lastPath

.

**Specified by:** valueChanged

in interface

TreeSelectionListener
**Parameters:** e

- the event that characterizes the change.

---

#### valueChanged

public void valueChanged​(

TreeSelectionEvent

e)

Resets

lastPath

.

actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Messaged when the timer fires, this will start the editing
session.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

Messaged when the timer fires, this will start the editing
session.

setTree

```java
protected void setTree​(
JTree
newTree)
```

Sets the tree currently editing for. This is needed to add
a selection listener.

**Parameters:** newTree

- the new tree to be edited

---

#### setTree

protected void setTree​(

JTree

newTree)

Sets the tree currently editing for. This is needed to add
a selection listener.

shouldStartEditingTimer

```java
protected boolean shouldStartEditingTimer​(
EventObject
event)
```

Returns true if

event

is a

MouseEvent

and the click count is 1.

**Parameters:** event

- the event being studied
**Returns:** whether

event

should starts the editing timer

---

#### shouldStartEditingTimer

protected boolean shouldStartEditingTimer​(

EventObject

event)

Returns true if

event

is a

MouseEvent

and the click count is 1.

startEditingTimer

```java
protected void startEditingTimer()
```

Starts the editing timer.

---

#### startEditingTimer

protected void startEditingTimer()

Starts the editing timer.

canEditImmediately

```java
protected boolean canEditImmediately​(
EventObject
event)
```

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

**Parameters:** event

- the event being studied
**Returns:** whether editing can be started for the given

event

---

#### canEditImmediately

protected boolean canEditImmediately​(

EventObject

event)

Returns true if

event

is

null

,
or it is a

MouseEvent

with a click count > 2
and

inHitRegion

returns true.

inHitRegion

```java
protected boolean inHitRegion​(int x,
int y)
```

Returns true if the passed in location is a valid mouse location
to start editing from. This is implemented to return false if

x

is <= the width of the icon and icon gap displayed
by the renderer. In other words this returns true if the user
clicks over the text part displayed by the renderer, and false
otherwise.

**Parameters:** x

- the x-coordinate of the point
**Parameters:** y

- the y-coordinate of the point
**Returns:** true if the passed in location is a valid mouse location

---

#### inHitRegion

protected boolean inHitRegion​(int x,
int y)

Returns true if the passed in location is a valid mouse location
to start editing from. This is implemented to return false if

x

is <= the width of the icon and icon gap displayed
by the renderer. In other words this returns true if the user
clicks over the text part displayed by the renderer, and false
otherwise.

determineOffset

```java
protected void determineOffset​(
JTree
tree,

Object
value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)
```

Determine the offset.

**Parameters:** tree

- a

JTree

object
**Parameters:** value

- a value
**Parameters:** isSelected

- selection status
**Parameters:** expanded

- expansion status
**Parameters:** leaf

- leaf status
**Parameters:** row

- current row

---

#### determineOffset

protected void determineOffset​(

JTree

tree,

Object

value,
boolean isSelected,
boolean expanded,
boolean leaf,
int row)

Determine the offset.

prepareForEditing

```java
protected void prepareForEditing()
```

Invoked just before editing is to start. Will add the

editingComponent

to the

editingContainer

.

---

#### prepareForEditing

protected void prepareForEditing()

Invoked just before editing is to start. Will add the

editingComponent

to the

editingContainer

.

createContainer

```java
protected
Container
createContainer()
```

Creates the container to manage placement of

editingComponent

.

**Returns:** new Container object

---

#### createContainer

protected

Container

createContainer()

Creates the container to manage placement of

editingComponent

.

createTreeCellEditor

```java
protected
TreeCellEditor
createTreeCellEditor()
```

This is invoked if a

TreeCellEditor

is not supplied in the constructor.
It returns a

TextField

editor.

**Returns:** a new

TextField

editor

---

#### createTreeCellEditor

protected

TreeCellEditor

createTreeCellEditor()

This is invoked if a

TreeCellEditor

is not supplied in the constructor.
It returns a

TextField

editor.

---

