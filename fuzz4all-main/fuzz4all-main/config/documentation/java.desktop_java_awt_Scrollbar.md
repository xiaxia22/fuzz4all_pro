# Class Scrollbar

**Source:** `java.desktop\java\awt\Scrollbar.html`

### Class Description

```java
public class
Scrollbar

extends
Component

implements
Adjustable
,
Accessible
```

The

Scrollbar

class embodies a scroll bar, a
familiar user-interface object. A scroll bar provides a
convenient means for allowing a user to select from a
range of values. The following three vertical
scroll bars could be used as slider controls to pick
the red, green, and blue components of a color:

Each scroll bar in this example could be created with
code similar to the following:

```java
redSlider=new Scrollbar(Scrollbar.VERTICAL, 0, 1, 0, 255);
add(redSlider);
```

Alternatively, a scroll bar can represent a range of values. For
example, if a scroll bar is used for scrolling through text, the
width of the "bubble" (also called the "thumb" or "scroll box")
can be used to represent the amount of text that is visible.
Here is an example of a scroll bar that represents a range:

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

**All Implemented Interfaces:** Adjustable

,

ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final int HORIZONTAL

A constant that indicates a horizontal scroll bar.

**See Also:**
- Constant Field Values

---

#### public static final int VERTICAL

A constant that indicates a vertical scroll bar.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public Scrollbar()
throws
HeadlessException

Constructs a new vertical scroll bar.
The default properties of the scroll bar are listed in
the following table:

Scrollbar default properties

Property

Description

Default Value

orientation

indicates whether the scroll bar is vertical or horizontal

Scrollbar.VERTICAL

value

value which controls the location of the scroll bar's bubble

0

visible amount

visible amount of the scroll bar's range, typically represented
by the size of the scroll bar's bubble

10

minimum

minimum value of the scroll bar

0

maximum

maximum value of the scroll bar

100

unit increment

amount the value changes when the Line Up or Line Down key is
pressed, or when the end arrows of the scrollbar are clicked

1

block increment

amount the value changes when the Page Up or Page Down key is
pressed, or when the scrollbar track is clicked

on either side of
the bubble

10

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public Scrollbar​(int orientation)
throws
HeadlessException

Constructs a new scroll bar with the specified orientation.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

**Parameters:**
- orientation

- indicates the orientation of the scroll bar

**Throws:**
- IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public Scrollbar​(int orientation,
int value,
int visible,
int minimum,
int maximum)
throws
HeadlessException

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

**Parameters:**
- orientation

- indicates the orientation of the scroll bar.
- value

- the initial value of the scroll bar
- visible

- the visible amount of the scroll bar, typically
represented by the size of the bubble
- minimum

- the minimum value of the scroll bar
- maximum

- the maximum value of the scroll bar

**Throws:**
- IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- setValues(int, int, int, int)

,

GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void addNotify()

Creates the

Scrollbar

's peer. The peer allows you to modify
the appearance of the

Scrollbar

without changing any of its
functionality.

**Overrides:**
- addNotify

in class

Component

**See Also:**
- Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

---

#### public int getOrientation()

Returns the orientation of this scroll bar.

**Specified by:**
- getOrientation

in interface

Adjustable

**Returns:**
- the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL

**See Also:**
- setOrientation(int)

---

#### public void setOrientation​(int orientation)

Sets the orientation for this scroll bar.

**Parameters:**
- orientation

- the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL

**Throws:**
- IllegalArgumentException

- if the value supplied
for

orientation

is not a
legal value

**See Also:**
- getOrientation()

**Since:**
- 1.1

---

#### public int getValue()

Gets the current value of this scroll bar.

**Specified by:**
- getValue

in interface

Adjustable

**Returns:**
- the current value of this scroll bar

**See Also:**
- getMinimum()

,

getMaximum()

---

#### public void setValue​(int newValue)

Sets the value of this scroll bar to the specified value.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

**Specified by:**
- setValue

in interface

Adjustable

**Parameters:**
- newValue

- the new value of the scroll bar

**See Also:**
- setValues(int, int, int, int)

,

getValue()

,

getMinimum()

,

getMaximum()

---

#### public int getMinimum()

Gets the minimum value of this scroll bar.

**Specified by:**
- getMinimum

in interface

Adjustable

**Returns:**
- the minimum value of this scroll bar

**See Also:**
- getValue()

,

getMaximum()

---

#### public void setMinimum​(int newMinimum)

Sets the minimum value of this scroll bar.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

**Specified by:**
- setMinimum

in interface

Adjustable

**Parameters:**
- newMinimum

- the new minimum value for this scroll bar

**See Also:**
- setValues(int, int, int, int)

,

setMaximum(int)

**Since:**
- 1.1

---

#### public int getMaximum()

Gets the maximum value of this scroll bar.

**Specified by:**
- getMaximum

in interface

Adjustable

**Returns:**
- the maximum value of this scroll bar

**See Also:**
- getValue()

,

getMinimum()

---

#### public void setMaximum​(int newMaximum)

Sets the maximum value of this scroll bar.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

**Specified by:**
- setMaximum

in interface

Adjustable

**Parameters:**
- newMaximum

- the new maximum value
for this scroll bar

**See Also:**
- setValues(int, int, int, int)

,

setMinimum(int)

**Since:**
- 1.1

---

#### public int getVisibleAmount()

Gets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

**Specified by:**
- getVisibleAmount

in interface

Adjustable

**Returns:**
- the visible amount of this scroll bar

**See Also:**
- setVisibleAmount(int)

**Since:**
- 1.1

---

#### @Deprecated

public int getVisible()

Returns the visible amount of this scroll bar.

**Returns:**
- the visible amount of this scroll bar

---

#### public void setVisibleAmount​(int newAmount)

Sets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

**Specified by:**
- setVisibleAmount

in interface

Adjustable

**Parameters:**
- newAmount

- the new visible amount

**See Also:**
- getVisibleAmount()

,

setValues(int, int, int, int)

**Since:**
- 1.1

---

#### public void setUnitIncrement​(int v)

Sets the unit increment for this scroll bar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:**
- setUnitIncrement

in interface

Adjustable

**Parameters:**
- v

- the amount by which to increment or decrement
the scroll bar's value

**See Also:**
- getUnitIncrement()

**Since:**
- 1.1

---

#### @Deprecated

public void setLineIncrement​(int v)

Sets the unit increment for this scroll bar.

**Parameters:**
- v

- the increment value

---

#### public int getUnitIncrement()

Gets the unit increment for this scrollbar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:**
- getUnitIncrement

in interface

Adjustable

**Returns:**
- the unit increment of this scroll bar

**See Also:**
- setUnitIncrement(int)

**Since:**
- 1.1

---

#### @Deprecated

public int getLineIncrement()

Returns the unit increment for this scrollbar.

**Returns:**
- the unit increment for this scrollbar

---

#### public void setBlockIncrement​(int v)

Sets the block increment for this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

**Specified by:**
- setBlockIncrement

in interface

Adjustable

**Parameters:**
- v

- the amount by which to increment or decrement
the scroll bar's value

**See Also:**
- getBlockIncrement()

**Since:**
- 1.1

---

#### @Deprecated

public void setPageIncrement​(int v)

Sets the block increment for this scroll bar.

**Parameters:**
- v

- the block increment

---

#### public int getBlockIncrement()

Gets the block increment of this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

**Specified by:**
- getBlockIncrement

in interface

Adjustable

**Returns:**
- the block increment of this scroll bar

**See Also:**
- setBlockIncrement(int)

**Since:**
- 1.1

---

#### @Deprecated

public int getPageIncrement()

Returns the block increment of this scroll bar.

**Returns:**
- the block increment of this scroll bar

---

#### public void setValues​(int value,
int visible,
int minimum,
int maximum)

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.
If the values supplied for these properties are inconsistent
or incorrect, they will be changed to ensure consistency.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:**
- value

- is the position in the current window
- visible

- is the visible amount of the scroll bar
- minimum

- is the minimum value of the scroll bar
- maximum

- is the maximum value of the scroll bar

**See Also:**
- setMinimum(int)

,

setMaximum(int)

,

setVisibleAmount(int)

,

setValue(int)

---

#### public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:**
- the value of the

valueIsAdjusting

property

**See Also:**
- setValueIsAdjusting(boolean)

**Since:**
- 1.4

---

#### public void setValueIsAdjusting​(boolean b)

Sets the

valueIsAdjusting

property.

**Parameters:**
- b

- new adjustment-in-progress status

**See Also:**
- getValueIsAdjusting()

**Since:**
- 1.4

---

#### public void addAdjustmentListener​(
AdjustmentListener
l)

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- addAdjustmentListener

in interface

Adjustable

**Parameters:**
- l

- the adjustment listener

**See Also:**
- removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

**Since:**
- 1.1

---

#### public void removeAdjustmentListener​(
AdjustmentListener
l)

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- removeAdjustmentListener

in interface

Adjustable

**Parameters:**
- l

- the adjustment listener

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

**Since:**
- 1.1

---

#### public
AdjustmentListener
[] getAdjustmentListeners()

Returns an array of all the adjustment listeners
registered on this scrollbar.

**Returns:**
- all of this scrollbar's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered

**See Also:**
- addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentEvent

,

AdjustmentListener

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:**
- getListeners

in class

Component

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- Component.getComponentListeners()

,

Component.getFocusListeners()

,

Component.getHierarchyListeners()

,

Component.getHierarchyBoundsListeners()

,

Component.getKeyListeners()

,

Component.getMouseListeners()

,

Component.getMouseMotionListeners()

,

Component.getMouseWheelListeners()

,

Component.getInputMethodListeners()

,

Component.getPropertyChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### protected void processEvent​(
AWTEvent
e)

Processes events on this scroll bar. If the event is an
instance of

AdjustmentEvent

, it invokes the

processAdjustmentEvent

method.
Otherwise, it invokes its superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processEvent

in class

Component

**Parameters:**
- e

- the event

**See Also:**
- AdjustmentEvent

,

processAdjustmentEvent(java.awt.event.AdjustmentEvent)

**Since:**
- 1.1

---

#### protected void processAdjustmentEvent​(
AdjustmentEvent
e)

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the adjustment event

**See Also:**
- AdjustmentEvent

,

AdjustmentListener

,

addAdjustmentListener(java.awt.event.AdjustmentListener)

,

Component.enableEvents(long)

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns a string representing the state of this

Scrollbar

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Component

**Returns:**
- the parameter string of this scroll bar

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

Scrollbar

. For scrollbars, the

AccessibleContext

takes the form of an

AccessibleAWTScrollBar

. A new

AccessibleAWTScrollBar

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an

AccessibleAWTScrollBar

that serves as the

AccessibleContext

of this

ScrollBar

**Since:**
- 1.3

---

### Additional Sections

#### Class Scrollbar

java.lang.Object

- java.awt.Component
- - java.awt.Scrollbar

java.awt.Component

- java.awt.Scrollbar

java.awt.Scrollbar

**All Implemented Interfaces:** Adjustable

,

ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
Scrollbar

extends
Component

implements
Adjustable
,
Accessible
```

The

Scrollbar

class embodies a scroll bar, a
familiar user-interface object. A scroll bar provides a
convenient means for allowing a user to select from a
range of values. The following three vertical
scroll bars could be used as slider controls to pick
the red, green, and blue components of a color:

Each scroll bar in this example could be created with
code similar to the following:

```java
redSlider=new Scrollbar(Scrollbar.VERTICAL, 0, 1, 0, 255);
add(redSlider);
```

Alternatively, a scroll bar can represent a range of values. For
example, if a scroll bar is used for scrolling through text, the
width of the "bubble" (also called the "thumb" or "scroll box")
can be used to represent the amount of text that is visible.
Here is an example of a scroll bar that represents a range:

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

**Since:** 1.0
**See Also:** AdjustmentEvent

,

AdjustmentListener

,

Serialized Form

public class

Scrollbar

extends

Component

implements

Adjustable

,

Accessible

The

Scrollbar

class embodies a scroll bar, a
familiar user-interface object. A scroll bar provides a
convenient means for allowing a user to select from a
range of values. The following three vertical
scroll bars could be used as slider controls to pick
the red, green, and blue components of a color:

Each scroll bar in this example could be created with
code similar to the following:

```java
redSlider=new Scrollbar(Scrollbar.VERTICAL, 0, 1, 0, 255);
add(redSlider);
```

Alternatively, a scroll bar can represent a range of values. For
example, if a scroll bar is used for scrolling through text, the
width of the "bubble" (also called the "thumb" or "scroll box")
can be used to represent the amount of text that is visible.
Here is an example of a scroll bar that represents a range:

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

Each scroll bar in this example could be created with
code similar to the following:

```java
redSlider=new Scrollbar(Scrollbar.VERTICAL, 0, 1, 0, 255);
add(redSlider);
```

Alternatively, a scroll bar can represent a range of values. For
example, if a scroll bar is used for scrolling through text, the
width of the "bubble" (also called the "thumb" or "scroll box")
can be used to represent the amount of text that is visible.
Here is an example of a scroll bar that represents a range:

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

redSlider=new Scrollbar(Scrollbar.VERTICAL, 0, 1, 0, 255);
add(redSlider);

Alternatively, a scroll bar can represent a range of values. For
example, if a scroll bar is used for scrolling through text, the
width of the "bubble" (also called the "thumb" or "scroll box")
can be used to represent the amount of text that is visible.
Here is an example of a scroll bar that represents a range:

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

The value range represented by the bubble in this example
is the

visible amount

. The horizontal scroll bar
in this example could be created with code like the following:

```java
ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);
```

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

ranger = new Scrollbar(Scrollbar.HORIZONTAL, 0, 60, 0, 300);
add(ranger);

Note that the actual maximum value of the scroll bar is the

maximum

minus the

visible amount

.
In the previous example, because the

maximum

is
300 and the

visible amount

is 60, the actual maximum
value is 240. The range of the scrollbar track is 0 - 300.
The left side of the bubble indicates the value of the
scroll bar.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

Normally, the user changes the value of the scroll bar by
making a gesture with the mouse. For example, the user can
drag the scroll bar's bubble up and down, or click in the
scroll bar's unit increment or block increment areas. Keyboard
gestures can also be mapped to the scroll bar. By convention,
the

Page Up

and

Page Down

keys are equivalent to clicking in the scroll bar's block
increment and block decrement areas.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

When the user changes the value of the scroll bar, the scroll bar
receives an instance of

AdjustmentEvent

.
The scroll bar processes this event, passing it along to
any registered listeners.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

Any object that wishes to be notified of changes to the
scroll bar's value should implement

AdjustmentListener

, an interface defined in
the package

java.awt.event

.
Listeners can be added and removed dynamically by calling
the methods

addAdjustmentListener

and

removeAdjustmentListener

.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

The

AdjustmentEvent

class defines five types
of adjustment event, listed here:

- AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

AdjustmentEvent.TRACK

is sent out when the
user drags the scroll bar's bubble.

AdjustmentEvent.UNIT_INCREMENT

is sent out
when the user clicks in the left arrow of a horizontal scroll
bar, or the top arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.UNIT_DECREMENT

is sent out
when the user clicks in the right arrow of a horizontal scroll
bar, or the bottom arrow of a vertical scroll bar, or makes the
equivalent gesture from the keyboard.

AdjustmentEvent.BLOCK_INCREMENT

is sent out
when the user clicks in the track, to the left of the bubble
on a horizontal scroll bar, or above the bubble on a vertical
scroll bar. By convention, the

Page Up

key is equivalent, if the user is using a keyboard that
defines a

Page Up

key.

AdjustmentEvent.BLOCK_DECREMENT

is sent out
when the user clicks in the track, to the right of the bubble
on a horizontal scroll bar, or below the bubble on a vertical
scroll bar. By convention, the

Page Down

key is equivalent, if the user is using a keyboard that
defines a

Page Down

key.

The JDK 1.0 event system is supported for backwards
compatibility, but its use with newer versions of the platform is
discouraged. The five types of adjustment events introduced
with JDK 1.1 correspond to the five event types
that are associated with scroll bars in previous platform versions.
The following list gives the adjustment event type,
and the corresponding JDK 1.0 event type it replaces.

- AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

AdjustmentEvent.TRACK

replaces

Event.SCROLL_ABSOLUTE

AdjustmentEvent.UNIT_INCREMENT

replaces

Event.SCROLL_LINE_UP

AdjustmentEvent.UNIT_DECREMENT

replaces

Event.SCROLL_LINE_DOWN

AdjustmentEvent.BLOCK_INCREMENT

replaces

Event.SCROLL_PAGE_UP

AdjustmentEvent.BLOCK_DECREMENT

replaces

Event.SCROLL_PAGE_DOWN

Note

: We recommend using a

Scrollbar

for value selection only. If you want to implement
a scrollable component inside a container, we recommend you use
a

ScrollPane

. If you use a

Scrollbar

for this purpose, you are likely to
encounter issues with painting, key handling, sizing and
positioning.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Scrollbar.AccessibleAWTScrollBar

This class implements accessibility support for the

Scrollbar

class.

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

HORIZONTAL

A constant that indicates a horizontal scroll bar.

static int

VERTICAL

A constant that indicates a vertical scroll bar.

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.

Adjustable

NO_ORIENTATION

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Scrollbar

()

Constructs a new vertical scroll bar.

Scrollbar

​(int orientation)

Constructs a new scroll bar with the specified orientation.

Scrollbar

​(int orientation,
int value,
int visible,
int minimum,
int maximum)

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

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

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.

void

addNotify

()

Creates the

Scrollbar

's peer.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

Scrollbar

.

AdjustmentListener

[]

getAdjustmentListeners

()

Returns an array of all the adjustment listeners
registered on this scrollbar.

int

getBlockIncrement

()

Gets the block increment of this scroll bar.

int

getLineIncrement

()

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

int

getMaximum

()

Gets the maximum value of this scroll bar.

int

getMinimum

()

Gets the minimum value of this scroll bar.

int

getOrientation

()

Returns the orientation of this scroll bar.

int

getPageIncrement

()

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

int

getUnitIncrement

()

Gets the unit increment for this scrollbar.

int

getValue

()

Gets the current value of this scroll bar.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

int

getVisible

()

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

int

getVisibleAmount

()

Gets the visible amount of this scroll bar.

protected

String

paramString

()

Returns a string representing the state of this

Scrollbar

.

protected void

processAdjustmentEvent

​(

AdjustmentEvent

e)

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this scroll bar.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.

void

setBlockIncrement

​(int v)

Sets the block increment for this scroll bar.

void

setLineIncrement

​(int v)

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

void

setMaximum

​(int newMaximum)

Sets the maximum value of this scroll bar.

void

setMinimum

​(int newMinimum)

Sets the minimum value of this scroll bar.

void

setOrientation

​(int orientation)

Sets the orientation for this scroll bar.

void

setPageIncrement

​(int v)

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

void

setUnitIncrement

​(int v)

Sets the unit increment for this scroll bar.

void

setValue

​(int newValue)

Sets the value of this scroll bar to the specified value.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

void

setValues

​(int value,
int visible,
int minimum,
int maximum)

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.

void

setVisibleAmount

​(int newAmount)

Sets the visible amount of this scroll bar.

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removeNotify

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

,

update

,

validate

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

protected class

Scrollbar.AccessibleAWTScrollBar

This class implements accessibility support for the

Scrollbar

class.

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

Scrollbar

class.

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

static int

HORIZONTAL

A constant that indicates a horizontal scroll bar.

static int

VERTICAL

A constant that indicates a vertical scroll bar.

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.

Adjustable

NO_ORIENTATION

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

A constant that indicates a horizontal scroll bar.

A constant that indicates a vertical scroll bar.

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.

Adjustable

NO_ORIENTATION

---

#### Fields declared in interface java.awt. Adjustable

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

Scrollbar

()

Constructs a new vertical scroll bar.

Scrollbar

​(int orientation)

Constructs a new scroll bar with the specified orientation.

Scrollbar

​(int orientation,
int value,
int visible,
int minimum,
int maximum)

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

---

#### Constructor Summary

Constructs a new vertical scroll bar.

Constructs a new scroll bar with the specified orientation.

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.

void

addNotify

()

Creates the

Scrollbar

's peer.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

Scrollbar

.

AdjustmentListener

[]

getAdjustmentListeners

()

Returns an array of all the adjustment listeners
registered on this scrollbar.

int

getBlockIncrement

()

Gets the block increment of this scroll bar.

int

getLineIncrement

()

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

int

getMaximum

()

Gets the maximum value of this scroll bar.

int

getMinimum

()

Gets the minimum value of this scroll bar.

int

getOrientation

()

Returns the orientation of this scroll bar.

int

getPageIncrement

()

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

int

getUnitIncrement

()

Gets the unit increment for this scrollbar.

int

getValue

()

Gets the current value of this scroll bar.

boolean

getValueIsAdjusting

()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

int

getVisible

()

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

int

getVisibleAmount

()

Gets the visible amount of this scroll bar.

protected

String

paramString

()

Returns a string representing the state of this

Scrollbar

.

protected void

processAdjustmentEvent

​(

AdjustmentEvent

e)

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this scroll bar.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.

void

setBlockIncrement

​(int v)

Sets the block increment for this scroll bar.

void

setLineIncrement

​(int v)

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

void

setMaximum

​(int newMaximum)

Sets the maximum value of this scroll bar.

void

setMinimum

​(int newMinimum)

Sets the minimum value of this scroll bar.

void

setOrientation

​(int orientation)

Sets the orientation for this scroll bar.

void

setPageIncrement

​(int v)

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

void

setUnitIncrement

​(int v)

Sets the unit increment for this scroll bar.

void

setValue

​(int newValue)

Sets the value of this scroll bar to the specified value.

void

setValueIsAdjusting

​(boolean b)

Sets the

valueIsAdjusting

property.

void

setValues

​(int value,
int visible,
int minimum,
int maximum)

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.

void

setVisibleAmount

​(int newAmount)

Sets the visible amount of this scroll bar.

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removeNotify

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

,

update

,

validate

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

wait

,

wait

,

wait

---

#### Method Summary

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.

Creates the

Scrollbar

's peer.

Gets the

AccessibleContext

associated with this

Scrollbar

.

Returns an array of all the adjustment listeners
registered on this scrollbar.

Gets the block increment of this scroll bar.

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Gets the maximum value of this scroll bar.

Gets the minimum value of this scroll bar.

Returns the orientation of this scroll bar.

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

Gets the unit increment for this scrollbar.

Gets the current value of this scroll bar.

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

Gets the visible amount of this scroll bar.

Returns a string representing the state of this

Scrollbar

.

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

Processes events on this scroll bar.

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.

Sets the block increment for this scroll bar.

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

Sets the maximum value of this scroll bar.

Sets the minimum value of this scroll bar.

Sets the orientation for this scroll bar.

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

Sets the unit increment for this scroll bar.

Sets the value of this scroll bar to the specified value.

Sets the

valueIsAdjusting

property.

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.

Sets the visible amount of this scroll bar.

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMaximumSize

,

getMinimumSize

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPreferredSize

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

layout

,

list

,

list

,

list

,

list

,

list

,

locate

,

location

,

lostFocus

,

minimumSize

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paint

,

paintAll

,

postEvent

,

preferredSize

,

prepareImage

,

prepareImage

,

print

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removeNotify

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

,

update

,

validate

---

#### Methods declared in class java.awt. Component

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- HORIZONTAL

```java
public static final int HORIZONTAL
```

A constant that indicates a horizontal scroll bar.

**See Also:** Constant Field Values

- VERTICAL

```java
public static final int VERTICAL
```

A constant that indicates a vertical scroll bar.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Scrollbar

```java
public Scrollbar()
throws
HeadlessException
```

Constructs a new vertical scroll bar.
The default properties of the scroll bar are listed in
the following table:

Scrollbar default properties

Property

Description

Default Value

orientation

indicates whether the scroll bar is vertical or horizontal

Scrollbar.VERTICAL

value

value which controls the location of the scroll bar's bubble

0

visible amount

visible amount of the scroll bar's range, typically represented
by the size of the scroll bar's bubble

10

minimum

minimum value of the scroll bar

0

maximum

maximum value of the scroll bar

100

unit increment

amount the value changes when the Line Up or Line Down key is
pressed, or when the end arrows of the scrollbar are clicked

1

block increment

amount the value changes when the Page Up or Page Down key is
pressed, or when the scrollbar track is clicked

on either side of
the bubble

10

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Scrollbar

```java
public Scrollbar​(int orientation)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

**Parameters:** orientation

- indicates the orientation of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Scrollbar

```java
public Scrollbar​(int orientation,
int value,
int visible,
int minimum,
int maximum)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

**Parameters:** orientation

- indicates the orientation of the scroll bar.
**Parameters:** value

- the initial value of the scroll bar
**Parameters:** visible

- the visible amount of the scroll bar, typically
represented by the size of the bubble
**Parameters:** minimum

- the minimum value of the scroll bar
**Parameters:** maximum

- the maximum value of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** setValues(int, int, int, int)

,

GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

Scrollbar

's peer. The peer allows you to modify
the appearance of the

Scrollbar

without changing any of its
functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scroll bar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the orientation for this scroll bar.

**Parameters:** orientation

- the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**Throws:** IllegalArgumentException

- if the value supplied
for

orientation

is not a
legal value
**Since:** 1.1
**See Also:** getOrientation()

- getValue

```java
public int getValue()
```

Gets the current value of this scroll bar.

**Specified by:** getValue

in interface

Adjustable
**Returns:** the current value of this scroll bar
**See Also:** getMinimum()

,

getMaximum()

- setValue

```java
public void setValue​(int newValue)
```

Sets the value of this scroll bar to the specified value.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** newValue

- the new value of the scroll bar
**See Also:** setValues(int, int, int, int)

,

getValue()

,

getMinimum()

,

getMaximum()

- getMinimum

```java
public int getMinimum()
```

Gets the minimum value of this scroll bar.

**Specified by:** getMinimum

in interface

Adjustable
**Returns:** the minimum value of this scroll bar
**See Also:** getValue()

,

getMaximum()

- setMinimum

```java
public void setMinimum​(int newMinimum)
```

Sets the minimum value of this scroll bar.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** newMinimum

- the new minimum value for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMaximum(int)

- getMaximum

```java
public int getMaximum()
```

Gets the maximum value of this scroll bar.

**Specified by:** getMaximum

in interface

Adjustable
**Returns:** the maximum value of this scroll bar
**See Also:** getValue()

,

getMinimum()

- setMaximum

```java
public void setMaximum​(int newMaximum)
```

Sets the maximum value of this scroll bar.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** newMaximum

- the new maximum value
for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMinimum(int)

- getVisibleAmount

```java
public int getVisibleAmount()
```

Gets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

**Specified by:** getVisibleAmount

in interface

Adjustable
**Returns:** the visible amount of this scroll bar
**Since:** 1.1
**See Also:** setVisibleAmount(int)

- getVisible

```java
@Deprecated

public int getVisible()
```

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

Returns the visible amount of this scroll bar.

**Returns:** the visible amount of this scroll bar

- setVisibleAmount

```java
public void setVisibleAmount​(int newAmount)
```

Sets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** newAmount

- the new visible amount
**Since:** 1.1
**See Also:** getVisibleAmount()

,

setValues(int, int, int, int)

- setUnitIncrement

```java
public void setUnitIncrement​(int v)
```

Sets the unit increment for this scroll bar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** setUnitIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getUnitIncrement()

- setLineIncrement

```java
@Deprecated

public void setLineIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

Sets the unit increment for this scroll bar.

**Parameters:** v

- the increment value

- getUnitIncrement

```java
public int getUnitIncrement()
```

Gets the unit increment for this scrollbar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** getUnitIncrement

in interface

Adjustable
**Returns:** the unit increment of this scroll bar
**Since:** 1.1
**See Also:** setUnitIncrement(int)

- getLineIncrement

```java
@Deprecated

public int getLineIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

Returns the unit increment for this scrollbar.

**Returns:** the unit increment for this scrollbar

- setBlockIncrement

```java
public void setBlockIncrement​(int v)
```

Sets the block increment for this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

**Specified by:** setBlockIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getBlockIncrement()

- setPageIncrement

```java
@Deprecated

public void setPageIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

Sets the block increment for this scroll bar.

**Parameters:** v

- the block increment

- getBlockIncrement

```java
public int getBlockIncrement()
```

Gets the block increment of this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

**Specified by:** getBlockIncrement

in interface

Adjustable
**Returns:** the block increment of this scroll bar
**Since:** 1.1
**See Also:** setBlockIncrement(int)

- getPageIncrement

```java
@Deprecated

public int getPageIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

Returns the block increment of this scroll bar.

**Returns:** the block increment of this scroll bar

- setValues

```java
public void setValues​(int value,
int visible,
int minimum,
int maximum)
```

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.
If the values supplied for these properties are inconsistent
or incorrect, they will be changed to ensure consistency.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** value

- is the position in the current window
**Parameters:** visible

- is the visible amount of the scroll bar
**Parameters:** minimum

- is the minimum value of the scroll bar
**Parameters:** maximum

- is the maximum value of the scroll bar
**See Also:** setMinimum(int)

,

setMaximum(int)

,

setVisibleAmount(int)

,

setValue(int)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**Since:** 1.4
**See Also:** setValueIsAdjusting(boolean)

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

- addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

- removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

- getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this scrollbar.

**Returns:** all of this scrollbar's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentEvent

,

AdjustmentListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** Component.getComponentListeners()

,

Component.getFocusListeners()

,

Component.getHierarchyListeners()

,

Component.getHierarchyBoundsListeners()

,

Component.getKeyListeners()

,

Component.getMouseListeners()

,

Component.getMouseMotionListeners()

,

Component.getMouseWheelListeners()

,

Component.getInputMethodListeners()

,

Component.getPropertyChangeListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scroll bar. If the event is an
instance of

AdjustmentEvent

, it invokes the

processAdjustmentEvent

method.
Otherwise, it invokes its superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

processAdjustmentEvent(java.awt.event.AdjustmentEvent)

- processAdjustmentEvent

```java
protected void processAdjustmentEvent​(
AdjustmentEvent
e)
```

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the adjustment event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

AdjustmentListener

,

addAdjustmentListener(java.awt.event.AdjustmentListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Scrollbar

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scroll bar

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

Scrollbar

. For scrollbars, the

AccessibleContext

takes the form of an

AccessibleAWTScrollBar

. A new

AccessibleAWTScrollBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTScrollBar

that serves as the

AccessibleContext

of this

ScrollBar
**Since:** 1.3

Field Detail

- HORIZONTAL

```java
public static final int HORIZONTAL
```

A constant that indicates a horizontal scroll bar.

**See Also:** Constant Field Values

- VERTICAL

```java
public static final int VERTICAL
```

A constant that indicates a vertical scroll bar.

**See Also:** Constant Field Values

---

#### Field Detail

HORIZONTAL

```java
public static final int HORIZONTAL
```

A constant that indicates a horizontal scroll bar.

**See Also:** Constant Field Values

---

#### HORIZONTAL

public static final int HORIZONTAL

A constant that indicates a horizontal scroll bar.

VERTICAL

```java
public static final int VERTICAL
```

A constant that indicates a vertical scroll bar.

**See Also:** Constant Field Values

---

#### VERTICAL

public static final int VERTICAL

A constant that indicates a vertical scroll bar.

Constructor Detail

- Scrollbar

```java
public Scrollbar()
throws
HeadlessException
```

Constructs a new vertical scroll bar.
The default properties of the scroll bar are listed in
the following table:

Scrollbar default properties

Property

Description

Default Value

orientation

indicates whether the scroll bar is vertical or horizontal

Scrollbar.VERTICAL

value

value which controls the location of the scroll bar's bubble

0

visible amount

visible amount of the scroll bar's range, typically represented
by the size of the scroll bar's bubble

10

minimum

minimum value of the scroll bar

0

maximum

maximum value of the scroll bar

100

unit increment

amount the value changes when the Line Up or Line Down key is
pressed, or when the end arrows of the scrollbar are clicked

1

block increment

amount the value changes when the Page Up or Page Down key is
pressed, or when the scrollbar track is clicked

on either side of
the bubble

10

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Scrollbar

```java
public Scrollbar​(int orientation)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

**Parameters:** orientation

- indicates the orientation of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- Scrollbar

```java
public Scrollbar​(int orientation,
int value,
int visible,
int minimum,
int maximum)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

**Parameters:** orientation

- indicates the orientation of the scroll bar.
**Parameters:** value

- the initial value of the scroll bar
**Parameters:** visible

- the visible amount of the scroll bar, typically
represented by the size of the bubble
**Parameters:** minimum

- the minimum value of the scroll bar
**Parameters:** maximum

- the maximum value of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** setValues(int, int, int, int)

,

GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

Scrollbar

```java
public Scrollbar()
throws
HeadlessException
```

Constructs a new vertical scroll bar.
The default properties of the scroll bar are listed in
the following table:

Scrollbar default properties

Property

Description

Default Value

orientation

indicates whether the scroll bar is vertical or horizontal

Scrollbar.VERTICAL

value

value which controls the location of the scroll bar's bubble

0

visible amount

visible amount of the scroll bar's range, typically represented
by the size of the scroll bar's bubble

10

minimum

minimum value of the scroll bar

0

maximum

maximum value of the scroll bar

100

unit increment

amount the value changes when the Line Up or Line Down key is
pressed, or when the end arrows of the scrollbar are clicked

1

block increment

amount the value changes when the Page Up or Page Down key is
pressed, or when the scrollbar track is clicked

on either side of
the bubble

10

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Scrollbar

public Scrollbar()
throws

HeadlessException

Constructs a new vertical scroll bar.
The default properties of the scroll bar are listed in
the following table:

Scrollbar default properties

Property

Description

Default Value

orientation

indicates whether the scroll bar is vertical or horizontal

Scrollbar.VERTICAL

value

value which controls the location of the scroll bar's bubble

0

visible amount

visible amount of the scroll bar's range, typically represented
by the size of the scroll bar's bubble

10

minimum

minimum value of the scroll bar

0

maximum

maximum value of the scroll bar

100

unit increment

amount the value changes when the Line Up or Line Down key is
pressed, or when the end arrows of the scrollbar are clicked

1

block increment

amount the value changes when the Page Up or Page Down key is
pressed, or when the scrollbar track is clicked

on either side of
the bubble

10

Scrollbar

```java
public Scrollbar​(int orientation)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

**Parameters:** orientation

- indicates the orientation of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Scrollbar

public Scrollbar​(int orientation)
throws

HeadlessException

Constructs a new scroll bar with the specified orientation.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

Scrollbar

```java
public Scrollbar​(int orientation,
int value,
int visible,
int minimum,
int maximum)
throws
HeadlessException
```

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

**Parameters:** orientation

- indicates the orientation of the scroll bar.
**Parameters:** value

- the initial value of the scroll bar
**Parameters:** visible

- the visible amount of the scroll bar, typically
represented by the size of the bubble
**Parameters:** minimum

- the minimum value of the scroll bar
**Parameters:** maximum

- the maximum value of the scroll bar
**Throws:** IllegalArgumentException

- when an illegal value for
the

orientation

argument is supplied
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** setValues(int, int, int, int)

,

GraphicsEnvironment.isHeadless()

---

#### Scrollbar

public Scrollbar​(int orientation,
int value,
int visible,
int minimum,
int maximum)
throws

HeadlessException

Constructs a new scroll bar with the specified orientation,
initial value, visible amount, and minimum and maximum values.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

The

orientation

argument must take one of the two
values

Scrollbar.HORIZONTAL

,
or

Scrollbar.VERTICAL

,
indicating a horizontal or vertical scroll bar, respectively.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

The parameters supplied to this constructor are subject to the
constraints described in

setValues(int, int, int, int)

.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

Scrollbar

's peer. The peer allows you to modify
the appearance of the

Scrollbar

without changing any of its
functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scroll bar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the orientation for this scroll bar.

**Parameters:** orientation

- the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**Throws:** IllegalArgumentException

- if the value supplied
for

orientation

is not a
legal value
**Since:** 1.1
**See Also:** getOrientation()

- getValue

```java
public int getValue()
```

Gets the current value of this scroll bar.

**Specified by:** getValue

in interface

Adjustable
**Returns:** the current value of this scroll bar
**See Also:** getMinimum()

,

getMaximum()

- setValue

```java
public void setValue​(int newValue)
```

Sets the value of this scroll bar to the specified value.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** newValue

- the new value of the scroll bar
**See Also:** setValues(int, int, int, int)

,

getValue()

,

getMinimum()

,

getMaximum()

- getMinimum

```java
public int getMinimum()
```

Gets the minimum value of this scroll bar.

**Specified by:** getMinimum

in interface

Adjustable
**Returns:** the minimum value of this scroll bar
**See Also:** getValue()

,

getMaximum()

- setMinimum

```java
public void setMinimum​(int newMinimum)
```

Sets the minimum value of this scroll bar.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** newMinimum

- the new minimum value for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMaximum(int)

- getMaximum

```java
public int getMaximum()
```

Gets the maximum value of this scroll bar.

**Specified by:** getMaximum

in interface

Adjustable
**Returns:** the maximum value of this scroll bar
**See Also:** getValue()

,

getMinimum()

- setMaximum

```java
public void setMaximum​(int newMaximum)
```

Sets the maximum value of this scroll bar.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** newMaximum

- the new maximum value
for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMinimum(int)

- getVisibleAmount

```java
public int getVisibleAmount()
```

Gets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

**Specified by:** getVisibleAmount

in interface

Adjustable
**Returns:** the visible amount of this scroll bar
**Since:** 1.1
**See Also:** setVisibleAmount(int)

- getVisible

```java
@Deprecated

public int getVisible()
```

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

Returns the visible amount of this scroll bar.

**Returns:** the visible amount of this scroll bar

- setVisibleAmount

```java
public void setVisibleAmount​(int newAmount)
```

Sets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** newAmount

- the new visible amount
**Since:** 1.1
**See Also:** getVisibleAmount()

,

setValues(int, int, int, int)

- setUnitIncrement

```java
public void setUnitIncrement​(int v)
```

Sets the unit increment for this scroll bar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** setUnitIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getUnitIncrement()

- setLineIncrement

```java
@Deprecated

public void setLineIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

Sets the unit increment for this scroll bar.

**Parameters:** v

- the increment value

- getUnitIncrement

```java
public int getUnitIncrement()
```

Gets the unit increment for this scrollbar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** getUnitIncrement

in interface

Adjustable
**Returns:** the unit increment of this scroll bar
**Since:** 1.1
**See Also:** setUnitIncrement(int)

- getLineIncrement

```java
@Deprecated

public int getLineIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

Returns the unit increment for this scrollbar.

**Returns:** the unit increment for this scrollbar

- setBlockIncrement

```java
public void setBlockIncrement​(int v)
```

Sets the block increment for this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

**Specified by:** setBlockIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getBlockIncrement()

- setPageIncrement

```java
@Deprecated

public void setPageIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

Sets the block increment for this scroll bar.

**Parameters:** v

- the block increment

- getBlockIncrement

```java
public int getBlockIncrement()
```

Gets the block increment of this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

**Specified by:** getBlockIncrement

in interface

Adjustable
**Returns:** the block increment of this scroll bar
**Since:** 1.1
**See Also:** setBlockIncrement(int)

- getPageIncrement

```java
@Deprecated

public int getPageIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

Returns the block increment of this scroll bar.

**Returns:** the block increment of this scroll bar

- setValues

```java
public void setValues​(int value,
int visible,
int minimum,
int maximum)
```

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.
If the values supplied for these properties are inconsistent
or incorrect, they will be changed to ensure consistency.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** value

- is the position in the current window
**Parameters:** visible

- is the visible amount of the scroll bar
**Parameters:** minimum

- is the minimum value of the scroll bar
**Parameters:** maximum

- is the maximum value of the scroll bar
**See Also:** setMinimum(int)

,

setMaximum(int)

,

setVisibleAmount(int)

,

setValue(int)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**Since:** 1.4
**See Also:** setValueIsAdjusting(boolean)

- setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

- addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

- removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

- getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this scrollbar.

**Returns:** all of this scrollbar's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentEvent

,

AdjustmentListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** Component.getComponentListeners()

,

Component.getFocusListeners()

,

Component.getHierarchyListeners()

,

Component.getHierarchyBoundsListeners()

,

Component.getKeyListeners()

,

Component.getMouseListeners()

,

Component.getMouseMotionListeners()

,

Component.getMouseWheelListeners()

,

Component.getInputMethodListeners()

,

Component.getPropertyChangeListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scroll bar. If the event is an
instance of

AdjustmentEvent

, it invokes the

processAdjustmentEvent

method.
Otherwise, it invokes its superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

processAdjustmentEvent(java.awt.event.AdjustmentEvent)

- processAdjustmentEvent

```java
protected void processAdjustmentEvent​(
AdjustmentEvent
e)
```

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the adjustment event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

AdjustmentListener

,

addAdjustmentListener(java.awt.event.AdjustmentListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Scrollbar

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scroll bar

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

Scrollbar

. For scrollbars, the

AccessibleContext

takes the form of an

AccessibleAWTScrollBar

. A new

AccessibleAWTScrollBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTScrollBar

that serves as the

AccessibleContext

of this

ScrollBar
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the

Scrollbar

's peer. The peer allows you to modify
the appearance of the

Scrollbar

without changing any of its
functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

---

#### addNotify

public void addNotify()

Creates the

Scrollbar

's peer. The peer allows you to modify
the appearance of the

Scrollbar

without changing any of its
functionality.

getOrientation

```java
public int getOrientation()
```

Returns the orientation of this scroll bar.

**Specified by:** getOrientation

in interface

Adjustable
**Returns:** the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Returns the orientation of this scroll bar.

setOrientation

```java
public void setOrientation​(int orientation)
```

Sets the orientation for this scroll bar.

**Parameters:** orientation

- the orientation of this scroll bar, either

Scrollbar.HORIZONTAL

or

Scrollbar.VERTICAL
**Throws:** IllegalArgumentException

- if the value supplied
for

orientation

is not a
legal value
**Since:** 1.1
**See Also:** getOrientation()

---

#### setOrientation

public void setOrientation​(int orientation)

Sets the orientation for this scroll bar.

getValue

```java
public int getValue()
```

Gets the current value of this scroll bar.

**Specified by:** getValue

in interface

Adjustable
**Returns:** the current value of this scroll bar
**See Also:** getMinimum()

,

getMaximum()

---

#### getValue

public int getValue()

Gets the current value of this scroll bar.

setValue

```java
public void setValue​(int newValue)
```

Sets the value of this scroll bar to the specified value.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

**Specified by:** setValue

in interface

Adjustable
**Parameters:** newValue

- the new value of the scroll bar
**See Also:** setValues(int, int, int, int)

,

getValue()

,

getMinimum()

,

getMaximum()

---

#### setValue

public void setValue​(int newValue)

Sets the value of this scroll bar to the specified value.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

If the value supplied is less than the current

minimum

or greater than the current

maximum - visibleAmount

,
then either

minimum

or

maximum - visibleAmount

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Calling this method does not fire an

AdjustmentEvent

.

Calling this method does not fire an

AdjustmentEvent

.

getMinimum

```java
public int getMinimum()
```

Gets the minimum value of this scroll bar.

**Specified by:** getMinimum

in interface

Adjustable
**Returns:** the minimum value of this scroll bar
**See Also:** getValue()

,

getMaximum()

---

#### getMinimum

public int getMinimum()

Gets the minimum value of this scroll bar.

setMinimum

```java
public void setMinimum​(int newMinimum)
```

Sets the minimum value of this scroll bar.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

**Specified by:** setMinimum

in interface

Adjustable
**Parameters:** newMinimum

- the new minimum value for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMaximum(int)

---

#### setMinimum

public void setMinimum​(int newMinimum)

Sets the minimum value of this scroll bar.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

When

setMinimum

is called, the minimum value
is changed, and other values (including the maximum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new minimum.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

Normally, a program should change a scroll bar's minimum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

Note that setting the minimum value to

Integer.MAX_VALUE

will result in the new minimum value being set to

Integer.MAX_VALUE - 1

.

getMaximum

```java
public int getMaximum()
```

Gets the maximum value of this scroll bar.

**Specified by:** getMaximum

in interface

Adjustable
**Returns:** the maximum value of this scroll bar
**See Also:** getValue()

,

getMinimum()

---

#### getMaximum

public int getMaximum()

Gets the maximum value of this scroll bar.

setMaximum

```java
public void setMaximum​(int newMaximum)
```

Sets the maximum value of this scroll bar.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

**Specified by:** setMaximum

in interface

Adjustable
**Parameters:** newMaximum

- the new maximum value
for this scroll bar
**Since:** 1.1
**See Also:** setValues(int, int, int, int)

,

setMinimum(int)

---

#### setMaximum

public void setMaximum​(int newMaximum)

Sets the maximum value of this scroll bar.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

When

setMaximum

is called, the maximum value
is changed, and other values (including the minimum, the
visible amount, and the current scroll bar value)
are changed to be consistent with the new maximum.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

Normally, a program should change a scroll bar's maximum
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

Note that setting the maximum value to

Integer.MIN_VALUE

will result in the new maximum value being set to

Integer.MIN_VALUE + 1

.

getVisibleAmount

```java
public int getVisibleAmount()
```

Gets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

**Specified by:** getVisibleAmount

in interface

Adjustable
**Returns:** the visible amount of this scroll bar
**Since:** 1.1
**See Also:** setVisibleAmount(int)

---

#### getVisibleAmount

public int getVisibleAmount()

Gets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

getVisible

```java
@Deprecated

public int getVisible()
```

Deprecated.

As of JDK version 1.1,
replaced by

getVisibleAmount()

.

Returns the visible amount of this scroll bar.

**Returns:** the visible amount of this scroll bar

---

#### getVisible

@Deprecated

public int getVisible()

Returns the visible amount of this scroll bar.

setVisibleAmount

```java
public void setVisibleAmount​(int newAmount)
```

Sets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

**Specified by:** setVisibleAmount

in interface

Adjustable
**Parameters:** newAmount

- the new visible amount
**Since:** 1.1
**See Also:** getVisibleAmount()

,

setValues(int, int, int, int)

---

#### setVisibleAmount

public void setVisibleAmount​(int newAmount)

Sets the visible amount of this scroll bar.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

When a scroll bar is used to select a range of values,
the visible amount is used to represent the range of values
that are currently visible. The size of the scroll bar's
bubble (also called a thumb or scroll box), usually gives a
visual representation of the relationship of the visible
amount to the range of the scroll bar.
Note that depending on platform, the value of the visible amount property
may not be visually indicated by the size of the bubble.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

The scroll bar's bubble may not be displayed when it is not
moveable (e.g. when it takes up the entire length of the
scroll bar's track, or when the scroll bar is disabled).
Whether the bubble is displayed or not will not affect
the value returned by

getVisibleAmount

.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

If the visible amount supplied is less than

one

or greater than the current

maximum - minimum

,
then either

one

or

maximum - minimum

is substituted, as appropriate.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

Normally, a program should change a scroll bar's
value only by calling

setValues

.
The

setValues

method simultaneously
and synchronously sets the minimum, maximum, visible amount,
and value properties of a scroll bar, so that they are
mutually consistent.

setUnitIncrement

```java
public void setUnitIncrement​(int v)
```

Sets the unit increment for this scroll bar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** setUnitIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getUnitIncrement()

---

#### setUnitIncrement

public void setUnitIncrement​(int v)

Sets the unit increment for this scroll bar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.
Attempts to set the unit increment to a value lower than 1
will result in a value of 1 being set.

In some operating systems, this property
can be ignored by the underlying controls.

In some operating systems, this property
can be ignored by the underlying controls.

setLineIncrement

```java
@Deprecated

public void setLineIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setUnitIncrement(int)

.

Sets the unit increment for this scroll bar.

**Parameters:** v

- the increment value

---

#### setLineIncrement

@Deprecated

public void setLineIncrement​(int v)

Sets the unit increment for this scroll bar.

getUnitIncrement

```java
public int getUnitIncrement()
```

Gets the unit increment for this scrollbar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

**Specified by:** getUnitIncrement

in interface

Adjustable
**Returns:** the unit increment of this scroll bar
**Since:** 1.1
**See Also:** setUnitIncrement(int)

---

#### getUnitIncrement

public int getUnitIncrement()

Gets the unit increment for this scrollbar.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

The unit increment is the value that is added or subtracted
when the user activates the unit increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The unit increment must be greater than zero.

In some operating systems, this property
can be ignored by the underlying controls.

In some operating systems, this property
can be ignored by the underlying controls.

getLineIncrement

```java
@Deprecated

public int getLineIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getUnitIncrement()

.

Returns the unit increment for this scrollbar.

**Returns:** the unit increment for this scrollbar

---

#### getLineIncrement

@Deprecated

public int getLineIncrement()

Returns the unit increment for this scrollbar.

setBlockIncrement

```java
public void setBlockIncrement​(int v)
```

Sets the block increment for this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

**Specified by:** setBlockIncrement

in interface

Adjustable
**Parameters:** v

- the amount by which to increment or decrement
the scroll bar's value
**Since:** 1.1
**See Also:** getBlockIncrement()

---

#### setBlockIncrement

public void setBlockIncrement​(int v)

Sets the block increment for this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.
Attempts to set the block increment to a value lower than 1
will result in a value of 1 being set.

setPageIncrement

```java
@Deprecated

public void setPageIncrement​(int v)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBlockIncrement()

.

Sets the block increment for this scroll bar.

**Parameters:** v

- the block increment

---

#### setPageIncrement

@Deprecated

public void setPageIncrement​(int v)

Sets the block increment for this scroll bar.

getBlockIncrement

```java
public int getBlockIncrement()
```

Gets the block increment of this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

**Specified by:** getBlockIncrement

in interface

Adjustable
**Returns:** the block increment of this scroll bar
**Since:** 1.1
**See Also:** setBlockIncrement(int)

---

#### getBlockIncrement

public int getBlockIncrement()

Gets the block increment of this scroll bar.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

The block increment is the value that is added or subtracted
when the user activates the block increment area of the
scroll bar, generally through a mouse or keyboard gesture
that the scroll bar receives as an adjustment event.
The block increment must be greater than zero.

getPageIncrement

```java
@Deprecated

public int getPageIncrement()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBlockIncrement()

.

Returns the block increment of this scroll bar.

**Returns:** the block increment of this scroll bar

---

#### getPageIncrement

@Deprecated

public int getPageIncrement()

Returns the block increment of this scroll bar.

setValues

```java
public void setValues​(int value,
int visible,
int minimum,
int maximum)
```

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.
If the values supplied for these properties are inconsistent
or incorrect, they will be changed to ensure consistency.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** value

- is the position in the current window
**Parameters:** visible

- is the visible amount of the scroll bar
**Parameters:** minimum

- is the minimum value of the scroll bar
**Parameters:** maximum

- is the maximum value of the scroll bar
**See Also:** setMinimum(int)

,

setMaximum(int)

,

setVisibleAmount(int)

,

setValue(int)

---

#### setValues

public void setValues​(int value,
int visible,
int minimum,
int maximum)

Sets the values of four properties for this scroll bar:

value

,

visibleAmount

,

minimum

, and

maximum

.
If the values supplied for these properties are inconsistent
or incorrect, they will be changed to ensure consistency.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

This method simultaneously and synchronously sets the values
of four scroll bar properties, assuring that the values of
these properties are mutually consistent. It enforces the
following constraints:

maximum

must be greater than

minimum

,

maximum - minimum

must not be greater
than

Integer.MAX_VALUE

,

visibleAmount

must be greater than zero.

visibleAmount

must not be greater than

maximum - minimum

,

value

must not be less than

minimum

,
and

value

must not be greater than

maximum - visibleAmount

Calling this method does not fire an

AdjustmentEvent

.

Calling this method does not fire an

AdjustmentEvent

.

getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

**Returns:** the value of the

valueIsAdjusting

property
**Since:** 1.4
**See Also:** setValueIsAdjusting(boolean)

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns true if the value is in the process of changing as a
result of actions being taken by the user.

setValueIsAdjusting

```java
public void setValueIsAdjusting​(boolean b)
```

Sets the

valueIsAdjusting

property.

**Parameters:** b

- new adjustment-in-progress status
**Since:** 1.4
**See Also:** getValueIsAdjusting()

---

#### setValueIsAdjusting

public void setValueIsAdjusting​(boolean b)

Sets the

valueIsAdjusting

property.

addAdjustmentListener

```java
public void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

---

#### addAdjustmentListener

public void addAdjustmentListener​(

AdjustmentListener

l)

Adds the specified adjustment listener to receive instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeAdjustmentListener

```java
public void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeAdjustmentListener

in interface

Adjustable
**Parameters:** l

- the adjustment listener
**Since:** 1.1
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

getAdjustmentListeners()

,

AdjustmentEvent

,

AdjustmentListener

---

#### removeAdjustmentListener

public void removeAdjustmentListener​(

AdjustmentListener

l)

Removes the specified adjustment listener so that it no longer
receives instances of

AdjustmentEvent

from this scroll bar.
If l is

null

, no exception is thrown and no action
is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getAdjustmentListeners

```java
public
AdjustmentListener
[] getAdjustmentListeners()
```

Returns an array of all the adjustment listeners
registered on this scrollbar.

**Returns:** all of this scrollbar's

AdjustmentListener

s
or an empty array if no adjustment
listeners are currently registered
**Since:** 1.4
**See Also:** addAdjustmentListener(java.awt.event.AdjustmentListener)

,

removeAdjustmentListener(java.awt.event.AdjustmentListener)

,

AdjustmentEvent

,

AdjustmentListener

---

#### getAdjustmentListeners

public

AdjustmentListener

[] getAdjustmentListeners()

Returns an array of all the adjustment listeners
registered on this scrollbar.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** Component.getComponentListeners()

,

Component.getFocusListeners()

,

Component.getHierarchyListeners()

,

Component.getHierarchyBoundsListeners()

,

Component.getKeyListeners()

,

Component.getMouseListeners()

,

Component.getMouseMotionListeners()

,

Component.getMouseWheelListeners()

,

Component.getInputMethodListeners()

,

Component.getPropertyChangeListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Scrollbar

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Scrollbar c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scroll bar. If the event is an
instance of

AdjustmentEvent

, it invokes the

processAdjustmentEvent

method.
Otherwise, it invokes its superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

processAdjustmentEvent(java.awt.event.AdjustmentEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events on this scroll bar. If the event is an
instance of

AdjustmentEvent

, it invokes the

processAdjustmentEvent

method.
Otherwise, it invokes its superclass's

processEvent

method.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processAdjustmentEvent

```java
protected void processAdjustmentEvent​(
AdjustmentEvent
e)
```

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the adjustment event
**Since:** 1.1
**See Also:** AdjustmentEvent

,

AdjustmentListener

,

addAdjustmentListener(java.awt.event.AdjustmentListener)

,

Component.enableEvents(long)

---

#### processAdjustmentEvent

protected void processAdjustmentEvent​(

AdjustmentEvent

e)

Processes adjustment events occurring on this
scrollbar by dispatching them to any registered

AdjustmentListener

objects.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless adjustment events are
enabled for this component. Adjustment events are enabled
when one of the following occurs:

- An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

AdjustmentListener

object is registered
via

addAdjustmentListener

.

Adjustment events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Scrollbar

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scroll bar

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

Scrollbar

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

Scrollbar

. For scrollbars, the

AccessibleContext

takes the form of an

AccessibleAWTScrollBar

. A new

AccessibleAWTScrollBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTScrollBar

that serves as the

AccessibleContext

of this

ScrollBar
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

Scrollbar

. For scrollbars, the

AccessibleContext

takes the form of an

AccessibleAWTScrollBar

. A new

AccessibleAWTScrollBar

instance is created if necessary.

---

