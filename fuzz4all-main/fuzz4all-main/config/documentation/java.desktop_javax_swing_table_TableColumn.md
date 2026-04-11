# Class TableColumn

**Source:** `java.desktop\javax\swing\table\TableColumn.html`

### Class Description

```java
public class
TableColumn

extends
Object

implements
Serializable
```

A

TableColumn

represents all the attributes of a column in a

JTable

, such as width, resizability, minimum and maximum width.
In addition, the

TableColumn

provides slots for a renderer and
an editor that can be used to display and edit the values in this column.

It is also possible to specify renderers and editors on a per type basis
rather than a per column basis - see the

setDefaultRenderer

method in the

JTable

class.
This default mechanism is only used when the renderer (or
editor) in the

TableColumn

is

null

.

The

TableColumn

stores the link between the columns in the

JTable

and the columns in the

TableModel

.
The

modelIndex

is the column in the

TableModel

, which will be queried for the data values for the
cells in this column. As the column moves around in the view this

modelIndex

does not change.

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
String
COLUMN_WIDTH_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:**
- Constant Field Values

---

#### public static final
String
HEADER_VALUE_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:**
- Constant Field Values

---

#### public static final
String
HEADER_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:**
- Constant Field Values

---

#### public static final
String
CELL_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:**
- Constant Field Values

---

#### protected int modelIndex

The index of the column in the model which is to be displayed by
this

TableColumn

. As columns are moved around in the
view

modelIndex

remains constant.

---

#### protected
Object
identifier

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns. The table package does
not modify or invoke any methods in these identifier objects other
than the

equals

method which is used in the

getColumnIndex()

method in the

DefaultTableColumnModel

.

---

#### protected int width

The width of the column.

---

#### protected int minWidth

The minimum width of the column.

---

#### protected int maxWidth

The maximum width of the column.

---

#### protected
TableCellRenderer
headerRenderer

The renderer used to draw the header of the column.

---

#### protected
Object
headerValue

The header value of the column.

---

#### protected
TableCellRenderer
cellRenderer

The renderer used to draw the data cells of the column.

---

#### protected
TableCellEditor
cellEditor

The editor used to edit the data cells of the column.

---

#### protected boolean isResizable

If true, the user is allowed to resize the column; the default is true.

---

#### @Deprecated

protected transient int resizedPostingDisableCount

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

### Constructor Details

#### public TableColumn()

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.
This method is intended for serialization.

**See Also:**
- TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### public TableColumn​(int modelIndex)

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

**Parameters:**
- modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view

**See Also:**
- TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### public TableColumn​(int modelIndex,
int width)

Cover method, using a

null

renderer and a

null

editor.

**Parameters:**
- modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
- width

- this column's preferred width and initial width

**See Also:**
- TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### public TableColumn​(int modelIndex,
int width,

TableCellRenderer
cellRenderer,

TableCellEditor
cellEditor)

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.
The value of

width

is used
for both the initial and preferred width;
if

width

is negative,
they're set to 0.
The minimum width is set to 15 unless the initial width is less,
in which case the minimum width is set to
the initial width.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

**Parameters:**
- modelIndex

- the index of the column
in the model that supplies the data for this column in the table;
the model index remains the same
even when columns are reordered in the view
- width

- this column's preferred width and initial width
- cellRenderer

- the object used to render values in this column
- cellEditor

- the object used to edit values in this column

**See Also:**
- getMinWidth()

,

JTable.getDefaultRenderer(Class)

,

JTable.getDefaultEditor(Class)

,

JTable.getCellRenderer(int, int)

,

JTable.getCellEditor(int, int)

---

### Method Details

#### @BeanProperty
(
description
="The model index.")
public void setModelIndex​(int modelIndex)

Sets the model index for this column. The model index is the
index of the column in the model that will be displayed by this

TableColumn

. As the

TableColumn

is moved around in the view the model index remains constant.

**Parameters:**
- modelIndex

- the new modelIndex

---

#### public int getModelIndex()

Returns the model index for this column.

**Returns:**
- the

modelIndex

property

---

#### @BeanProperty
(
description
="A unique identifier for this column.")
public void setIdentifier​(
Object
identifier)

Sets the

TableColumn

's identifier to

anIdentifier

.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

**Parameters:**
- identifier

- an identifier for this column

**See Also:**
- getIdentifier()

---

#### public
Object
getIdentifier()

Returns the

identifier

object for this column.
Note identifiers are not used by

JTable

,
they are purely a convenience for external use.
If the

identifier

is

null

,

getIdentifier()

returns

getHeaderValue

as a default.

**Returns:**
- the

identifier

property

**See Also:**
- setIdentifier(java.lang.Object)

---

#### @BeanProperty
(
description
="The text to be used by the header renderer.")
public void setHeaderValue​(
Object
headerValue)

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

. When the

TableColumn

is created, the default

headerValue

is

null

.

**Parameters:**
- headerValue

- the new headerValue

**See Also:**
- getHeaderValue()

---

#### public
Object
getHeaderValue()

Returns the

Object

used as the value for the header
renderer.

**Returns:**
- the

headerValue

property

**See Also:**
- setHeaderValue(java.lang.Object)

---

#### @BeanProperty
(
description
="The header renderer.")
public void setHeaderRenderer​(
TableCellRenderer
headerRenderer)

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

**Parameters:**
- headerRenderer

- the new headerRenderer

**See Also:**
- getHeaderRenderer()

---

#### public
TableCellRenderer
getHeaderRenderer()

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

. When the

headerRenderer

is

null

, the

JTableHeader

uses its

defaultRenderer

. The default value for a

headerRenderer

is

null

.

**Returns:**
- the

headerRenderer

property

**See Also:**
- setHeaderRenderer(javax.swing.table.TableCellRenderer)

,

setHeaderValue(java.lang.Object)

,

JTableHeader.getDefaultRenderer()

---

#### @BeanProperty
(
description
="The renderer to use for cell values.")
public void setCellRenderer​(
TableCellRenderer
cellRenderer)

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

**Parameters:**
- cellRenderer

- the new cellRenderer

**See Also:**
- getCellRenderer()

---

#### public
TableCellRenderer
getCellRenderer()

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column. The

cellRenderer

of the column
not only controls the visual look for the column, but is also used to
interpret the value object supplied by the

TableModel

.
When the

cellRenderer

is

null

,
the

JTable

uses a default renderer based on the
class of the cells in that column. The default value for a

cellRenderer

is

null

.

**Returns:**
- the

cellRenderer

property

**See Also:**
- setCellRenderer(javax.swing.table.TableCellRenderer)

,

JTable.setDefaultRenderer(java.lang.Class<?>, javax.swing.table.TableCellRenderer)

---

#### @BeanProperty
(
description
="The editor to use for cell values.")
public void setCellEditor​(
TableCellEditor
cellEditor)

Sets the editor to used by when a cell in this column is edited.

**Parameters:**
- cellEditor

- the new cellEditor

**See Also:**
- getCellEditor()

---

#### public
TableCellEditor
getCellEditor()

Returns the

TableCellEditor

used by the

JTable

to edit values for this column. When the

cellEditor

is

null

, the

JTable

uses a default editor based on the
class of the cells in that column. The default value for a

cellEditor

is

null

.

**Returns:**
- the

cellEditor

property

**See Also:**
- setCellEditor(javax.swing.table.TableCellEditor)

,

JTable.setDefaultEditor(java.lang.Class<?>, javax.swing.table.TableCellEditor)

---

#### @BeanProperty
(
description
="The width of the column.")
public void setWidth​(int width)

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.
Like a layout manager in the
AWT, the

JTable

adjusts a column's width automatically
whenever the
table itself changes size, or a column's preferred width is changed.
Setting widths programmatically therefore has no long term effect.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

**Parameters:**
- width

- the new width

**See Also:**
- getWidth()

,

setMinWidth(int)

,

setMaxWidth(int)

,

setPreferredWidth(int)

,

JTable.doLayout()

---

#### public int getWidth()

Returns the width of the

TableColumn

. The default width is
75.

**Returns:**
- the

width

property

**See Also:**
- setWidth(int)

---

#### @BeanProperty
(
description
="The preferred width of the column.")
public void setPreferredWidth​(int preferredWidth)

Sets this column's preferred width to

preferredWidth

.
If

preferredWidth

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

**Parameters:**
- preferredWidth

- the new preferred width

**See Also:**
- getPreferredWidth()

,

JTable.doLayout()

---

#### public int getPreferredWidth()

Returns the preferred width of the

TableColumn

.
The default preferred width is 75.

**Returns:**
- the

preferredWidth

property

**See Also:**
- setPreferredWidth(int)

---

#### @BeanProperty
(
description
="The minimum width of the column.")
public void setMinWidth​(int minWidth)

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.
For example, if the

minWidth

argument is negative,
this method sets the

minWidth

property to 0.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

**Parameters:**
- minWidth

- the new minimum width

**See Also:**
- getMinWidth()

,

setPreferredWidth(int)

,

setMaxWidth(int)

---

#### public int getMinWidth()

Returns the minimum width for the

TableColumn

. The

TableColumn

's width can't be made less than this either
by the user or programmatically.

**Returns:**
- the

minWidth

property

**See Also:**
- setMinWidth(int)

,

TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### @BeanProperty
(
description
="The maximum width of the column.")
public void setMaxWidth​(int maxWidth)

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

**Parameters:**
- maxWidth

- the new maximum width

**See Also:**
- getMaxWidth()

,

setPreferredWidth(int)

,

setMinWidth(int)

---

#### public int getMaxWidth()

Returns the maximum width for the

TableColumn

. The

TableColumn

's width can't be made larger than this
either by the user or programmatically. The default maxWidth
is Integer.MAX_VALUE.

**Returns:**
- the

maxWidth

property

**See Also:**
- setMaxWidth(int)

---

#### @BeanProperty
(
description
="Whether or not this column can be resized.")
public void setResizable​(boolean isResizable)

Sets whether this column can be resized.

**Parameters:**
- isResizable

- if true, resizing is allowed; otherwise false

**See Also:**
- getResizable()

---

#### public boolean getResizable()

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise. You can change the width programmatically
regardless of this setting. The default is true.

**Returns:**
- the

isResizable

property

**See Also:**
- setResizable(boolean)

---

#### public void sizeWidthToFit()

Resizes the

TableColumn

to fit the width of its header cell.
This method does nothing if the header renderer is

null

(the default case). Otherwise, it sets the minimum, maximum and preferred
widths of this column to the widths of the minimum, maximum and preferred
sizes of the Component delivered by the header renderer.
The transient "width" property of this TableColumn is also set to the
preferred width. Note this method is not used internally by the table
package.

**See Also:**
- setPreferredWidth(int)

---

#### @Deprecated

public void disableResizedPosting()

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### @Deprecated

public void enableResizedPosting()

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all bound properties of this class, including the
following:

- this TableColumn's modelIndex ("modelIndex")
- this TableColumn's identifier ("identifier")
- this TableColumn's header value ("headerValue")
- this TableColumn's header renderer ("headerRenderer")
- this TableColumn's cell renderer ("cellRenderer")
- this TableColumn's cell editor ("cellEditor")
- this TableColumn's width ("width")
- this TableColumn's preferred width ("preferredWidth")
- this TableColumn's minimum width ("minWidth")
- this TableColumn's maximum width ("maxWidth")
- this TableColumn's resizable state ("isResizable")

**Parameters:**
- listener

- the listener to be added

**See Also:**
- removePropertyChangeListener(PropertyChangeListener)

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list.
The

PropertyChangeListener

to be removed was registered
for all properties.

**Parameters:**
- listener

- the listener to be removed

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners()

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

**Returns:**
- all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected
TableCellRenderer
createDefaultHeaderRenderer()

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor. Previously this method was used by the

TableColumn

to create a default header renderer.
As of Java 2 platform v1.3, the default header renderer is

null

.

JTableHeader

now provides its own shared default
renderer, just as the

JTable

does for its cell renderers.

**Returns:**
- the default header renderer

**See Also:**
- JTableHeader.createDefaultRenderer()

---

### Additional Sections

#### Class TableColumn

java.lang.Object

- javax.swing.table.TableColumn

javax.swing.table.TableColumn

**All Implemented Interfaces:** Serializable

```java
public class
TableColumn

extends
Object

implements
Serializable
```

A

TableColumn

represents all the attributes of a column in a

JTable

, such as width, resizability, minimum and maximum width.
In addition, the

TableColumn

provides slots for a renderer and
an editor that can be used to display and edit the values in this column.

It is also possible to specify renderers and editors on a per type basis
rather than a per column basis - see the

setDefaultRenderer

method in the

JTable

class.
This default mechanism is only used when the renderer (or
editor) in the

TableColumn

is

null

.

The

TableColumn

stores the link between the columns in the

JTable

and the columns in the

TableModel

.
The

modelIndex

is the column in the

TableModel

, which will be queried for the data values for the
cells in this column. As the column moves around in the view this

modelIndex

does not change.

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

**See Also:** TableColumnModel

,

DefaultTableColumnModel

,

JTableHeader.getDefaultRenderer()

,

JTable.getDefaultRenderer(Class)

,

JTable.getDefaultEditor(Class)

,

JTable.getCellRenderer(int, int)

,

JTable.getCellEditor(int, int)

,

Serialized Form

public class

TableColumn

extends

Object

implements

Serializable

A

TableColumn

represents all the attributes of a column in a

JTable

, such as width, resizability, minimum and maximum width.
In addition, the

TableColumn

provides slots for a renderer and
an editor that can be used to display and edit the values in this column.

It is also possible to specify renderers and editors on a per type basis
rather than a per column basis - see the

setDefaultRenderer

method in the

JTable

class.
This default mechanism is only used when the renderer (or
editor) in the

TableColumn

is

null

.

The

TableColumn

stores the link between the columns in the

JTable

and the columns in the

TableModel

.
The

modelIndex

is the column in the

TableModel

, which will be queried for the data values for the
cells in this column. As the column moves around in the view this

modelIndex

does not change.

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

It is also possible to specify renderers and editors on a per type basis
rather than a per column basis - see the

setDefaultRenderer

method in the

JTable

class.
This default mechanism is only used when the renderer (or
editor) in the

TableColumn

is

null

.

The

TableColumn

stores the link between the columns in the

JTable

and the columns in the

TableModel

.
The

modelIndex

is the column in the

TableModel

, which will be queried for the data values for the
cells in this column. As the column moves around in the view this

modelIndex

does not change.

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

The

TableColumn

stores the link between the columns in the

JTable

and the columns in the

TableModel

.
The

modelIndex

is the column in the

TableModel

, which will be queried for the data values for the
cells in this column. As the column moves around in the view this

modelIndex

does not change.

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

Note:

Some implementations may assume that all

TableColumnModel

s are unique, therefore we would
recommend that the same

TableColumn

instance
not be added more than once to a

TableColumnModel

.
To show

TableColumn

s with the same column of
data from the model, create a new instance with the same

modelIndex

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CELL_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3.

protected

TableCellEditor

cellEditor

The editor used to edit the data cells of the column.

protected

TableCellRenderer

cellRenderer

The renderer used to draw the data cells of the column.

static

String

COLUMN_WIDTH_PROPERTY

Obsolete as of Java 2 platform v1.3.

static

String

HEADER_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3.

static

String

HEADER_VALUE_PROPERTY

Obsolete as of Java 2 platform v1.3.

protected

TableCellRenderer

headerRenderer

The renderer used to draw the header of the column.

protected

Object

headerValue

The header value of the column.

protected

Object

identifier

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns.

protected boolean

isResizable

If true, the user is allowed to resize the column; the default is true.

protected int

maxWidth

The maximum width of the column.

protected int

minWidth

The minimum width of the column.

protected int

modelIndex

The index of the column in the model which is to be displayed by
this

TableColumn

.

protected int

resizedPostingDisableCount

Deprecated.

as of Java 2 platform v1.3

protected int

width

The width of the column.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TableColumn

()

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex)

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex,
int width)

Cover method, using a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex,
int width,

TableCellRenderer

cellRenderer,

TableCellEditor

cellEditor)

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

protected

TableCellRenderer

createDefaultHeaderRenderer

()

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor.

void

disableResizedPosting

()

Deprecated.

as of Java 2 platform v1.3

void

enableResizedPosting

()

Deprecated.

as of Java 2 platform v1.3

TableCellEditor

getCellEditor

()

Returns the

TableCellEditor

used by the

JTable

to edit values for this column.

TableCellRenderer

getCellRenderer

()

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column.

TableCellRenderer

getHeaderRenderer

()

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

.

Object

getHeaderValue

()

Returns the

Object

used as the value for the header
renderer.

Object

getIdentifier

()

Returns the

identifier

object for this column.

int

getMaxWidth

()

Returns the maximum width for the

TableColumn

.

int

getMinWidth

()

Returns the minimum width for the

TableColumn

.

int

getModelIndex

()

Returns the model index for this column.

int

getPreferredWidth

()

Returns the preferred width of the

TableColumn

.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

boolean

getResizable

()

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise.

int

getWidth

()

Returns the width of the

TableColumn

.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setCellEditor

​(

TableCellEditor

cellEditor)

Sets the editor to used by when a cell in this column is edited.

void

setCellRenderer

​(

TableCellRenderer

cellRenderer)

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

void

setHeaderRenderer

​(

TableCellRenderer

headerRenderer)

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

void

setHeaderValue

​(

Object

headerValue)

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

.

void

setIdentifier

​(

Object

identifier)

Sets the

TableColumn

's identifier to

anIdentifier

.

void

setMaxWidth

​(int maxWidth)

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

void

setMinWidth

​(int minWidth)

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.

void

setModelIndex

​(int modelIndex)

Sets the model index for this column.

void

setPreferredWidth

​(int preferredWidth)

Sets this column's preferred width to

preferredWidth

.

void

setResizable

​(boolean isResizable)

Sets whether this column can be resized.

void

setWidth

​(int width)

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.

void

sizeWidthToFit

()

Resizes the

TableColumn

to fit the width of its header cell.

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

String

CELL_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3.

protected

TableCellEditor

cellEditor

The editor used to edit the data cells of the column.

protected

TableCellRenderer

cellRenderer

The renderer used to draw the data cells of the column.

static

String

COLUMN_WIDTH_PROPERTY

Obsolete as of Java 2 platform v1.3.

static

String

HEADER_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3.

static

String

HEADER_VALUE_PROPERTY

Obsolete as of Java 2 platform v1.3.

protected

TableCellRenderer

headerRenderer

The renderer used to draw the header of the column.

protected

Object

headerValue

The header value of the column.

protected

Object

identifier

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns.

protected boolean

isResizable

If true, the user is allowed to resize the column; the default is true.

protected int

maxWidth

The maximum width of the column.

protected int

minWidth

The minimum width of the column.

protected int

modelIndex

The index of the column in the model which is to be displayed by
this

TableColumn

.

protected int

resizedPostingDisableCount

Deprecated.

as of Java 2 platform v1.3

protected int

width

The width of the column.

---

#### Field Summary

Obsolete as of Java 2 platform v1.3.

The editor used to edit the data cells of the column.

The renderer used to draw the data cells of the column.

The renderer used to draw the header of the column.

The header value of the column.

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns.

If true, the user is allowed to resize the column; the default is true.

The maximum width of the column.

The minimum width of the column.

The index of the column in the model which is to be displayed by
this

TableColumn

.

Deprecated.

as of Java 2 platform v1.3

The width of the column.

Constructor Summary

Constructors

Constructor

Description

TableColumn

()

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex)

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex,
int width)

Cover method, using a

null

renderer and a

null

editor.

TableColumn

​(int modelIndex,
int width,

TableCellRenderer

cellRenderer,

TableCellEditor

cellEditor)

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.

---

#### Constructor Summary

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

Cover method, using a

null

renderer and a

null

editor.

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

protected

TableCellRenderer

createDefaultHeaderRenderer

()

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor.

void

disableResizedPosting

()

Deprecated.

as of Java 2 platform v1.3

void

enableResizedPosting

()

Deprecated.

as of Java 2 platform v1.3

TableCellEditor

getCellEditor

()

Returns the

TableCellEditor

used by the

JTable

to edit values for this column.

TableCellRenderer

getCellRenderer

()

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column.

TableCellRenderer

getHeaderRenderer

()

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

.

Object

getHeaderValue

()

Returns the

Object

used as the value for the header
renderer.

Object

getIdentifier

()

Returns the

identifier

object for this column.

int

getMaxWidth

()

Returns the maximum width for the

TableColumn

.

int

getMinWidth

()

Returns the minimum width for the

TableColumn

.

int

getModelIndex

()

Returns the model index for this column.

int

getPreferredWidth

()

Returns the preferred width of the

TableColumn

.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

boolean

getResizable

()

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise.

int

getWidth

()

Returns the width of the

TableColumn

.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setCellEditor

​(

TableCellEditor

cellEditor)

Sets the editor to used by when a cell in this column is edited.

void

setCellRenderer

​(

TableCellRenderer

cellRenderer)

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

void

setHeaderRenderer

​(

TableCellRenderer

headerRenderer)

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

void

setHeaderValue

​(

Object

headerValue)

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

.

void

setIdentifier

​(

Object

identifier)

Sets the

TableColumn

's identifier to

anIdentifier

.

void

setMaxWidth

​(int maxWidth)

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

void

setMinWidth

​(int minWidth)

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.

void

setModelIndex

​(int modelIndex)

Sets the model index for this column.

void

setPreferredWidth

​(int preferredWidth)

Sets this column's preferred width to

preferredWidth

.

void

setResizable

​(boolean isResizable)

Sets whether this column can be resized.

void

setWidth

​(int width)

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.

void

sizeWidthToFit

()

Resizes the

TableColumn

to fit the width of its header cell.

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

Adds a

PropertyChangeListener

to the listener list.

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor.

Deprecated.

as of Java 2 platform v1.3

Returns the

TableCellEditor

used by the

JTable

to edit values for this column.

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column.

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

.

Returns the

Object

used as the value for the header
renderer.

Returns the

identifier

object for this column.

Returns the maximum width for the

TableColumn

.

Returns the minimum width for the

TableColumn

.

Returns the model index for this column.

Returns the preferred width of the

TableColumn

.

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise.

Returns the width of the

TableColumn

.

Removes a

PropertyChangeListener

from the listener list.

Sets the editor to used by when a cell in this column is edited.

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

.

Sets the

TableColumn

's identifier to

anIdentifier

.

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.

Sets the model index for this column.

Sets this column's preferred width to

preferredWidth

.

Sets whether this column can be resized.

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.

Resizes the

TableColumn

to fit the width of its header cell.

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

- COLUMN_WIDTH_PROPERTY

```java
public static final
String
COLUMN_WIDTH_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- HEADER_VALUE_PROPERTY

```java
public static final
String
HEADER_VALUE_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- HEADER_RENDERER_PROPERTY

```java
public static final
String
HEADER_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- modelIndex

```java
protected int modelIndex
```

The index of the column in the model which is to be displayed by
this

TableColumn

. As columns are moved around in the
view

modelIndex

remains constant.

- identifier

```java
protected
Object
identifier
```

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns. The table package does
not modify or invoke any methods in these identifier objects other
than the

equals

method which is used in the

getColumnIndex()

method in the

DefaultTableColumnModel

.

- width

```java
protected int width
```

The width of the column.

- minWidth

```java
protected int minWidth
```

The minimum width of the column.

- maxWidth

```java
protected int maxWidth
```

The maximum width of the column.

- headerRenderer

```java
protected
TableCellRenderer
headerRenderer
```

The renderer used to draw the header of the column.

- headerValue

```java
protected
Object
headerValue
```

The header value of the column.

- cellRenderer

```java
protected
TableCellRenderer
cellRenderer
```

The renderer used to draw the data cells of the column.

- cellEditor

```java
protected
TableCellEditor
cellEditor
```

The editor used to edit the data cells of the column.

- isResizable

```java
protected boolean isResizable
```

If true, the user is allowed to resize the column; the default is true.

- resizedPostingDisableCount

```java
@Deprecated

protected transient int resizedPostingDisableCount
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TableColumn

```java
public TableColumn()
```

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.
This method is intended for serialization.

**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex)
```

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex,
int width)
```

Cover method, using a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex,
int width,

TableCellRenderer
cellRenderer,

TableCellEditor
cellEditor)
```

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.
The value of

width

is used
for both the initial and preferred width;
if

width

is negative,
they're set to 0.
The minimum width is set to 15 unless the initial width is less,
in which case the minimum width is set to
the initial width.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

**Parameters:** modelIndex

- the index of the column
in the model that supplies the data for this column in the table;
the model index remains the same
even when columns are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**Parameters:** cellRenderer

- the object used to render values in this column
**Parameters:** cellEditor

- the object used to edit values in this column
**See Also:** getMinWidth()

,

JTable.getDefaultRenderer(Class)

,

JTable.getDefaultEditor(Class)

,

JTable.getCellRenderer(int, int)

,

JTable.getCellEditor(int, int)

============ METHOD DETAIL ==========

- Method Detail

- setModelIndex

```java
@BeanProperty
(
description
="The model index.")
public void setModelIndex​(int modelIndex)
```

Sets the model index for this column. The model index is the
index of the column in the model that will be displayed by this

TableColumn

. As the

TableColumn

is moved around in the view the model index remains constant.

**Parameters:** modelIndex

- the new modelIndex

- getModelIndex

```java
public int getModelIndex()
```

Returns the model index for this column.

**Returns:** the

modelIndex

property

- setIdentifier

```java
@BeanProperty
(
description
="A unique identifier for this column.")
public void setIdentifier​(
Object
identifier)
```

Sets the

TableColumn

's identifier to

anIdentifier

.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

**Parameters:** identifier

- an identifier for this column
**See Also:** getIdentifier()

- getIdentifier

```java
public
Object
getIdentifier()
```

Returns the

identifier

object for this column.
Note identifiers are not used by

JTable

,
they are purely a convenience for external use.
If the

identifier

is

null

,

getIdentifier()

returns

getHeaderValue

as a default.

**Returns:** the

identifier

property
**See Also:** setIdentifier(java.lang.Object)

- setHeaderValue

```java
@BeanProperty
(
description
="The text to be used by the header renderer.")
public void setHeaderValue​(
Object
headerValue)
```

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

. When the

TableColumn

is created, the default

headerValue

is

null

.

**Parameters:** headerValue

- the new headerValue
**See Also:** getHeaderValue()

- getHeaderValue

```java
public
Object
getHeaderValue()
```

Returns the

Object

used as the value for the header
renderer.

**Returns:** the

headerValue

property
**See Also:** setHeaderValue(java.lang.Object)

- setHeaderRenderer

```java
@BeanProperty
(
description
="The header renderer.")
public void setHeaderRenderer​(
TableCellRenderer
headerRenderer)
```

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

**Parameters:** headerRenderer

- the new headerRenderer
**See Also:** getHeaderRenderer()

- getHeaderRenderer

```java
public
TableCellRenderer
getHeaderRenderer()
```

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

. When the

headerRenderer

is

null

, the

JTableHeader

uses its

defaultRenderer

. The default value for a

headerRenderer

is

null

.

**Returns:** the

headerRenderer

property
**See Also:** setHeaderRenderer(javax.swing.table.TableCellRenderer)

,

setHeaderValue(java.lang.Object)

,

JTableHeader.getDefaultRenderer()

- setCellRenderer

```java
@BeanProperty
(
description
="The renderer to use for cell values.")
public void setCellRenderer​(
TableCellRenderer
cellRenderer)
```

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

**Parameters:** cellRenderer

- the new cellRenderer
**See Also:** getCellRenderer()

- getCellRenderer

```java
public
TableCellRenderer
getCellRenderer()
```

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column. The

cellRenderer

of the column
not only controls the visual look for the column, but is also used to
interpret the value object supplied by the

TableModel

.
When the

cellRenderer

is

null

,
the

JTable

uses a default renderer based on the
class of the cells in that column. The default value for a

cellRenderer

is

null

.

**Returns:** the

cellRenderer

property
**See Also:** setCellRenderer(javax.swing.table.TableCellRenderer)

,

JTable.setDefaultRenderer(java.lang.Class<?>, javax.swing.table.TableCellRenderer)

- setCellEditor

```java
@BeanProperty
(
description
="The editor to use for cell values.")
public void setCellEditor​(
TableCellEditor
cellEditor)
```

Sets the editor to used by when a cell in this column is edited.

**Parameters:** cellEditor

- the new cellEditor
**See Also:** getCellEditor()

- getCellEditor

```java
public
TableCellEditor
getCellEditor()
```

Returns the

TableCellEditor

used by the

JTable

to edit values for this column. When the

cellEditor

is

null

, the

JTable

uses a default editor based on the
class of the cells in that column. The default value for a

cellEditor

is

null

.

**Returns:** the

cellEditor

property
**See Also:** setCellEditor(javax.swing.table.TableCellEditor)

,

JTable.setDefaultEditor(java.lang.Class<?>, javax.swing.table.TableCellEditor)

- setWidth

```java
@BeanProperty
(
description
="The width of the column.")
public void setWidth​(int width)
```

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.
Like a layout manager in the
AWT, the

JTable

adjusts a column's width automatically
whenever the
table itself changes size, or a column's preferred width is changed.
Setting widths programmatically therefore has no long term effect.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

**Parameters:** width

- the new width
**See Also:** getWidth()

,

setMinWidth(int)

,

setMaxWidth(int)

,

setPreferredWidth(int)

,

JTable.doLayout()

- getWidth

```java
public int getWidth()
```

Returns the width of the

TableColumn

. The default width is
75.

**Returns:** the

width

property
**See Also:** setWidth(int)

- setPreferredWidth

```java
@BeanProperty
(
description
="The preferred width of the column.")
public void setPreferredWidth​(int preferredWidth)
```

Sets this column's preferred width to

preferredWidth

.
If

preferredWidth

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

**Parameters:** preferredWidth

- the new preferred width
**See Also:** getPreferredWidth()

,

JTable.doLayout()

- getPreferredWidth

```java
public int getPreferredWidth()
```

Returns the preferred width of the

TableColumn

.
The default preferred width is 75.

**Returns:** the

preferredWidth

property
**See Also:** setPreferredWidth(int)

- setMinWidth

```java
@BeanProperty
(
description
="The minimum width of the column.")
public void setMinWidth​(int minWidth)
```

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.
For example, if the

minWidth

argument is negative,
this method sets the

minWidth

property to 0.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

**Parameters:** minWidth

- the new minimum width
**See Also:** getMinWidth()

,

setPreferredWidth(int)

,

setMaxWidth(int)

- getMinWidth

```java
public int getMinWidth()
```

Returns the minimum width for the

TableColumn

. The

TableColumn

's width can't be made less than this either
by the user or programmatically.

**Returns:** the

minWidth

property
**See Also:** setMinWidth(int)

,

TableColumn(int, int, TableCellRenderer, TableCellEditor)

- setMaxWidth

```java
@BeanProperty
(
description
="The maximum width of the column.")
public void setMaxWidth​(int maxWidth)
```

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

**Parameters:** maxWidth

- the new maximum width
**See Also:** getMaxWidth()

,

setPreferredWidth(int)

,

setMinWidth(int)

- getMaxWidth

```java
public int getMaxWidth()
```

Returns the maximum width for the

TableColumn

. The

TableColumn

's width can't be made larger than this
either by the user or programmatically. The default maxWidth
is Integer.MAX_VALUE.

**Returns:** the

maxWidth

property
**See Also:** setMaxWidth(int)

- setResizable

```java
@BeanProperty
(
description
="Whether or not this column can be resized.")
public void setResizable​(boolean isResizable)
```

Sets whether this column can be resized.

**Parameters:** isResizable

- if true, resizing is allowed; otherwise false
**See Also:** getResizable()

- getResizable

```java
public boolean getResizable()
```

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise. You can change the width programmatically
regardless of this setting. The default is true.

**Returns:** the

isResizable

property
**See Also:** setResizable(boolean)

- sizeWidthToFit

```java
public void sizeWidthToFit()
```

Resizes the

TableColumn

to fit the width of its header cell.
This method does nothing if the header renderer is

null

(the default case). Otherwise, it sets the minimum, maximum and preferred
widths of this column to the widths of the minimum, maximum and preferred
sizes of the Component delivered by the header renderer.
The transient "width" property of this TableColumn is also set to the
preferred width. Note this method is not used internally by the table
package.

**See Also:** setPreferredWidth(int)

- disableResizedPosting

```java
@Deprecated

public void disableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

- enableResizedPosting

```java
@Deprecated

public void enableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all bound properties of this class, including the
following:

- this TableColumn's modelIndex ("modelIndex")
- this TableColumn's identifier ("identifier")
- this TableColumn's header value ("headerValue")
- this TableColumn's header renderer ("headerRenderer")
- this TableColumn's cell renderer ("cellRenderer")
- this TableColumn's cell editor ("cellEditor")
- this TableColumn's width ("width")
- this TableColumn's preferred width ("preferredWidth")
- this TableColumn's minimum width ("minWidth")
- this TableColumn's maximum width ("maxWidth")
- this TableColumn's resizable state ("isResizable")

**Parameters:** listener

- the listener to be added
**See Also:** removePropertyChangeListener(PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
The

PropertyChangeListener

to be removed was registered
for all properties.

**Parameters:** listener

- the listener to be removed

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- createDefaultHeaderRenderer

```java
protected
TableCellRenderer
createDefaultHeaderRenderer()
```

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor. Previously this method was used by the

TableColumn

to create a default header renderer.
As of Java 2 platform v1.3, the default header renderer is

null

.

JTableHeader

now provides its own shared default
renderer, just as the

JTable

does for its cell renderers.

**Returns:** the default header renderer
**See Also:** JTableHeader.createDefaultRenderer()

Field Detail

- COLUMN_WIDTH_PROPERTY

```java
public static final
String
COLUMN_WIDTH_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- HEADER_VALUE_PROPERTY

```java
public static final
String
HEADER_VALUE_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- HEADER_RENDERER_PROPERTY

```java
public static final
String
HEADER_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

- modelIndex

```java
protected int modelIndex
```

The index of the column in the model which is to be displayed by
this

TableColumn

. As columns are moved around in the
view

modelIndex

remains constant.

- identifier

```java
protected
Object
identifier
```

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns. The table package does
not modify or invoke any methods in these identifier objects other
than the

equals

method which is used in the

getColumnIndex()

method in the

DefaultTableColumnModel

.

- width

```java
protected int width
```

The width of the column.

- minWidth

```java
protected int minWidth
```

The minimum width of the column.

- maxWidth

```java
protected int maxWidth
```

The maximum width of the column.

- headerRenderer

```java
protected
TableCellRenderer
headerRenderer
```

The renderer used to draw the header of the column.

- headerValue

```java
protected
Object
headerValue
```

The header value of the column.

- cellRenderer

```java
protected
TableCellRenderer
cellRenderer
```

The renderer used to draw the data cells of the column.

- cellEditor

```java
protected
TableCellEditor
cellEditor
```

The editor used to edit the data cells of the column.

- isResizable

```java
protected boolean isResizable
```

If true, the user is allowed to resize the column; the default is true.

- resizedPostingDisableCount

```java
@Deprecated

protected transient int resizedPostingDisableCount
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### Field Detail

COLUMN_WIDTH_PROPERTY

```java
public static final
String
COLUMN_WIDTH_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

---

#### COLUMN_WIDTH_PROPERTY

public static final

String

COLUMN_WIDTH_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

HEADER_VALUE_PROPERTY

```java
public static final
String
HEADER_VALUE_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

---

#### HEADER_VALUE_PROPERTY

public static final

String

HEADER_VALUE_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

HEADER_RENDERER_PROPERTY

```java
public static final
String
HEADER_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

---

#### HEADER_RENDERER_PROPERTY

public static final

String

HEADER_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

**See Also:** Constant Field Values

---

#### CELL_RENDERER_PROPERTY

public static final

String

CELL_RENDERER_PROPERTY

Obsolete as of Java 2 platform v1.3. Please use string literals to identify
properties.

modelIndex

```java
protected int modelIndex
```

The index of the column in the model which is to be displayed by
this

TableColumn

. As columns are moved around in the
view

modelIndex

remains constant.

---

#### modelIndex

protected int modelIndex

The index of the column in the model which is to be displayed by
this

TableColumn

. As columns are moved around in the
view

modelIndex

remains constant.

identifier

```java
protected
Object
identifier
```

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns. The table package does
not modify or invoke any methods in these identifier objects other
than the

equals

method which is used in the

getColumnIndex()

method in the

DefaultTableColumnModel

.

---

#### identifier

protected

Object

identifier

This object is not used internally by the drawing machinery of
the

JTable

; identifiers may be set in the

TableColumn

as an
optional way to tag and locate table columns. The table package does
not modify or invoke any methods in these identifier objects other
than the

equals

method which is used in the

getColumnIndex()

method in the

DefaultTableColumnModel

.

width

```java
protected int width
```

The width of the column.

---

#### width

protected int width

The width of the column.

minWidth

```java
protected int minWidth
```

The minimum width of the column.

---

#### minWidth

protected int minWidth

The minimum width of the column.

maxWidth

```java
protected int maxWidth
```

The maximum width of the column.

---

#### maxWidth

protected int maxWidth

The maximum width of the column.

headerRenderer

```java
protected
TableCellRenderer
headerRenderer
```

The renderer used to draw the header of the column.

---

#### headerRenderer

protected

TableCellRenderer

headerRenderer

The renderer used to draw the header of the column.

headerValue

```java
protected
Object
headerValue
```

The header value of the column.

---

#### headerValue

protected

Object

headerValue

The header value of the column.

cellRenderer

```java
protected
TableCellRenderer
cellRenderer
```

The renderer used to draw the data cells of the column.

---

#### cellRenderer

protected

TableCellRenderer

cellRenderer

The renderer used to draw the data cells of the column.

cellEditor

```java
protected
TableCellEditor
cellEditor
```

The editor used to edit the data cells of the column.

---

#### cellEditor

protected

TableCellEditor

cellEditor

The editor used to edit the data cells of the column.

isResizable

```java
protected boolean isResizable
```

If true, the user is allowed to resize the column; the default is true.

---

#### isResizable

protected boolean isResizable

If true, the user is allowed to resize the column; the default is true.

resizedPostingDisableCount

```java
@Deprecated

protected transient int resizedPostingDisableCount
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### resizedPostingDisableCount

@Deprecated

protected transient int resizedPostingDisableCount

This field was not used in previous releases and there are
currently no plans to support it in the future.

Constructor Detail

- TableColumn

```java
public TableColumn()
```

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.
This method is intended for serialization.

**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex)
```

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex,
int width)
```

Cover method, using a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

- TableColumn

```java
public TableColumn​(int modelIndex,
int width,

TableCellRenderer
cellRenderer,

TableCellEditor
cellEditor)
```

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.
The value of

width

is used
for both the initial and preferred width;
if

width

is negative,
they're set to 0.
The minimum width is set to 15 unless the initial width is less,
in which case the minimum width is set to
the initial width.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

**Parameters:** modelIndex

- the index of the column
in the model that supplies the data for this column in the table;
the model index remains the same
even when columns are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**Parameters:** cellRenderer

- the object used to render values in this column
**Parameters:** cellEditor

- the object used to edit values in this column
**See Also:** getMinWidth()

,

JTable.getDefaultRenderer(Class)

,

JTable.getDefaultEditor(Class)

,

JTable.getCellRenderer(int, int)

,

JTable.getCellEditor(int, int)

---

#### Constructor Detail

TableColumn

```java
public TableColumn()
```

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.
This method is intended for serialization.

**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### TableColumn

public TableColumn()

Cover method, using a default model index of 0,
default width of 75, a

null

renderer and a

null

editor.
This method is intended for serialization.

TableColumn

```java
public TableColumn​(int modelIndex)
```

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### TableColumn

public TableColumn​(int modelIndex)

Cover method, using a default width of 75, a

null

renderer and a

null

editor.

TableColumn

```java
public TableColumn​(int modelIndex,
int width)
```

Cover method, using a

null

renderer and a

null

editor.

**Parameters:** modelIndex

- the index of the column in the model
that supplies the data for this column in the table;
the model index remains the same even when columns
are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**See Also:** TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### TableColumn

public TableColumn​(int modelIndex,
int width)

Cover method, using a

null

renderer and a

null

editor.

TableColumn

```java
public TableColumn​(int modelIndex,
int width,

TableCellRenderer
cellRenderer,

TableCellEditor
cellEditor)
```

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.
The value of

width

is used
for both the initial and preferred width;
if

width

is negative,
they're set to 0.
The minimum width is set to 15 unless the initial width is less,
in which case the minimum width is set to
the initial width.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

**Parameters:** modelIndex

- the index of the column
in the model that supplies the data for this column in the table;
the model index remains the same
even when columns are reordered in the view
**Parameters:** width

- this column's preferred width and initial width
**Parameters:** cellRenderer

- the object used to render values in this column
**Parameters:** cellEditor

- the object used to edit values in this column
**See Also:** getMinWidth()

,

JTable.getDefaultRenderer(Class)

,

JTable.getDefaultEditor(Class)

,

JTable.getCellRenderer(int, int)

,

JTable.getCellEditor(int, int)

---

#### TableColumn

public TableColumn​(int modelIndex,
int width,

TableCellRenderer

cellRenderer,

TableCellEditor

cellEditor)

Creates and initializes an instance of

TableColumn

with the specified model index,
width, cell renderer, and cell editor;
all

TableColumn

constructors delegate to this one.
The value of

width

is used
for both the initial and preferred width;
if

width

is negative,
they're set to 0.
The minimum width is set to 15 unless the initial width is less,
in which case the minimum width is set to
the initial width.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

When the

cellRenderer

or

cellEditor

parameter is

null

,
a default value provided by the

JTable

getDefaultRenderer

or

getDefaultEditor

method, respectively,
is used to
provide defaults based on the type of the data in this column.
This column-centric rendering strategy can be circumvented by overriding
the

getCellRenderer

methods in

JTable

.

Method Detail

- setModelIndex

```java
@BeanProperty
(
description
="The model index.")
public void setModelIndex​(int modelIndex)
```

Sets the model index for this column. The model index is the
index of the column in the model that will be displayed by this

TableColumn

. As the

TableColumn

is moved around in the view the model index remains constant.

**Parameters:** modelIndex

- the new modelIndex

- getModelIndex

```java
public int getModelIndex()
```

Returns the model index for this column.

**Returns:** the

modelIndex

property

- setIdentifier

```java
@BeanProperty
(
description
="A unique identifier for this column.")
public void setIdentifier​(
Object
identifier)
```

Sets the

TableColumn

's identifier to

anIdentifier

.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

**Parameters:** identifier

- an identifier for this column
**See Also:** getIdentifier()

- getIdentifier

```java
public
Object
getIdentifier()
```

Returns the

identifier

object for this column.
Note identifiers are not used by

JTable

,
they are purely a convenience for external use.
If the

identifier

is

null

,

getIdentifier()

returns

getHeaderValue

as a default.

**Returns:** the

identifier

property
**See Also:** setIdentifier(java.lang.Object)

- setHeaderValue

```java
@BeanProperty
(
description
="The text to be used by the header renderer.")
public void setHeaderValue​(
Object
headerValue)
```

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

. When the

TableColumn

is created, the default

headerValue

is

null

.

**Parameters:** headerValue

- the new headerValue
**See Also:** getHeaderValue()

- getHeaderValue

```java
public
Object
getHeaderValue()
```

Returns the

Object

used as the value for the header
renderer.

**Returns:** the

headerValue

property
**See Also:** setHeaderValue(java.lang.Object)

- setHeaderRenderer

```java
@BeanProperty
(
description
="The header renderer.")
public void setHeaderRenderer​(
TableCellRenderer
headerRenderer)
```

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

**Parameters:** headerRenderer

- the new headerRenderer
**See Also:** getHeaderRenderer()

- getHeaderRenderer

```java
public
TableCellRenderer
getHeaderRenderer()
```

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

. When the

headerRenderer

is

null

, the

JTableHeader

uses its

defaultRenderer

. The default value for a

headerRenderer

is

null

.

**Returns:** the

headerRenderer

property
**See Also:** setHeaderRenderer(javax.swing.table.TableCellRenderer)

,

setHeaderValue(java.lang.Object)

,

JTableHeader.getDefaultRenderer()

- setCellRenderer

```java
@BeanProperty
(
description
="The renderer to use for cell values.")
public void setCellRenderer​(
TableCellRenderer
cellRenderer)
```

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

**Parameters:** cellRenderer

- the new cellRenderer
**See Also:** getCellRenderer()

- getCellRenderer

```java
public
TableCellRenderer
getCellRenderer()
```

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column. The

cellRenderer

of the column
not only controls the visual look for the column, but is also used to
interpret the value object supplied by the

TableModel

.
When the

cellRenderer

is

null

,
the

JTable

uses a default renderer based on the
class of the cells in that column. The default value for a

cellRenderer

is

null

.

**Returns:** the

cellRenderer

property
**See Also:** setCellRenderer(javax.swing.table.TableCellRenderer)

,

JTable.setDefaultRenderer(java.lang.Class<?>, javax.swing.table.TableCellRenderer)

- setCellEditor

```java
@BeanProperty
(
description
="The editor to use for cell values.")
public void setCellEditor​(
TableCellEditor
cellEditor)
```

Sets the editor to used by when a cell in this column is edited.

**Parameters:** cellEditor

- the new cellEditor
**See Also:** getCellEditor()

- getCellEditor

```java
public
TableCellEditor
getCellEditor()
```

Returns the

TableCellEditor

used by the

JTable

to edit values for this column. When the

cellEditor

is

null

, the

JTable

uses a default editor based on the
class of the cells in that column. The default value for a

cellEditor

is

null

.

**Returns:** the

cellEditor

property
**See Also:** setCellEditor(javax.swing.table.TableCellEditor)

,

JTable.setDefaultEditor(java.lang.Class<?>, javax.swing.table.TableCellEditor)

- setWidth

```java
@BeanProperty
(
description
="The width of the column.")
public void setWidth​(int width)
```

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.
Like a layout manager in the
AWT, the

JTable

adjusts a column's width automatically
whenever the
table itself changes size, or a column's preferred width is changed.
Setting widths programmatically therefore has no long term effect.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

**Parameters:** width

- the new width
**See Also:** getWidth()

,

setMinWidth(int)

,

setMaxWidth(int)

,

setPreferredWidth(int)

,

JTable.doLayout()

- getWidth

```java
public int getWidth()
```

Returns the width of the

TableColumn

. The default width is
75.

**Returns:** the

width

property
**See Also:** setWidth(int)

- setPreferredWidth

```java
@BeanProperty
(
description
="The preferred width of the column.")
public void setPreferredWidth​(int preferredWidth)
```

Sets this column's preferred width to

preferredWidth

.
If

preferredWidth

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

**Parameters:** preferredWidth

- the new preferred width
**See Also:** getPreferredWidth()

,

JTable.doLayout()

- getPreferredWidth

```java
public int getPreferredWidth()
```

Returns the preferred width of the

TableColumn

.
The default preferred width is 75.

**Returns:** the

preferredWidth

property
**See Also:** setPreferredWidth(int)

- setMinWidth

```java
@BeanProperty
(
description
="The minimum width of the column.")
public void setMinWidth​(int minWidth)
```

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.
For example, if the

minWidth

argument is negative,
this method sets the

minWidth

property to 0.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

**Parameters:** minWidth

- the new minimum width
**See Also:** getMinWidth()

,

setPreferredWidth(int)

,

setMaxWidth(int)

- getMinWidth

```java
public int getMinWidth()
```

Returns the minimum width for the

TableColumn

. The

TableColumn

's width can't be made less than this either
by the user or programmatically.

**Returns:** the

minWidth

property
**See Also:** setMinWidth(int)

,

TableColumn(int, int, TableCellRenderer, TableCellEditor)

- setMaxWidth

```java
@BeanProperty
(
description
="The maximum width of the column.")
public void setMaxWidth​(int maxWidth)
```

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

**Parameters:** maxWidth

- the new maximum width
**See Also:** getMaxWidth()

,

setPreferredWidth(int)

,

setMinWidth(int)

- getMaxWidth

```java
public int getMaxWidth()
```

Returns the maximum width for the

TableColumn

. The

TableColumn

's width can't be made larger than this
either by the user or programmatically. The default maxWidth
is Integer.MAX_VALUE.

**Returns:** the

maxWidth

property
**See Also:** setMaxWidth(int)

- setResizable

```java
@BeanProperty
(
description
="Whether or not this column can be resized.")
public void setResizable​(boolean isResizable)
```

Sets whether this column can be resized.

**Parameters:** isResizable

- if true, resizing is allowed; otherwise false
**See Also:** getResizable()

- getResizable

```java
public boolean getResizable()
```

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise. You can change the width programmatically
regardless of this setting. The default is true.

**Returns:** the

isResizable

property
**See Also:** setResizable(boolean)

- sizeWidthToFit

```java
public void sizeWidthToFit()
```

Resizes the

TableColumn

to fit the width of its header cell.
This method does nothing if the header renderer is

null

(the default case). Otherwise, it sets the minimum, maximum and preferred
widths of this column to the widths of the minimum, maximum and preferred
sizes of the Component delivered by the header renderer.
The transient "width" property of this TableColumn is also set to the
preferred width. Note this method is not used internally by the table
package.

**See Also:** setPreferredWidth(int)

- disableResizedPosting

```java
@Deprecated

public void disableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

- enableResizedPosting

```java
@Deprecated

public void enableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all bound properties of this class, including the
following:

- this TableColumn's modelIndex ("modelIndex")
- this TableColumn's identifier ("identifier")
- this TableColumn's header value ("headerValue")
- this TableColumn's header renderer ("headerRenderer")
- this TableColumn's cell renderer ("cellRenderer")
- this TableColumn's cell editor ("cellEditor")
- this TableColumn's width ("width")
- this TableColumn's preferred width ("preferredWidth")
- this TableColumn's minimum width ("minWidth")
- this TableColumn's maximum width ("maxWidth")
- this TableColumn's resizable state ("isResizable")

**Parameters:** listener

- the listener to be added
**See Also:** removePropertyChangeListener(PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
The

PropertyChangeListener

to be removed was registered
for all properties.

**Parameters:** listener

- the listener to be removed

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- createDefaultHeaderRenderer

```java
protected
TableCellRenderer
createDefaultHeaderRenderer()
```

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor. Previously this method was used by the

TableColumn

to create a default header renderer.
As of Java 2 platform v1.3, the default header renderer is

null

.

JTableHeader

now provides its own shared default
renderer, just as the

JTable

does for its cell renderers.

**Returns:** the default header renderer
**See Also:** JTableHeader.createDefaultRenderer()

---

#### Method Detail

setModelIndex

```java
@BeanProperty
(
description
="The model index.")
public void setModelIndex​(int modelIndex)
```

Sets the model index for this column. The model index is the
index of the column in the model that will be displayed by this

TableColumn

. As the

TableColumn

is moved around in the view the model index remains constant.

**Parameters:** modelIndex

- the new modelIndex

---

#### setModelIndex

@BeanProperty

(

description

="The model index.")
public void setModelIndex​(int modelIndex)

Sets the model index for this column. The model index is the
index of the column in the model that will be displayed by this

TableColumn

. As the

TableColumn

is moved around in the view the model index remains constant.

getModelIndex

```java
public int getModelIndex()
```

Returns the model index for this column.

**Returns:** the

modelIndex

property

---

#### getModelIndex

public int getModelIndex()

Returns the model index for this column.

setIdentifier

```java
@BeanProperty
(
description
="A unique identifier for this column.")
public void setIdentifier​(
Object
identifier)
```

Sets the

TableColumn

's identifier to

anIdentifier

.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

**Parameters:** identifier

- an identifier for this column
**See Also:** getIdentifier()

---

#### setIdentifier

@BeanProperty

(

description

="A unique identifier for this column.")
public void setIdentifier​(

Object

identifier)

Sets the

TableColumn

's identifier to

anIdentifier

.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

Note: identifiers are not used by the

JTable

,
they are purely a
convenience for the external tagging and location of columns.

getIdentifier

```java
public
Object
getIdentifier()
```

Returns the

identifier

object for this column.
Note identifiers are not used by

JTable

,
they are purely a convenience for external use.
If the

identifier

is

null

,

getIdentifier()

returns

getHeaderValue

as a default.

**Returns:** the

identifier

property
**See Also:** setIdentifier(java.lang.Object)

---

#### getIdentifier

public

Object

getIdentifier()

Returns the

identifier

object for this column.
Note identifiers are not used by

JTable

,
they are purely a convenience for external use.
If the

identifier

is

null

,

getIdentifier()

returns

getHeaderValue

as a default.

setHeaderValue

```java
@BeanProperty
(
description
="The text to be used by the header renderer.")
public void setHeaderValue​(
Object
headerValue)
```

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

. When the

TableColumn

is created, the default

headerValue

is

null

.

**Parameters:** headerValue

- the new headerValue
**See Also:** getHeaderValue()

---

#### setHeaderValue

@BeanProperty

(

description

="The text to be used by the header renderer.")
public void setHeaderValue​(

Object

headerValue)

Sets the

Object

whose string representation will be
used as the value for the

headerRenderer

. When the

TableColumn

is created, the default

headerValue

is

null

.

getHeaderValue

```java
public
Object
getHeaderValue()
```

Returns the

Object

used as the value for the header
renderer.

**Returns:** the

headerValue

property
**See Also:** setHeaderValue(java.lang.Object)

---

#### getHeaderValue

public

Object

getHeaderValue()

Returns the

Object

used as the value for the header
renderer.

setHeaderRenderer

```java
@BeanProperty
(
description
="The header renderer.")
public void setHeaderRenderer​(
TableCellRenderer
headerRenderer)
```

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

**Parameters:** headerRenderer

- the new headerRenderer
**See Also:** getHeaderRenderer()

---

#### setHeaderRenderer

@BeanProperty

(

description

="The header renderer.")
public void setHeaderRenderer​(

TableCellRenderer

headerRenderer)

Sets the

TableCellRenderer

used to draw the

TableColumn

's header to

headerRenderer

.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

It is the header renderers responsibility to render the sorting
indicator. If you are using sorting and specify a renderer your
renderer must render the sorting indication.

getHeaderRenderer

```java
public
TableCellRenderer
getHeaderRenderer()
```

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

. When the

headerRenderer

is

null

, the

JTableHeader

uses its

defaultRenderer

. The default value for a

headerRenderer

is

null

.

**Returns:** the

headerRenderer

property
**See Also:** setHeaderRenderer(javax.swing.table.TableCellRenderer)

,

setHeaderValue(java.lang.Object)

,

JTableHeader.getDefaultRenderer()

---

#### getHeaderRenderer

public

TableCellRenderer

getHeaderRenderer()

Returns the

TableCellRenderer

used to draw the header of the

TableColumn

. When the

headerRenderer

is

null

, the

JTableHeader

uses its

defaultRenderer

. The default value for a

headerRenderer

is

null

.

setCellRenderer

```java
@BeanProperty
(
description
="The renderer to use for cell values.")
public void setCellRenderer​(
TableCellRenderer
cellRenderer)
```

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

**Parameters:** cellRenderer

- the new cellRenderer
**See Also:** getCellRenderer()

---

#### setCellRenderer

@BeanProperty

(

description

="The renderer to use for cell values.")
public void setCellRenderer​(

TableCellRenderer

cellRenderer)

Sets the

TableCellRenderer

used by

JTable

to draw individual values for this column.

getCellRenderer

```java
public
TableCellRenderer
getCellRenderer()
```

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column. The

cellRenderer

of the column
not only controls the visual look for the column, but is also used to
interpret the value object supplied by the

TableModel

.
When the

cellRenderer

is

null

,
the

JTable

uses a default renderer based on the
class of the cells in that column. The default value for a

cellRenderer

is

null

.

**Returns:** the

cellRenderer

property
**See Also:** setCellRenderer(javax.swing.table.TableCellRenderer)

,

JTable.setDefaultRenderer(java.lang.Class<?>, javax.swing.table.TableCellRenderer)

---

#### getCellRenderer

public

TableCellRenderer

getCellRenderer()

Returns the

TableCellRenderer

used by the

JTable

to draw
values for this column. The

cellRenderer

of the column
not only controls the visual look for the column, but is also used to
interpret the value object supplied by the

TableModel

.
When the

cellRenderer

is

null

,
the

JTable

uses a default renderer based on the
class of the cells in that column. The default value for a

cellRenderer

is

null

.

setCellEditor

```java
@BeanProperty
(
description
="The editor to use for cell values.")
public void setCellEditor​(
TableCellEditor
cellEditor)
```

Sets the editor to used by when a cell in this column is edited.

**Parameters:** cellEditor

- the new cellEditor
**See Also:** getCellEditor()

---

#### setCellEditor

@BeanProperty

(

description

="The editor to use for cell values.")
public void setCellEditor​(

TableCellEditor

cellEditor)

Sets the editor to used by when a cell in this column is edited.

getCellEditor

```java
public
TableCellEditor
getCellEditor()
```

Returns the

TableCellEditor

used by the

JTable

to edit values for this column. When the

cellEditor

is

null

, the

JTable

uses a default editor based on the
class of the cells in that column. The default value for a

cellEditor

is

null

.

**Returns:** the

cellEditor

property
**See Also:** setCellEditor(javax.swing.table.TableCellEditor)

,

JTable.setDefaultEditor(java.lang.Class<?>, javax.swing.table.TableCellEditor)

---

#### getCellEditor

public

TableCellEditor

getCellEditor()

Returns the

TableCellEditor

used by the

JTable

to edit values for this column. When the

cellEditor

is

null

, the

JTable

uses a default editor based on the
class of the cells in that column. The default value for a

cellEditor

is

null

.

setWidth

```java
@BeanProperty
(
description
="The width of the column.")
public void setWidth​(int width)
```

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.
Like a layout manager in the
AWT, the

JTable

adjusts a column's width automatically
whenever the
table itself changes size, or a column's preferred width is changed.
Setting widths programmatically therefore has no long term effect.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

**Parameters:** width

- the new width
**See Also:** getWidth()

,

setMinWidth(int)

,

setMaxWidth(int)

,

setPreferredWidth(int)

,

JTable.doLayout()

---

#### setWidth

@BeanProperty

(

description

="The width of the column.")
public void setWidth​(int width)

This method should not be used to set the widths of columns in the

JTable

, use

setPreferredWidth

instead.
Like a layout manager in the
AWT, the

JTable

adjusts a column's width automatically
whenever the
table itself changes size, or a column's preferred width is changed.
Setting widths programmatically therefore has no long term effect.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

This method sets this column's width to

width

.
If

width

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

getWidth

```java
public int getWidth()
```

Returns the width of the

TableColumn

. The default width is
75.

**Returns:** the

width

property
**See Also:** setWidth(int)

---

#### getWidth

public int getWidth()

Returns the width of the

TableColumn

. The default width is
75.

setPreferredWidth

```java
@BeanProperty
(
description
="The preferred width of the column.")
public void setPreferredWidth​(int preferredWidth)
```

Sets this column's preferred width to

preferredWidth

.
If

preferredWidth

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

**Parameters:** preferredWidth

- the new preferred width
**See Also:** getPreferredWidth()

,

JTable.doLayout()

---

#### setPreferredWidth

@BeanProperty

(

description

="The preferred width of the column.")
public void setPreferredWidth​(int preferredWidth)

Sets this column's preferred width to

preferredWidth

.
If

preferredWidth

exceeds the minimum or maximum width,
it is adjusted to the appropriate limiting value.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

For details on how the widths of columns in the

JTable

(and

JTableHeader

) are calculated from the

preferredWidth

,
see the

doLayout

method in

JTable

.

getPreferredWidth

```java
public int getPreferredWidth()
```

Returns the preferred width of the

TableColumn

.
The default preferred width is 75.

**Returns:** the

preferredWidth

property
**See Also:** setPreferredWidth(int)

---

#### getPreferredWidth

public int getPreferredWidth()

Returns the preferred width of the

TableColumn

.
The default preferred width is 75.

setMinWidth

```java
@BeanProperty
(
description
="The minimum width of the column.")
public void setMinWidth​(int minWidth)
```

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.
For example, if the

minWidth

argument is negative,
this method sets the

minWidth

property to 0.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

**Parameters:** minWidth

- the new minimum width
**See Also:** getMinWidth()

,

setPreferredWidth(int)

,

setMaxWidth(int)

---

#### setMinWidth

@BeanProperty

(

description

="The minimum width of the column.")
public void setMinWidth​(int minWidth)

Sets the

TableColumn

's minimum width to

minWidth

,
adjusting the new minimum width if necessary to ensure that
0 <=

minWidth

<=

maxWidth

.
For example, if the

minWidth

argument is negative,
this method sets the

minWidth

property to 0.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

If the value of the

width

or

preferredWidth

property
is less than the new minimum width,
this method sets that property to the new minimum width.

getMinWidth

```java
public int getMinWidth()
```

Returns the minimum width for the

TableColumn

. The

TableColumn

's width can't be made less than this either
by the user or programmatically.

**Returns:** the

minWidth

property
**See Also:** setMinWidth(int)

,

TableColumn(int, int, TableCellRenderer, TableCellEditor)

---

#### getMinWidth

public int getMinWidth()

Returns the minimum width for the

TableColumn

. The

TableColumn

's width can't be made less than this either
by the user or programmatically.

setMaxWidth

```java
@BeanProperty
(
description
="The maximum width of the column.")
public void setMaxWidth​(int maxWidth)
```

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

**Parameters:** maxWidth

- the new maximum width
**See Also:** getMaxWidth()

,

setPreferredWidth(int)

,

setMinWidth(int)

---

#### setMaxWidth

@BeanProperty

(

description

="The maximum width of the column.")
public void setMaxWidth​(int maxWidth)

Sets the

TableColumn

's maximum width to

maxWidth

or,
if

maxWidth

is less than the minimum width,
to the minimum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

If the value of the

width

or

preferredWidth

property
is more than the new maximum width,
this method sets that property to the new maximum width.

getMaxWidth

```java
public int getMaxWidth()
```

Returns the maximum width for the

TableColumn

. The

TableColumn

's width can't be made larger than this
either by the user or programmatically. The default maxWidth
is Integer.MAX_VALUE.

**Returns:** the

maxWidth

property
**See Also:** setMaxWidth(int)

---

#### getMaxWidth

public int getMaxWidth()

Returns the maximum width for the

TableColumn

. The

TableColumn

's width can't be made larger than this
either by the user or programmatically. The default maxWidth
is Integer.MAX_VALUE.

setResizable

```java
@BeanProperty
(
description
="Whether or not this column can be resized.")
public void setResizable​(boolean isResizable)
```

Sets whether this column can be resized.

**Parameters:** isResizable

- if true, resizing is allowed; otherwise false
**See Also:** getResizable()

---

#### setResizable

@BeanProperty

(

description

="Whether or not this column can be resized.")
public void setResizable​(boolean isResizable)

Sets whether this column can be resized.

getResizable

```java
public boolean getResizable()
```

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise. You can change the width programmatically
regardless of this setting. The default is true.

**Returns:** the

isResizable

property
**See Also:** setResizable(boolean)

---

#### getResizable

public boolean getResizable()

Returns true if the user is allowed to resize the

TableColumn

's
width, false otherwise. You can change the width programmatically
regardless of this setting. The default is true.

sizeWidthToFit

```java
public void sizeWidthToFit()
```

Resizes the

TableColumn

to fit the width of its header cell.
This method does nothing if the header renderer is

null

(the default case). Otherwise, it sets the minimum, maximum and preferred
widths of this column to the widths of the minimum, maximum and preferred
sizes of the Component delivered by the header renderer.
The transient "width" property of this TableColumn is also set to the
preferred width. Note this method is not used internally by the table
package.

**See Also:** setPreferredWidth(int)

---

#### sizeWidthToFit

public void sizeWidthToFit()

Resizes the

TableColumn

to fit the width of its header cell.
This method does nothing if the header renderer is

null

(the default case). Otherwise, it sets the minimum, maximum and preferred
widths of this column to the widths of the minimum, maximum and preferred
sizes of the Component delivered by the header renderer.
The transient "width" property of this TableColumn is also set to the
preferred width. Note this method is not used internally by the table
package.

disableResizedPosting

```java
@Deprecated

public void disableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### disableResizedPosting

@Deprecated

public void disableResizedPosting()

This field was not used in previous releases and there are
currently no plans to support it in the future.

enableResizedPosting

```java
@Deprecated

public void enableResizedPosting()
```

Deprecated.

as of Java 2 platform v1.3

This field was not used in previous releases and there are
currently no plans to support it in the future.

---

#### enableResizedPosting

@Deprecated

public void enableResizedPosting()

This field was not used in previous releases and there are
currently no plans to support it in the future.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all bound properties of this class, including the
following:

- this TableColumn's modelIndex ("modelIndex")
- this TableColumn's identifier ("identifier")
- this TableColumn's header value ("headerValue")
- this TableColumn's header renderer ("headerRenderer")
- this TableColumn's cell renderer ("cellRenderer")
- this TableColumn's cell editor ("cellEditor")
- this TableColumn's width ("width")
- this TableColumn's preferred width ("preferredWidth")
- this TableColumn's minimum width ("minWidth")
- this TableColumn's maximum width ("maxWidth")
- this TableColumn's resizable state ("isResizable")

**Parameters:** listener

- the listener to be added
**See Also:** removePropertyChangeListener(PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all bound properties of this class, including the
following:

- this TableColumn's modelIndex ("modelIndex")
- this TableColumn's identifier ("identifier")
- this TableColumn's header value ("headerValue")
- this TableColumn's header renderer ("headerRenderer")
- this TableColumn's cell renderer ("cellRenderer")
- this TableColumn's cell editor ("cellEditor")
- this TableColumn's width ("width")
- this TableColumn's preferred width ("preferredWidth")
- this TableColumn's minimum width ("minWidth")
- this TableColumn's maximum width ("maxWidth")
- this TableColumn's resizable state ("isResizable")

this TableColumn's modelIndex ("modelIndex")

this TableColumn's identifier ("identifier")

this TableColumn's header value ("headerValue")

this TableColumn's header renderer ("headerRenderer")

this TableColumn's cell renderer ("cellRenderer")

this TableColumn's cell editor ("cellEditor")

this TableColumn's width ("width")

this TableColumn's preferred width ("preferredWidth")

this TableColumn's minimum width ("minWidth")

this TableColumn's maximum width ("maxWidth")

this TableColumn's resizable state ("isResizable")

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
The

PropertyChangeListener

to be removed was registered
for all properties.

**Parameters:** listener

- the listener to be removed

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.
The

PropertyChangeListener

to be removed was registered
for all properties.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners()

Returns an array of all the

PropertyChangeListener

s added
to this TableColumn with addPropertyChangeListener().

createDefaultHeaderRenderer

```java
protected
TableCellRenderer
createDefaultHeaderRenderer()
```

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor. Previously this method was used by the

TableColumn

to create a default header renderer.
As of Java 2 platform v1.3, the default header renderer is

null

.

JTableHeader

now provides its own shared default
renderer, just as the

JTable

does for its cell renderers.

**Returns:** the default header renderer
**See Also:** JTableHeader.createDefaultRenderer()

---

#### createDefaultHeaderRenderer

protected

TableCellRenderer

createDefaultHeaderRenderer()

As of Java 2 platform v1.3, this method is not called by the

TableColumn

constructor. Previously this method was used by the

TableColumn

to create a default header renderer.
As of Java 2 platform v1.3, the default header renderer is

null

.

JTableHeader

now provides its own shared default
renderer, just as the

JTable

does for its cell renderers.

---

