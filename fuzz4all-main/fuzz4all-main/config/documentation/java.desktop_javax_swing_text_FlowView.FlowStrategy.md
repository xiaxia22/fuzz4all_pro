# Class FlowView.FlowStrategy

**Source:** `java.desktop\javax\swing\text\FlowView.FlowStrategy.html`

### Class Description

```java
public static class
FlowView.FlowStrategy

extends
Object
```

Strategy for maintaining the physical form
of the flow. The default implementation is
completely stateless, and recalculates the
entire flow if the layout is invalid on the
given FlowView. Alternative strategies can
be implemented by subclassing, and might
perform incremental repair to the layout
or alternative breaking behavior.

**Enclosing class:** FlowView

---

### Field Details

*No entries found.*

### Constructor Details

#### public FlowStrategy()

*No description found.*

---

### Method Details

#### public void insertUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for. The
strategy should update the appropriate changed region (which
depends upon the strategy used for repair).

**Parameters:**
- fv

- the flow view
- e

- the change information from the associated document
- alloc

- the current allocation of the view inside of the insets.
This value will be null if the view has not yet been displayed.

**See Also:**
- View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### public void removeUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

**Parameters:**
- fv

- the flow view
- e

- the change information from the associated document
- alloc

- the current allocation of the view inside of the insets.

**See Also:**
- View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### public void changedUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Parameters:**
- fv

- the

FlowView

containing the changes
- e

- the

DocumentEvent

describing the changes
done to the Document
- alloc

- Bounds of the View

**See Also:**
- View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### protected
View
getLogicalView​(
FlowView
fv)

This method gives flow strategies access to the logical
view of the FlowView.

**Parameters:**
- fv

- the FlowView

**Returns:**
- the logical view of the FlowView

---

#### public void layout​(
FlowView
fv)

Update the flow on the given FlowView. By default, this causes
all of the rows (child views) to be rebuilt to match the given
constraints for each row. This is called by a FlowView.layout
to update the child views in the flow.

**Parameters:**
- fv

- the view to reflow

---

#### protected int layoutRow​(
FlowView
fv,
int rowIndex,
int pos)

Creates a row of views that will fit within the
layout span of the row. This is called by the layout method.
This is implemented to fill the row by repeatedly calling
the createView method until the available span has been
exhausted, a forced break was encountered, or the createView
method returned null. If the remaining span was exhausted,
the adjustRow method will be called to perform adjustments
to the row to try and make it fit into the given span.

**Parameters:**
- fv

- the flow view
- rowIndex

- the index of the row to fill in with views. The
row is assumed to be empty on entry.
- pos

- The current position in the children of
this views element from which to start.

**Returns:**
- the position to start the next row

---

#### protected void adjustRow​(
FlowView
fv,
int rowIndex,
int desiredSpan,
int x)

Adjusts the given row if possible to fit within the
layout span. By default this will try to find the
highest break weight possible nearest the end of
the row. If a forced break is encountered, the
break will be positioned there.

**Parameters:**
- fv

- the flow view
- rowIndex

- the row to adjust to the current layout
span.
- desiredSpan

- the current layout span >= 0
- x

- the location r starts at.

---

#### protected
View
createView​(
FlowView
fv,
int startOffset,
int spanLeft,
int rowIndex)

Creates a view that can be used to represent the current piece
of the flow. This can be either an entire view from the
logical view, or a fragment of the logical view.

**Parameters:**
- fv

- the view holding the flow
- startOffset

- the start location for the view being created
- spanLeft

- the about of span left to fill in the row
- rowIndex

- the row the view will be placed into

**Returns:**
- a view that can be used to represent the current piece
of the flow

---

### Additional Sections

#### Class FlowView.FlowStrategy

java.lang.Object

- javax.swing.text.FlowView.FlowStrategy

javax.swing.text.FlowView.FlowStrategy

**Enclosing class:** FlowView

```java
public static class
FlowView.FlowStrategy

extends
Object
```

Strategy for maintaining the physical form
of the flow. The default implementation is
completely stateless, and recalculates the
entire flow if the layout is invalid on the
given FlowView. Alternative strategies can
be implemented by subclassing, and might
perform incremental repair to the layout
or alternative breaking behavior.

**Since:** 1.3

public static class

FlowView.FlowStrategy

extends

Object

Strategy for maintaining the physical form
of the flow. The default implementation is
completely stateless, and recalculates the
entire flow if the layout is invalid on the
given FlowView. Alternative strategies can
be implemented by subclassing, and might
perform incremental repair to the layout
or alternative breaking behavior.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FlowStrategy

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

adjustRow

​(

FlowView

fv,
int rowIndex,
int desiredSpan,
int x)

Adjusts the given row if possible to fit within the
layout span.

void

changedUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected

View

createView

​(

FlowView

fv,
int startOffset,
int spanLeft,
int rowIndex)

Creates a view that can be used to represent the current piece
of the flow.

protected

View

getLogicalView

​(

FlowView

fv)

This method gives flow strategies access to the logical
view of the FlowView.

void

insertUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for.

void

layout

​(

FlowView

fv)

Update the flow on the given FlowView.

protected int

layoutRow

​(

FlowView

fv,
int rowIndex,
int pos)

Creates a row of views that will fit within the
layout span of the row.

void

removeUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

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

Constructor Summary

Constructors

Constructor

Description

FlowStrategy

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

protected void

adjustRow

​(

FlowView

fv,
int rowIndex,
int desiredSpan,
int x)

Adjusts the given row if possible to fit within the
layout span.

void

changedUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

protected

View

createView

​(

FlowView

fv,
int startOffset,
int spanLeft,
int rowIndex)

Creates a view that can be used to represent the current piece
of the flow.

protected

View

getLogicalView

​(

FlowView

fv)

This method gives flow strategies access to the logical
view of the FlowView.

void

insertUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for.

void

layout

​(

FlowView

fv)

Update the flow on the given FlowView.

protected int

layoutRow

​(

FlowView

fv,
int rowIndex,
int pos)

Creates a row of views that will fit within the
layout span of the row.

void

removeUpdate

​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

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

Adjusts the given row if possible to fit within the
layout span.

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Creates a view that can be used to represent the current piece
of the flow.

This method gives flow strategies access to the logical
view of the FlowView.

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for.

Update the flow on the given FlowView.

Creates a row of views that will fit within the
layout span of the row.

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

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

- FlowStrategy

```java
public FlowStrategy()
```

============ METHOD DETAIL ==========

- Method Detail

- insertUpdate

```java
public void insertUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for. The
strategy should update the appropriate changed region (which
depends upon the strategy used for repair).

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
This value will be null if the view has not yet been displayed.
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- removeUpdate

```java
public void removeUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- changedUpdate

```java
public void changedUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Parameters:** fv

- the

FlowView

containing the changes
**Parameters:** e

- the

DocumentEvent

describing the changes
done to the Document
**Parameters:** alloc

- Bounds of the View
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- getLogicalView

```java
protected
View
getLogicalView​(
FlowView
fv)
```

This method gives flow strategies access to the logical
view of the FlowView.

**Parameters:** fv

- the FlowView
**Returns:** the logical view of the FlowView

- layout

```java
public void layout​(
FlowView
fv)
```

Update the flow on the given FlowView. By default, this causes
all of the rows (child views) to be rebuilt to match the given
constraints for each row. This is called by a FlowView.layout
to update the child views in the flow.

**Parameters:** fv

- the view to reflow

- layoutRow

```java
protected int layoutRow​(
FlowView
fv,
int rowIndex,
int pos)
```

Creates a row of views that will fit within the
layout span of the row. This is called by the layout method.
This is implemented to fill the row by repeatedly calling
the createView method until the available span has been
exhausted, a forced break was encountered, or the createView
method returned null. If the remaining span was exhausted,
the adjustRow method will be called to perform adjustments
to the row to try and make it fit into the given span.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the index of the row to fill in with views. The
row is assumed to be empty on entry.
**Parameters:** pos

- The current position in the children of
this views element from which to start.
**Returns:** the position to start the next row

- adjustRow

```java
protected void adjustRow​(
FlowView
fv,
int rowIndex,
int desiredSpan,
int x)
```

Adjusts the given row if possible to fit within the
layout span. By default this will try to find the
highest break weight possible nearest the end of
the row. If a forced break is encountered, the
break will be positioned there.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the row to adjust to the current layout
span.
**Parameters:** desiredSpan

- the current layout span >= 0
**Parameters:** x

- the location r starts at.

- createView

```java
protected
View
createView​(
FlowView
fv,
int startOffset,
int spanLeft,
int rowIndex)
```

Creates a view that can be used to represent the current piece
of the flow. This can be either an entire view from the
logical view, or a fragment of the logical view.

**Parameters:** fv

- the view holding the flow
**Parameters:** startOffset

- the start location for the view being created
**Parameters:** spanLeft

- the about of span left to fill in the row
**Parameters:** rowIndex

- the row the view will be placed into
**Returns:** a view that can be used to represent the current piece
of the flow

Constructor Detail

- FlowStrategy

```java
public FlowStrategy()
```

---

#### Constructor Detail

FlowStrategy

```java
public FlowStrategy()
```

---

#### FlowStrategy

public FlowStrategy()

Method Detail

- insertUpdate

```java
public void insertUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for. The
strategy should update the appropriate changed region (which
depends upon the strategy used for repair).

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
This value will be null if the view has not yet been displayed.
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- removeUpdate

```java
public void removeUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- changedUpdate

```java
public void changedUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Parameters:** fv

- the

FlowView

containing the changes
**Parameters:** e

- the

DocumentEvent

describing the changes
done to the Document
**Parameters:** alloc

- Bounds of the View
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- getLogicalView

```java
protected
View
getLogicalView​(
FlowView
fv)
```

This method gives flow strategies access to the logical
view of the FlowView.

**Parameters:** fv

- the FlowView
**Returns:** the logical view of the FlowView

- layout

```java
public void layout​(
FlowView
fv)
```

Update the flow on the given FlowView. By default, this causes
all of the rows (child views) to be rebuilt to match the given
constraints for each row. This is called by a FlowView.layout
to update the child views in the flow.

**Parameters:** fv

- the view to reflow

- layoutRow

```java
protected int layoutRow​(
FlowView
fv,
int rowIndex,
int pos)
```

Creates a row of views that will fit within the
layout span of the row. This is called by the layout method.
This is implemented to fill the row by repeatedly calling
the createView method until the available span has been
exhausted, a forced break was encountered, or the createView
method returned null. If the remaining span was exhausted,
the adjustRow method will be called to perform adjustments
to the row to try and make it fit into the given span.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the index of the row to fill in with views. The
row is assumed to be empty on entry.
**Parameters:** pos

- The current position in the children of
this views element from which to start.
**Returns:** the position to start the next row

- adjustRow

```java
protected void adjustRow​(
FlowView
fv,
int rowIndex,
int desiredSpan,
int x)
```

Adjusts the given row if possible to fit within the
layout span. By default this will try to find the
highest break weight possible nearest the end of
the row. If a forced break is encountered, the
break will be positioned there.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the row to adjust to the current layout
span.
**Parameters:** desiredSpan

- the current layout span >= 0
**Parameters:** x

- the location r starts at.

- createView

```java
protected
View
createView​(
FlowView
fv,
int startOffset,
int spanLeft,
int rowIndex)
```

Creates a view that can be used to represent the current piece
of the flow. This can be either an entire view from the
logical view, or a fragment of the logical view.

**Parameters:** fv

- the view holding the flow
**Parameters:** startOffset

- the start location for the view being created
**Parameters:** spanLeft

- the about of span left to fill in the row
**Parameters:** rowIndex

- the row the view will be placed into
**Returns:** a view that can be used to represent the current piece
of the flow

---

#### Method Detail

insertUpdate

```java
public void insertUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for. The
strategy should update the appropriate changed region (which
depends upon the strategy used for repair).

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
This value will be null if the view has not yet been displayed.
**See Also:** View.insertUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### insertUpdate

public void insertUpdate​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was inserted into the document
in a location that the given flow view is responsible for. The
strategy should update the appropriate changed region (which
depends upon the strategy used for repair).

removeUpdate

```java
public void removeUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

**Parameters:** fv

- the flow view
**Parameters:** e

- the change information from the associated document
**Parameters:** alloc

- the current allocation of the view inside of the insets.
**See Also:** View.removeUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### removeUpdate

public void removeUpdate​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification that something was removed from the document
in a location that the given flow view is responsible for.

changedUpdate

```java
public void changedUpdate​(
FlowView
fv,

DocumentEvent
e,

Rectangle
alloc)
```

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Parameters:** fv

- the

FlowView

containing the changes
**Parameters:** e

- the

DocumentEvent

describing the changes
done to the Document
**Parameters:** alloc

- Bounds of the View
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### changedUpdate

public void changedUpdate​(

FlowView

fv,

DocumentEvent

e,

Rectangle

alloc)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

getLogicalView

```java
protected
View
getLogicalView​(
FlowView
fv)
```

This method gives flow strategies access to the logical
view of the FlowView.

**Parameters:** fv

- the FlowView
**Returns:** the logical view of the FlowView

---

#### getLogicalView

protected

View

getLogicalView​(

FlowView

fv)

This method gives flow strategies access to the logical
view of the FlowView.

layout

```java
public void layout​(
FlowView
fv)
```

Update the flow on the given FlowView. By default, this causes
all of the rows (child views) to be rebuilt to match the given
constraints for each row. This is called by a FlowView.layout
to update the child views in the flow.

**Parameters:** fv

- the view to reflow

---

#### layout

public void layout​(

FlowView

fv)

Update the flow on the given FlowView. By default, this causes
all of the rows (child views) to be rebuilt to match the given
constraints for each row. This is called by a FlowView.layout
to update the child views in the flow.

layoutRow

```java
protected int layoutRow​(
FlowView
fv,
int rowIndex,
int pos)
```

Creates a row of views that will fit within the
layout span of the row. This is called by the layout method.
This is implemented to fill the row by repeatedly calling
the createView method until the available span has been
exhausted, a forced break was encountered, or the createView
method returned null. If the remaining span was exhausted,
the adjustRow method will be called to perform adjustments
to the row to try and make it fit into the given span.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the index of the row to fill in with views. The
row is assumed to be empty on entry.
**Parameters:** pos

- The current position in the children of
this views element from which to start.
**Returns:** the position to start the next row

---

#### layoutRow

protected int layoutRow​(

FlowView

fv,
int rowIndex,
int pos)

Creates a row of views that will fit within the
layout span of the row. This is called by the layout method.
This is implemented to fill the row by repeatedly calling
the createView method until the available span has been
exhausted, a forced break was encountered, or the createView
method returned null. If the remaining span was exhausted,
the adjustRow method will be called to perform adjustments
to the row to try and make it fit into the given span.

adjustRow

```java
protected void adjustRow​(
FlowView
fv,
int rowIndex,
int desiredSpan,
int x)
```

Adjusts the given row if possible to fit within the
layout span. By default this will try to find the
highest break weight possible nearest the end of
the row. If a forced break is encountered, the
break will be positioned there.

**Parameters:** fv

- the flow view
**Parameters:** rowIndex

- the row to adjust to the current layout
span.
**Parameters:** desiredSpan

- the current layout span >= 0
**Parameters:** x

- the location r starts at.

---

#### adjustRow

protected void adjustRow​(

FlowView

fv,
int rowIndex,
int desiredSpan,
int x)

Adjusts the given row if possible to fit within the
layout span. By default this will try to find the
highest break weight possible nearest the end of
the row. If a forced break is encountered, the
break will be positioned there.

createView

```java
protected
View
createView​(
FlowView
fv,
int startOffset,
int spanLeft,
int rowIndex)
```

Creates a view that can be used to represent the current piece
of the flow. This can be either an entire view from the
logical view, or a fragment of the logical view.

**Parameters:** fv

- the view holding the flow
**Parameters:** startOffset

- the start location for the view being created
**Parameters:** spanLeft

- the about of span left to fill in the row
**Parameters:** rowIndex

- the row the view will be placed into
**Returns:** a view that can be used to represent the current piece
of the flow

---

#### createView

protected

View

createView​(

FlowView

fv,
int startOffset,
int spanLeft,
int rowIndex)

Creates a view that can be used to represent the current piece
of the flow. This can be either an entire view from the
logical view, or a fragment of the logical view.

---

