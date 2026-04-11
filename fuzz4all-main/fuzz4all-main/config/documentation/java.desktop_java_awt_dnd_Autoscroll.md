# Interface Autoscroll

**Source:** `java.desktop\java\awt\dnd\Autoscroll.html`

### Class Description

```java
public interface
Autoscroll
```

During DnD operations it is possible that a user may wish to drop the
subject of the operation on a region of a scrollable GUI control that is
not currently visible to the user.

In such situations it is desirable that the GUI control detect this
and institute a scroll operation in order to make obscured region(s)
visible to the user. This feature is known as autoscrolling.

If a GUI control is both an active

DropTarget

and is also scrollable, it
can receive notifications of autoscrolling gestures by the user from
the DnD system by implementing this interface.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Insets
getAutoscrollInsets()

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

**Returns:**
- the Insets

---

#### void autoscroll​(
Point
cursorLocn)

notify the

Component

to autoscroll

**Parameters:**
- cursorLocn

- A

Point

indicating the
location of the cursor that triggered this operation.

---

### Additional Sections

#### Interface Autoscroll

```java
public interface
Autoscroll
```

During DnD operations it is possible that a user may wish to drop the
subject of the operation on a region of a scrollable GUI control that is
not currently visible to the user.

In such situations it is desirable that the GUI control detect this
and institute a scroll operation in order to make obscured region(s)
visible to the user. This feature is known as autoscrolling.

If a GUI control is both an active

DropTarget

and is also scrollable, it
can receive notifications of autoscrolling gestures by the user from
the DnD system by implementing this interface.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

**Since:** 1.2

public interface

Autoscroll

During DnD operations it is possible that a user may wish to drop the
subject of the operation on a region of a scrollable GUI control that is
not currently visible to the user.

In such situations it is desirable that the GUI control detect this
and institute a scroll operation in order to make obscured region(s)
visible to the user. This feature is known as autoscrolling.

If a GUI control is both an active

DropTarget

and is also scrollable, it
can receive notifications of autoscrolling gestures by the user from
the DnD system by implementing this interface.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

In such situations it is desirable that the GUI control detect this
and institute a scroll operation in order to make obscured region(s)
visible to the user. This feature is known as autoscrolling.

If a GUI control is both an active

DropTarget

and is also scrollable, it
can receive notifications of autoscrolling gestures by the user from
the DnD system by implementing this interface.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

If a GUI control is both an active

DropTarget

and is also scrollable, it
can receive notifications of autoscrolling gestures by the user from
the DnD system by implementing this interface.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

An autoscrolling gesture is initiated by the user by keeping the drag
cursor motionless with a border region of the

Component

,
referred to as
the "autoscrolling region", for a predefined period of time, this will
result in repeated scroll requests to the

Component

until the drag

Cursor

resumes its motion.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

autoscroll

​(

Point

cursorLocn)

notify the

Component

to autoscroll

Insets

getAutoscrollInsets

()

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

autoscroll

​(

Point

cursorLocn)

notify the

Component

to autoscroll

Insets

getAutoscrollInsets

()

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

---

#### Method Summary

notify the

Component

to autoscroll

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

============ METHOD DETAIL ==========

- Method Detail

- getAutoscrollInsets

```java
Insets
getAutoscrollInsets()
```

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

**Returns:** the Insets

- autoscroll

```java
void autoscroll​(
Point
cursorLocn)
```

notify the

Component

to autoscroll

**Parameters:** cursorLocn

- A

Point

indicating the
location of the cursor that triggered this operation.

Method Detail

- getAutoscrollInsets

```java
Insets
getAutoscrollInsets()
```

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

**Returns:** the Insets

- autoscroll

```java
void autoscroll​(
Point
cursorLocn)
```

notify the

Component

to autoscroll

**Parameters:** cursorLocn

- A

Point

indicating the
location of the cursor that triggered this operation.

---

#### Method Detail

getAutoscrollInsets

```java
Insets
getAutoscrollInsets()
```

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

**Returns:** the Insets

---

#### getAutoscrollInsets

Insets

getAutoscrollInsets()

This method returns the

Insets

describing
the autoscrolling region or border relative
to the geometry of the implementing Component.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

This value is read once by the

DropTarget

upon entry of the drag

Cursor

into the associated

Component

.

autoscroll

```java
void autoscroll​(
Point
cursorLocn)
```

notify the

Component

to autoscroll

**Parameters:** cursorLocn

- A

Point

indicating the
location of the cursor that triggered this operation.

---

#### autoscroll

void autoscroll​(

Point

cursorLocn)

notify the

Component

to autoscroll

---

